import os
from letta_client import Letta

def test_python_support():
    print("Testing Python Support example...")

    # Test sync client
    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create agent to verify client works
    agent = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
    )

    print(f"Created agent with sync client: {agent.id}")

    # Cleanup
    client.agents.delete(agent_id=agent.id)
    print("Python Support test passed!")

if __name__ == "__main__":
    try:
        test_python_support()
    except Exception as err:
        print(f"Python Support test failed: {err}")
        exit(1)
