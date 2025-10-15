"""
Comprehensive examples of Letta memory integration usage patterns.

This file demonstrates all the different ways to use Letta memory with Claude Agent SDK.
"""

from letta_client.memory import memory, memory_fetch, memory_add, memory_query
from letta_client.client import Letta
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
import asyncio


# ============================================================================
# Example 1: Zero-Config (Automatic Everything)
# ============================================================================

async def example_zero_config():
    """
    The simplest possible usage - just wrap your code in the memory context.
    Everything is automatic: client creation, agent creation, memory injection.
    """
    print("Example 1: Zero-Config (Automatic Everything)")
    print("=" * 60)

    async with memory():  # Uses LETTA_API_KEY from env, agent name "letta_agent"
        # Your existing Claude SDK code - no changes needed!
        client = ClaudeSDKClient()
        await client.connect()
        await client.query("My name is Alice")
        async for msg in client.receive_response():
            print(msg)
        await client.disconnect()

    print("\n")


# ============================================================================
# Example 2: Custom Agent Name
# ============================================================================

async def example_custom_agent():
    """
    Use a custom agent name to separate different contexts.
    """
    print("Example 2: Custom Agent Name")
    print("=" * 60)

    # Different agents for different purposes
    async with memory(agent="code_assistant"):
        # Code-related conversations go here
        pass

    async with memory(agent="customer_support"):
        # Customer support conversations go here
        pass

    print("\n")


# ============================================================================
# Example 3: Custom Letta Client
# ============================================================================

async def example_custom_client():
    """
    Use a custom Letta client (e.g., for local server or specific config).
    """
    print("Example 3: Custom Letta Client")
    print("=" * 60)

    # Connect to local Letta server
    letta = Letta(base_url="http://localhost:8283", token=None)

    async with memory(agent="my_agent", client=letta):
        # Your Claude SDK code
        pass

    print("\n")


# ============================================================================
# Example 4: Capture-Only Mode (No Auto-Injection)
# ============================================================================

async def example_capture_only():
    """
    Capture conversations but skip memory injection for lower latency.
    Good for building up memory history or when latency is critical.
    """
    print("Example 4: Capture-Only Mode (No Auto-Injection)")
    print("=" * 60)

    async with memory(agent="my_agent", auto_inject=False):
        # ✅ Captures and saves messages
        # ❌ Skips memory retrieval/injection
        # ⚡ Lower latency
        client = ClaudeSDKClient()
        await client.connect()
        await client.query("Fast query without memory injection")
        async for msg in client.receive_response():
            print(msg)
        await client.disconnect()

    print("\n")


# ============================================================================
# Example 5: Manual Memory Injection (fetch_memory)
# ============================================================================

async def example_manual_injection():
    """
    Manually fetch and inject memory based on your own logic.
    Full control over when and how memory is used.
    """
    print("Example 5: Manual Memory Injection (fetch_memory)")
    print("=" * 60)

    letta = Letta(base_url="http://localhost:8283", token=None)

    # Conditionally fetch memory
    should_use_memory = True  # Your custom logic
    turn_count = 0

    async with memory(agent="my_agent", client=letta, auto_inject=False):
        client = ClaudeSDKClient()

        # Manually inject memory only when needed
        if should_use_memory:
            memory_context = memory_fetch(agent="my_agent", client=letta)
            if memory_context:
                # Manually inject into your options
                options = ClaudeAgentOptions(
                    system_prompt=f"You are a helpful assistant.\n\n{memory_context}"
                )
                # Use these options...

        await client.connect()
        await client.query("Query with manual memory control")
        async for msg in client.receive_response():
            print(msg)
        await client.disconnect()

    print("\n")


# ============================================================================
# Example 6: Periodic Memory Refresh
# ============================================================================

async def example_periodic_refresh():
    """
    Fetch memory on a schedule (e.g., every N turns) instead of every request.
    Good balance between freshness and performance.
    """
    print("Example 6: Periodic Memory Refresh")
    print("=" * 60)

    letta = Letta()
    turn_count = 0
    REFRESH_INTERVAL = 5  # Fetch memory every 5 turns

    async with memory(agent="my_agent", client=letta, auto_inject=False):
        client = ClaudeSDKClient()
        await client.connect()

        for i in range(10):  # Multi-turn conversation
            turn_count += 1

            # Fetch memory every REFRESH_INTERVAL turns
            if turn_count % REFRESH_INTERVAL == 1:
                memory_context = memory_fetch(agent="my_agent", client=letta)
                print(f"[Turn {turn_count}] Refreshed memory: {len(memory_context)} chars")
                # Update system prompt with fresh memory...

            await client.query(f"Turn {turn_count} query")
            async for msg in client.receive_response():
                print(msg)

        await client.disconnect()

    print("\n")


