import os
from letta_client import Letta

def test_multi_agent():
    print("Testing Multi-agent Shared Memory example...")

    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create shared block
    shared_block = client.blocks.create(
        label="organization",
        value="Shared team context"
    )

    print(f"Created shared block: {shared_block.id}")

    # Attach to multiple agents
    agent1 = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
        memory_blocks=[{"label": "persona", "value": "I am a supervisor"}],
        block_ids=[shared_block.id]
    )

    agent2 = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
        memory_blocks=[{"label": "persona", "value": "I am a worker"}],
        block_ids=[shared_block.id]
    )

    print(f"Created agent1: {agent1.id}")
    print(f"Created agent2: {agent2.id}")

    # Cleanup
    client.agents.delete(agent_id=agent1.id)
    client.agents.delete(agent_id=agent2.id)
    client.blocks.delete(block_id=shared_block.id)
    print("Multi-agent test passed!")

if __name__ == "__main__":
    try:
        test_multi_agent()
    except Exception as err:
        print(f"Multi-agent test failed: {err}")
        exit(1)
