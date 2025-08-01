# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.agent_state import AgentState
from ...types.letta_message_union import LettaMessageUnion
from ...types.letta_response import LettaResponse
from ...types.message_create import MessageCreate
from ...types.message_type import MessageType
from ...types.run import Run
from .raw_client import AsyncRawMessagesClient, RawMessagesClient
from .types.letta_streaming_response import LettaStreamingResponse
from .types.messages_modify_request import MessagesModifyRequest
from .types.messages_modify_response import MessagesModifyResponse
from .types.messages_preview_raw_payload_request import MessagesPreviewRawPayloadRequest

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMessagesClient
        """
        return self._raw_client

    def list(
        self,
        agent_id: str,
        *,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        group_id: typing.Optional[str] = None,
        use_assistant_message: typing.Optional[bool] = None,
        assistant_message_tool_name: typing.Optional[str] = None,
        assistant_message_tool_kwarg: typing.Optional[str] = None,
        include_err: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LettaMessageUnion]:
        """
        Retrieve message history for an agent.

        Parameters
        ----------
        agent_id : str

        after : typing.Optional[str]
            Message after which to retrieve the returned messages.

        before : typing.Optional[str]
            Message before which to retrieve the returned messages.

        limit : typing.Optional[int]
            Maximum number of messages to retrieve.

        group_id : typing.Optional[str]
            Group ID to filter messages by.

        use_assistant_message : typing.Optional[bool]
            Whether to use assistant messages

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument.

        include_err : typing.Optional[bool]
            Whether to include error messages and error statuses. For debugging purposes only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.messages.list(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.list(
            agent_id,
            after=after,
            before=before,
            limit=limit,
            group_id=group_id,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_err=include_err,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[MessageCreate],
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LettaResponse:
        """
        Process a user message and return the agent's response.
        This endpoint accepts a message from a user and processes it through the agent.

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[MessageCreate]
            The messages to be sent to the agent.

        max_steps : typing.Optional[int]
            Maximum number of steps the agent should take to process the request.

        use_assistant_message : typing.Optional[bool]
            Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument in the designated message tool.

        include_return_message_types : typing.Optional[typing.Sequence[MessageType]]
            Only return specified message types in the response. If `None` (default) returns all messages.

        enable_thinking : typing.Optional[str]
            If set to True, enables reasoning before responses or tool calls from the agent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LettaResponse
            Successful Response

        Examples
        --------
        from letta_client import Letta, MessageCreate, TextContent

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.messages.create(
            agent_id="agent_id",
            messages=[
                MessageCreate(
                    role="user",
                    content=[
                        TextContent(
                            text="text",
                        )
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.create(
            agent_id,
            messages=messages,
            max_steps=max_steps,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_return_message_types=include_return_message_types,
            enable_thinking=enable_thinking,
            request_options=request_options,
        )
        return _response.data

    def modify(
        self,
        agent_id: str,
        message_id: str,
        *,
        request: MessagesModifyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagesModifyResponse:
        """
        Update the details of a message associated with an agent.

        Parameters
        ----------
        agent_id : str

        message_id : str

        request : MessagesModifyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagesModifyResponse
            Successful Response

        Examples
        --------
        from letta_client import Letta, UpdateSystemMessage

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.messages.modify(
            agent_id="agent_id",
            message_id="message_id",
            request=UpdateSystemMessage(
                content="content",
            ),
        )
        """
        _response = self._raw_client.modify(agent_id, message_id, request=request, request_options=request_options)
        return _response.data

    def create_stream(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[MessageCreate],
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        stream_tokens: typing.Optional[bool] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[LettaStreamingResponse]:
        """
        Process a user message and return the agent's response.
        This endpoint accepts a message from a user and processes it through the agent.
        It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[MessageCreate]
            The messages to be sent to the agent.

        max_steps : typing.Optional[int]
            Maximum number of steps the agent should take to process the request.

        use_assistant_message : typing.Optional[bool]
            Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument in the designated message tool.

        include_return_message_types : typing.Optional[typing.Sequence[MessageType]]
            Only return specified message types in the response. If `None` (default) returns all messages.

        enable_thinking : typing.Optional[str]
            If set to True, enables reasoning before responses or tool calls from the agent.

        stream_tokens : typing.Optional[bool]
            Flag to determine if individual tokens should be streamed. Set to True for token streaming (requires stream_steps = True).

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[LettaStreamingResponse]
            Successful response

        Examples
        --------
        from letta_client import Letta, MessageCreate, TextContent

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        response = client.agents.messages.create_stream(
            agent_id="agent_id",
            messages=[
                MessageCreate(
                    role="user",
                    content=[
                        TextContent(
                            text="text",
                        )
                    ],
                )
            ],
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.create_stream(
            agent_id,
            messages=messages,
            max_steps=max_steps,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_return_message_types=include_return_message_types,
            enable_thinking=enable_thinking,
            stream_tokens=stream_tokens,
            include_pings=include_pings,
            request_options=request_options,
        ) as r:
            yield from r.data

    def cancel(
        self,
        agent_id: str,
        *,
        request: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Cancel runs associated with an agent. If run_ids are passed in, cancel those in particular.

        Note to cancel active runs associated with an agent, redis is required.

        Parameters
        ----------
        agent_id : str

        request : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.messages.cancel(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.cancel(agent_id, request=request, request_options=request_options)
        return _response.data

    def create_async(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[MessageCreate],
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Run:
        """
        Asynchronously process a user message and return a run object.
        The actual processing happens in the background, and the status can be checked using the run ID.

        This is "asynchronous" in the sense that it's a background job and explicitly must be fetched by the run ID.
        This is more like `send_message_job`

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[MessageCreate]
            The messages to be sent to the agent.

        max_steps : typing.Optional[int]
            Maximum number of steps the agent should take to process the request.

        use_assistant_message : typing.Optional[bool]
            Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument in the designated message tool.

        include_return_message_types : typing.Optional[typing.Sequence[MessageType]]
            Only return specified message types in the response. If `None` (default) returns all messages.

        enable_thinking : typing.Optional[str]
            If set to True, enables reasoning before responses or tool calls from the agent.

        callback_url : typing.Optional[str]
            Optional callback URL to POST to when the job completes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Run
            Successful Response

        Examples
        --------
        from letta_client import Letta, MessageCreate, TextContent

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.messages.create_async(
            agent_id="agent_id",
            messages=[
                MessageCreate(
                    role="user",
                    content=[
                        TextContent(
                            text="text",
                        )
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.create_async(
            agent_id,
            messages=messages,
            max_steps=max_steps,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_return_message_types=include_return_message_types,
            enable_thinking=enable_thinking,
            callback_url=callback_url,
            request_options=request_options,
        )
        return _response.data

    def reset(
        self,
        agent_id: str,
        *,
        add_default_initial_messages: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentState:
        """
        Resets the messages for an agent

        Parameters
        ----------
        agent_id : str

        add_default_initial_messages : typing.Optional[bool]
            If true, adds the default initial messages after resetting.

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
        client.agents.messages.reset(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.reset(
            agent_id, add_default_initial_messages=add_default_initial_messages, request_options=request_options
        )
        return _response.data

    def preview_raw_payload(
        self,
        agent_id: str,
        *,
        request: MessagesPreviewRawPayloadRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Inspect the raw LLM request payload without sending it.

        This endpoint processes the message through the agent loop up until
        the LLM request, then returns the raw request payload that would
        be sent to the LLM provider. Useful for debugging and inspection.

        Parameters
        ----------
        agent_id : str

        request : MessagesPreviewRawPayloadRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            Successful Response

        Examples
        --------
        from letta_client import Letta, LettaRequest, MessageCreate, TextContent

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            request=LettaRequest(
                messages=[
                    MessageCreate(
                        role="user",
                        content=[
                            TextContent(
                                text="text",
                            )
                        ],
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.preview_raw_payload(agent_id, request=request, request_options=request_options)
        return _response.data


class AsyncMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMessagesClient
        """
        return self._raw_client

    async def list(
        self,
        agent_id: str,
        *,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        group_id: typing.Optional[str] = None,
        use_assistant_message: typing.Optional[bool] = None,
        assistant_message_tool_name: typing.Optional[str] = None,
        assistant_message_tool_kwarg: typing.Optional[str] = None,
        include_err: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LettaMessageUnion]:
        """
        Retrieve message history for an agent.

        Parameters
        ----------
        agent_id : str

        after : typing.Optional[str]
            Message after which to retrieve the returned messages.

        before : typing.Optional[str]
            Message before which to retrieve the returned messages.

        limit : typing.Optional[int]
            Maximum number of messages to retrieve.

        group_id : typing.Optional[str]
            Group ID to filter messages by.

        use_assistant_message : typing.Optional[bool]
            Whether to use assistant messages

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument.

        include_err : typing.Optional[bool]
            Whether to include error messages and error statuses. For debugging purposes only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
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
            await client.agents.messages.list(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            agent_id,
            after=after,
            before=before,
            limit=limit,
            group_id=group_id,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_err=include_err,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[MessageCreate],
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LettaResponse:
        """
        Process a user message and return the agent's response.
        This endpoint accepts a message from a user and processes it through the agent.

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[MessageCreate]
            The messages to be sent to the agent.

        max_steps : typing.Optional[int]
            Maximum number of steps the agent should take to process the request.

        use_assistant_message : typing.Optional[bool]
            Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument in the designated message tool.

        include_return_message_types : typing.Optional[typing.Sequence[MessageType]]
            Only return specified message types in the response. If `None` (default) returns all messages.

        enable_thinking : typing.Optional[str]
            If set to True, enables reasoning before responses or tool calls from the agent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LettaResponse
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta, MessageCreate, TextContent

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.messages.create(
                agent_id="agent_id",
                messages=[
                    MessageCreate(
                        role="user",
                        content=[
                            TextContent(
                                text="text",
                            )
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            agent_id,
            messages=messages,
            max_steps=max_steps,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_return_message_types=include_return_message_types,
            enable_thinking=enable_thinking,
            request_options=request_options,
        )
        return _response.data

    async def modify(
        self,
        agent_id: str,
        message_id: str,
        *,
        request: MessagesModifyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagesModifyResponse:
        """
        Update the details of a message associated with an agent.

        Parameters
        ----------
        agent_id : str

        message_id : str

        request : MessagesModifyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagesModifyResponse
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta, UpdateSystemMessage

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.messages.modify(
                agent_id="agent_id",
                message_id="message_id",
                request=UpdateSystemMessage(
                    content="content",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify(
            agent_id, message_id, request=request, request_options=request_options
        )
        return _response.data

    async def create_stream(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[MessageCreate],
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        stream_tokens: typing.Optional[bool] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[LettaStreamingResponse]:
        """
        Process a user message and return the agent's response.
        This endpoint accepts a message from a user and processes it through the agent.
        It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[MessageCreate]
            The messages to be sent to the agent.

        max_steps : typing.Optional[int]
            Maximum number of steps the agent should take to process the request.

        use_assistant_message : typing.Optional[bool]
            Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument in the designated message tool.

        include_return_message_types : typing.Optional[typing.Sequence[MessageType]]
            Only return specified message types in the response. If `None` (default) returns all messages.

        enable_thinking : typing.Optional[str]
            If set to True, enables reasoning before responses or tool calls from the agent.

        stream_tokens : typing.Optional[bool]
            Flag to determine if individual tokens should be streamed. Set to True for token streaming (requires stream_steps = True).

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[LettaStreamingResponse]
            Successful response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta, MessageCreate, TextContent

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.agents.messages.create_stream(
                agent_id="agent_id",
                messages=[
                    MessageCreate(
                        role="user",
                        content=[
                            TextContent(
                                text="text",
                            )
                        ],
                    )
                ],
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.create_stream(
            agent_id,
            messages=messages,
            max_steps=max_steps,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_return_message_types=include_return_message_types,
            enable_thinking=enable_thinking,
            stream_tokens=stream_tokens,
            include_pings=include_pings,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def cancel(
        self,
        agent_id: str,
        *,
        request: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Cancel runs associated with an agent. If run_ids are passed in, cancel those in particular.

        Note to cancel active runs associated with an agent, redis is required.

        Parameters
        ----------
        agent_id : str

        request : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
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
            await client.agents.messages.cancel(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel(agent_id, request=request, request_options=request_options)
        return _response.data

    async def create_async(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[MessageCreate],
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Run:
        """
        Asynchronously process a user message and return a run object.
        The actual processing happens in the background, and the status can be checked using the run ID.

        This is "asynchronous" in the sense that it's a background job and explicitly must be fetched by the run ID.
        This is more like `send_message_job`

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[MessageCreate]
            The messages to be sent to the agent.

        max_steps : typing.Optional[int]
            Maximum number of steps the agent should take to process the request.

        use_assistant_message : typing.Optional[bool]
            Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument in the designated message tool.

        include_return_message_types : typing.Optional[typing.Sequence[MessageType]]
            Only return specified message types in the response. If `None` (default) returns all messages.

        enable_thinking : typing.Optional[str]
            If set to True, enables reasoning before responses or tool calls from the agent.

        callback_url : typing.Optional[str]
            Optional callback URL to POST to when the job completes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Run
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta, MessageCreate, TextContent

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.messages.create_async(
                agent_id="agent_id",
                messages=[
                    MessageCreate(
                        role="user",
                        content=[
                            TextContent(
                                text="text",
                            )
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_async(
            agent_id,
            messages=messages,
            max_steps=max_steps,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_return_message_types=include_return_message_types,
            enable_thinking=enable_thinking,
            callback_url=callback_url,
            request_options=request_options,
        )
        return _response.data

    async def reset(
        self,
        agent_id: str,
        *,
        add_default_initial_messages: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentState:
        """
        Resets the messages for an agent

        Parameters
        ----------
        agent_id : str

        add_default_initial_messages : typing.Optional[bool]
            If true, adds the default initial messages after resetting.

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
            await client.agents.messages.reset(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset(
            agent_id, add_default_initial_messages=add_default_initial_messages, request_options=request_options
        )
        return _response.data

    async def preview_raw_payload(
        self,
        agent_id: str,
        *,
        request: MessagesPreviewRawPayloadRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Inspect the raw LLM request payload without sending it.

        This endpoint processes the message through the agent loop up until
        the LLM request, then returns the raw request payload that would
        be sent to the LLM provider. Useful for debugging and inspection.

        Parameters
        ----------
        agent_id : str

        request : MessagesPreviewRawPayloadRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta, LettaRequest, MessageCreate, TextContent

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.messages.preview_raw_payload(
                agent_id="agent_id",
                request=LettaRequest(
                    messages=[
                        MessageCreate(
                            role="user",
                            content=[
                                TextContent(
                                    text="text",
                                )
                            ],
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_raw_payload(
            agent_id, request=request, request_options=request_options
        )
        return _response.data
