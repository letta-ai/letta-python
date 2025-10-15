# Gemini SDK Integration - Implementation Plan

## Difficulty Assessment: **Easy-Medium** ⭐⭐⭐

Adding Gemini SDK support would be similar in complexity to the OpenAI implementation we just completed.

## What's Needed

### 1. SDK Overview

**Package**: `google-generativeai`
**Import**: `import google.generativeai as genai`

```python
# Client creation
model = genai.GenerativeModel('gemini-2.5-flash')

# Non-streaming
response = model.generate_content("Hello")

# Streaming
response = model.generate_content("Hello", stream=True)
for chunk in response:
    print(chunk.text)
```

### 2. Key Differences from OpenAI/Anthropic

| Aspect | OpenAI | Anthropic | Gemini |
|--------|--------|-----------|--------|
| Client | `AsyncOpenAI()` | `AsyncAnthropic()` | `GenerativeModel()` |
| Method | `.chat.completions.create()` | `.messages.create()` | `.generate_content_async()` |
| Messages format | `messages=[...]` | `messages=[...]` | `contents=[...]` |
| System instruction | In messages array | `system` parameter | `system_instruction` (model-level) |
| Streaming | `stream=True` | `stream=True` | `stream=True` |
| Response | `ChatCompletion` | `Message` | `GenerateContentResponse` |

### 3. Implementation Steps

#### Step 1: Add Interceptor (~50 lines)

```python
def _install_gemini_interceptor():
    """
    Monkey-patch Gemini SDK to intercept message flow.
    """
    try:
        import google.generativeai as genai
        from google.generativeai.generative_models import GenerativeModel
    except ImportError:
        print("[Letta Memory] Gemini SDK not found, skipping interceptor installation")
        return

    # Save original method (only once)
    if not hasattr(GenerativeModel, '_original_generate_content_async'):
        GenerativeModel._original_generate_content_async = GenerativeModel.generate_content_async

    # Patch generate_content_async
    async def patched_generate_content_async(self, contents, **kwargs):
        # Inject memory and capture user message if memory is enabled
        if _is_memory_enabled():
            # Inject memory into system instruction
            contents, kwargs = await _inject_memory_into_gemini_kwargs(contents, kwargs)

            # Capture user message
            await _capture_gemini_user_message(contents)

        # Call original method
        response = await GenerativeModel._original_generate_content_async(self, contents, **kwargs)

        # Capture response if memory is enabled
        if _is_memory_enabled():
            if kwargs.get("stream", False):
                # Streaming: wrap the response
                return _wrap_gemini_streaming_response(response)
            else:
                # Non-streaming: capture response
                await _capture_gemini_response(response)

        return response

    # Apply patch
    GenerativeModel.generate_content_async = patched_generate_content_async
```

#### Step 2: Memory Injection (~60 lines)

```python
async def _inject_memory_into_gemini_kwargs(contents, kwargs):
    """
    Inject memory into Gemini generate_content_async() kwargs.

    Gemini has two approaches:
    1. system_instruction at model level (can't modify after creation)
    2. Add as first message in contents array (our approach)
    """
    config = _get_current_config()
    if not config or config.get("capture_only", False):
        return contents, kwargs

    agent_name = config["agent_name"]
    letta_client = config["letta_client"]

    if not letta_client:
        return contents, kwargs

    try:
        # Fetch memory blocks
        agents = letta_client.agents.list(name=agent_name)
        if not agents or len(agents) == 0:
            return contents, kwargs

        agent = agents[0]
        blocks = letta_client.agents.blocks.list(agent_id=agent.id)
        memory_context = _format_memory_blocks(blocks)

        if not memory_context:
            return contents, kwargs

        # Gemini contents format: [{"role": "user", "parts": ["text"]}]
        # Inject memory as first user message
        memory_content = {
            "role": "user",
            "parts": [f"## Previous Context from Letta Memory\n{memory_context}"]
        }

        # Ensure contents is a list
        if isinstance(contents, str):
            contents = [{"role": "user", "parts": [contents]}]
        elif not isinstance(contents, list):
            contents = [contents]

        # Prepend memory content
        contents = [memory_content] + contents

        print(f"[Letta Memory] Injected memory into request ({len(memory_context)} chars)")

    except Exception as e:
        print(f"[Letta Memory] Error injecting memory: {e}")
        import traceback
        traceback.print_exc()

    return contents, kwargs
```

#### Step 3: Message Capture (~40 lines)

```python
async def _capture_gemini_user_message(contents):
    """Capture user message from Gemini contents."""
    config = _get_current_config()
    if not config:
        return

    try:
        # Find last user message
        for content in reversed(contents):
            if isinstance(content, dict) and content.get("role") == "user":
                parts = content.get("parts", [])
                # Combine all text parts
                text_parts = [p for p in parts if isinstance(p, str)]
                if text_parts:
                    config["pending_user_message"] = " ".join(text_parts)
                    break
            elif isinstance(content, str):
                config["pending_user_message"] = content
                break

    except Exception as e:
        print(f"[Letta Memory] Error capturing user message: {e}")
        import traceback
        traceback.print_exc()
```

