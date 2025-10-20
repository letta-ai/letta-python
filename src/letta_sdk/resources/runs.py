# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    StopReasonType,
    run_list_params,
    run_list_steps_params,
    run_list_active_params,
    run_list_messages_params,
    run_retrieve_stream_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.agents.run import Run
from ..types.stop_reason_type import StopReasonType
from ..types.run_list_response import RunListResponse
from ..types.run_list_steps_response import RunListStepsResponse
from ..types.run_list_active_response import RunListActiveResponse
from ..types.run_list_messages_response import RunListMessagesResponse
from ..types.run_retrieve_usage_response import RunRetrieveUsageResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """
        Get the status of a run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/v1/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    def list(
        self,
        *,
        active: bool | Omit = omit,
        after: Optional[str] | Omit = omit,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ascending: bool | Omit = omit,
        background: Optional[bool] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        stop_reason: Optional[StopReasonType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """
        List all runs.

        Args:
          active: Filter for active runs.

          after: Cursor for pagination

          agent_ids: The unique identifier of the agent associated with the run.

          ascending: Whether to sort agents oldest to newest (True) or newest to oldest (False,
              default)

          background: If True, filters for runs that were created in background mode.

          before: Cursor for pagination

          limit: Maximum number of runs to return

          stop_reason: Filter runs by stop reason.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/runs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "after": after,
                        "agent_ids": agent_ids,
                        "ascending": ascending,
                        "background": background,
                        "before": before,
                        "limit": limit,
                        "stop_reason": stop_reason,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    def delete(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """
        Delete a run by its run_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._delete(
            f"/v1/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    @typing_extensions.deprecated("deprecated")
    def list_active(
        self,
        *,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        background: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListActiveResponse:
        """
        List all active runs.

        Args:
          agent_ids: The unique identifier of the agent associated with the run.

          background: If True, filters for runs that were created in background mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/runs/active",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_ids": agent_ids,
                        "background": background,
                    },
                    run_list_active_params.RunListActiveParams,
                ),
            ),
            cast_to=RunListActiveResponse,
        )

    def list_messages(
        self,
        run_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListMessagesResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/v1/runs/{run_id}/messages",
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
                    },
                    run_list_messages_params.RunListMessagesParams,
                ),
            ),
            cast_to=RunListMessagesResponse,
        )

    def list_steps(
        self,
        run_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListStepsResponse:
        """
        Get messages associated with a run with filtering options.

        Args: run_id: ID of the run before: A cursor for use in pagination. `before` is
        an object ID that defines your place in the list. For instance, if you make a
        list request and receive 100 objects, starting with obj_foo, your subsequent
        call can include before=obj_foo in order to fetch the previous page of the list.
        after: A cursor for use in pagination. `after` is an object ID that defines your
        place in the list. For instance, if you make a list request and receive 100
        objects, ending with obj_foo, your subsequent call can include after=obj_foo in
        order to fetch the next page of the list. limit: Maximum number of steps to
        return order: Sort order by the created_at timestamp of the objects. asc for
        ascending order and desc for descending order.

        Returns: A list of steps associated with the run.

        Args:
          after: Cursor for pagination

          before: Cursor for pagination

          limit: Maximum number of messages to return

          order: Sort order by the created_at timestamp of the objects. asc for ascending order
              and desc for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/v1/runs/{run_id}/steps",
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
                    },
                    run_list_steps_params.RunListStepsParams,
                ),
            ),
            cast_to=RunListStepsResponse,
        )

    def retrieve_stream(
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
                run_retrieve_stream_params.RunRetrieveStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_usage(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveUsageResponse:
        """
        Get usage statistics for a run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/v1/runs/{run_id}/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunRetrieveUsageResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """
        Get the status of a run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/v1/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    async def list(
        self,
        *,
        active: bool | Omit = omit,
        after: Optional[str] | Omit = omit,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ascending: bool | Omit = omit,
        background: Optional[bool] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        stop_reason: Optional[StopReasonType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """
        List all runs.

        Args:
          active: Filter for active runs.

          after: Cursor for pagination

          agent_ids: The unique identifier of the agent associated with the run.

          ascending: Whether to sort agents oldest to newest (True) or newest to oldest (False,
              default)

          background: If True, filters for runs that were created in background mode.

          before: Cursor for pagination

          limit: Maximum number of runs to return

          stop_reason: Filter runs by stop reason.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/runs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "after": after,
                        "agent_ids": agent_ids,
                        "ascending": ascending,
                        "background": background,
                        "before": before,
                        "limit": limit,
                        "stop_reason": stop_reason,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    async def delete(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """
        Delete a run by its run_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._delete(
            f"/v1/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Run,
        )

    @typing_extensions.deprecated("deprecated")
    async def list_active(
        self,
        *,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        background: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListActiveResponse:
        """
        List all active runs.

        Args:
          agent_ids: The unique identifier of the agent associated with the run.

          background: If True, filters for runs that were created in background mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/runs/active",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_ids": agent_ids,
                        "background": background,
                    },
                    run_list_active_params.RunListActiveParams,
                ),
            ),
            cast_to=RunListActiveResponse,
        )

    async def list_messages(
        self,
        run_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListMessagesResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/v1/runs/{run_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    run_list_messages_params.RunListMessagesParams,
                ),
            ),
            cast_to=RunListMessagesResponse,
        )

    async def list_steps(
        self,
        run_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListStepsResponse:
        """
        Get messages associated with a run with filtering options.

        Args: run_id: ID of the run before: A cursor for use in pagination. `before` is
        an object ID that defines your place in the list. For instance, if you make a
        list request and receive 100 objects, starting with obj_foo, your subsequent
        call can include before=obj_foo in order to fetch the previous page of the list.
        after: A cursor for use in pagination. `after` is an object ID that defines your
        place in the list. For instance, if you make a list request and receive 100
        objects, ending with obj_foo, your subsequent call can include after=obj_foo in
        order to fetch the next page of the list. limit: Maximum number of steps to
        return order: Sort order by the created_at timestamp of the objects. asc for
        ascending order and desc for descending order.

        Returns: A list of steps associated with the run.

        Args:
          after: Cursor for pagination

          before: Cursor for pagination

          limit: Maximum number of messages to return

          order: Sort order by the created_at timestamp of the objects. asc for ascending order
              and desc for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/v1/runs/{run_id}/steps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    run_list_steps_params.RunListStepsParams,
                ),
            ),
            cast_to=RunListStepsResponse,
        )

    async def retrieve_stream(
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
                run_retrieve_stream_params.RunRetrieveStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_usage(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveUsageResponse:
        """
        Get usage statistics for a run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/v1/runs/{run_id}/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunRetrieveUsageResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.delete = to_raw_response_wrapper(
            runs.delete,
        )
        self.list_active = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.list_active,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_messages = to_raw_response_wrapper(
            runs.list_messages,
        )
        self.list_steps = to_raw_response_wrapper(
            runs.list_steps,
        )
        self.retrieve_stream = to_raw_response_wrapper(
            runs.retrieve_stream,
        )
        self.retrieve_usage = to_raw_response_wrapper(
            runs.retrieve_usage,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            runs.delete,
        )
        self.list_active = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.list_active,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_messages = async_to_raw_response_wrapper(
            runs.list_messages,
        )
        self.list_steps = async_to_raw_response_wrapper(
            runs.list_steps,
        )
        self.retrieve_stream = async_to_raw_response_wrapper(
            runs.retrieve_stream,
        )
        self.retrieve_usage = async_to_raw_response_wrapper(
            runs.retrieve_usage,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.delete = to_streamed_response_wrapper(
            runs.delete,
        )
        self.list_active = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.list_active,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_messages = to_streamed_response_wrapper(
            runs.list_messages,
        )
        self.list_steps = to_streamed_response_wrapper(
            runs.list_steps,
        )
        self.retrieve_stream = to_streamed_response_wrapper(
            runs.retrieve_stream,
        )
        self.retrieve_usage = to_streamed_response_wrapper(
            runs.retrieve_usage,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            runs.delete,
        )
        self.list_active = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.list_active,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_messages = async_to_streamed_response_wrapper(
            runs.list_messages,
        )
        self.list_steps = async_to_streamed_response_wrapper(
            runs.list_steps,
        )
        self.retrieve_stream = async_to_streamed_response_wrapper(
            runs.retrieve_stream,
        )
        self.retrieve_usage = async_to_streamed_response_wrapper(
            runs.retrieve_usage,
        )
