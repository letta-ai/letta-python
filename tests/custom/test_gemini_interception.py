"""
Test script to verify Gemini SDK memory integration is working.

This tests both non-streaming and streaming cases.
"""

import asyncio
import sys
import os

# Add the src directory to path so we can import from letta_client
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from letta_client.memory import memory
from letta_client.client import Letta


async def test_gemini_non_streaming():
    """Test Gemini SDK with non-streaming responses."""
    print("=== Testing Gemini SDK Non-Streaming Memory Integration ===")
    print("Goal: Verify memory capture and cross-session recall\n")

    # Check if Gemini SDK is installed
    try:
        import google.generativeai as genai
    except ImportError:
        print("❌ Gemini SDK not installed. Install with: pip install google-generativeai")
        return

    # For local Letta server (default: http://localhost:8283)
    letta_client = Letta(base_url="http://localhost:8283", token=None)

    # For Letta Cloud
    # letta_client = Letta(token=os.getenv("LETTA_API_KEY"))

    try:
        # ========================================
        # SESSION 1: Introduce myself
        # ========================================
        print("=== SESSION 1: First Gemini SDK session ===\n")

        # Configure Gemini
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-2.5-flash')

        print("[Test] Sending query: 'My name is Bob. Hello!'")

        async with memory(agent="gemini_test_agent", client=letta_client):
            response = await model.generate_content_async("My name is Bob. Hello!")

            # Print response
            print("[Test] Response:")
            response_text = response.text
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

        async with memory(agent="gemini_test_agent", client=letta_client):
            response = await model.generate_content_async("What is my name?")

            # Print response - should remember "Bob"
            print("[Test] Response:")
            response_text = response.text
            print(f"  {response_text}")

            # Check if it remembered "Bob"
            if "bob" in response_text.lower():
                print("\n✅ SUCCESS: Gemini remembered 'Bob' from Session 1!")
            else:
                print("\n⚠️  WARNING: Gemini did not mention 'Bob' - memory may not have been injected")

        # ========================================
        # Inspect memory
        # ========================================
        print(f"\n=== Memory Inspection ===")
        memory_content = letta_client.memory.retrieve(agent="gemini_test_agent")
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


async def test_gemini_streaming():
    """Test Gemini SDK with streaming responses."""
    print("\n\n=== Testing Gemini SDK Streaming Memory Integration ===")
    print("Goal: Verify streaming responses are captured and saved to Letta\n")

    try:
        import google.generativeai as genai
    except ImportError:
        print("❌ Gemini SDK not installed")
        return

    letta_client = Letta(base_url="http://localhost:8283", token=None)

    try:
        # ========================================
        # SESSION 1: Send streaming request
        # ========================================
        print("=== SESSION 1: Streaming request ===\n")
        print("[Test] Sending streaming query: 'My favorite food is pizza. Count to 5.'")

        # Configure Gemini
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-2.5-flash')

        async with memory(agent="gemini_streaming_agent", client=letta_client):
            response = await model.generate_content_async(
                "My favorite food is pizza. Count to 5.",
                stream=True
            )

            print("[Test] Receiving streaming response:")
            captured_text = []
            async for chunk in response:
                if chunk.text:
                    captured_text.append(chunk.text)
                    print(chunk.text, end="", flush=True)

            final_response = "".join(captured_text)
            print(f"\n\n[Test] ✅ Streaming complete ({len(final_response)} chars received)")

        # Wait for memory to be saved
        print("[Test] Waiting for memory to be saved...")
        await asyncio.sleep(2)

        # ========================================
        # SESSION 2: Test memory recall
        # ========================================
        print("\n=== SESSION 2: Testing memory recall ===\n")
        print("[Test] Sending query: 'What is my favorite food?'")

        async with memory(agent="gemini_streaming_agent", client=letta_client):
            response = await model.generate_content_async("What is my favorite food?")

            response_text = response.text
            print(f"[Test] Response: {response_text}")

            # Check if it remembered "pizza"
            if "pizza" in response_text.lower():
                print("\n✅ SUCCESS: Gemini remembered 'pizza' from streaming session!")
            else:
                print("\n⚠️  WARNING: Gemini did not mention 'pizza' - memory may not have been captured")

        # ========================================
        # Inspect memory
        # ========================================
        print(f"\n=== Memory Inspection ===")
        memory_content = letta_client.memory.retrieve(agent="gemini_streaming_agent")
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
    print("=== Gemini SDK Cross-Session Memory Integration Tests ===")
    print("=" * 70)
    print("\nThis test suite will verify:")
    print("  1. Non-streaming: Memory capture and recall across sessions")
    print("  2. Streaming: Memory capture from streaming responses")
    print("  3. Memory persistence in Letta agents")
    print()

    async def run_all_tests():
        await test_gemini_non_streaming()
        await test_gemini_streaming()

        print("\n" + "=" * 70)
        print("=== All Tests Complete ===")
        print("=" * 70)

    asyncio.run(run_all_tests())
