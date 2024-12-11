# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import message_list_params, message_create_params, message_update_params
from ...types.agents.message_list_response import MessageListResponse
from ...types.agents.message_create_response import MessageCreateResponse
from ...types.agents.message_update_response import MessageUpdateResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        agent_id: str,
        *,
        messages: Iterable[message_create_params.Message],
        assistant_message_tool_kwarg: str | NotGiven = NOT_GIVEN,
        assistant_message_tool_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCreateResponse:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent.

        Args:
          messages: The messages to be sent to the agent.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool.

          assistant_message_tool_name: The name of the designated message tool.

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
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateResponse,
        )

    def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_by_id: Optional[str] | NotGiven = NOT_GIVEN,
        last_updated_by_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        role: Optional[Literal["assistant", "user", "tool", "function", "system"]] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        tool_call_id: Optional[str] | NotGiven = NOT_GIVEN,
        tool_calls: Optional[Iterable[message_update_params.ToolCall]] | NotGiven = NOT_GIVEN,
        updated_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          created_at: The timestamp when the object was created.

          created_by_id: The id of the user that made this object.

          last_updated_by_id: The id of the user that made this object.

          name: The name of the participant.

          role: The role of the participant.

          text: The text of the message.

          tool_call_id: The id of the tool call.

          tool_calls: The list of tool calls requested.

          updated_at: The timestamp when the object was last updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/messages/{message_id}",
            body=maybe_transform(
                {
                    "created_at": created_at,
                    "created_by_id": created_by_id,
                    "last_updated_by_id": last_updated_by_id,
                    "name": name,
                    "role": role,
                    "text": text,
                    "tool_call_id": tool_call_id,
                    "tool_calls": tool_calls,
                    "updated_at": updated_at,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | NotGiven = NOT_GIVEN,
        assistant_message_tool_name: str | NotGiven = NOT_GIVEN,
        before: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        msg_object: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageListResponse:
        """
        Retrieve message history for an agent.

        Args:
          assistant_message_tool_kwarg: The name of the message argument in the designated message tool.

          assistant_message_tool_name: The name of the designated message tool.

          before: Message before which to retrieve the returned messages.

          limit: Maximum number of messages to retrieve.

          msg_object: If true, returns Message objects. If false, return LettaMessage objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return cast(
            MessageListResponse,
            self._get(
                f"/v1/agents/{agent_id}/messages",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                            "assistant_message_tool_name": assistant_message_tool_name,
                            "before": before,
                            "limit": limit,
                            "msg_object": msg_object,
                        },
                        message_list_params.MessageListParams,
                    ),
                ),
                cast_to=cast(
                    Any, MessageListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        agent_id: str,
        *,
        messages: Iterable[message_create_params.Message],
        assistant_message_tool_kwarg: str | NotGiven = NOT_GIVEN,
        assistant_message_tool_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCreateResponse:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent.

        Args:
          messages: The messages to be sent to the agent.

          assistant_message_tool_kwarg: The name of the message argument in the designated message tool.

          assistant_message_tool_name: The name of the designated message tool.

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
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateResponse,
        )

    async def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_by_id: Optional[str] | NotGiven = NOT_GIVEN,
        last_updated_by_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        role: Optional[Literal["assistant", "user", "tool", "function", "system"]] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        tool_call_id: Optional[str] | NotGiven = NOT_GIVEN,
        tool_calls: Optional[Iterable[message_update_params.ToolCall]] | NotGiven = NOT_GIVEN,
        updated_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageUpdateResponse:
        """
        Update the details of a message associated with an agent.

        Args:
          created_at: The timestamp when the object was created.

          created_by_id: The id of the user that made this object.

          last_updated_by_id: The id of the user that made this object.

          name: The name of the participant.

          role: The role of the participant.

          text: The text of the message.

          tool_call_id: The id of the tool call.

          tool_calls: The list of tool calls requested.

          updated_at: The timestamp when the object was last updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/messages/{message_id}",
            body=await async_maybe_transform(
                {
                    "created_at": created_at,
                    "created_by_id": created_by_id,
                    "last_updated_by_id": last_updated_by_id,
                    "name": name,
                    "role": role,
                    "text": text,
                    "tool_call_id": tool_call_id,
                    "tool_calls": tool_calls,
                    "updated_at": updated_at,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateResponse,
        )

    async def list(
        self,
        agent_id: str,
        *,
        assistant_message_tool_kwarg: str | NotGiven = NOT_GIVEN,
        assistant_message_tool_name: str | NotGiven = NOT_GIVEN,
        before: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        msg_object: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageListResponse:
        """
        Retrieve message history for an agent.

        Args:
          assistant_message_tool_kwarg: The name of the message argument in the designated message tool.

          assistant_message_tool_name: The name of the designated message tool.

          before: Message before which to retrieve the returned messages.

          limit: Maximum number of messages to retrieve.

          msg_object: If true, returns Message objects. If false, return LettaMessage objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return cast(
            MessageListResponse,
            await self._get(
                f"/v1/agents/{agent_id}/messages",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                            "assistant_message_tool_name": assistant_message_tool_name,
                            "before": before,
                            "limit": limit,
                            "msg_object": msg_object,
                        },
                        message_list_params.MessageListParams,
                    ),
                ),
                cast_to=cast(
                    Any, MessageListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_streamed_response_wrapper(
            messages.create,
        )
        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
