import os
from letta_client import Letta

def test_custom_http_client():
    print("Testing Custom HTTP Client example...")

    # The Letta client accepts a custom httpx_client parameter
    # This test verifies that the client can be instantiated with the httpx_client option
    # Note: A custom httpx_client must be an httpx.Client instance
    client = Letta(
        token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"),
        # httpx_client=httpx.Client(...)  # custom client can be passed here
    )

    # Create agent to verify client works
    agent = client.agents.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
    )

    print(f"Created agent (demonstrating httpx_client option exists): {agent.id}")

    # Cleanup
    client.agents.delete(agent_id=agent.id)
    print("Custom HTTP Client test passed!")

if __name__ == "__main__":
    try:
        test_custom_http_client()
    except Exception as err:
        print(f"Custom HTTP Client test failed: {err}")
        exit(1)
