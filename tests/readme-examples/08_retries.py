import os
from letta_client import Letta

def test_retries():
    print("Testing Retries example...")

    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create agent with custom retry configuration
    agent = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
        request_options={"max_retries": 3}
    )

    print(f"Created agent with custom retries: {agent.id}")

    # Cleanup
    client.agents.delete(agent_id=agent.id)
    print("Retries test passed!")

if __name__ == "__main__":
    try:
        test_retries()
    except Exception as err:
        print(f"Retries test failed: {err}")
        exit(1)
