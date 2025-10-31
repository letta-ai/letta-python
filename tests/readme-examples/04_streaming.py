import os
from letta_client import Letta

def test_streaming():
    print("Testing Streaming example...")

    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create agent
    agent = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
    )

    print(f"Created agent: {agent.id}")

    # Stream agent responses in real-time
    stream = client.agents.messages.create_stream(
        agent_id=agent.id,
        messages=[{"role": "user", "content": "Hello!"}]
    )

    chunk_count = 0
    for chunk in stream:
        chunk_count += 1
        print(f"Chunk {chunk_count}: {chunk}")

    print(f"Received {chunk_count} chunks")

    # Cleanup
    client.agents.delete(agent_id=agent.id)
    print("Streaming test passed!")

if __name__ == "__main__":
    try:
        test_streaming()
    except Exception as err:
        print(f"Streaming test failed: {err}")
        exit(1)
