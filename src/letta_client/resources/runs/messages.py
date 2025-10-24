# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
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
from ...pagination import SyncArrayPage, AsyncArrayPage
from ...types.runs import message_list_params, message_stream_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.agents.letta_message_union import LettaMessageUnion

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
        run_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncArrayPage[LettaMessageUnion]:
        """
        Get response messages associated with a run.

        Args:
          after: Message ID cursor for pagination. Returns messages that come after this message
              ID in the specified sort order

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          limit: Maximum number of messages to return

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get_api_list(
            f"/v1/runs/{run_id}/messages",
            page=SyncArrayPage[LettaMessageUnion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=cast(Any, LettaMessageUnion),  # Union types cannot be passed in as arguments in the type system
        )

    def stream(
        self,
        run_id: str,
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
    ) -> object:
        """
        Retrieve Stream

        Args:
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
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            f"/v1/runs/{run_id}/stream",
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
        run_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LettaMessageUnion, AsyncArrayPage[LettaMessageUnion]]:
        """
        Get response messages associated with a run.

        Args:
          after: Message ID cursor for pagination. Returns messages that come after this message
              ID in the specified sort order

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          limit: Maximum number of messages to return

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get_api_list(
            f"/v1/runs/{run_id}/messages",
            page=AsyncArrayPage[LettaMessageUnion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=cast(Any, LettaMessageUnion),  # Union types cannot be passed in as arguments in the type system
        )

    async def stream(
        self,
        run_id: str,
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
    ) -> object:
        """
        Retrieve Stream

        Args:
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
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            f"/v1/runs/{run_id}/stream",
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
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
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
        self.stream = async_to_raw_response_wrapper(
            messages.stream,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
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
        self.stream = async_to_streamed_response_wrapper(
            messages.stream,
        )
