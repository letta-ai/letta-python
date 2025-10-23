# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import (
    message_list_params,
    message_send_params,
    message_reset_params,
    message_cancel_params,
    message_stream_params,
    message_update_params,
    message_send_async_params,
)
from ...types.agents.run import Run
from ...types.agent_state import AgentState
from ...types.agents.message_type import MessageType
from ...types.agents.letta_response import LettaResponse
from ...types.agents.message_list_response import MessageListResponse
from ...types.agents.message_cancel_response import MessageCancelResponse
from ...types.agents.message_update_response import MessageUpdateResponse
from ...types.agents.letta_user_message_content_union_param import LettaUserMessageContentUnionParam
from ...types.agents.letta_assistant_message_content_union_param import LettaAssistantMessageContentUnionParam

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
    def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        content: str,
        message_type: Literal["system_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          content: The message content sent by the system (can be a string or an array of
              multi-modal content parts)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        content: Union[Iterable[LettaUserMessageContentUnionParam], str],
        message_type: Literal["user_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          content: The message content sent by the user (can be a string or an array of multi-modal
              content parts)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        reasoning: str,
        message_type: Literal["reasoning_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        content: Union[Iterable[LettaAssistantMessageContentUnionParam], str],
        message_type: Literal["assistant_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          content: The message content sent by the assistant (can be a string or an array of
              content parts)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "content"], ["agent_id", "reasoning"])
    def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        content: str | Union[Iterable[LettaUserMessageContentUnionParam], str] | Omit = omit,
        message_type: Literal["system_message"]
        | Literal["user_message"]
        | Literal["reasoning_message"]
        | Literal["assistant_message"]
        | Omit = omit,
        reasoning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return cast(
            MessageUpdateResponse,
            self._patch(
                f"/v1/agents/{agent_id}/messages/{message_id}",
                body=maybe_transform(
                    {
                        "content": content,
                        "message_type": message_type,
                        "reasoning": reasoning,
                    },
                    message_update_params.MessageUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MessageUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> MessageListResponse:
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
        return self._get(
            f"/v1/agents/{agent_id}/messages",
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
            cast_to=MessageListResponse,
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
    ) -> AgentState:
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

    def send(
        self,
        agent_id: str,
        *,
        messages: Iterable[message_send_params.Message],
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        max_steps: int | Omit = omit,
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

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          messages: The messages to be sent to the agent.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          max_steps: Maximum number of steps the agent should take to process the request.

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
            f"/v1/agents/{agent_id}/messages",
            body=maybe_transform(
                {
                    "messages": messages,
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "enable_thinking": enable_thinking,
                    "include_return_message_types": include_return_message_types,
                    "max_steps": max_steps,
                    "use_assistant_message": use_assistant_message,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LettaResponse,
        )

    def send_async(
        self,
        agent_id: str,
        *,
        messages: Iterable[message_send_async_params.Message],
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        callback_url: Optional[str] | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        max_steps: int | Omit = omit,
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

          messages: The messages to be sent to the agent.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          callback_url: Optional callback URL to POST to when the job completes

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          max_steps: Maximum number of steps the agent should take to process the request.

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
                    "messages": messages,
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "callback_url": callback_url,
                    "enable_thinking": enable_thinking,
                    "include_return_message_types": include_return_message_types,
                    "max_steps": max_steps,
                    "use_assistant_message": use_assistant_message,
                },
                message_send_async_params.MessageSendAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    def stream(
        self,
        agent_id: str,
        *,
        messages: Iterable[message_stream_params.Message],
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        max_steps: int | Omit = omit,
        stream_tokens: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent. It will stream the steps
        of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          messages: The messages to be sent to the agent.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background.

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts.

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          max_steps: Maximum number of steps the agent should take to process the request.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step.

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
                    "messages": messages,
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "background": background,
                    "enable_thinking": enable_thinking,
                    "include_pings": include_pings,
                    "include_return_message_types": include_return_message_types,
                    "max_steps": max_steps,
                    "stream_tokens": stream_tokens,
                    "use_assistant_message": use_assistant_message,
                },
                message_stream_params.MessageStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def summarize(
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
    async def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        content: str,
        message_type: Literal["system_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          content: The message content sent by the system (can be a string or an array of
              multi-modal content parts)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        content: Union[Iterable[LettaUserMessageContentUnionParam], str],
        message_type: Literal["user_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          content: The message content sent by the user (can be a string or an array of multi-modal
              content parts)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        reasoning: str,
        message_type: Literal["reasoning_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        content: Union[Iterable[LettaAssistantMessageContentUnionParam], str],
        message_type: Literal["assistant_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          content: The message content sent by the assistant (can be a string or an array of
              content parts)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "content"], ["agent_id", "reasoning"])
    async def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        content: str | Union[Iterable[LettaUserMessageContentUnionParam], str] | Omit = omit,
        message_type: Literal["system_message"]
        | Literal["user_message"]
        | Literal["reasoning_message"]
        | Literal["assistant_message"]
        | Omit = omit,
        reasoning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return cast(
            MessageUpdateResponse,
            await self._patch(
                f"/v1/agents/{agent_id}/messages/{message_id}",
                body=await async_maybe_transform(
                    {
                        "content": content,
                        "message_type": message_type,
                        "reasoning": reasoning,
                    },
                    message_update_params.MessageUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MessageUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
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
    ) -> MessageListResponse:
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
        return await self._get(
            f"/v1/agents/{agent_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
            cast_to=MessageListResponse,
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
    ) -> AgentState:
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

    async def send(
        self,
        agent_id: str,
        *,
        messages: Iterable[message_send_params.Message],
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        max_steps: int | Omit = omit,
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

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          messages: The messages to be sent to the agent.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          max_steps: Maximum number of steps the agent should take to process the request.

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
            f"/v1/agents/{agent_id}/messages",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "enable_thinking": enable_thinking,
                    "include_return_message_types": include_return_message_types,
                    "max_steps": max_steps,
                    "use_assistant_message": use_assistant_message,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LettaResponse,
        )

    async def send_async(
        self,
        agent_id: str,
        *,
        messages: Iterable[message_send_async_params.Message],
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        callback_url: Optional[str] | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        max_steps: int | Omit = omit,
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

          messages: The messages to be sent to the agent.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          callback_url: Optional callback URL to POST to when the job completes

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          max_steps: Maximum number of steps the agent should take to process the request.

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
                    "messages": messages,
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "callback_url": callback_url,
                    "enable_thinking": enable_thinking,
                    "include_return_message_types": include_return_message_types,
                    "max_steps": max_steps,
                    "use_assistant_message": use_assistant_message,
                },
                message_send_async_params.MessageSendAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    async def stream(
        self,
        agent_id: str,
        *,
        messages: Iterable[message_stream_params.Message],
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        background: bool | Omit = omit,
        enable_thinking: str | Omit = omit,
        include_pings: bool | Omit = omit,
        include_return_message_types: Optional[List[MessageType]] | Omit = omit,
        max_steps: int | Omit = omit,
        stream_tokens: bool | Omit = omit,
        use_assistant_message: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent. It will stream the steps
        of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          messages: The messages to be sent to the agent.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool. Still supported
              for legacy agent types, but deprecated for letta_v1_agent onward.

          assistant_message_tool_name: The name of the designated message tool. Still supported for legacy agent types,
              but deprecated for letta_v1_agent onward.

          background: Whether to process the request in the background.

          enable_thinking: If set to True, enables reasoning before responses or tool calls from the agent.

          include_pings: Whether to include periodic keepalive ping messages in the stream to prevent
              connection timeouts.

          include_return_message_types: Only return specified message types in the response. If `None` (default) returns
              all messages.

          max_steps: Maximum number of steps the agent should take to process the request.

          stream_tokens: Flag to determine if individual tokens should be streamed, rather than streaming
              per step.

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
                    "messages": messages,
                    "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                    "assistant_message_tool_name": assistant_message_tool_name,
                    "background": background,
                    "enable_thinking": enable_thinking,
                    "include_pings": include_pings,
                    "include_return_message_types": include_return_message_types,
                    "max_steps": max_steps,
                    "stream_tokens": stream_tokens,
                    "use_assistant_message": use_assistant_message,
                },
                message_stream_params.MessageStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def summarize(
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


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.cancel = to_raw_response_wrapper(
            messages.cancel,
        )
        self.reset = to_raw_response_wrapper(
            messages.reset,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )
        self.send_async = to_raw_response_wrapper(
            messages.send_async,
        )
        self.stream = to_raw_response_wrapper(
            messages.stream,
        )
        self.summarize = to_raw_response_wrapper(
            messages.summarize,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            messages.cancel,
        )
        self.reset = async_to_raw_response_wrapper(
            messages.reset,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )
        self.send_async = async_to_raw_response_wrapper(
            messages.send_async,
        )
        self.stream = async_to_raw_response_wrapper(
            messages.stream,
        )
        self.summarize = async_to_raw_response_wrapper(
            messages.summarize,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.cancel = to_streamed_response_wrapper(
            messages.cancel,
        )
        self.reset = to_streamed_response_wrapper(
            messages.reset,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )
        self.send_async = to_streamed_response_wrapper(
            messages.send_async,
        )
        self.stream = to_streamed_response_wrapper(
            messages.stream,
        )
        self.summarize = to_streamed_response_wrapper(
            messages.summarize,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            messages.cancel,
        )
        self.reset = async_to_streamed_response_wrapper(
            messages.reset,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
        self.send_async = async_to_streamed_response_wrapper(
            messages.send_async,
        )
        self.stream = async_to_streamed_response_wrapper(
            messages.stream,
        )
        self.summarize = async_to_streamed_response_wrapper(
            messages.summarize,
        )
