"""
Test script to verify HTTP interception is working.

This should print log messages showing that requests are being intercepted.
"""

from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, TextBlock
import asyncio
import sys
import os

# Add the src directory to path so we can import from letta_client
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from letta_client.memory import memory, memory_fetch
from letta_client.client import Letta

# Check if Anthropic SDK is available
try:
    from anthropic import AsyncAnthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


async def test_claude_interception():
    print("=== Testing Claude SDK Memory Integration ===\n")

    # For local Letta server (default: http://localhost:8283)
    letta_client = Letta(base_url="http://localhost:8283", token=None)

    # For Letta Cloud
    # letta_client = Letta(token=os.getenv("LETTA_API_KEY"))

    try:
        # ========================================
        # SESSION 1: Introduce myself
        # ========================================
        print("\n=== SESSION 1: First Claude SDK session ===\n")

        options_1 = ClaudeAgentOptions(
            allowed_tools=["Read", "Write", "Bash"],
            permission_mode="acceptEdits"
        )
        client_1 = ClaudeSDKClient(options_1)

        async with memory(agent="memory_test_agent", client=letta_client):
            await client_1.connect()
            print("[Test] Connected to Claude SDK (Session 1)")

            await client_1.query("My name is Caren. Hello!")
            print("[Test] Sent query: 'My name is Caren. Hello!'")

            # Receive response
            print("[Test] Receiving response:")
            async for message in client_1.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"  {block.text}")

            await client_1.disconnect()
            print("\n[Test] Disconnected from Session 1")

        # Wait a moment for memory to be saved
        print("\n[Test] Waiting for memory to be saved...")
        await asyncio.sleep(2)

        # ========================================
        # SESSION 2: New session - test memory recall
        # ========================================
        print("\n=== SESSION 2: New Claude SDK session (testing memory) ===\n")

        options_2 = ClaudeAgentOptions(
            allowed_tools=["Read", "Write", "Bash"],
            permission_mode="acceptEdits"
        )
        client_2 = ClaudeSDKClient(options_2)

        async with memory(agent="memory_test_agent", client=letta_client):
            await client_2.connect()
            print("[Test] Connected to Claude SDK (Session 2 - NEW SESSION)")

            await client_2.query("What is my name?")
            print("[Test] Sent query: 'What is my name?'")

            # Receive response - Claude should remember "Caren"
            print("[Test] Receiving response (should remember name from Session 1):")
            async for message in client_2.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"  {block.text}")

            await client_2.disconnect()
            print("\n[Test] Disconnected from Session 2")

        # ========================================
        # Inspect memory
        # ========================================
        print(f"\n=== Final Memory Inspection ===")
        memory_content = memory_fetch(agent="memory_test_agent", client=letta_client)
        print(f"\n[Test] Fetch Memory results ({len(memory_content)} chars):")
        print(memory_content)

    except Exception as e:
        print(f"\n[Test] Error: {e}")
        import traceback
        traceback.print_exc()


async def test_anthropic_interception():
    """Test Anthropic SDK memory integration."""
    if not ANTHROPIC_AVAILABLE:
        print("\n=== Skipping Anthropic Test ===")
        print("Anthropic SDK not installed. Install with: pip install anthropic\n")
        return

    print("\n=== Testing Anthropic SDK Memory Integration ===\n")

    letta_client = Letta(base_url="http://localhost:8283", token=None)

    try:
        # ========================================
        # SESSION 1: Introduce myself
        # ========================================
        print("\n=== SESSION 1: First Anthropic SDK session ===\n")

        anthropic_client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        async with memory(agent="anthropic_test_agent", client=letta_client):
            print("[Test] Sending query: 'My name is Alice. Hello!'")

            response = await anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": "My name is Alice. Hello!"}]
            )

            print("[Test] Receiving response:")
            for block in response.content:
                if block.type == "text":
                    print(f"  {block.text}")

        print("\n[Test] Waiting for memory to be saved...")
        await asyncio.sleep(2)

        # ========================================
        # SESSION 2: Test memory recall
        # ========================================
        print("\n=== SESSION 2: New Anthropic SDK session (testing memory) ===\n")

        async with memory(agent="anthropic_test_agent", client=letta_client):
            print("[Test] Sending query: 'What is my name?'")

            response = await anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": "What is my name?"}]
            )

            print("[Test] Receiving response (should remember 'Alice'):")
            for block in response.content:
                if block.type == "text":
                    print(f"  {block.text}")

        # ========================================
        # Inspect memory
        # ========================================
        print(f"\n=== Final Memory Inspection ===")
        memory_content = memory_fetch(agent="anthropic_test_agent", client=letta_client)
        print(f"\n[Test] Fetch Memory results ({len(memory_content)} chars):")
        print(memory_content)

    except Exception as e:
        print(f"\n[Test] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("=== Cross-Session Memory Test ===")
    print("This test will run memory integration tests for:")
    print("  1. Claude Agent SDK")
    print("  2. Anthropic SDK (if installed)")
    print("\nEach test:")
    print("  - Session 1: Introduce a name")
    print("  - Session 2: Ask 'What is my name?' in a NEW session")
    print("  - Verify memory persistence across sessions\n")

    async def run_all_tests():
        await test_claude_interception()
        await test_anthropic_interception()

    asyncio.run(run_all_tests())
