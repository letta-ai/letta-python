from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, TextBlock
from letta_client.memory import memory
from letta_client.client import Letta
import asyncio


# =============================================================================
# Example 1: Basic Memory Integration
# =============================================================================

async def basic_memory_example():
	"""
	Demonstrates basic memory integration with Claude Agent SDK.

	Memory is automatically captured and persisted to Letta during the conversation.
	The agent will remember this conversation in future sessions.
	"""
	print("=" * 80)
	print("EXAMPLE 1: Basic Memory Integration")
	print("=" * 80)
	print()

	# Initialize Letta client
	letta_client = Letta(base_url="http://localhost:8283", token=None)

	# Set up Claude Agent SDK options
	options = ClaudeAgentOptions(
		allowed_tools=["Read", "Write", "Bash"],
		permission_mode="acceptEdits"
	)
	client = ClaudeSDKClient(options)

	# Wrap conversation in memory context
	# All conversation turns will be automatically saved to Letta
	async with memory(agent="my_assistant", client=letta_client):
		await client.connect()

		# First turn - introduce yourself
		print("You: My name is Alice and I work on AI agents.")
		await client.query("My name is Alice and I work on AI agents.")

		print("Claude: ", end="")
		async for message in client.receive_response():
			if isinstance(message, AssistantMessage):
				for block in message.content:
					if isinstance(block, TextBlock):
						print(block.text, end="")
		print("\n")

		# Second turn - ask a question
		print("You: What are some interesting AI projects I could work on?")
		await client.query("What are some interesting AI projects I could work on?")

		print("Claude: ", end="")
		async for message in client.receive_response():
			if isinstance(message, AssistantMessage):
				for block in message.content:
					if isinstance(block, TextBlock):
						print(block.text, end="")
		print("\n")

		await client.disconnect()

	print("✅ Conversation saved to Letta! Agent 'my_assistant' will remember this.")
	print()


# =============================================================================
# Example 2: Cross-Session Memory Persistence
# =============================================================================

async def cross_session_memory_example():
	"""
	Demonstrates cross-session memory persistence.

	This example shows how Claude remembers information from previous sessions
	by using the same agent name. Run this after basic_memory_example() to see
	Claude recall information from the previous conversation.
	"""
	print("=" * 80)
	print("EXAMPLE 2: Cross-Session Memory Persistence")
	print("=" * 80)
	print()

	# Initialize Letta client
	letta_client = Letta(base_url="http://localhost:8283", token=None)

	# Set up Claude Agent SDK options
	options = ClaudeAgentOptions(
		allowed_tools=["Read", "Write", "Bash"],
		permission_mode="acceptEdits"
	)
	client = ClaudeSDKClient(options)

	# Use the SAME agent name to access previous memories
	async with memory(agent="my_assistant", client=letta_client):
		await client.connect()

		# Ask Claude to recall information from previous session
		print("You: What is my name and what do I work on?")
		await client.query("What is my name and what do I work on?")

		print("Claude: ", end="")
		async for message in client.receive_response():
			if isinstance(message, AssistantMessage):
				for block in message.content:
					if isinstance(block, TextBlock):
						print(block.text, end="")
		print("\n")

		await client.disconnect()

	print("✅ Claude remembered information from the previous session!")
	print()


# =============================================================================
# Example 3: Interactive Session with Memory
# =============================================================================

