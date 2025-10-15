"""
Test script to verify auto_inject=False works correctly.
"""

from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, TextBlock
import asyncio
import sys
import os

# Add the src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

# Import Letta client and memory
from letta_client.client import Letta
from letta_client.memory import memory


async def test_auto_inject_disabled():
    print("=== Testing auto_inject=False ===\n")

    letta_client = Letta(base_url="http://localhost:8283", token=None)

    # Create Claude client
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Bash"],
        permission_mode="acceptEdits"
    )
    client = ClaudeSDKClient(options)

    try:
        # Use memory context with auto_inject=False
        async with memory(agent="test_agent", client=letta_client, auto_inject=False):
            await client.connect()
            print("\n[Test] Connected to Claude SDK")

            await client.query("Say hello!")
            print("[Test] Sent query")

            # Receive response
            print("[Test] Receiving response:")
            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"  {block.text}")

            await client.disconnect()
            print("\n[Test] Disconnected")

    except Exception as e:
        print(f"\n[Test] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("This test should show 'Auto-inject disabled' message\n")
    asyncio.run(test_auto_inject_disabled())
