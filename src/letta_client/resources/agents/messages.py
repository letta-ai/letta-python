# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.agents import (
    message_list_params,
    message_reset_params,
    message_cancel_params,
    message_create_params,
    message_stream_params,
    message_create_async_params,
)
from ...types.agents.run import Run
from ...types.agent_state import AgentState
from ...types.agents.message import Message
from ...types.agents.message_type import MessageType
from ...types.agents.letta_response import LettaResponse
from ...types.agents.message_cancel_response import MessageCancelResponse
from ...types.agents.letta_streaming_response import LettaStreamingResponse

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

    @overload
    def create(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        streaming: Literal[False] | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LettaResponse:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent.

        The response format is controlled by the `streaming` field in the request body:

        - If `streaming=false` (default): Returns a complete LettaResponse with all
          messages
        - If `streaming=true`: Returns a Server-Sent Events (SSE) stream

        Additional streaming options (only used when streaming=true):

        - `stream_tokens`: Stream individual tokens instead of complete steps
        - `include_pings`: Include keepalive pings to prevent connection timeouts
        - `background`: Process the request in the background

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when
              streaming=true).

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when streaming=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when streaming=true).

          streaming: If True, returns a streaming response (Server-Sent Events). If False (default),
              returns a complete response.

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        agent_id: str,
        *,
        streaming: Literal[True],
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[LettaStreamingResponse]:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent.

        The response format is controlled by the `streaming` field in the request body:

        - If `streaming=false` (default): Returns a complete LettaResponse with all
          messages
        - If `streaming=true`: Returns a Server-Sent Events (SSE) stream

        Additional streaming options (only used when streaming=true):

        - `stream_tokens`: Stream individual tokens instead of complete steps
        - `include_pings`: Include keepalive pings to prevent connection timeouts
        - `background`: Process the request in the background

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          streaming: If True, returns a streaming response (Server-Sent Events). If False (default),
              returns a complete response.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when
              streaming=true).

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when streaming=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when streaming=true).

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        agent_id: str,
        *,
        streaming: bool,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LettaResponse | Stream[LettaStreamingResponse]:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent.

        The response format is controlled by the `streaming` field in the request body:

        - If `streaming=false` (default): Returns a complete LettaResponse with all
          messages
        - If `streaming=true`: Returns a Server-Sent Events (SSE) stream

        Additional streaming options (only used when streaming=true):

        - `stream_tokens`: Stream individual tokens instead of complete steps
        - `include_pings`: Include keepalive pings to prevent connection timeouts
        - `background`: Process the request in the background

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          streaming: If True, returns a streaming response (Server-Sent Events). If False (default),
              returns a complete response.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when
              streaming=true).

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when streaming=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when streaming=true).

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def create(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        streaming: Literal[False] | Literal[True] | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LettaResponse | Stream[LettaStreamingResponse]:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/messages",
            body=maybe_transform(
                {
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "background": background,
                    "enable_thinking": enable_thinking,
                    "include_pings": include_pings,
                    "include_return_message_types": include_return_message_types,
                    "input": input,
                    "max_steps": max_steps,
                    "messages": messages,
                    "stream_tokens": stream_tokens,
                    "streaming": streaming,
                    "use_assistant_message": use_assistant_message,
                },
                message_create_params.MessageCreateParamsStreaming
                if streaming
                else message_create_params.MessageCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LettaResponse,
            stream=streaming or False,
            stream_cls=Stream[LettaStreamingResponse],
        )

    def list(
        self,
        agent_id: str,
        *,
        after: Optional[str] | Omit = omit,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        before: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        include_err: Optional[bool] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncArrayPage[Message]:
        """
        Retrieve message history for an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          after: Message ID cursor for pagination. Returns messages that come after this message
              ID in the specified sort order

          assistant_message_tool_kwarg: The name of the message argument.

          assistant_message_tool_name: The name of the designated message tool.

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          group_id: Group ID to filter messages by.

          include_err: Whether to include error messages and error statuses. For debugging purposes
              only.

          limit: Maximum number of messages to return

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          use_assistant_message: Whether to use assistant messages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/v1/agents/{agent_id}/messages",
            page=SyncArrayPage[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                        "assistant_message_tool_name": assistant_message_tool_name,
                        "before": before,
                        "group_id": group_id,
                        "include_err": include_err,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                        "use_assistant_message": use_assistant_message,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=cast(Any, Message),  # Union types cannot be passed in as arguments in the type system
        )

    def cancel(
        self,
        agent_id: str,
        *,
        run_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCancelResponse:
        """Cancel runs associated with an agent.

        If run_ids are passed in, cancel those in
        particular.

        Note to cancel active runs associated with an agent, redis is required.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          run_ids: Optional list of run IDs to cancel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/messages/cancel",
            body=maybe_transform({"run_ids": run_ids}, message_cancel_params.MessageCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCancelResponse,
        )

    def compact(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Summarize an agent's conversation history.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/agents/{agent_id}/summarize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_async(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        callback_url: Optional[str] | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_async_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_async_params.Message]] | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """Asynchronously process a user message and return a run object.

        The actual
        processing happens in the background, and the status can be checked using the
        run ID.

        This is "asynchronous" in the sense that it's a background run and explicitly
        must be fetched by the run ID.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          callback_url: Optional callback URL to POST to when the job completes

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/messages/async",
            body=maybe_transform(
                {
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "callback_url": callback_url,
                    "enable_thinking": enable_thinking,
                    "include_return_message_types": include_return_message_types,
                    "input": input,
                    "max_steps": max_steps,
                    "messages": messages,
                    "use_assistant_message": use_assistant_message,
                },
                message_create_async_params.MessageCreateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    def reset(
        self,
        agent_id: str,
        *,
        add_default_initial_messages: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AgentState]:
        """
        Resets the messages for an agent

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          add_default_initial_messages: If true, adds the default initial messages after resetting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/reset-messages",
            body=maybe_transform(
                {"add_default_initial_messages": add_default_initial_messages}, message_reset_params.MessageResetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def stream(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_stream_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_stream_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        streaming: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[LettaStreamingResponse]:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent. It will stream the steps
        of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when
              streaming=true).

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when streaming=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when streaming=true).

          streaming: If True, returns a streaming response (Server-Sent Events). If False (default),
              returns a complete response.

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/messages/stream",
            body=maybe_transform(
                {
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "background": background,
                    "enable_thinking": enable_thinking,
                    "include_pings": include_pings,
                    "include_return_message_types": include_return_message_types,
                    "input": input,
                    "max_steps": max_steps,
                    "messages": messages,
                    "stream_tokens": stream_tokens,
                    "streaming": streaming,
                    "use_assistant_message": use_assistant_message,
                },
                message_stream_params.MessageStreamParams,
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

    @overload
    async def create(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        streaming: Literal[False] | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LettaResponse:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent.

        The response format is controlled by the `streaming` field in the request body:

        - If `streaming=false` (default): Returns a complete LettaResponse with all
          messages
        - If `streaming=true`: Returns a Server-Sent Events (SSE) stream

        Additional streaming options (only used when streaming=true):

        - `stream_tokens`: Stream individual tokens instead of complete steps
        - `include_pings`: Include keepalive pings to prevent connection timeouts
        - `background`: Process the request in the background

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when
              streaming=true).

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when streaming=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when streaming=true).

          streaming: If True, returns a streaming response (Server-Sent Events). If False (default),
              returns a complete response.

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        agent_id: str,
        *,
        streaming: Literal[True],
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[LettaStreamingResponse]:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent.

        The response format is controlled by the `streaming` field in the request body:

        - If `streaming=false` (default): Returns a complete LettaResponse with all
          messages
        - If `streaming=true`: Returns a Server-Sent Events (SSE) stream

        Additional streaming options (only used when streaming=true):

        - `stream_tokens`: Stream individual tokens instead of complete steps
        - `include_pings`: Include keepalive pings to prevent connection timeouts
        - `background`: Process the request in the background

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          streaming: If True, returns a streaming response (Server-Sent Events). If False (default),
              returns a complete response.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when
              streaming=true).

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when streaming=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when streaming=true).

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        agent_id: str,
        *,
        streaming: bool,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LettaResponse | AsyncStream[LettaStreamingResponse]:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent.

        The response format is controlled by the `streaming` field in the request body:

        - If `streaming=false` (default): Returns a complete LettaResponse with all
          messages
        - If `streaming=true`: Returns a Server-Sent Events (SSE) stream

        Additional streaming options (only used when streaming=true):

        - `stream_tokens`: Stream individual tokens instead of complete steps
        - `include_pings`: Include keepalive pings to prevent connection timeouts
        - `background`: Process the request in the background

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          streaming: If True, returns a streaming response (Server-Sent Events). If False (default),
              returns a complete response.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when
              streaming=true).

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when streaming=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when streaming=true).

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def create(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        streaming: Literal[False] | Literal[True] | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LettaResponse | AsyncStream[LettaStreamingResponse]:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/messages",
            body=await async_maybe_transform(
                {
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "background": background,
                    "enable_thinking": enable_thinking,
                    "include_pings": include_pings,
                    "include_return_message_types": include_return_message_types,
                    "input": input,
                    "max_steps": max_steps,
                    "messages": messages,
                    "stream_tokens": stream_tokens,
                    "streaming": streaming,
                    "use_assistant_message": use_assistant_message,
                },
                message_create_params.MessageCreateParamsStreaming
                if streaming
                else message_create_params.MessageCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LettaResponse,
            stream=streaming or False,
            stream_cls=AsyncStream[LettaStreamingResponse],
        )

    def list(
        self,
        agent_id: str,
        *,
        after: Optional[str] | Omit = omit,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        before: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        include_err: Optional[bool] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncArrayPage[Message]]:
        """
        Retrieve message history for an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          after: Message ID cursor for pagination. Returns messages that come after this message
              ID in the specified sort order

          assistant_message_tool_kwarg: The name of the message argument.

          assistant_message_tool_name: The name of the designated message tool.

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          group_id: Group ID to filter messages by.

          include_err: Whether to include error messages and error statuses. For debugging purposes
              only.

          limit: Maximum number of messages to return

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          use_assistant_message: Whether to use assistant messages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/v1/agents/{agent_id}/messages",
            page=AsyncArrayPage[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                        "assistant_message_tool_name": assistant_message_tool_name,
                        "before": before,
                        "group_id": group_id,
                        "include_err": include_err,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                        "use_assistant_message": use_assistant_message,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=cast(Any, Message),  # Union types cannot be passed in as arguments in the type system
        )

    async def cancel(
        self,
        agent_id: str,
        *,
        run_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCancelResponse:
        """Cancel runs associated with an agent.

        If run_ids are passed in, cancel those in
        particular.

        Note to cancel active runs associated with an agent, redis is required.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          run_ids: Optional list of run IDs to cancel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/messages/cancel",
            body=await async_maybe_transform({"run_ids": run_ids}, message_cancel_params.MessageCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCancelResponse,
        )

    async def compact(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Summarize an agent's conversation history.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/agents/{agent_id}/summarize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_async(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        callback_url: Optional[str] | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_create_async_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_create_async_params.Message]] | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """Asynchronously process a user message and return a run object.

        The actual
        processing happens in the background, and the status can be checked using the
        run ID.

        This is "asynchronous" in the sense that it's a background run and explicitly
        must be fetched by the run ID.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          callback_url: Optional callback URL to POST to when the job completes

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/messages/async",
            body=await async_maybe_transform(
                {
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "callback_url": callback_url,
                    "enable_thinking": enable_thinking,
                    "include_return_message_types": include_return_message_types,
                    "input": input,
                    "max_steps": max_steps,
                    "messages": messages,
                    "use_assistant_message": use_assistant_message,
                },
                message_create_async_params.MessageCreateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    async def reset(
        self,
        agent_id: str,
        *,
        add_default_initial_messages: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AgentState]:
        """
        Resets the messages for an agent

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          add_default_initial_messages: If true, adds the default initial messages after resetting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/reset-messages",
            body=await async_maybe_transform(
                {"add_default_initial_messages": add_default_initial_messages}, message_reset_params.MessageResetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def stream(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        input: Union[str, Iterable[message_stream_params.InputUnionMember1], None] | Omit = omit,
        max_steps: int | Omit = omit,
        messages: Optional[Iterable[message_stream_params.Message]] | Omit = omit,
        stream_tokens: bool | Omit = omit,
        streaming: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[LettaStreamingResponse]:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent. It will stream the steps
        of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background (only used when
              streaming=true).

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts (only used when streaming=true).

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          input:
              Syntactic sugar for a single user message. Equivalent to messages=[{'role':
              'user', 'content': input}].

          max_steps: Maximum number of steps the agent should take to process the request.

          messages: The messages to be sent to the agent.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step (only used when streaming=true).

          streaming: If True, returns a streaming response (Server-Sent Events). If False (default),
              returns a complete response.

          use_assistant_message: Whether the server should parse specific tool call arguments (default
              `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
              types, but deprecated for letta_v1_agent onward.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/messages/stream",
            body=await async_maybe_transform(
                {
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "background": background,
                    "enable_thinking": enable_thinking,
                    "include_pings": include_pings,
                    "include_return_message_types": include_return_message_types,
                    "input": input,
                    "max_steps": max_steps,
                    "messages": messages,
                    "stream_tokens": stream_tokens,
                    "streaming": streaming,
                    "use_assistant_message": use_assistant_message,
                },
                message_stream_params.MessageStreamParams,
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


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.cancel = to_raw_response_wrapper(
            messages.cancel,
        )
        self.compact = to_raw_response_wrapper(
            messages.compact,
        )
        self.create_async = to_raw_response_wrapper(
            messages.create_async,
        )
        self.reset = to_raw_response_wrapper(
            messages.reset,
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
        self.cancel = async_to_raw_response_wrapper(
            messages.cancel,
        )
        self.compact = async_to_raw_response_wrapper(
            messages.compact,
        )
        self.create_async = async_to_raw_response_wrapper(
            messages.create_async,
        )
        self.reset = async_to_raw_response_wrapper(
            messages.reset,
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
        self.cancel = to_streamed_response_wrapper(
            messages.cancel,
        )
        self.compact = to_streamed_response_wrapper(
            messages.compact,
        )
        self.create_async = to_streamed_response_wrapper(
            messages.create_async,
        )
        self.reset = to_streamed_response_wrapper(
            messages.reset,
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
        self.cancel = async_to_streamed_response_wrapper(
            messages.cancel,
        )
        self.compact = async_to_streamed_response_wrapper(
            messages.compact,
        )
        self.create_async = async_to_streamed_response_wrapper(
            messages.create_async,
        )
        self.reset = async_to_streamed_response_wrapper(
            messages.reset,
        )
        self.stream = async_to_streamed_response_wrapper(
            messages.stream,
        )
