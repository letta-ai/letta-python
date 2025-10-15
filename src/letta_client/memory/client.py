from datetime import datetime, timezone
import typing
from uuid import uuid4

from .messages.client import AsyncMessagesClient, MessagesClient
from ..agents.client import AgentsClient, AsyncAgentsClient
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.assistant_message import AssistantMessage
from ..types.letta_message_union import LettaMessageUnion


class MemoryClient:
	def __init__(self, *, client_wrapper: SyncClientWrapper):
		self._agents = AgentsClient(client_wrapper=client_wrapper)
		self.messages = MessagesClient(agents_client=self._agents)

	def retrieve(self, agent: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
		agents = self._agents.list(name=agent, request_options=request_options)
		if not agents or len(agents) == 0:
			return ""

		agent_id = agents[0].id
		blocks = self._agents.blocks.list(agent_id=agent_id, request_options=request_options)
		return _format_memory_context([b.model_dump() for b in blocks])

	def create(self, agent: str, prompt: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
		agents = self._agents.list(name=agent, request_options=request_options)
		if not agents or len(agents) == 0:
			# TODO: create agent
			return ""

		agent_id = agents[0].id
		# TODO: invoke sleeptime agent directly
		self._agents.messages.create(
			agent_id=agent_id,
			messages=[{"role": "user", "content": prompt}],
			request_options=request_options,
		)

		blocks = self._agents.blocks.list(agent_id=agent_id, request_options=request_options)
		return _format_memory_context([b.model_dump() for b in blocks])

	def query(self, agent: str, prompt: str, *, request_options: typing.Optional[RequestOptions] = None) -> list[LettaMessageUnion]:
		agents = self._agents.list(name=agent, request_options=request_options)
		if not agents or len(agents) == 0:
			return [AssistantMessage(id=f"message-{uuid4()}", date=datetime.now(timezone.utc), content="Memory is empty.")]

		agent_id = agents[0].id
		# TODO: invoke sleeptime agent directly
		response = self._agents.messages.create(
			agent_id=agent_id,
			messages=[{"role": "user", "content": prompt}],
			request_options=request_options,
		)
		return response.messages

class AsyncMemoryClient:
	def __init__(self, *, client_wrapper: AsyncClientWrapper):
		self._agents = AsyncAgentsClient(client_wrapper=client_wrapper)
		self.messages = AsyncMessagesClient(agents_client=self._agents)

	async def retrieve(self, agent: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
		agents = await self._agents.list(name=agent, request_options=request_options)
		if not agents or len(agents) == 0:
			return ""

		agent_id = agents[0].id
		blocks = await self._agents.blocks.list(agent_id=agent_id, request_options=request_options)
		return _format_memory_context([b.model_dump() for b in blocks])

	async def create(self, agent: str, prompt: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
		agents = await self._agents.list(name=agent, request_options=request_options)
		if not agents or len(agents) == 0:
			return ""

		agent_id = agents[0].id
		await self._agents.messages.create(
			agent_id=agent_id,
			messages=[{"role": "user", "content": prompt}],
			request_options=request_options,
		)

		blocks = await self._agents.blocks.list(agent_id=agent_id, request_options=request_options)
		return _format_memory_context([b.model_dump() for b in blocks])

	async def query(self, agent: str, prompt: str, *, request_options: typing.Optional[RequestOptions] = None) -> list[LettaMessageUnion]:
		agents = await self._agents.list(name=agent, request_options=request_options)
		if not agents or len(agents) == 0:
			return [AssistantMessage(id=f"message-{uuid4()}", date=datetime.now(timezone.utc), content="Memory is empty.")]

		agent_id = agents[0].id
		response = await self._agents.messages.create(
			agent_id=agent_id,
			messages=[{"role": "user", "content": prompt}],
			request_options=request_options,
		)
		return response.messages


def _format_memory_context(memory_blocks: list[dict]) -> str:
	"""Format memory blocks into XML-structured context string."""
	if not memory_blocks:
		return ""

	formatted_lines = []
	for block in memory_blocks:
		if not block or not block.get("value"):
			continue

		label = block.get("label", "block")
		formatted_lines.append(f"<{label}>")

		if description := block.get("description"):
			formatted_lines.append(f"<description>{description}</description>")

		formatted_lines.append(f"<value>{block['value']}</value>")
		formatted_lines.append(f"</{label}>")

	if not formatted_lines:
		return ""

	memory_xml = "\n".join(formatted_lines)
	return f"<memory_blocks>\nThe following memory blocks are currently engaged in your core memory unit:\n{memory_xml}\n</memory_blocks>"