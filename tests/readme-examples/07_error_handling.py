from letta_client import Letta
from letta_client.core.api_error import ApiError

def test_error_handling():
    print("Testing Error Handling example...")

    # Create client with invalid token to trigger error
    client = Letta(token="INVALID_TOKEN")

    try:
        # This should raise an ApiError
        client.agents.create(
            model="openai/gpt-4o-mini",
            embedding="openai/text-embedding-3-small",
        )
        print("Error: Expected ApiError was not raised")
        exit(1)
    except ApiError as e:
        print(f"Caught expected ApiError: {e.status_code}")
        print(f"Message: {e.message if hasattr(e, 'message') else 'N/A'}")
        print(f"Body: {e.body}")
        print("Error Handling test passed!")

if __name__ == "__main__":
    try:
        test_error_handling()
    except Exception as err:
        print(f"Error Handling test failed unexpectedly: {err}")
        exit(1)
