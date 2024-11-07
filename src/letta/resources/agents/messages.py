# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
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
from ...types.agents import message_update_params, message_process_params, message_retrieve_params
from ...types.agents.messageoutput import Messageoutput
from ...types.agents.message_retrieve_response import MessageRetrieveResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        agent_id: str,
        *,
        assistant_message_function_kwarg: str | NotGiven = NOT_GIVEN,
        assistant_message_function_name: str | NotGiven = NOT_GIVEN,
        before: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        msg_object: bool | NotGiven = NOT_GIVEN,
        use_assistant_message: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageRetrieveResponse:
        """
        Retrieve message history for an agent.

        Args:
          assistant_message_function_kwarg: [Only applicable if use_assistant_message is True] The name of the message
              argument in the designated message tool.

          assistant_message_function_name: [Only applicable if use_assistant_message is True] The name of the designated
              message tool.

          before: Message before which to retrieve the returned messages.

          limit: Maximum number of messages to retrieve.

          msg_object: If true, returns Message objects. If false, return LettaMessage objects.

          use_assistant_message: [Only applicable if msg_object is False] If true, returns AssistantMessage
              objects when the agent calls a designated message tool. If false, return
              FunctionCallMessage objects for all tool calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return cast(
            MessageRetrieveResponse,
            self._get(
                f"/v1/agents/{agent_id}/messages",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "assistant_message_function_kwarg": assistant_message_function_kwarg,
                            "assistant_message_function_name": assistant_message_function_name,
                            "before": before,
                            "limit": limit,
                            "msg_object": msg_object,
                            "use_assistant_message": use_assistant_message,
                        },
                        message_retrieve_params.MessageRetrieveParams,
                    ),
                ),
                cast_to=cast(
                    Any, MessageRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        id: str,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        role: Optional[Literal["assistant", "user", "tool", "function", "system"]] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        tool_call_id: Optional[str] | NotGiven = NOT_GIVEN,
        tool_calls: Optional[Iterable[message_update_params.ToolCall]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Messageoutput:
        """
        Update the details of a message associated with an agent.

        Args:
          id: The id of the message.

          name: The name of the participant.

          role: The role of the participant.

          text: The text of the message.

          tool_call_id: The id of the tool call.

          tool_calls: The list of tool calls requested.

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
                    "id": id,
                    "name": name,
                    "role": role,
                    "text": text,
                    "tool_call_id": tool_call_id,
                    "tool_calls": tool_calls,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Messageoutput,
        )

    def process(
        self,
        agent_id: str,
        *,
        messages: Union[
            Iterable[message_process_params.MessagesUnionMember0], Iterable[message_process_params.MessagesUnionMember1]
        ],
        assistant_message_function_kwarg: str | NotGiven = NOT_GIVEN,
        assistant_message_function_name: str | NotGiven = NOT_GIVEN,
        return_message_object: bool | NotGiven = NOT_GIVEN,
        run_async: bool | NotGiven = NOT_GIVEN,
        stream_steps: bool | NotGiven = NOT_GIVEN,
        stream_tokens: bool | NotGiven = NOT_GIVEN,
        use_assistant_message: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent. It can optionally stream
        the response if 'stream_steps' or 'stream_tokens' is set to True.

        Args:
          messages: The messages to be sent to the agent.

          assistant_message_function_kwarg: [Only applicable if use_assistant_message is True] The name of the message
              argument in the designated message tool.

          assistant_message_function_name: [Only applicable if use_assistant_message is True] The name of the designated
              message tool.

          return_message_object: Set True to return the raw Message object. Set False to return the Message in
              the format of the Letta API.

          run_async: Whether to asynchronously send the messages to the agent.

          stream_steps: Flag to determine if the response should be streamed. Set to True for streaming
              agent steps.

          stream_tokens: Flag to determine if individual tokens should be streamed. Set to True for token
              streaming (requires stream_steps = True).

          use_assistant_message: [Only applicable if return_message_object is False] If true, returns
              AssistantMessage objects when the agent calls a designated message tool. If
              false, return FunctionCallMessage objects for all tool calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._post(
            f"/v1/agents/{agent_id}/messages",
            body=maybe_transform(
                {
                    "messages": messages,
                    "assistant_message_function_kwarg": assistant_message_function_kwarg,
                    "assistant_message_function_name": assistant_message_function_name,
                    "return_message_object": return_message_object,
                    "run_async": run_async,
                    "stream_steps": stream_steps,
                    "stream_tokens": stream_tokens,
                    "use_assistant_message": use_assistant_message,
                },
                message_process_params.MessageProcessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        agent_id: str,
        *,
        assistant_message_function_kwarg: str | NotGiven = NOT_GIVEN,
        assistant_message_function_name: str | NotGiven = NOT_GIVEN,
        before: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        msg_object: bool | NotGiven = NOT_GIVEN,
        use_assistant_message: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageRetrieveResponse:
        """
        Retrieve message history for an agent.

        Args:
          assistant_message_function_kwarg: [Only applicable if use_assistant_message is True] The name of the message
              argument in the designated message tool.

          assistant_message_function_name: [Only applicable if use_assistant_message is True] The name of the designated
              message tool.

          before: Message before which to retrieve the returned messages.

          limit: Maximum number of messages to retrieve.

          msg_object: If true, returns Message objects. If false, return LettaMessage objects.

          use_assistant_message: [Only applicable if msg_object is False] If true, returns AssistantMessage
              objects when the agent calls a designated message tool. If false, return
              FunctionCallMessage objects for all tool calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return cast(
            MessageRetrieveResponse,
            await self._get(
                f"/v1/agents/{agent_id}/messages",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "assistant_message_function_kwarg": assistant_message_function_kwarg,
                            "assistant_message_function_name": assistant_message_function_name,
                            "before": before,
                            "limit": limit,
                            "msg_object": msg_object,
                            "use_assistant_message": use_assistant_message,
                        },
                        message_retrieve_params.MessageRetrieveParams,
                    ),
                ),
                cast_to=cast(
                    Any, MessageRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        message_id: str,
        *,
        agent_id: str,
        id: str,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        role: Optional[Literal["assistant", "user", "tool", "function", "system"]] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        tool_call_id: Optional[str] | NotGiven = NOT_GIVEN,
        tool_calls: Optional[Iterable[message_update_params.ToolCall]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Messageoutput:
        """
        Update the details of a message associated with an agent.

        Args:
          id: The id of the message.

          name: The name of the participant.

          role: The role of the participant.

          text: The text of the message.

          tool_call_id: The id of the tool call.

          tool_calls: The list of tool calls requested.

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
                    "id": id,
                    "name": name,
                    "role": role,
                    "text": text,
                    "tool_call_id": tool_call_id,
                    "tool_calls": tool_calls,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Messageoutput,
        )

    async def process(
        self,
        agent_id: str,
        *,
        messages: Union[
            Iterable[message_process_params.MessagesUnionMember0], Iterable[message_process_params.MessagesUnionMember1]
        ],
        assistant_message_function_kwarg: str | NotGiven = NOT_GIVEN,
        assistant_message_function_name: str | NotGiven = NOT_GIVEN,
        return_message_object: bool | NotGiven = NOT_GIVEN,
        run_async: bool | NotGiven = NOT_GIVEN,
        stream_steps: bool | NotGiven = NOT_GIVEN,
        stream_tokens: bool | NotGiven = NOT_GIVEN,
        use_assistant_message: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Process a user message and return the agent's response.

        This endpoint accepts a
        message from a user and processes it through the agent. It can optionally stream
        the response if 'stream_steps' or 'stream_tokens' is set to True.

        Args:
          messages: The messages to be sent to the agent.

          assistant_message_function_kwarg: [Only applicable if use_assistant_message is True] The name of the message
              argument in the designated message tool.

          assistant_message_function_name: [Only applicable if use_assistant_message is True] The name of the designated
              message tool.

          return_message_object: Set True to return the raw Message object. Set False to return the Message in
              the format of the Letta API.

          run_async: Whether to asynchronously send the messages to the agent.

          stream_steps: Flag to determine if the response should be streamed. Set to True for streaming
              agent steps.

          stream_tokens: Flag to determine if individual tokens should be streamed. Set to True for token
              streaming (requires stream_steps = True).

          use_assistant_message: [Only applicable if return_message_object is False] If true, returns
              AssistantMessage objects when the agent calls a designated message tool. If
              false, return FunctionCallMessage objects for all tool calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._post(
            f"/v1/agents/{agent_id}/messages",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "assistant_message_function_kwarg": assistant_message_function_kwarg,
                    "assistant_message_function_name": assistant_message_function_name,
                    "return_message_object": return_message_object,
                    "run_async": run_async,
                    "stream_steps": stream_steps,
                    "stream_tokens": stream_tokens,
                    "use_assistant_message": use_assistant_message,
                },
                message_process_params.MessageProcessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.process = to_raw_response_wrapper(
            messages.process,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.process = async_to_raw_response_wrapper(
            messages.process,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.process = to_streamed_response_wrapper(
            messages.process,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.process = async_to_streamed_response_wrapper(
            messages.process,
        )
