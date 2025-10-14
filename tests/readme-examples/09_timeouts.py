import os
from letta_client import Letta

def test_timeouts():
    print("Testing Timeouts example...")

    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create agent with custom timeout configuration
    agent = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
        request_options={"timeout_in_seconds": 30}
    )

    print(f"Created agent with custom timeout: {agent.id}")

    # Cleanup
    client.agents.delete(agent_id=agent.id)
    print("Timeouts test passed!")

if __name__ == "__main__":
    try:
        test_timeouts()
    except Exception as err:
        print(f"Timeouts test failed: {err}")
        exit(1)
