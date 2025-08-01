# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.agent_state import AgentState
from ...types.source import Source
from .raw_client import AsyncRawSourcesClient, RawSourcesClient


class SourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourcesClient
        """
        return self._raw_client

    def attach(
        self, agent_id: str, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentState:
        """
        Attach a source to an agent.

        Parameters
        ----------
        agent_id : str

        source_id : str

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
        client.agents.sources.attach(
            agent_id="agent_id",
            source_id="source_id",
        )
        """
        _response = self._raw_client.attach(agent_id, source_id, request_options=request_options)
        return _response.data

    def detach(
        self, agent_id: str, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentState:
        """
        Detach a source from an agent.

        Parameters
        ----------
        agent_id : str

        source_id : str

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
        client.agents.sources.detach(
            agent_id="agent_id",
            source_id="source_id",
        )
        """
        _response = self._raw_client.detach(agent_id, source_id, request_options=request_options)
        return _response.data

    def list(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Source]:
        """
        Get the sources associated with an agent.

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Source]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.sources.list(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.list(agent_id, request_options=request_options)
        return _response.data


class AsyncSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourcesClient
        """
        return self._raw_client

    async def attach(
        self, agent_id: str, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentState:
        """
        Attach a source to an agent.

        Parameters
        ----------
        agent_id : str

        source_id : str

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
            await client.agents.sources.attach(
                agent_id="agent_id",
                source_id="source_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.attach(agent_id, source_id, request_options=request_options)
        return _response.data

    async def detach(
        self, agent_id: str, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentState:
        """
        Detach a source from an agent.

        Parameters
        ----------
        agent_id : str

        source_id : str

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
            await client.agents.sources.detach(
                agent_id="agent_id",
                source_id="source_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detach(agent_id, source_id, request_options=request_options)
        return _response.data

    async def list(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Source]:
        """
        Get the sources associated with an agent.

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Source]
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
            await client.agents.sources.list(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(agent_id, request_options=request_options)
        return _response.data
