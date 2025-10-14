import os
from letta_client import Letta

def test_quick_start():
    print("Testing Quick Start example...")

    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create an agent with memory
    agent = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
        memory_blocks=[
            {
                "label": "persona",
                "value": "I'm a helpful AI assistant that remembers our conversations."
            },
            {
                "label": "human",
                "value": "The user's name is Alice. She likes TypeScript."
            }
        ],
        tools=["web_search"]
    )

    print(f"Created agent: {agent.id}")

    # Send a message
    response = client.agents.messages.create(
        agent_id=agent.id,
        messages=[{
            "role": "user",
            "content": "What's my name?"
        }]
    )

    # Agent remembers: "Your name is Alice!"
    print(f"Response messages: {response.messages}")

    # Retrieve the human block
    human_block = client.agents.blocks.retrieve(agent_id=agent.id, block_label="human")
    print(f"Human block value: {human_block.value}")

    # Cleanup
    client.agents.delete(agent_id=agent.id)
    print("Quick Start test passed!")

if __name__ == "__main__":
    try:
        test_quick_start()
    except Exception as err:
        print(f"Quick Start test failed: {err}")
        exit(1)
