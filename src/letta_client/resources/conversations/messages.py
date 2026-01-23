# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...pagination import SyncArrayPage, AsyncArrayPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.conversations import (
    message_list_params,
    message_create_params,
    message_stream_params,
    message_compact_params,
)
from ...types.agents.message import Message
from ...types.agents.message_type import MessageType
from ...types.agents.letta_streaming_response import LettaStreamingResponse
from ...types.conversations.compaction_response import CompactionResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def create(
        self,
        conversation_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        client_tools: Optional[Iterable[message_create_params.ClientTool]] | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        override_model: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        stream_tokens: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[LettaStreamingResponse]:
        """
        Send a message to a conversation and get a response.

        This endpoint sends a message to an existing conversation. By default
        (stream=true), returns a streaming response (Server-Sent Events). Set
        stream=false to get a complete JSON response.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when stream=true).

          client_tools: Client-side tools that the agent can call. When the agent calls a client-side
              tool, execution pauses and returns control to the client to execute the tool and
              provide the result via a ToolReturn.

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when stream=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          override_model: Model handle to use for this request instead of the agent's default model. This
              allows sending a message to a different model without changing the agent's
              configuration.

          stream: If True (default), returns a streaming response (Server-Sent Events). If False,
              returns a complete JSON response.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when stream=true).

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            f"/v1/conversations/{conversation_id}/messages",
            body=maybe_transform(
                {
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "background": background,
                    "client_tools": client_tools,
                    "enable_thinking": enable_thinking,
                    "include_pings": include_pings,
                    "include_return_message_types": include_return_message_types,
                    "input": input,
                    "max_steps": max_steps,
                    "messages": messages,
                    "override_model": override_model,
                    "stream": stream,
                    "stream_tokens": stream_tokens,
                    "use_assistant_message": use_assistant_message,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, LettaStreamingResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[LettaStreamingResponse],
        )

    def list(
        self,
        conversation_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        include_err: Optional[bool] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncArrayPage[Message]:
        """
        List all messages in a conversation.

        Returns LettaMessage objects (UserMessage, AssistantMessage, etc.) for all
        messages in the conversation, with support for cursor-based pagination.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          after: Message ID cursor for pagination. Returns messages that come after this message
              ID in the specified sort order

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          group_id: Group ID to filter messages by.

          include_err: Whether to include error messages and error statuses. For debugging purposes
              only.

          limit: Maximum number of messages to return

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get_api_list(
            f"/v1/conversations/{conversation_id}/messages",
            page=SyncArrayPage[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "group_id": group_id,
                        "include_err": include_err,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=cast(Any, Message),  # Union types cannot be passed in as arguments in the type system
        )

    def compact(
        self,
        conversation_id: str,
        *,
        compaction_settings: Optional[message_compact_params.CompactionSettings] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompactionResponse:
        """
        Compact (summarize) a conversation's message history.

        This endpoint summarizes the in-context messages for a specific conversation,
        reducing the message count while preserving important context.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          compaction_settings: Configuration for conversation compaction / summarization.

              `model` is the only required user-facing field – it specifies the summarizer
              model handle (e.g. `"openai/gpt-4o-mini"`). Per-model settings (temperature, max
              tokens, etc.) are derived from the default configuration for that handle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            f"/v1/conversations/{conversation_id}/compact",
            body=maybe_transform(
                {"compaction_settings": compaction_settings}, message_compact_params.MessageCompactParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompactionResponse,
        )

    def stream(
        self,
        conversation_id: str,
        *,
        batch_size: Optional[int] | Omit = omit,
        include_pings: Optional[bool] | Omit = omit,
        poll_interval: Optional[float] | Omit = omit,
        starting_after: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[LettaStreamingResponse]:
        """
        Resume the stream for the most recent active run in a conversation.

        This endpoint allows you to reconnect to an active background stream for a
        conversation, enabling recovery from network interruptions.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          batch_size: Number of entries to read per batch.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts.

          poll_interval: Seconds to wait between polls when no new data.

          starting_after: Sequence id to use as a cursor for pagination. Response will start streaming
              after this chunk sequence id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            f"/v1/conversations/{conversation_id}/stream",
            body=maybe_transform(
                {
                    "batch_size": batch_size,
                    "include_pings": include_pings,
                    "poll_interval": poll_interval,
                    "starting_after": starting_after,
                },
                message_stream_params.MessageStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
            stream=True,
            stream_cls=Stream[LettaStreamingResponse],
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        conversation_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        client_tools: Optional[Iterable[message_create_params.ClientTool]] | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        override_model: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        stream_tokens: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[LettaStreamingResponse]:
        """
        Send a message to a conversation and get a response.

        This endpoint sends a message to an existing conversation. By default
        (stream=true), returns a streaming response (Server-Sent Events). Set
        stream=false to get a complete JSON response.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when stream=true).

          client_tools: Client-side tools that the agent can call. When the agent calls a client-side
              tool, execution pauses and returns control to the client to execute the tool and
              provide the result via a ToolReturn.

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when stream=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          override_model: Model handle to use for this request instead of the agent's default model. This
              allows sending a message to a different model without changing the agent's
              configuration.

          stream: If True (default), returns a streaming response (Server-Sent Events). If False,
              returns a complete JSON response.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when stream=true).

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            f"/v1/conversations/{conversation_id}/messages",
            body=await async_maybe_transform(
                {
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "background": background,
                    "client_tools": client_tools,
                    "enable_thinking": enable_thinking,
                    "include_pings": include_pings,
                    "include_return_message_types": include_return_message_types,
                    "input": input,
                    "max_steps": max_steps,
                    "messages": messages,
                    "override_model": override_model,
                    "stream": stream,
                    "stream_tokens": stream_tokens,
                    "use_assistant_message": use_assistant_message,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, LettaStreamingResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[LettaStreamingResponse],
        )

    def list(
        self,
        conversation_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        include_err: Optional[bool] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncArrayPage[Message]]:
        """
        List all messages in a conversation.

        Returns LettaMessage objects (UserMessage, AssistantMessage, etc.) for all
        messages in the conversation, with support for cursor-based pagination.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          after: Message ID cursor for pagination. Returns messages that come after this message
              ID in the specified sort order

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          group_id: Group ID to filter messages by.

          include_err: Whether to include error messages and error statuses. For debugging purposes
              only.

          limit: Maximum number of messages to return

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get_api_list(
            f"/v1/conversations/{conversation_id}/messages",
            page=AsyncArrayPage[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "group_id": group_id,
                        "include_err": include_err,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=cast(Any, Message),  # Union types cannot be passed in as arguments in the type system
        )

    async def compact(
        self,
        conversation_id: str,
        *,
        compaction_settings: Optional[message_compact_params.CompactionSettings] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompactionResponse:
        """
        Compact (summarize) a conversation's message history.

        This endpoint summarizes the in-context messages for a specific conversation,
        reducing the message count while preserving important context.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          compaction_settings: Configuration for conversation compaction / summarization.

              `model` is the only required user-facing field – it specifies the summarizer
              model handle (e.g. `"openai/gpt-4o-mini"`). Per-model settings (temperature, max
              tokens, etc.) are derived from the default configuration for that handle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            f"/v1/conversations/{conversation_id}/compact",
            body=await async_maybe_transform(
                {"compaction_settings": compaction_settings}, message_compact_params.MessageCompactParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompactionResponse,
        )

    async def stream(
        self,
        conversation_id: str,
        *,
        batch_size: Optional[int] | Omit = omit,
        include_pings: Optional[bool] | Omit = omit,
        poll_interval: Optional[float] | Omit = omit,
        starting_after: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[LettaStreamingResponse]:
        """
        Resume the stream for the most recent active run in a conversation.

        This endpoint allows you to reconnect to an active background stream for a
        conversation, enabling recovery from network interruptions.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          batch_size: Number of entries to read per batch.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts.

          poll_interval: Seconds to wait between polls when no new data.

          starting_after: Sequence id to use as a cursor for pagination. Response will start streaming
              after this chunk sequence id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            f"/v1/conversations/{conversation_id}/stream",
            body=await async_maybe_transform(
                {
                    "batch_size": batch_size,
                    "include_pings": include_pings,
                    "poll_interval": poll_interval,
                    "starting_after": starting_after,
                },
                message_stream_params.MessageStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
            stream=True,
            stream_cls=AsyncStream[LettaStreamingResponse],
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.compact = to_raw_response_wrapper(
            messages.compact,
        )
        self.stream = to_raw_response_wrapper(
            messages.stream,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.compact = async_to_raw_response_wrapper(
            messages.compact,
        )
        self.stream = async_to_raw_response_wrapper(
            messages.stream,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_streamed_response_wrapper(
            messages.create,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.compact = to_streamed_response_wrapper(
            messages.compact,
        )
        self.stream = to_streamed_response_wrapper(
            messages.stream,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.compact = async_to_streamed_response_wrapper(
            messages.compact,
        )
        self.stream = async_to_streamed_response_wrapper(
            messages.stream,
        )
