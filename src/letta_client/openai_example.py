from openai import AsyncOpenAI
from letta_client.memory import memory
from letta_client.client import Letta
import asyncio
import os


# =============================================================================
# Example 1: Basic Memory Integration
# =============================================================================

async def basic_memory_example():
	"""
	Demonstrates basic memory integration with OpenAI SDK.

	Memory is automatically captured and persisted to Letta during the conversation.
	The agent will remember this conversation in future sessions.
	"""
	print("=" * 80)
	print("EXAMPLE 1: Basic Memory Integration")
	print("=" * 80)
	print()

	# Initialize Letta client
	letta_client = Letta(base_url="http://localhost:8283", token=None)

	# Initialize OpenAI client
	openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

	# Wrap conversation in memory context
	# All conversation turns will be automatically saved to Letta
	async with memory(agent="openai_assistant", client=letta_client):
		# First turn - introduce yourself
		print("You: My name is Alice and I work on AI agents.")
		response = await openai.chat.completions.create(
			model="gpt-4o-mini",
			messages=[
				{"role": "user", "content": "My name is Alice and I work on AI agents."}
			]
		)
		print(f"GPT: {response.choices[0].message.content}\n")

		# Second turn - ask a question
		print("You: What are some interesting AI projects I could work on?")
		response = await openai.chat.completions.create(
			model="gpt-4o-mini",
			messages=[
				{"role": "user", "content": "What are some interesting AI projects I could work on?"}
			]
		)
		print(f"GPT: {response.choices[0].message.content}\n")

	print("✅ Conversation saved to Letta! Agent 'openai_assistant' will remember this.")
	print()


# =============================================================================
# Example 2: Cross-Session Memory Persistence
# =============================================================================

async def cross_session_memory_example():
	"""
	Demonstrates cross-session memory persistence.

	This example shows how GPT remembers information from previous sessions
	by using the same agent name. Run this after basic_memory_example() to see
	GPT recall information from the previous conversation.
	"""
	print("=" * 80)
	print("EXAMPLE 2: Cross-Session Memory Persistence")
	print("=" * 80)
	print()

	# Initialize Letta client
	letta_client = Letta(base_url="http://localhost:8283", token=None)

	# Initialize OpenAI client
	openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

	# Use the SAME agent name to access previous memories
	async with memory(agent="openai_assistant", client=letta_client):
		# Ask GPT to recall information from previous session
		print("You: What is my name and what do I work on?")
		response = await openai.chat.completions.create(
			model="gpt-4o-mini",
			messages=[
				{"role": "user", "content": "What is my name and what do I work on?"}
			]
		)
		print(f"GPT: {response.choices[0].message.content}\n")

	print("✅ GPT remembered information from the previous session!")
	print()


# =============================================================================
# Example 3: Streaming Support
# =============================================================================

async def streaming_example():
	"""
	Demonstrates streaming responses with memory integration.

	Memory is captured even with streaming responses.
	"""
	print("=" * 80)
	print("EXAMPLE 3: Streaming Support")
	print("=" * 80)
	print()

	# Initialize Letta client
	letta_client = Letta(base_url="http://localhost:8283", token=None)

	# Initialize OpenAI client
	openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

	# Streaming works seamlessly with memory
	async with memory(agent="openai_assistant", client=letta_client):
		print("You: Count to 5 for me.")
		print("GPT: ", end="", flush=True)

		stream = await openai.chat.completions.create(
			model="gpt-4o-mini",
			messages=[
				{"role": "user", "content": "Count to 5 for me."}
			],
			stream=True
		)

		async for chunk in stream:
			if chunk.choices[0].delta.content:
				print(chunk.choices[0].delta.content, end="", flush=True)

		print("\n")

	print("✅ Streaming response captured and saved to memory!")
	print()


# =============================================================================
# Example 4: Capture-Only Mode
# =============================================================================

async def capture_only_example():
	"""
	Demonstrates capture-only mode where conversations are saved but
	memory is not injected into prompts.

	Useful for logging conversations without influencing GPT's responses.
	"""
	print("=" * 80)
	print("EXAMPLE 4: Capture-Only Mode")
	print("=" * 80)
	print()

	# Initialize Letta client
	letta_client = Letta(base_url="http://localhost:8283", token=None)

	# Initialize OpenAI client
	openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

	# Use capture_only=True to log conversations without memory injection
	async with memory(agent="capture_only_agent", client=letta_client, capture_only=True):
		print("You: Hello! I'm testing capture-only mode.")
		response = await openai.chat.completions.create(
			model="gpt-4o-mini",
			messages=[
				{"role": "user", "content": "Hello! I'm testing capture-only mode."}
			]
		)
		print(f"GPT: {response.choices[0].message.content}\n")

	print("✅ Conversation captured but no memory was injected into prompts.")
	print()


# =============================================================================
# Main Entry Point
# =============================================================================

async def main():
	"""
	Run all examples demonstrating memory integration with OpenAI SDK.

	Note: Make sure Letta server is running at http://localhost:8283
	      and OPENAI_API_KEY environment variable is set.
	"""
	print("\n")
	print("╔" + "=" * 78 + "╗")
	print("║" + " " * 20 + "Letta Memory Integration with OpenAI SDK" + " " * 19 + "║")
	print("╚" + "=" * 78 + "╝")
	print()
	print("These examples demonstrate how to use Letta memory with OpenAI SDK.")
	print("Memory automatically persists across sessions using the same agent name.")
	print()

	# Example 1: Basic usage
	await basic_memory_example()

	# Wait a moment for memory to be saved
	await asyncio.sleep(1)

	# Example 2: Cross-session recall
	await cross_session_memory_example()

	# Example 3: Streaming
	await streaming_example()

	# Example 4: Capture-only mode
	# await capture_only_example()

	print("=" * 80)
	print("All examples complete!")
	print("=" * 80)


if __name__ == "__main__":
	# Check for API key
	if not os.getenv("OPENAI_API_KEY"):
		print("Error: OPENAI_API_KEY environment variable not set")
		print("Please set it with: export OPENAI_API_KEY='your-key-here'")
		exit(1)

	asyncio.run(main())
