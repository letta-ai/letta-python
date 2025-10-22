# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.provider_trace import ProviderTrace

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
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ProviderTrace]:
        """
        Retrieve Trace For Step

        Args:
          step_id: The ID of the step in the format 'step-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._get(
            f"/v1/steps/{step_id}/trace",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderTrace,
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
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ProviderTrace]:
        """
        Retrieve Trace For Step

        Args:
          step_id: The ID of the step in the format 'step-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._get(
            f"/v1/steps/{step_id}/trace",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderTrace,
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
