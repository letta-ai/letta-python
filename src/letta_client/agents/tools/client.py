# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.agent_state import AgentState
from ...types.tool import Tool
from .raw_client import AsyncRawToolsClient, RawToolsClient


class ToolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawToolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawToolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawToolsClient
        """
        return self._raw_client

    def list(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Tool]:
        """
        Get tools from an existing agent

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tool]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.tools.list(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.list(agent_id, request_options=request_options)
        return _response.data

    def attach(
        self, agent_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentState:
        """
        Attach a tool to an agent.

        Parameters
        ----------
        agent_id : str

        tool_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentState
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.tools.attach(
            agent_id="agent_id",
            tool_id="tool_id",
        )
        """
        _response = self._raw_client.attach(agent_id, tool_id, request_options=request_options)
        return _response.data

    def detach(
        self, agent_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentState:
        """
        Detach a tool from an agent.

        Parameters
        ----------
        agent_id : str

        tool_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentState
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.tools.detach(
            agent_id="agent_id",
            tool_id="tool_id",
        )
        """
        _response = self._raw_client.detach(agent_id, tool_id, request_options=request_options)
        return _response.data


class AsyncToolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawToolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawToolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawToolsClient
        """
        return self._raw_client

    async def list(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tool]:
        """
        Get tools from an existing agent

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tool]
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.tools.list(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(agent_id, request_options=request_options)
        return _response.data

    async def attach(
        self, agent_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentState:
        """
        Attach a tool to an agent.

        Parameters
        ----------
        agent_id : str

        tool_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentState
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.tools.attach(
                agent_id="agent_id",
                tool_id="tool_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.attach(agent_id, tool_id, request_options=request_options)
        return _response.data

    async def detach(
        self, agent_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentState:
        """
        Detach a tool from an agent.

        Parameters
        ----------
        agent_id : str

        tool_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentState
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.tools.detach(
                agent_id="agent_id",
                tool_id="tool_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detach(agent_id, tool_id, request_options=request_options)
        return _response.data
