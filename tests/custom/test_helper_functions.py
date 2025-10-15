"""
Test script for memory_add() and memory_query() helper functions.
"""

import sys
import os

# Add the src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

# Import Letta client
from letta_client.client import Letta

# Import helper functions
from letta_client.memory import memory_add, memory_query, memory_fetch


def test_helper_functions():
    print("=== Testing Memory Helper Functions ===\n")

    # Use local Letta server
    letta_client = Letta(base_url="http://localhost:8283", token=None)

    # Test 1: Add memory manually
    print("Test 1: Adding memory manually")
    print("-" * 60)
    success = memory_add(
        "My name is Alice and I prefer TypeScript over JavaScript. I always use trailing commas.",
        agent="helper_test_agent",
        client=letta_client
    )
    if success:
        print("✅ Successfully added memory\n")
    else:
        print("❌ Failed to add memory\n")

    # Test 2: Add more context
    print("Test 2: Adding project context")
    print("-" * 60)
    success = memory_add(
        "I'm working on a web application using FastAPI, PostgreSQL, and React.",
        agent="helper_test_agent",
        client=letta_client
    )
    if success:
        print("✅ Successfully added project context\n")
    else:
        print("❌ Failed to add project context\n")

    # Test 3: Query memory
    print("Test 3: Querying memory - What is my name?")
    print("-" * 60)
    response = memory_query(
        "What is my name?",
        agent="helper_test_agent",
        client=letta_client
    )
    if response:
        print(f"Response: {response}\n")
    else:
        print("❌ No response received\n")

    # Test 4: Query about preferences
    print("Test 4: Querying memory - What are my coding preferences?")
    print("-" * 60)
    response = memory_query(
        "What are my coding preferences?",
        agent="helper_test_agent",
        client=letta_client
    )
    if response:
        print(f"Response: {response}\n")
    else:
        print("❌ No response received\n")

    # Test 5: Query about project
    print("Test 5: Querying memory - What project am I working on?")
    print("-" * 60)
    response = memory_query(
        "What project am I working on?",
        agent="helper_test_agent",
        client=letta_client
    )
    if response:
        print(f"Response: {response}\n")
    else:
        print("❌ No response received\n")

    # Test 6: Fetch memory for inspection
    print("Test 6: Fetching memory for inspection")
    print("-" * 60)
    memory_context = memory_fetch(
        agent="helper_test_agent",
        client=letta_client
    )
    if memory_context:
        print(f"Memory content ({len(memory_context)} chars):")
        print(memory_context[:500] + "..." if len(memory_context) > 500 else memory_context)
    else:
        print("❌ No memory found")

    print("\n" + "=" * 60)
    print("All tests completed!")


if __name__ == "__main__":
    test_helper_functions()
