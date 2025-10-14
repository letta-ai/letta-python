import os
from letta_client import Letta

def test_raw_response():
    print("Testing Raw Response Access example...")

    client = Letta(token=os.environ.get("LETTA_API_KEY", "YOUR_API_KEY"))

    # Create agent with raw response access
    response = client.agents.with_raw_response.create(
        model="openai/gpt-4o-mini",
        embedding="openai/text-embedding-3-small",
    )

    print(f"Raw response headers: {response.headers}")
    print(f"Created agent: {response.data.id}")

    # Cleanup
    client.agents.delete(agent_id=response.data.id)
    print("Raw Response test passed!")

if __name__ == "__main__":
    try:
        test_raw_response()
    except Exception as err:
        print(f"Raw Response test failed: {err}")
        exit(1)
