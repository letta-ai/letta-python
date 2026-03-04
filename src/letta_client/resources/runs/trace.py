# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.runs import trace_retrieve_params
from ..._base_client import make_request_options
from ...types.runs.trace_retrieve_response import TraceRetrieveResponse

__all__ = ["TraceResource", "AsyncTraceResource"]


class TraceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TraceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return TraceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TraceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return TraceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        run_id: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TraceRetrieveResponse:
        """
        Retrieve OTEL trace spans for a run.

        Returns a filtered set of spans relevant for observability:

        - agent_step: Individual agent reasoning steps
        - tool executions: Tool call spans
        - Root span: The top-level request span
        - time_to_first_token: TTFT measurement span

        Requires ClickHouse to be configured for trace storage.

        Args:
          limit: Maximum number of spans to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/v1/runs/{run_id}/trace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, trace_retrieve_params.TraceRetrieveParams),
            ),
            cast_to=TraceRetrieveResponse,
        )


class AsyncTraceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTraceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTraceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTraceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncTraceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        run_id: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TraceRetrieveResponse:
        """
        Retrieve OTEL trace spans for a run.

        Returns a filtered set of spans relevant for observability:

        - agent_step: Individual agent reasoning steps
        - tool executions: Tool call spans
        - Root span: The top-level request span
        - time_to_first_token: TTFT measurement span

        Requires ClickHouse to be configured for trace storage.

        Args:
          limit: Maximum number of spans to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/v1/runs/{run_id}/trace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, trace_retrieve_params.TraceRetrieveParams),
            ),
            cast_to=TraceRetrieveResponse,
        )


class TraceResourceWithRawResponse:
    def __init__(self, trace: TraceResource) -> None:
        self._trace = trace

        self.retrieve = to_raw_response_wrapper(
            trace.retrieve,
        )


class AsyncTraceResourceWithRawResponse:
    def __init__(self, trace: AsyncTraceResource) -> None:
        self._trace = trace

        self.retrieve = async_to_raw_response_wrapper(
            trace.retrieve,
        )


class TraceResourceWithStreamingResponse:
    def __init__(self, trace: TraceResource) -> None:
        self._trace = trace

        self.retrieve = to_streamed_response_wrapper(
            trace.retrieve,
        )


class AsyncTraceResourceWithStreamingResponse:
    def __init__(self, trace: AsyncTraceResource) -> None:
        self._trace = trace

        self.retrieve = async_to_streamed_response_wrapper(
            trace.retrieve,
        )
