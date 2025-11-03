# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
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
from ...types.groups import message_list_params, message_send_params, message_modify_params, message_stream_params
from ...types.agents.message_type import MessageType
from ...types.agents.letta_response import LettaResponse
from ...types.agents.letta_message_union import LettaMessageUnion
from ...types.groups.message_modify_response import MessageModifyResponse
from ...types.agents.letta_streaming_response import LettaStreamingResponse
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

    def list(
        self,
        group_id: str,
        *,
        after: Optional[str] | Omit = omit,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        before: Optional[str] | Omit = omit,
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
    ) -> SyncArrayPage[LettaMessageUnion]:
        """
        Retrieve message history for an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

          after: Message ID cursor for pagination. Returns messages that come after this message
              ID in the specified sort order

          assistant_message_tool_kwarg: The name of the message argument.

          assistant_message_tool_name: The name of the designated message tool.

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          limit: Maximum number of messages to retrieve

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          use_assistant_message: Whether to use assistant messages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get_api_list(
            f"/v1/groups/{group_id}/messages",
            page=SyncArrayPage[LettaMessageUnion],
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
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                        "use_assistant_message": use_assistant_message,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=cast(Any, LettaMessageUnion),  # Union types cannot be passed in as arguments in the type system
        )

    @overload
    def modify(
        self,
        message_id: str,
        *,
        group_id: str,
        content: str,
        message_type: Literal["system_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageModifyResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

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
    def modify(
        self,
        message_id: str,
        *,
        group_id: str,
        content: Union[Iterable[LettaUserMessageContentUnionParam], str],
        message_type: Literal["user_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageModifyResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

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
    def modify(
        self,
        message_id: str,
        *,
        group_id: str,
        reasoning: str,
        message_type: Literal["reasoning_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageModifyResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def modify(
        self,
        message_id: str,
        *,
        group_id: str,
        content: Union[Iterable[LettaAssistantMessageContentUnionParam], str],
        message_type: Literal["assistant_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageModifyResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          content: The message content sent by the assistant (can be a string or an array of
              content parts)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["group_id", "content"], ["group_id", "reasoning"])
    def modify(
        self,
        message_id: str,
        *,
        group_id: str,
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
    ) -> MessageModifyResponse:
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return cast(
            MessageModifyResponse,
            self._patch(
                f"/v1/groups/{group_id}/messages/{message_id}",
                body=maybe_transform(
                    {
                        "content": content,
                        "message_type": message_type,
                        "reasoning": reasoning,
                    },
                    message_modify_params.MessageModifyParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MessageModifyResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def reset(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete the group messages for all agents that are part of the multi-agent group.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._patch(
            f"/v1/groups/{group_id}/reset-messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def send(
        self,
        group_id: str,
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
        """Process a user message and return the group's response.

        This endpoint accepts a
        message from a user and processes it through through agents in the group based
        on the specified pattern

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            f"/v1/groups/{group_id}/messages",
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

    def stream(
        self,
        group_id: str,
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
    ) -> Stream[LettaStreamingResponse]:
        """Process a user message and return the group's responses.

        This endpoint accepts a
        message from a user and processes it through agents in the group based on the
        specified pattern. It will stream the steps of the response always, and stream
        the tokens if 'stream_tokens' is set to True.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            f"/v1/groups/{group_id}/messages/stream",
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

    def list(
        self,
        group_id: str,
        *,
        after: Optional[str] | Omit = omit,
        assistant_message_tool_kwarg: str | Omit = omit,
        assistant_message_tool_name: str | Omit = omit,
        before: Optional[str] | Omit = omit,
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
    ) -> AsyncPaginator[LettaMessageUnion, AsyncArrayPage[LettaMessageUnion]]:
        """
        Retrieve message history for an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

          after: Message ID cursor for pagination. Returns messages that come after this message
              ID in the specified sort order

          assistant_message_tool_kwarg: The name of the message argument.

          assistant_message_tool_name: The name of the designated message tool.

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          limit: Maximum number of messages to retrieve

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          use_assistant_message: Whether to use assistant messages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get_api_list(
            f"/v1/groups/{group_id}/messages",
            page=AsyncArrayPage[LettaMessageUnion],
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
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                        "use_assistant_message": use_assistant_message,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=cast(Any, LettaMessageUnion),  # Union types cannot be passed in as arguments in the type system
        )

    @overload
    async def modify(
        self,
        message_id: str,
        *,
        group_id: str,
        content: str,
        message_type: Literal["system_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageModifyResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

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
    async def modify(
        self,
        message_id: str,
        *,
        group_id: str,
        content: Union[Iterable[LettaUserMessageContentUnionParam], str],
        message_type: Literal["user_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageModifyResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

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
    async def modify(
        self,
        message_id: str,
        *,
        group_id: str,
        reasoning: str,
        message_type: Literal["reasoning_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageModifyResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def modify(
        self,
        message_id: str,
        *,
        group_id: str,
        content: Union[Iterable[LettaAssistantMessageContentUnionParam], str],
        message_type: Literal["assistant_message"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageModifyResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

          message_id: The ID of the message in the format 'message-<uuid4>'

          content: The message content sent by the assistant (can be a string or an array of
              content parts)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["group_id", "content"], ["group_id", "reasoning"])
    async def modify(
        self,
        message_id: str,
        *,
        group_id: str,
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
    ) -> MessageModifyResponse:
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return cast(
            MessageModifyResponse,
            await self._patch(
                f"/v1/groups/{group_id}/messages/{message_id}",
                body=await async_maybe_transform(
                    {
                        "content": content,
                        "message_type": message_type,
                        "reasoning": reasoning,
                    },
                    message_modify_params.MessageModifyParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MessageModifyResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def reset(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete the group messages for all agents that are part of the multi-agent group.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._patch(
            f"/v1/groups/{group_id}/reset-messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def send(
        self,
        group_id: str,
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
        """Process a user message and return the group's response.

        This endpoint accepts a
        message from a user and processes it through through agents in the group based
        on the specified pattern

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            f"/v1/groups/{group_id}/messages",
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

    async def stream(
        self,
        group_id: str,
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
    ) -> AsyncStream[LettaStreamingResponse]:
        """Process a user message and return the group's responses.

        This endpoint accepts a
        message from a user and processes it through agents in the group based on the
        specified pattern. It will stream the steps of the response always, and stream
        the tokens if 'stream_tokens' is set to True.

        Args:
          group_id: The ID of the group in the format 'group-<uuid4>'

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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            f"/v1/groups/{group_id}/messages/stream",
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
            stream=True,
            stream_cls=AsyncStream[LettaStreamingResponse],
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.modify = to_raw_response_wrapper(
            messages.modify,
        )
        self.reset = to_raw_response_wrapper(
            messages.reset,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )
        self.stream = to_raw_response_wrapper(
            messages.stream,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.modify = async_to_raw_response_wrapper(
            messages.modify,
        )
        self.reset = async_to_raw_response_wrapper(
            messages.reset,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )
        self.stream = async_to_raw_response_wrapper(
            messages.stream,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.modify = to_streamed_response_wrapper(
            messages.modify,
        )
        self.reset = to_streamed_response_wrapper(
            messages.reset,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )
        self.stream = to_streamed_response_wrapper(
            messages.stream,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.modify = async_to_streamed_response_wrapper(
            messages.modify,
        )
        self.reset = async_to_streamed_response_wrapper(
            messages.reset,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
        self.stream = async_to_streamed_response_wrapper(
            messages.stream,
        )