class MemoryEnabledSession:
	"""
	Interactive conversation session with persistent memory.

	All conversations are automatically saved to Letta and will be remembered
	across different program runs when using the same agent name.
	"""

	def __init__(self, agent_name: str, letta_client: Letta, options: ClaudeAgentOptions = None):
		self.agent_name = agent_name
		self.letta_client = letta_client
		self.client = ClaudeSDKClient(options)
		self.turn_count = 0

	async def start(self):
		print(f"Starting memory-enabled session with agent: {self.agent_name}")
		print("All conversations will be saved and remembered in future sessions.")
		print("Commands: 'exit' to quit, 'interrupt' to stop current task")
		print()

		# Wrap entire session in memory context
		async with memory(agent=self.agent_name, client=self.letta_client):
			await self.client.connect()

			while True:
				user_input = input(f"\n[Turn {self.turn_count + 1}] You: ")

				if user_input.lower() == 'exit':
					break
				elif user_input.lower() == 'interrupt':
					await self.client.interrupt()
					print("Task interrupted!")
					continue

				# Send message - will be captured by Letta memory
				await self.client.query(user_input)
				self.turn_count += 1

				# Process response
				print(f"[Turn {self.turn_count}] Claude: ", end="")
				async for message in self.client.receive_response():
					if isinstance(message, AssistantMessage):
						for block in message.content:
							if isinstance(block, TextBlock):
								print(block.text, end="")
				print()  # New line after response

			await self.client.disconnect()

		print(f"\nConversation ended after {self.turn_count} turns.")
		print(f"✅ All turns saved to Letta agent '{self.agent_name}'")


async def interactive_memory_example():
	"""
	Run an interactive session with memory enabled.
	"""
	print("=" * 80)
	print("EXAMPLE 3: Interactive Session with Memory")
	print("=" * 80)
	print()

	# Initialize Letta client
	letta_client = Letta(base_url="http://localhost:8283", token=None)

	# Set up Claude Agent SDK options
	options = ClaudeAgentOptions(
		allowed_tools=["Read", "Write", "Bash"],
		permission_mode="acceptEdits"
	)

	# Start interactive session
	session = MemoryEnabledSession(
		agent_name="interactive_assistant",
		letta_client=letta_client,
		options=options
	)
	await session.start()


# =============================================================================
# Example 4: Capture-Only Mode (No Memory Injection)
# =============================================================================

async def capture_only_example():
	"""
	Demonstrates capture-only mode where conversations are saved but
	memory is not injected into prompts.

	Useful for logging conversations without influencing Claude's responses.
	"""
	print("=" * 80)
	print("EXAMPLE 4: Capture-Only Mode")
	print("=" * 80)
	print()

	# Initialize Letta client
	letta_client = Letta(base_url="http://localhost:8283", token=None)

	# Set up Claude Agent SDK options
	options = ClaudeAgentOptions(
		allowed_tools=["Read", "Write", "Bash"],
		permission_mode="acceptEdits"
	)
	client = ClaudeSDKClient(options)

	# Use capture_only=True to log conversations without memory injection
	async with memory(agent="capture_only_agent", client=letta_client, capture_only=True):
		await client.connect()

		print("You: Hello! I'm testing capture-only mode.")
		await client.query("Hello! I'm testing capture-only mode.")

		print("Claude: ", end="")
		async for message in client.receive_response():
			if isinstance(message, AssistantMessage):
				for block in message.content:
					if isinstance(block, TextBlock):
						print(block.text, end="")
		print("\n")

		await client.disconnect()

	print("✅ Conversation captured but no memory was injected into prompts.")
	print()


# =============================================================================
# Main Entry Point
# =============================================================================

async def main():
	"""
	Run all examples demonstrating memory integration with Claude Agent SDK.

	Note: Make sure Letta server is running at http://localhost:8283
	"""
	print("\n")
	print("╔" + "=" * 78 + "╗")
	print("║" + " " * 15 + "Letta Memory Integration with Claude Agent SDK" + " " * 16 + "║")
	print("╚" + "=" * 78 + "╝")
	print()
	print("These examples demonstrate how to use Letta memory with Claude Agent SDK.")
	print("Memory automatically persists across sessions using the same agent name.")
	print()

	# Example 1: Basic usage
	await basic_memory_example()

	# Wait a moment for memory to be saved
	await asyncio.sleep(1)

	# Example 2: Cross-session recall
	await cross_session_memory_example()

	# Uncomment to run interactive session:
	# await interactive_memory_example()

	# Example 4: Capture-only mode
	# await capture_only_example()

	print("=" * 80)
	print("All examples complete!")
	print("=" * 80)


if __name__ == "__main__":
	asyncio.run(main())