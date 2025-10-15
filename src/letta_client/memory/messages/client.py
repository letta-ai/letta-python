import typing

from ...agents.client import AgentsClient, AsyncAgentsClient
from ...core.request_options import RequestOptions
from ...types.letta_message_union import LettaMessageUnion


class MessagesClient:
	def __init__(self, *, agents_client: AgentsClient):
		self._agents = agents_client

	def list(
		self,
		agent: str,
		*,
		after: typing.Optional[str] = None,
		before: typing.Optional[str] = None,
		limit: typing.Optional[int] = None,
		request_options: typing.Optional[RequestOptions] = None,
	) -> typing.List[LettaMessageUnion]:
		agents = self._agents.list(name=agent, request_options=request_options)
		if not agents or len(agents) == 0:
			return []

		agent_id = agents[0].id
		return self._agents.messages.list(
			agent_id=agent_id,
			after=after,
			before=before,
			limit=limit,
			request_options=request_options
		)

class AsyncMessagesClient:
	def __init__(self, *, agents_client: AsyncAgentsClient):
		self._agents = agents_client

	async def list(
		self,
		agent: str,
		*,
		after: typing.Optional[str] = None,
		before: typing.Optional[str] = None,
		limit: typing.Optional[int] = None,
		request_options: typing.Optional[RequestOptions] = None,
	) -> typing.List[LettaMessageUnion]:
		agents = await self._agents.list(name=agent, request_options=request_options)
		if not agents or len(agents) == 0:
			return []

		agent_id = agents[0].id
		return await self._agents.messages.list(
			agent_id=agent_id,
			after=after,
			before=before,
			limit=limit,
			request_options=request_options
		)
