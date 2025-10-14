import os
from letta_client import Letta

def test_memory_management():
    print("Testing Memory Management example...")

    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create agent with memory blocks
    agent = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
        memory_blocks=[
            {"label": "persona", "value": "I'm a helpful assistant."},
            {"label": "human", "value": "User preferences and info."}
        ]
    )

    print(f"Created agent: {agent.id}")

    # Modify blocks manually
    client.agents.blocks.modify(
        agent_id=agent.id,
        block_label="human",
        value="Updated user information"
    )

    # Retrieve a block
    block = client.agents.blocks.retrieve(agent_id=agent.id, block_label="human")
    print(f"Retrieved block value: {block.value}")

    # Cleanup
    client.agents.delete(agent_id=agent.id)
    print("Memory Management test passed!")

if __name__ == "__main__":
    try:
        test_memory_management()
    except Exception as err:
        print(f"Memory Management test failed: {err}")
        exit(1)
