"""
Letta Memory Integration for Claude Agent SDK (v0 Prototype)

This module provides Transport-layer interception to automatically capture and inject
memory from Letta into Claude Agent SDK calls.

Architecture:
- Claude Agent SDK → SubprocessCLITransport → Claude Code CLI (subprocess)
- We intercept the Transport layer to capture messages going in/out

Usage:
    from letta_client import memory

    async with memory(agent="my_agent", letta_client=letta):
        # All Claude SDK calls in this block automatically have memory
        async for message in query(prompt="My name is Alice"):
            print(message)
"""

import asyncio
import json
import os
from contextvars import ContextVar
from typing import Any, AsyncIterator, Literal, Optional


# Context-local state for memory configuration (isolated per async task/thread)
_MEMORY_CONFIG: ContextVar[Optional[dict]] = ContextVar('memory_config', default=None)

# Global set to track which SDK interceptors have been installed (per-process)
_INSTALLED_INTERCEPTORS: set[Literal["claude", "anthropic", "openai", "gemini"]] = set()


class MemoryContext:
    """Context manager for Letta memory integration."""

    def __init__(self, client: Any, agent: str, capture_only: bool = False):
        """
        Initialize memory context.

        Args:
            client: Letta client instance
            agent: Name of the Letta agent to use for memory storage
            capture_only: Whether to skip auto-injecting memory into system prompts (default: False)
                Set to True to skip memory injection and reduce latency
        """
        self.agent_name = agent
        self.letta_client = client
        self.capture_only = capture_only

    async def __aenter__(self):
        """Enter the memory context."""
        print(f"[Letta Memory] Entering memory context for agent: {self.agent_name}")
        if self.capture_only:
            print(f"[Letta Memory] Auto-inject disabled (capture-only mode)")

        # Set context-local memory configuration
        _MEMORY_CONFIG.set({
            "agent_name": self.agent_name,
            "letta_client": self.letta_client,
            "enabled": True,
            "capture_only": self.capture_only,
            "pending_user_message": None  # Buffer for batching messages
        })

        # Install interceptors on first use (auto-detect available SDKs)
        _ensure_interceptors_installed()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the memory context."""
        print(f"[Letta Memory] Exiting memory context for agent: {self.agent_name}")

        # Clear context-local memory configuration
        _MEMORY_CONFIG.set(None)

        # Don't suppress exceptions
        return False


def memory(agent: str = "letta_agent", client: Any = None, capture_only: bool = False) -> MemoryContext:
    """
    Create a memory context for automatic Letta integration.

    All Claude SDK interactions within this context will automatically:
    1. Capture user messages and save to Letta
    2. Inject Letta memory into system prompts (if capture_only=False)
    3. Capture streaming responses and save to Letta

    Args:
        agent: Name of the Letta agent to use for memory storage. Defaults to 'letta_agent'.
        client: Optional Letta client instance (if None, will create one)
        capture_only: Whether to skip auto-injecting memory into system prompts (default: False)
            Set to True to skip memory injection and reduce latency

    Returns:
        MemoryContext that can be used as an async context manager

    Example:
        >>> from letta_client import Letta, memory
        >>> letta = Letta(token="sk-...ruAA")
        >>>
        >>> async with memory(agent="my_agent", client=letta):
        >>>     async for msg in query(prompt="Hello"):
        >>>         print(msg)
    """
    if client is None:
        from .client import Letta
        client = Letta(token=os.getenv("LETTA_API_KEY"))
    return MemoryContext(agent=agent, client=client, capture_only=capture_only)


def register(providers: Optional[list[Literal["claude", "anthropic", "openai", "gemini"]]] = None):
    """
    Register SDK interceptors for memory integration.

    This function can be called at application startup to install interceptors
    early, rather than waiting for the first memory context to be entered.

    The installation is idempotent - calling this multiple times is safe.

    Args:
        providers: Optional list of SDK providers to install interceptors for.
                  Supported values: "claude", "anthropic", "openai", "gemini".
                  If None, auto-detects which SDKs are installed.

    Example:
        >>> from letta_client.memory import register
        >>>
        >>> # Auto-detect and install all available SDKs
        >>> register()
        >>>
        >>> # Manually specify which SDKs to intercept
        >>> register(providers=["claude", "anthropic"])
        >>>
        >>> # Later, memory contexts work immediately
        >>> async with memory(agent="my_agent"):
        >>>     # SDK code here
        >>>     pass
    """
    if providers is None:
        providers = _detect_available_providers()

    for provider in providers:
        _install_interceptor_for_provider(provider)


def _detect_available_providers() -> list[str]:
    """
    Auto-detect which SDK providers are installed.

    Returns:
        List of provider names that are installed
    """
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


def _ensure_interceptors_installed():
    """
    Ensure interceptors are installed for available SDKs.

    Called automatically when entering a memory context.
    Only installs interceptors that haven't been installed yet.
    """
    providers = _detect_available_providers()

    for provider in providers:
        if provider not in _INSTALLED_INTERCEPTORS:
            _install_interceptor_for_provider(provider)


def _install_interceptor_for_provider(provider: str):
    """
    Install interceptor for a specific provider.

    Args:
        provider: SDK provider name ("claude", "anthropic", "openai", "gemini")
    """
    global _INSTALLED_INTERCEPTORS

    if provider in _INSTALLED_INTERCEPTORS:
        return

    if provider == "claude":
        _install_claude_interceptor()
    elif provider == "anthropic":
        _install_anthropic_interceptor()
    elif provider == "openai":
        _install_openai_interceptor()
    elif provider == "gemini":
        _install_gemini_interceptor()
    else:
        return

    _INSTALLED_INTERCEPTORS.add(provider)
    print(f"[Letta Memory] ✅ Installed {provider} interceptor")


def _get_current_config() -> Optional[dict]:
    """Get the current active memory configuration (context-local)."""
    return _MEMORY_CONFIG.get()


def _is_memory_enabled() -> bool:
    """Check if memory is currently enabled (context-local)."""
    config = _get_current_config()
    return config is not None and config.get("enabled", False)


def _install_claude_interceptor():
    """
    Monkey-patch Claude Agent SDK's SubprocessCLITransport to intercept message flow.

    We patch:
    1. __init__ - to inject memory into system_prompt
    2. write() - to capture outgoing user messages
    3. read_messages() - to capture incoming assistant messages
    """
    try:
        from claude_agent_sdk._internal.transport.subprocess_cli import SubprocessCLITransport
    except ImportError:
        print("[Letta Memory] Claude Agent SDK not found, skipping interceptor installation")
        return

    # Save original methods (only once)
    if not hasattr(SubprocessCLITransport, '_original_init'):
        SubprocessCLITransport._original_init = SubprocessCLITransport.__init__
        SubprocessCLITransport._original_write = SubprocessCLITransport.write
        SubprocessCLITransport._original_read_messages = SubprocessCLITransport.read_messages

    # Patch __init__ to inject memory into system prompt
    def patched_init(self, *args, **kwargs):
        # Call original init first
        SubprocessCLITransport._original_init(self, *args, **kwargs)

        # Inject memory into system prompt if enabled
        if _is_memory_enabled():
            _inject_memory_into_options(self._options)

    # Patch write() to capture outgoing messages
    async def patched_write(self, data: str):
        # Capture user message
        if _is_memory_enabled():
            await _capture_outgoing_message(data)

        # Call original write
        return await SubprocessCLITransport._original_write(self, data)

    # Patch read_messages() to capture incoming messages
    def patched_read_messages(self):
        # Get original message iterator
        original_iterator = SubprocessCLITransport._original_read_messages(self)

        # Wrap it if memory is enabled
        if _is_memory_enabled():
            return _wrap_message_iterator(original_iterator)
        else:
            return original_iterator

    # Apply patches
    SubprocessCLITransport.__init__ = patched_init
    SubprocessCLITransport.write = patched_write
    SubprocessCLITransport.read_messages = patched_read_messages


def _install_anthropic_interceptor():
    """
    Monkey-patch Anthropic SDK's Messages API to intercept message flow.

    Instead of patching httpx (which is created before we can intercept it),
    we patch the Anthropic SDK's messages.create() method directly.
    """
    try:
        from anthropic.resources.messages import AsyncMessages
    except ImportError:
        print("[Letta Memory] Anthropic SDK not found, skipping interceptor installation")
        return

    # Save original method (only once)
    if not hasattr(AsyncMessages, '_original_create'):
        AsyncMessages._original_create = AsyncMessages.create

    # Patch AsyncMessages.create
    async def patched_create(self, **kwargs):
        # Inject memory and capture user message if memory is enabled
        if _is_memory_enabled():
            # Inject memory into request
            kwargs = await _inject_memory_into_anthropic_kwargs(kwargs)

            # Capture user message
            await _capture_anthropic_user_message_from_kwargs(kwargs)

        # Call original create
        response = await AsyncMessages._original_create(self, **kwargs)

        # Capture response if memory is enabled
        if _is_memory_enabled():
            if kwargs.get("stream", False):
                # Streaming: wrap the response to capture deltas
                return _wrap_anthropic_streaming_response(response)
            else:
                # Non-streaming: capture response
                await _capture_anthropic_message_response(response)

        return response

    # Apply patch
    AsyncMessages.create = patched_create


def _install_openai_interceptor():
    """
    Monkey-patch OpenAI SDK's Chat Completions API to intercept message flow.

    We patch the AsyncOpenAI.chat.completions.create() method directly.
    """
    try:
        from openai.resources.chat.completions import AsyncCompletions
    except ImportError:
        print("[Letta Memory] OpenAI SDK not found, skipping interceptor installation")
        return

    # Save original method (only once)
    if not hasattr(AsyncCompletions, '_original_create'):
        AsyncCompletions._original_create = AsyncCompletions.create

    # Patch AsyncCompletions.create
    async def patched_create(self, **kwargs):
        # Inject memory and capture user message if memory is enabled
        if _is_memory_enabled():
            # Inject memory into request
            kwargs = await _inject_memory_into_openai_kwargs(kwargs)

            # Capture user message
            await _capture_openai_user_message_from_kwargs(kwargs)

        # Call original create
        response = await AsyncCompletions._original_create(self, **kwargs)

        # Capture response if memory is enabled
        if _is_memory_enabled():
            if kwargs.get("stream", False):
                # Streaming: wrap the response to capture deltas
                return _wrap_openai_streaming_response(response)
            else:
                # Non-streaming: capture response
                await _capture_openai_completion_response(response)

        return response

    # Apply patch
    AsyncCompletions.create = patched_create


def _install_gemini_interceptor():
    """
    Monkey-patch Gemini SDK's GenerativeModel to intercept message flow.

    We patch the GenerativeModel.generate_content_async() method directly.
    """
    try:
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
            # Inject memory into contents
            contents = await _inject_memory_into_gemini_contents(contents, kwargs)

            # Capture user message
            await _capture_gemini_user_message(contents)

        # Call original method
        response = await GenerativeModel._original_generate_content_async(self, contents, **kwargs)

        # Capture response if memory is enabled
        if _is_memory_enabled():
            if kwargs.get("stream", False):
                # Streaming: wrap the response to capture deltas
                return _wrap_gemini_streaming_response(response)
            else:
                # Non-streaming: capture response
                await _capture_gemini_response(response)

        return response

    # Apply patch
    GenerativeModel.generate_content_async = patched_generate_content_async


async def _inject_memory_into_anthropic_kwargs(kwargs: dict) -> dict:
    """
    Inject memory into Anthropic messages.create() kwargs.

    Args:
        kwargs: Anthropic messages.create() kwargs

    Returns:
        Modified kwargs with memory injected
    """
    config = _get_current_config()
    if not config or config.get("capture_only", False):
        return kwargs

    # Get memory content
    agent_name = config["agent_name"]
    letta_client = config["letta_client"]

    if not letta_client:
        return kwargs

    try:
        # Fetch memory blocks
        agents = letta_client.agents.list(name=agent_name)
        if not agents or len(agents) == 0:
            return kwargs

        agent = agents[0]
        blocks = letta_client.agents.blocks.list(agent_id=agent.id)
        memory_context = _format_memory_blocks(blocks)

        if not memory_context:
            return kwargs

        # Inject into system parameter
        if "system" in kwargs:
            if isinstance(kwargs["system"], str):
                kwargs["system"] += f"\n\n## Previous Context from Letta Memory\n{memory_context}"
            elif isinstance(kwargs["system"], list):
                # System is a list of content blocks
                kwargs["system"].append({
                    "type": "text",
                    "text": f"\n\n## Previous Context from Letta Memory\n{memory_context}"
                })
        else:
            kwargs["system"] = f"## Previous Context from Letta Memory\n{memory_context}"

        print(f"[Letta Memory] Injected memory into request ({len(memory_context)} chars)")

    except Exception as e:
        print(f"[Letta Memory] Error injecting memory: {e}")
        import traceback
        traceback.print_exc()

    return kwargs


async def _capture_anthropic_user_message_from_kwargs(kwargs: dict):
    """
    Capture user message from Anthropic messages.create() kwargs.

    Args:
        kwargs: Anthropic messages.create() kwargs
    """
    config = _get_current_config()
    if not config:
        return

    try:
        if "messages" in kwargs:
            messages = kwargs["messages"]

            # Get last user message
            for msg in reversed(messages):
                if msg.get("role") == "user":
                    content = msg.get("content", "")
                    if isinstance(content, str):
                        config["pending_user_message"] = content
                    elif isinstance(content, list):
                        # Handle multi-modal content
                        text_parts = [c.get("text", "") for c in content if c.get("type") == "text"]
                        combined = " ".join(text_parts)
                        config["pending_user_message"] = combined
                    break

    except Exception as e:
        print(f"[Letta Memory] Error capturing user message: {e}")
        import traceback
        traceback.print_exc()


async def _capture_anthropic_message_response(response):
    """
    Capture non-streaming Anthropic Message response and save to Letta.

    Args:
        response: Anthropic Message response object
    """
    config = _get_current_config()
    if not config:
        return

    try:
        # Extract assistant message from Anthropic Message response
        # Response format: Message(content=[ContentBlock(type='text', text='...')], ...)
        text_parts = []

        for block in response.content:
            if hasattr(block, 'type') and block.type == "text":
                if hasattr(block, 'text'):
                    text_parts.append(block.text)

        assistant_message = " ".join(text_parts)

        if assistant_message:
            # Save conversation turn (non-blocking)
            asyncio.create_task(
                _save_conversation_turn(
                    user_message=config.get("pending_user_message"),
                    assistant_message=assistant_message
                )
            )

            # Clear buffer
            config["pending_user_message"] = None

    except Exception as e:
        print(f"[Letta Memory] Error capturing response: {e}")
        import traceback
        traceback.print_exc()


class _AnthropicStreamWrapper:
    """
    Wrapper for Anthropic streaming responses that captures text deltas.

    This class wraps the AsyncStream returned by Anthropic SDK and:
    1. Passes through all events to the consumer
    2. Captures text deltas from content_block_delta events
    3. Saves accumulated text to Letta when stream is exhausted
    """

    def __init__(self, stream):
        self._stream = stream
        self._accumulated_text = []

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            # Get next event from original stream
            event = await self._stream.__anext__()

            # Capture text deltas from content_block_delta events
            if hasattr(event, 'type') and event.type == "content_block_delta":
                if hasattr(event, 'delta') and hasattr(event.delta, 'text'):
                    self._accumulated_text.append(event.delta.text)

            return event

        except StopAsyncIteration:
            # Stream is complete, save accumulated text
            await self._save_accumulated_text()
            raise

    async def _save_accumulated_text(self):
        """Save accumulated text to Letta when streaming is complete."""
        if not self._accumulated_text:
            return

        config = _get_current_config()
        if not config:
            return

        assistant_message = "".join(self._accumulated_text)

        # Save conversation turn (non-blocking)
        asyncio.create_task(
            _save_conversation_turn(
                user_message=config.get("pending_user_message"),
                assistant_message=assistant_message
            )
        )

        # Clear buffer
        config["pending_user_message"] = None


def _wrap_anthropic_streaming_response(stream):
    """
    Wrap Anthropic streaming response to capture assistant messages.

    Args:
        stream: Anthropic AsyncStream[MessageStreamEvent]

    Returns:
        Wrapped async iterator that captures text deltas
    """
    return _AnthropicStreamWrapper(stream)


# ============================================================================
# OpenAI SDK Integration
# ============================================================================

async def _inject_memory_into_openai_kwargs(kwargs: dict) -> dict:
    """
    Inject memory into OpenAI chat.completions.create() kwargs.

    Args:
        kwargs: OpenAI chat.completions.create() kwargs

    Returns:
        Modified kwargs with memory injected
    """
    config = _get_current_config()
    if not config or config.get("capture_only", False):
        return kwargs

    # Get memory content
    agent_name = config["agent_name"]
    letta_client = config["letta_client"]

    if not letta_client:
        return kwargs

    try:
        # Fetch memory blocks
        agents = letta_client.agents.list(name=agent_name)
        if not agents or len(agents) == 0:
            return kwargs

        agent = agents[0]
        blocks = letta_client.agents.blocks.list(agent_id=agent.id)
        memory_context = _format_memory_blocks(blocks)

        if not memory_context:
            return kwargs

        # Inject into messages array as a system message
        if "messages" in kwargs:
            messages = kwargs["messages"]

            # Insert memory as system message at the beginning
            memory_message = {
                "role": "system",
                "content": f"## Previous Context from Letta Memory\n{memory_context}"
            }

            # If there's already a system message at the start, append to it
            if messages and messages[0].get("role") == "system":
                messages[0]["content"] += f"\n\n{memory_message['content']}"
            else:
                # Insert at the beginning
                kwargs["messages"] = [memory_message] + messages

        print(f"[Letta Memory] Injected memory into request ({len(memory_context)} chars)")

    except Exception as e:
        print(f"[Letta Memory] Error injecting memory: {e}")
        import traceback
        traceback.print_exc()

    return kwargs


async def _capture_openai_user_message_from_kwargs(kwargs: dict):
    """
    Capture user message from OpenAI chat.completions.create() kwargs.

    Args:
        kwargs: OpenAI chat.completions.create() kwargs
    """
    config = _get_current_config()
    if not config:
        return

    try:
        if "messages" in kwargs:
            messages = kwargs["messages"]

            # Get last user message
            for msg in reversed(messages):
                if msg.get("role") == "user":
                    content = msg.get("content", "")
                    if isinstance(content, str):
                        config["pending_user_message"] = content
                    elif isinstance(content, list):
                        # Handle multi-modal content
                        text_parts = [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"]
                        combined = " ".join(text_parts)
                        config["pending_user_message"] = combined
                    break

    except Exception as e:
        print(f"[Letta Memory] Error capturing user message: {e}")
        import traceback
        traceback.print_exc()


async def _capture_openai_completion_response(response):
    """
    Capture non-streaming OpenAI ChatCompletion response and save to Letta.

    Args:
        response: OpenAI ChatCompletion response object
    """
    config = _get_current_config()
    if not config:
        return

    try:
        # Extract assistant message from ChatCompletion response
        # Response format: ChatCompletion(choices=[Choice(message=ChatCompletionMessage(content='...'))])
        if hasattr(response, 'choices') and response.choices:
            choice = response.choices[0]
            if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
                assistant_message = choice.message.content

                if assistant_message:
                    # Save conversation turn (non-blocking)
                    asyncio.create_task(
                        _save_conversation_turn(
                            user_message=config.get("pending_user_message"),
                            assistant_message=assistant_message
                        )
                    )

                    # Clear buffer
                    config["pending_user_message"] = None

    except Exception as e:
        print(f"[Letta Memory] Error capturing response: {e}")
        import traceback
        traceback.print_exc()


class _OpenAIStreamWrapper:
    """
    Wrapper for OpenAI streaming responses that captures text deltas.

    This class wraps the AsyncStream returned by OpenAI SDK and:
    1. Passes through all chunks to the consumer
    2. Captures text deltas from chunk.choices[0].delta.content
    3. Saves accumulated text to Letta when stream is exhausted
    """

    def __init__(self, stream):
        self._stream = stream
        self._accumulated_text = []

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            # Get next chunk from original stream
            chunk = await self._stream.__anext__()

            # Capture text deltas from chunks
            if hasattr(chunk, 'choices') and chunk.choices:
                choice = chunk.choices[0]
                if hasattr(choice, 'delta') and hasattr(choice.delta, 'content'):
                    if choice.delta.content is not None:
                        self._accumulated_text.append(choice.delta.content)

            return chunk

        except StopAsyncIteration:
            # Stream is complete, save accumulated text
            await self._save_accumulated_text()
            raise

    async def _save_accumulated_text(self):
        """Save accumulated text to Letta when streaming is complete."""
        if not self._accumulated_text:
            return

        config = _get_current_config()
        if not config:
            return

        assistant_message = "".join(self._accumulated_text)

        # Save conversation turn (non-blocking)
        asyncio.create_task(
            _save_conversation_turn(
                user_message=config.get("pending_user_message"),
                assistant_message=assistant_message
            )
        )

        # Clear buffer
        config["pending_user_message"] = None


def _wrap_openai_streaming_response(stream):
    """
    Wrap OpenAI streaming response to capture assistant messages.

    Args:
        stream: OpenAI AsyncStream[ChatCompletionChunk]

    Returns:
        Wrapped async iterator that captures text deltas
    """
    return _OpenAIStreamWrapper(stream)


# ============================================================================
# Gemini SDK Integration
# ============================================================================

async def _inject_memory_into_gemini_contents(contents, kwargs: dict):
    """
    Inject memory into Gemini generate_content_async() contents.

    Args:
        contents: Gemini contents (can be string, list, or Content objects)
        kwargs: Additional kwargs (for checking stream mode, etc.)

    Returns:
        Modified contents with memory injected
    """
    config = _get_current_config()
    if not config or config.get("capture_only", False):
        return contents

    # Get memory content
    agent_name = config["agent_name"]
    letta_client = config["letta_client"]

    if not letta_client:
        return contents

    try:
        # Fetch memory blocks
        agents = letta_client.agents.list(name=agent_name)
        if not agents or len(agents) == 0:
            return contents

        agent = agents[0]
        blocks = letta_client.agents.blocks.list(agent_id=agent.id)
        memory_context = _format_memory_blocks(blocks)

        if not memory_context:
            return contents

        # Normalize contents to list format
        # Gemini accepts: str, list of dicts, list of Content objects
        if isinstance(contents, str):
            # Convert string to list format
            contents = [
                {"role": "user", "parts": [f"## Previous Context from Letta Memory\n{memory_context}"]},
                {"role": "user", "parts": [contents]}
            ]
        elif isinstance(contents, list):
            # Prepend memory as first user message
            memory_content = {
                "role": "user",
                "parts": [f"## Previous Context from Letta Memory\n{memory_context}"]
            }
            contents = [memory_content] + contents
        else:
            # For other formats (Content objects), convert to string and inject
            # This is a fallback - most usage will be string or list
            contents = [
                {"role": "user", "parts": [f"## Previous Context from Letta Memory\n{memory_context}"]},
                contents
            ]

        print(f"[Letta Memory] Injected memory into request ({len(memory_context)} chars)")

    except Exception as e:
        print(f"[Letta Memory] Error injecting memory: {e}")
        import traceback
        traceback.print_exc()

    return contents


async def _capture_gemini_user_message(contents):
    """
    Capture user message from Gemini contents.

    Args:
        contents: Gemini contents (string, list of dicts, or Content objects)
    """
    config = _get_current_config()
    if not config:
        return

    try:
        # Handle different content formats
        if isinstance(contents, str):
            config["pending_user_message"] = contents
        elif isinstance(contents, list):
            # Find last user message in list
            for content in reversed(contents):
                if isinstance(content, dict):
                    if content.get("role") == "user":
                        parts = content.get("parts", [])
                        # Combine all text parts
                        text_parts = [p for p in parts if isinstance(p, str)]
                        if text_parts:
                            config["pending_user_message"] = " ".join(text_parts)
                            break
                elif isinstance(content, str):
                    config["pending_user_message"] = content
                    break
                elif hasattr(content, 'parts'):
                    # Content object
                    text_parts = [p.text for p in content.parts if hasattr(p, 'text')]
                    if text_parts:
                        config["pending_user_message"] = " ".join(text_parts)
                        break

    except Exception as e:
        print(f"[Letta Memory] Error capturing user message: {e}")
        import traceback
        traceback.print_exc()


async def _capture_gemini_response(response):
    """
    Capture non-streaming Gemini response and save to Letta.

    Args:
        response: Gemini GenerateContentResponse object
    """
    config = _get_current_config()
    if not config:
        return

    try:
        # Extract text from response
        # Response has a .text property for convenience
        assistant_message = None

        if hasattr(response, 'text'):
            assistant_message = response.text
        elif hasattr(response, 'candidates') and response.candidates:
            # Fallback: extract from candidates
            candidate = response.candidates[0]
            if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                text_parts = [part.text for part in candidate.content.parts if hasattr(part, 'text')]
                assistant_message = "".join(text_parts)

        if assistant_message:
            # Save conversation turn (non-blocking)
            asyncio.create_task(
                _save_conversation_turn(
                    user_message=config.get("pending_user_message"),
                    assistant_message=assistant_message
                )
            )

            # Clear buffer
            config["pending_user_message"] = None

    except Exception as e:
        print(f"[Letta Memory] Error capturing response: {e}")
        import traceback
        traceback.print_exc()


class _GeminiStreamWrapper:
    """
    Wrapper for Gemini streaming responses that captures text deltas.

    This class wraps the async iterator returned by Gemini SDK and:
    1. Passes through all chunks to the consumer
    2. Captures text from each chunk
    3. Saves accumulated text to Letta when stream is exhausted
    """

    def __init__(self, stream):
        self._stream_iterable = stream
        self._stream = None  # Will be set in __aiter__
        self._accumulated_text = []

    def __aiter__(self):
        # Get the actual iterator from the async iterable
        self._stream = self._stream_iterable.__aiter__()
        return self

    async def __anext__(self):
        try:
            # Get next chunk from original stream
            chunk = await self._stream.__anext__()

            # Capture text from chunk
            # Gemini chunks have a .text property
            if hasattr(chunk, 'text') and chunk.text:
                self._accumulated_text.append(chunk.text)

            return chunk

        except StopAsyncIteration:
            # Stream is complete, save accumulated text
            await self._save_accumulated_text()
            raise

    async def _save_accumulated_text(self):
        """Save accumulated text to Letta when streaming is complete."""
        if not self._accumulated_text:
            return

        config = _get_current_config()
        if not config:
            return

        assistant_message = "".join(self._accumulated_text)

        # Save conversation turn (non-blocking)
        asyncio.create_task(
            _save_conversation_turn(
                user_message=config.get("pending_user_message"),
                assistant_message=assistant_message
            )
        )

        # Clear buffer
        config["pending_user_message"] = None


def _wrap_gemini_streaming_response(stream):
    """
    Wrap Gemini streaming response to capture assistant messages.

    Args:
        stream: Gemini async iterator

    Returns:
        Wrapped async iterator that captures text
    """
    return _GeminiStreamWrapper(stream)


async def _create_agent_async(letta_client, agent_name: str):
    """
    Create a Letta agent asynchronously (non-blocking).

    Args:
        letta_client: Letta client instance
        agent_name: Name of the agent to create
    """
    try:
        print(f"[Letta Memory] Creating agent '{agent_name}' in background...")
        agent = letta_client.agents.create(
            name=agent_name,
            agent_type="sleeptime_agent",
            memory_blocks=[
                {
                    "value": "",
                    "label": "human",
                },
            ],
            model="openai/gpt-4o-mini",
            embedding="openai/text-embedding-3-small",
        )
        print(f"[Letta Memory] ✅ Created agent: {agent.id}")
    except Exception as e:
        print(f"[Letta Memory] Error creating agent: {e}")
        import traceback
        traceback.print_exc()


def _inject_memory_into_options(options):
    """
    Inject Letta memory into the Claude Agent options system prompt.

    This retrieves relevant context from Letta and adds it to the system prompt
    so Claude is aware of previous conversations.
    """
    config = _get_current_config()
    if not config:
        return

    # Check if capture_only is enabled
    if config.get("capture_only", True):
        return

    agent_name = config["agent_name"]
    letta_client = config["letta_client"]

    # If no Letta client provided, skip memory injection
    if not letta_client:
        return

    try:
        # Step 1: Check if agent exists (non-blocking check)
        agents = letta_client.agents.list(name=agent_name)

        # Step 2: If agent doesn't exist, create it asynchronously and return early
        if not agents or len(agents) == 0:
            # Create agent in background, don't wait for it
            asyncio.create_task(_create_agent_async(letta_client, agent_name))
            return

        # Step 3: Agent exists, proceed with memory injection
        agent = agents[0]

        # Fetch memory blocks for this agent
        blocks = letta_client.agents.blocks.list(agent_id=agent.id)

        # Format memory blocks into context string
        memory_context = _format_memory_blocks(blocks)

        if not memory_context:
            return

        # Inject into system prompt
        if options.system_prompt:
            # Append to existing system prompt
            if isinstance(options.system_prompt, str):
                options.system_prompt += f"\n\n## Previous Context from Letta Memory\n{memory_context}"
            # Handle dict-style system prompts
            elif isinstance(options.system_prompt, dict) and "append" in options.system_prompt:
                options.system_prompt["append"] += f"\n\n## Previous Context from Letta Memory\n{memory_context}"
        else:
            # Create new system prompt
            options.system_prompt = f"## Previous Context from Letta Memory\n{memory_context}"

        print(f"[Letta Memory] Injected memory into request ({len(memory_context)} chars)")

    except Exception as e:
        # Don't crash if memory injection fails - just log and continue
        print(f"[Letta Memory] Error injecting memory: {e}")
        import traceback
        traceback.print_exc()


def _format_memory_blocks(blocks) -> str:
    """
    Format memory blocks into a readable context string.

    Args:
        blocks: List of memory block objects from Letta

    Returns:
        Formatted string containing memory block contents
    """
    if not blocks:
        return ""

    formatted_lines = []
    """
    </base_instructions>\n\n<memory_blocks>\nThe following memory blocks are currently engaged in your core memory unit:\n\n<human>\n<description>\nThe human block: Stores key details about the person you are conversing with, allowing for more personalized and friend-like conversation.\n</description>\n<metadata>\n- chars_current=66\n- chars_limit=20000\n</metadata>\n<value>\n# NOTE: Line numbers shown below are to help during editing. Do NOT include line number prefixes in your memory edit tool calls.\nLine 1: User\'s first login occurred on October 15, 2025, at 12:01 AM UTC.\nLine 2: \n</value>\n</human>\n\n</memory_blocks>
    """

    for block in blocks:
        if not block or not block.value:
            continue

        formatted_lines.append(f"<{block.label}>")
        if block.description:
            formatted_lines.append(f"<description>{block.description}</description>")
        formatted_lines.append(f"<value>{block.value}</value>")
        formatted_lines.append(f"</{block.label}>")

    if not formatted_lines:
        return ""

    memory_system_message = "\n".join(formatted_lines)
    return f"<memory_blocks>\nThe following memory blocks are currently engaged in your core memory unit:\n{memory_system_message}\n</memory_blocks>"



async def _capture_outgoing_message(data: str):
    """
    Capture user messages and buffer them for batching.

    Instead of saving immediately, we buffer the user message and send it together
    with the assistant response in a single API call.

    Args:
        data: JSON string being sent to the Claude subprocess
    """
    try:
        # Parse the JSON message
        message = json.loads(data)
        msg_type = message.get('type')

        # Buffer user messages for batching
        if msg_type == "user":
            # Structure: {"type": "user", "message": {"role": "user", "content": "..."}}
            user_message = message.get("message", {})
            content = user_message.get("content", "")

            if content:
                # Buffer the user message instead of saving immediately
                config = _get_current_config()
                if config:
                    config["pending_user_message"] = content

    except json.JSONDecodeError:
        pass
    except Exception as e:
        print(f"[Letta Memory] Error capturing message: {e}")


async def _wrap_message_iterator(original_iterator: AsyncIterator[dict]) -> AsyncIterator[dict]:
    """
    Wrap the message iterator to accumulate and save assistant responses.

    This generator:
    1. Yields each message immediately (pass-through for streaming)
    2. Accumulates assistant text messages
    3. Saves accumulated text to Letta when done

    Args:
        original_iterator: Original async iterator from Transport.read_messages()

    Yields:
        Same messages as original iterator
    """
    accumulated_text = []

    try:
        async for message in original_iterator:
            msg_type = message.get("type", "unknown")

            # Accumulate assistant text
            if msg_type == "assistant":
                # Structure: {"type": "assistant", "message": {"content": [{"type": "text", "text": "..."}]}}
                assistant_message = message.get("message", {})
                content_blocks = assistant_message.get("content", [])

                for block in content_blocks:
                    if block.get("type") == "text":
                        text = block.get("text", "")
                        if text:
                            accumulated_text.append(text)

            # Always yield immediately for streaming
            yield message

    finally:
        # Batch save user message + assistant response to Letta
        config = _get_current_config()
        if not config:
            return

        # Get the buffered user message
        user_message = config.get("pending_user_message")
        assistant_message = "".join(accumulated_text) if accumulated_text else None

        # Only save if we have at least one message
        if user_message or assistant_message:
            # Batch both messages into a single API call
            asyncio.create_task(
                _save_conversation_turn(
                    user_message=user_message,
                    assistant_message=assistant_message
                )
            )

            # Clear the buffer
            config["pending_user_message"] = None


async def _save_conversation_turn(user_message: str = None, assistant_message: str = None):
    """
    Save a conversation turn (user + assistant messages) to Letta in a single API call.

    This batches both messages together to reduce API calls from 2 per turn to 1 per turn.

    Args:
        user_message: Optional user message content
        assistant_message: Optional assistant message content
    """
    config = _get_current_config()
    if not config:
        return

    agent_name = config["agent_name"]
    letta_client = config["letta_client"]

    if not letta_client:
        return

    # Build the combined message content
    parts = []
    if user_message:
        parts.append(f"user: {user_message}")
    if assistant_message:
        parts.append(f"assistant: {assistant_message}")

    if not parts:
        return

    combined_content = "\n\n".join(parts)

    try:
        # Check if agent exists
        agents = letta_client.agents.list(name=agent_name)

        # If agent doesn't exist, create it (we're already async, so safe to block here)
        if not agents or len(agents) == 0:
            print(f"[Letta Memory] Creating agent '{agent_name}'...")
            agent = letta_client.agents.create(
                name=agent_name,
                agent_type="sleeptime_agent",
                memory_blocks=[
                    {
                        "value": "",
                        "label": "human",
                    },
                ],
                model="openai/gpt-4o-mini",
                embedding="openai/text-embedding-3-small",
            )
            print(f"[Letta Memory] ✅ Created agent: {agent.id}")
        else:
            agent = agents[0]

        # Save the batched conversation turn to Letta (single API call)
        letta_client.agents.messages.create(
            agent_id=agent.id,
            messages=[{
                "role": "user",
                "content": combined_content
            }]
        )
        print(f"[Letta Memory] ✅ Saved conversation to agent {agent.id}")

    except Exception as e:
        print(f"[Letta Memory] Error saving to Letta: {e}")
        import traceback
        traceback.print_exc()


# Helper functions for debugging
def is_memory_enabled() -> bool:
    """Check if memory integration is currently enabled."""
    return _is_memory_enabled()


def get_memory_config() -> Optional[dict]:
    """Get current memory configuration (for debugging)."""
    return _get_current_config()