#### Step 4: Response Capture (~80 lines)

```python
async def _capture_gemini_response(response):
    """Capture non-streaming Gemini response."""
    config = _get_current_config()
    if not config:
        return

    try:
        # Extract text from response
        # Response format: GenerateContentResponse(candidates=[Candidate(content=Content(parts=[Part(text='...')]))])
        if hasattr(response, 'text'):
            assistant_message = response.text
        elif hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate.content, 'parts'):
                text_parts = [part.text for part in candidate.content.parts if hasattr(part, 'text')]
                assistant_message = " ".join(text_parts)
            else:
                return
        else:
            return

        if assistant_message:
            asyncio.create_task(
                _save_conversation_turn(
                    user_message=config.get("pending_user_message"),
                    assistant_message=assistant_message
                )
            )
            config["pending_user_message"] = None

    except Exception as e:
        print(f"[Letta Memory] Error capturing response: {e}")
        import traceback
        traceback.print_exc()


class _GeminiStreamWrapper:
    """Wrapper for Gemini streaming responses."""

    def __init__(self, stream):
        self._stream = stream
        self._accumulated_text = []

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            chunk = await self._stream.__anext__()

            # Capture text from chunk
            if hasattr(chunk, 'text'):
                self._accumulated_text.append(chunk.text)

            return chunk

        except StopAsyncIteration:
            await self._save_accumulated_text()
            raise

    async def _save_accumulated_text(self):
        if not self._accumulated_text:
            return

        config = _get_current_config()
        if not config:
            return

        assistant_message = "".join(self._accumulated_text)

        asyncio.create_task(
            _save_conversation_turn(
                user_message=config.get("pending_user_message"),
                assistant_message=assistant_message
            )
        )

        config["pending_user_message"] = None


def _wrap_gemini_streaming_response(stream):
    """Wrap Gemini streaming response."""
    return _GeminiStreamWrapper(stream)
```

#### Step 5: Test File (~200 lines)

Create `tests/custom/test_gemini_interception.py` following the same structure as the OpenAI test.

### 4. Estimated Effort

| Task | Lines of Code | Time Estimate |
|------|---------------|---------------|
| Interceptor installation | ~50 | 15 min |
| Memory injection | ~60 | 20 min |
| Message capture | ~40 | 15 min |
| Response capture (non-streaming) | ~40 | 15 min |
| Stream wrapper | ~40 | 20 min |
| Test file | ~200 | 30 min |
| Testing & debugging | - | 30 min |
| **TOTAL** | **~430 lines** | **~2-3 hours** |

### 5. Challenges

#### Easy Parts ✅
- Similar structure to OpenAI/Anthropic
- Streaming uses same async iterator pattern
- Response format is straightforward

#### Potential Gotchas ⚠️
1. **System instruction** - Gemini's system instruction is set at model creation time, not per-request
   - **Solution**: Inject memory as first user message instead
2. **Contents format** - More flexible than other SDKs (can be string or list)
   - **Solution**: Normalize to list format
3. **Response structure** - Nested candidates/content/parts
   - **Solution**: Handle multiple formats with fallbacks
4. **SDK variations** - Different behavior between sync and async versions
   - **Solution**: Focus on async version only (like other SDKs)

### 6. Auto-Detection Update

Add Gemini to the provider detection:

```python
def _detect_available_providers() -> list[str]:
    """Auto-detect which SDK providers are installed."""
    available = []

    # Check for Claude Agent SDK
    try:
        import claude_agent_sdk
        available.append("claude")
    except ImportError:
        pass

    # Check for Anthropic SDK
    try:
        import anthropic
        available.append("anthropic")
    except ImportError:
        pass

    # Check for OpenAI SDK
    try:
        import openai
        available.append("openai")
    except ImportError:
        pass

    # Check for Gemini SDK
    try:
        import google.generativeai
        available.append("gemini")
    except ImportError:
        pass

    return available
```

### 7. Usage Example

```python
import google.generativeai as genai
from letta_client.memory import memory
from letta_client.client import Letta

letta = Letta(base_url="http://localhost:8283", token=None)
genai.configure(api_key="...")

model = genai.GenerativeModel('gemini-2.5-flash')

# Session 1
async with memory(agent="my_assistant", client=letta):
    response = await model.generate_content_async("My name is Charlie")
    print(response.text)

# Session 2 - Gemini remembers!
async with memory(agent="my_assistant", client=letta):
    response = await model.generate_content_async("What is my name?")
    print(response.text)  # "Your name is Charlie!"
```

## Conclusion

**Difficulty**: ⭐⭐⭐ (Medium - same as OpenAI)

**Estimated Time**: 2-3 hours for full implementation + testing

**Recommendation**: ✅ **Go for it!** The pattern is well-established now, and Gemini would be a great addition to complete the "Big 4" LLM SDKs (OpenAI, Anthropic, Google, Claude).

## Next Steps

1. Install Gemini SDK: `pip install google-generativeai`
2. Follow the implementation steps above
3. Test with both streaming and non-streaming
4. Verify cross-session memory recall
5. Update documentation

Would you like me to implement it? 🚀
