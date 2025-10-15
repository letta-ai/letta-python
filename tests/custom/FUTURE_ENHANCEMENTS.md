# Future Enhancements & Known Gaps

## OpenAI Responses API (Not Yet Supported) ⚠️

### The Issue

The OpenAI SDK has **two different APIs** with different interfaces:

#### 1. Chat Completions API (✅ Currently Supported)

```python
from openai import AsyncOpenAI

client = AsyncOpenAI()

# This works - we intercept this!
response = await client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}]
)

# Response structure
response.choices[0].message.content
```

**Status**: ✅ **Fully supported** - We patch `AsyncCompletions.create()`

#### 2. Responses API (❌ Not Yet Supported)

```python
from openai import AsyncOpenAI

client = AsyncOpenAI()

# This does NOT work yet - we don't intercept this!
response = await client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn."
)

# Different response structure
response.output_text
```

**Status**: ❌ **Not supported** - We need to patch `AsyncResponses.create()`

### Key Differences

| Aspect | Chat Completions API | Responses API |
|--------|---------------------|---------------|
| **Endpoint** | `client.chat.completions.create()` | `client.responses.create()` |
| **Input Format** | `messages=[...]` | `input="..."` (simple string) |
| **Response Format** | `response.choices[0].message.content` | `response.output_text` |
| **Streaming** | `stream=True` → chunks | Different streaming format |
| **Model Support** | GPT-3.5, GPT-4, etc. | GPT-5+ (newer models) |

### Why This Matters

Users might try to use the Responses API and wonder why memory isn't working:

```python
# User code - memory won't work! ⚠️
async with memory(agent="my_agent", client=letta):
    response = await client.responses.create(
        model="gpt-5",
        input="What is my name?"
    )
    # Memory NOT injected or captured!
```

### Implementation Plan (Future)

To support the Responses API, we need to:

1. **Add new interceptor** (~40 lines)
   ```python
   def _install_openai_responses_interceptor():
       """Patch AsyncResponses.create()"""
       from openai.resources.responses import AsyncResponses

       if not hasattr(AsyncResponses, '_original_create'):
           AsyncResponses._original_create = AsyncResponses.create

       async def patched_create(self, **kwargs):
           if _is_memory_enabled():
               kwargs = await _inject_memory_into_openai_responses_kwargs(kwargs)
               await _capture_openai_responses_input(kwargs)

           response = await AsyncResponses._original_create(self, **kwargs)

           if _is_memory_enabled():
               if kwargs.get("stream", False):
                   return _wrap_openai_responses_streaming(response)
               else:
                   await _capture_openai_responses_output(response)

           return response

       AsyncResponses.create = patched_create
   ```

2. **Memory injection helper** (~50 lines)
   ```python
   async def _inject_memory_into_openai_responses_kwargs(kwargs: dict) -> dict:
       """Inject memory into Responses API kwargs."""
       # Responses API uses 'input' instead of 'messages'
       # We need to prepend memory context to the input string

       if "input" in kwargs:
           memory_context = await _fetch_memory_context()
           kwargs["input"] = f"{memory_context}\n\n{kwargs['input']}"

       return kwargs
   ```

3. **Input capture** (~30 lines)
   ```python
   async def _capture_openai_responses_input(kwargs: dict):
       """Capture input from Responses API."""
       config = _get_current_config()
       if config and "input" in kwargs:
           config["pending_user_message"] = kwargs["input"]
   ```

4. **Output capture** (~30 lines)
   ```python
   async def _capture_openai_responses_output(response):
       """Capture output from Responses API."""
       config = _get_current_config()
       if config and hasattr(response, 'output_text'):
           await _save_conversation_turn(
               user_message=config.get("pending_user_message"),
               assistant_message=response.output_text
           )
   ```

5. **Streaming wrapper** (~60 lines)
   ```python
   class _OpenAIResponsesStreamWrapper:
       """Wrapper for Responses API streaming."""
       # Similar to existing stream wrappers but for Responses API format
   ```

### Testing Required

Would need a new test file:

```python
# tests/custom/test_openai_responses_interception.py

async def test_openai_responses_non_streaming():
    """Test OpenAI Responses API (non-streaming)."""
    client = AsyncOpenAI()

    async with memory(agent="test_agent", client=letta):
        # Session 1
        response = await client.responses.create(
            model="gpt-5",
            input="My name is Alice"
        )

        # Session 2
        response = await client.responses.create(
            model="gpt-5",
            input="What is my name?"
        )

        assert "alice" in response.output_text.lower()
```

### Estimated Effort

| Task | Lines of Code | Time |
|------|---------------|------|
| Interceptor | ~40 | 30 min |
| Helper functions | ~170 | 1 hour |
| Test file | ~150 | 30 min |
| Testing & debugging | - | 1 hour |
| **Total** | **~360 lines** | **3 hours** |

### Detection Strategy

Since both APIs are in the same SDK, we should:

1. **Patch both in `_install_openai_interceptor()`**
   ```python
   def _install_openai_interceptor():
       """Install interceptors for both OpenAI APIs."""
       _patch_openai_chat_completions()  # Existing
       _patch_openai_responses()         # New
   ```

2. **Auto-detect at runtime**
   - Both patches installed when OpenAI SDK is detected
   - No user configuration needed
   - Works transparently for both APIs

### Priority

**Medium Priority** ⭐⭐⭐

**Reasons**:
- Responses API is newer and less widely used (GPT-5+)
- Chat Completions API covers 95%+ of current use cases
- Easy to add when needed (follows same pattern)
- Users can still use Chat Completions API for now

**When to implement**:
- When GPT-5 becomes GA
- When users start requesting it
- When Responses API becomes standard

## Other Known Gaps

### 1. Azure OpenAI (Likely Already Works)

Azure OpenAI uses the same SDK as OpenAI, so our interceptor might already work:

```python
from openai import AsyncAzureOpenAI

# Might already work! (untested)
client = AsyncAzureOpenAI(...)
async with memory(agent="test", client=letta):
    response = await client.chat.completions.create(...)
```

**Status**: Untested, but likely works since it's the same SDK.

### 2. Synchronous SDKs

Currently only async methods are intercepted:

```python
# These don't work:
anthropic.messages.create()      # sync version
openai.chat.completions.create()  # sync version
model.generate_content()          # sync Gemini
```

**Solution**: Add sync interceptors (straightforward, just non-async versions)

### 3. Batch APIs

OpenAI and other providers have batch APIs:

```python
# Not intercepted
client.batches.create(...)
```

**Solution**: Intercept batch endpoints if needed

### 4. Function Calling / Tools

SDKs with function/tool calling need special handling:

```python
# Memory might interfere with function calls
response = await client.chat.completions.create(
    messages=[...],
    tools=[...]
)
```

**Solution**: Detect tool usage and adjust memory injection

## Summary

**OpenAI Responses API** is the main known gap:
- ✅ Chat Completions API: Fully supported
- ❌ Responses API: Not yet supported
- 📅 Recommended implementation: When GPT-5 GA or user requests

**Other gaps** are minor and can be addressed as needed.

## Tracking

When implementing OpenAI Responses API support:

1. Update this document
2. Add `_install_openai_responses_interceptor()`
3. Create `test_openai_responses_interception.py`
4. Update `ALL_SDKS_SUMMARY.md`
5. Update `QUICK_START.md`

---

**Good catch on identifying this!** 👍 It's definitely something to keep in mind for future implementation.
