"""
Unit test for Anthropic streaming wrapper.

This test verifies the streaming wrapper captures text deltas correctly
without requiring actual API calls.
"""

import asyncio
import sys
import os

# Add the src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from letta_client.memory import memory
from letta_client.client import Letta


class MockStreamEvent:
    """Mock Anthropic streaming event."""

    def __init__(self, event_type, text=None):
        self.type = event_type
        if text is not None:
            self.delta = MockDelta(text)


class MockDelta:
    """Mock Anthropic delta object."""

    def __init__(self, text):
        self.text = text


class MockAsyncStream:
    """Mock Anthropic AsyncStream that simulates streaming events."""

    def __init__(self, events):
        self.events = events
        self.index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.index >= len(self.events):
            raise StopAsyncIteration

        event = self.events[self.index]
        self.index += 1
        return event


async def test_streaming_wrapper():
    """Test that the streaming wrapper captures text correctly."""
    print("=== Testing Anthropic Streaming Wrapper ===\n")

    from letta_client.memory import _AnthropicStreamWrapper, _MEMORY_CONFIG

    # Set up a mock memory context
    _MEMORY_CONFIG.set({
        "agent_name": "test_agent",
        "letta_client": None,  # Not needed for this test
        "enabled": True,
        "capture_only": False,
        "pending_user_message": "Count to 3"
    })

    # Create mock stream with events
    events = [
        MockStreamEvent("message_start"),
        MockStreamEvent("content_block_start"),
        MockStreamEvent("content_block_delta", "1"),
        MockStreamEvent("content_block_delta", ", "),
        MockStreamEvent("content_block_delta", "2"),
        MockStreamEvent("content_block_delta", ", "),
        MockStreamEvent("content_block_delta", "3"),
        MockStreamEvent("content_block_stop"),
        MockStreamEvent("message_stop"),
    ]

    mock_stream = MockAsyncStream(events)
    wrapper = _AnthropicStreamWrapper(mock_stream)

    # Consume the stream
    print("[Test] Consuming wrapped stream...")
    accumulated = []
    event_count = 0

    async for event in wrapper:
        event_count += 1
        print(f"[Test] Received event: {event.type}")

        # Simulate user consuming text deltas
        if event.type == "content_block_delta" and hasattr(event, 'delta'):
            accumulated.append(event.delta.text)
            print(f"[Test] Text delta: '{event.delta.text}'")

    # Check results
    final_text = "".join(accumulated)
    print(f"\n[Test] Total events: {event_count}")
    print(f"[Test] Accumulated text: '{final_text}'")

    # Verify
    expected_text = "1, 2, 3"
    if final_text == expected_text:
        print(f"\n✅ SUCCESS: Wrapper captured text correctly!")
        print(f"   Expected: '{expected_text}'")
        print(f"   Got:      '{final_text}'")
        return True
    else:
        print(f"\n❌ FAILURE: Text mismatch!")
        print(f"   Expected: '{expected_text}'")
        print(f"   Got:      '{final_text}'")
        return False


async def test_streaming_wrapper_with_memory_disabled():
    """Test that wrapper still works when memory is disabled."""
    print("\n\n=== Testing Wrapper with Memory Disabled ===\n")

    from letta_client.memory import _AnthropicStreamWrapper, _MEMORY_CONFIG

    # Disable memory
    _MEMORY_CONFIG.set(None)

    # Create mock stream
    events = [
        MockStreamEvent("content_block_delta", "Hello"),
        MockStreamEvent("content_block_delta", " world"),
    ]

    mock_stream = MockAsyncStream(events)
    wrapper = _AnthropicStreamWrapper(mock_stream)

    # Consume the stream
    print("[Test] Consuming wrapped stream (memory disabled)...")
    accumulated = []

    async for event in wrapper:
        if event.type == "content_block_delta" and hasattr(event, 'delta'):
            accumulated.append(event.delta.text)

    final_text = "".join(accumulated)
    print(f"[Test] Accumulated text: '{final_text}'")

    if final_text == "Hello world":
        print("\n✅ SUCCESS: Wrapper works correctly with memory disabled!")
        return True
    else:
        print("\n❌ FAILURE: Unexpected text")
        return False


if __name__ == "__main__":
    async def run_all_tests():
        test1 = await test_streaming_wrapper()
        test2 = await test_streaming_wrapper_with_memory_disabled()

        print("\n" + "="*50)
        if test1 and test2:
            print("✅ ALL TESTS PASSED")
        else:
            print("❌ SOME TESTS FAILED")
        print("="*50)

    asyncio.run(run_all_tests())
