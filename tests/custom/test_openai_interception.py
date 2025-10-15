"""
Test script to verify OpenAI SDK memory integration is working.

This tests both non-streaming and streaming cases.
"""

import asyncio
import sys
import os

# Add the src directory to path so we can import from letta_client
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from letta_client.memory import memory
from letta_client.client import Letta


async def test_openai_non_streaming():
    """Test OpenAI SDK with non-streaming responses."""
    print("=== Testing OpenAI SDK Non-Streaming Memory Integration ===")
    print("Goal: Verify memory capture and cross-session recall\n")

    # Check if OpenAI SDK is installed
    try:
        from openai import AsyncOpenAI
    except ImportError:
        print("❌ OpenAI SDK not installed. Install with: pip install openai")
        return

    # For local Letta server (default: http://localhost:8283)
    letta_client = Letta(base_url="http://localhost:8283", token=None)

    # For Letta Cloud
    # letta_client = Letta(token=os.getenv("LETTA_API_KEY"))

    try:
        # ========================================
        # SESSION 1: Introduce myself
        # ========================================
        print("=== SESSION 1: First OpenAI SDK session ===\n")

        # Create OpenAI client
        openai_client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        print("[Test] Sending query: 'My name is Alice. Hello!'")

        async with memory(agent="openai_test_agent", client=letta_client):
            response = await openai_client.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": "My name is Alice. Hello!"}
                ]
            )

            # Print response
            print("[Test] Response:")
            response_text = response.choices[0].message.content
            print(f"  {response_text}")

            print("\n[Test] ✅ Session 1 complete")

        # Wait a moment for memory to be saved
        print("[Test] Waiting for memory to be saved...")
        await asyncio.sleep(2)

        # ========================================
        # SESSION 2: New session - test memory recall
        # ========================================
        print("\n=== SESSION 2: New session (testing memory recall) ===\n")
        print("[Test] Sending query: 'What is my name?'")

        async with memory(agent="openai_test_agent", client=letta_client):
            response = await openai_client.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": "What is my name?"}
                ]
            )

            # Print response - should remember "Alice"
            print("[Test] Response:")
            response_text = response.choices[0].message.content
            print(f"  {response_text}")

            # Check if it remembered "Alice"
            if "alice" in response_text.lower():
                print("\n✅ SUCCESS: GPT remembered 'Alice' from Session 1!")
            else:
                print("\n⚠️  WARNING: GPT did not mention 'Alice' - memory may not have been injected")

        # ========================================
        # Inspect memory
        # ========================================
        print(f"\n=== Memory Inspection ===")
        memory_content = letta_client.memory.retrieve(agent="openai_test_agent")
        print(f"Memory size: {len(memory_content)} chars")

        if len(memory_content) > 0:
            print(f"\n✅ NON-STREAMING TEST PASSED: Memory was captured and persisted!")
            print(f"\nMemory content preview:")
            print(memory_content[:500] + "..." if len(memory_content) > 500 else memory_content)
        else:
            print("\n❌ NON-STREAMING TEST FAILED: No memory was saved")

    except Exception as e:
        print(f"\n❌ NON-STREAMING TEST FAILED: {e}")
        import traceback
        traceback.print_exc()


async def test_openai_streaming():
    """Test OpenAI SDK with streaming responses."""
    print("\n\n=== Testing OpenAI SDK Streaming Memory Integration ===")
    print("Goal: Verify streaming responses are captured and saved to Letta\n")

    try:
        from openai import AsyncOpenAI
    except ImportError:
        print("❌ OpenAI SDK not installed")
        return

    letta_client = Letta(base_url="http://localhost:8283", token=None)
    openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        # ========================================
        # SESSION 1: Send streaming request
        # ========================================
        print("=== SESSION 1: Streaming request ===\n")
        print("[Test] Sending streaming query: 'My favorite animal is a dog. Count to 5.'")

        async with memory(agent="openai_streaming_agent", client=letta_client):
            stream = await openai_client.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": "My favorite animal is a dog. Count to 5."}
                ],
                stream=True
            )

            print("[Test] Receiving streaming response:")
            captured_text = []
            async for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    text = chunk.choices[0].delta.content
                    captured_text.append(text)
                    print(text, end="", flush=True)

            final_response = "".join(captured_text)
            print(f"\n\n[Test] ✅ Streaming complete ({len(final_response)} chars received)")

        # Wait for memory to be saved
        print("[Test] Waiting for memory to be saved...")
        await asyncio.sleep(2)

        # ========================================
        # SESSION 2: Test memory recall
        # ========================================
        print("\n=== SESSION 2: Testing memory recall ===\n")
        print("[Test] Sending query: 'What is my favorite animal?'")

        async with memory(agent="openai_streaming_agent", client=letta_client):
            response = await openai_client.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": "What is my favorite animal?"}
                ]
            )

            response_text = response.choices[0].message.content
            print(f"[Test] Response: {response_text}")

            # Check if it remembered "dog"
            if "dog" in response_text.lower():
                print("\n✅ SUCCESS: GPT remembered 'dog' from streaming session!")
            else:
                print("\n⚠️  WARNING: GPT did not mention 'dog' - memory may not have been captured")

        # ========================================
        # Inspect memory
        # ========================================
        print(f"\n=== Memory Inspection ===")
        memory_content = letta_client.memory.retrieve(agent="openai_streaming_agent")
        print(f"Memory size: {len(memory_content)} chars")

        if len(memory_content) > 0:
            print(f"\n✅ STREAMING TEST PASSED: Memory was captured from streaming response!")
            print(f"\nMemory content preview:")
            print(memory_content[:500] + "..." if len(memory_content) > 500 else memory_content)
        else:
            print("\n❌ STREAMING TEST FAILED: No memory was saved")

    except Exception as e:
        print(f"\n❌ STREAMING TEST FAILED: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("=" * 70)
    print("=== OpenAI SDK Cross-Session Memory Integration Tests ===")
    print("=" * 70)
    print("\nThis test suite will verify:")
    print("  1. Non-streaming: Memory capture and recall across sessions")
    print("  2. Streaming: Memory capture from streaming responses")
    print("  3. Memory persistence in Letta agents")
    print()

    async def run_all_tests():
        await test_openai_non_streaming()
        await test_openai_streaming()

        print("\n" + "=" * 70)
        print("=== All Tests Complete ===")
        print("=" * 70)

    asyncio.run(run_all_tests())