# ============================================================================
# Example 7: Selective Memory Injection
# ============================================================================

async def example_selective_injection():
    """
    Use different memory injection strategies based on query type.
    """
    print("Example 7: Selective Memory Injection")
    print("=" * 60)

    letta = Letta()

    async with memory(agent="my_agent", client=letta, auto_inject=False):
        client = ClaudeSDKClient()
        await client.connect()

        # Query 1: Complex query - use memory
        memory_context = memory_fetch(agent="my_agent", client=letta)
        await client.query(f"Complex query that needs context: {memory_context[:100]}")
        async for msg in client.receive_response():
            print(msg)

        # Query 2: Simple query - no memory needed
        await client.query("What's 2+2?")  # No memory injection
        async for msg in client.receive_response():
            print(msg)

        await client.disconnect()

    print("\n")


# ============================================================================
# Example 8: Multi-Agent Coordination
# ============================================================================

async def example_multi_agent():
    """
    Use multiple agents with separate memory spaces but coordinate their work.
    """
    print("Example 8: Multi-Agent Coordination")
    print("=" * 60)

    # Backend agent
    async with memory(agent="backend_agent"):
        # Backend development work
        pass

    # Frontend agent
    async with memory(agent="frontend_agent"):
        # Frontend development work
        pass

    # Coordinator agent - can fetch memory from both
    letta = Letta()
    backend_context = memory_fetch(agent="backend_agent", client=letta)
    frontend_context = memory_fetch(agent="frontend_agent", client=letta)

    combined_context = f"""
    Backend Context:
    {backend_context}

    Frontend Context:
    {frontend_context}
    """

    async with memory(agent="coordinator"):
        # Coordinator can see both contexts
        client = ClaudeSDKClient(
            ClaudeAgentOptions(system_prompt=combined_context)
        )
        # Coordinate the work...

    print("\n")


# ============================================================================
# Example 9: Memory Inspection
# ============================================================================

def example_inspect_memory():
    """
    Inspect memory contents before deciding whether to use it.
    """
    print("Example 9: Memory Inspection")
    print("=" * 60)

    letta = Letta()

    # Fetch and inspect memory
    memory_context = memory_fetch(agent="my_agent", client=letta)

    if memory_context:
        print(f"Memory available: {len(memory_context)} characters")
        print(f"Preview: {memory_context[:200]}...")

        # Decide based on memory content
        if len(memory_context) > 1000:
            print("Using memory (substantial context available)")
            # Use memory...
        else:
            print("Skipping memory (insufficient context)")
            # Don't use memory...
    else:
        print("No memory available (new agent)")

    print("\n")


# ============================================================================
# Example 10: Using Helper Functions
# ============================================================================

def example_helper_functions():
    """
    Use memory_add() and memory_query() for manual memory management.
    """
    print("Example 10: Using Helper Functions")
    print("=" * 60)

    from letta_client.memory import memory_add, memory_query, memory_fetch

    # Add memory manually without conversation
    print("Adding user preferences to memory...")
    memory_add(
        "Remember: I prefer TypeScript over JavaScript and always use trailing commas.",
        agent="my_agent"
    )

    print("Adding project context to memory...")
    memory_add(
        "I'm working on a FastAPI + React application deployed on AWS.",
        agent="my_agent"
    )

    # Query the stored memory
    print("\nQuerying memory about preferences...")
    response = memory_query(
        "What are my coding preferences?",
        agent="my_agent"
    )
    print(f"Response: {response}")

    print("\nQuerying memory about project...")
    response = memory_query(
        "What project am I working on?",
        agent="my_agent"
    )
    print(f"Response: {response}")

    # Fetch and inspect raw memory
    print("\nFetching raw memory for inspection...")
    memory_context = memory_fetch(agent="my_agent")
    if memory_context:
        print(f"Memory content ({len(memory_context)} chars):")
        print(memory_context[:200] + "..." if len(memory_context) > 200 else memory_context)

    print("\n")


# ============================================================================
# Run all examples
# ============================================================================

async def main():
    print("\n" + "=" * 60)
    print("LETTA MEMORY INTEGRATION - USAGE EXAMPLES")
    print("=" * 60 + "\n")

    # Note: Most examples are shown for demonstration
    # In practice, you'd run one at a time based on your use case

    # example_zero_config()
    # example_custom_agent()
    # example_custom_client()
    # example_capture_only()
    # example_manual_injection()
    # example_periodic_refresh()
    # example_selective_injection()
    # example_multi_agent()
    # example_inspect_memory()
    example_helper_functions()


if __name__ == "__main__":
    asyncio.run(main())
