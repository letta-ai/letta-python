"""
Test script to verify memory_fetch() works correctly.
"""

import sys
import os

# Add the src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

# Import Letta client
from letta_client.client import Letta

# Import memory module
from letta_client.memory import memory_fetch


def test_fetch_memory():
    print("=== Testing memory_fetch() ===\n")

    # Test 1: Fetch memory with local Letta client
    print("Test 1: Fetch memory for existing agent")
    letta_client = Letta(base_url="http://localhost:8283", token=None)
    memory_context = memory_fetch(agent="test_agent", client=letta_client)

    if memory_context:
        print(f"✅ Memory fetched successfully!")
        print(f"   Length: {len(memory_context)} characters")
        print(f"   Preview: {memory_context[:200]}...")
    else:
        print("⚠️  No memory found (agent may be new or have no blocks)")

    print("\n" + "="*60 + "\n")

    # Test 2: Fetch memory for non-existent agent
    print("Test 2: Fetch memory for non-existent agent")
    memory_context = memory_fetch(agent="nonexistent_agent", client=letta_client)

    if not memory_context:
        print("✅ Correctly returns empty string for non-existent agent")
    else:
        print(f"❌ Unexpected: Got memory for non-existent agent")

    print("\n" + "="*60 + "\n")

    # Test 3: Manual injection use case
    print("Test 3: Manual injection use case")
    should_inject = True  # User's custom logic

    if should_inject:
        memory_context = memory_fetch(agent="test_agent", client=letta_client)
        if memory_context:
            system_prompt = f"You are a helpful assistant.\n\n## Previous Context\n{memory_context}"
            print(f"✅ System prompt created with memory")
            print(f"   Total length: {len(system_prompt)} characters")
        else:
            system_prompt = "You are a helpful assistant."
            print(f"✅ System prompt created without memory (none available)")

    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    test_fetch_memory()
