import os
from letta_client import Letta

def test_custom_headers():
    print("Testing Custom Headers example...")

    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create agent with custom headers
    agent = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
        request_options={
            "additional_headers": {
                "X-Custom-Header": "value"
            }
        }
    )

    print(f"Created agent with custom headers: {agent.id}")

    # Cleanup
    client.agents.delete(agent_id=agent.id)
    print("Custom Headers test passed!")

if __name__ == "__main__":
    try:
        test_custom_headers()
    except Exception as err:
        print(f"Custom Headers test failed: {err}")
        exit(1)
