# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sources.passage_list_response import PassageListResponse

__all__ = ["PassagesResource", "AsyncPassagesResource"]


class PassagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PassagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return PassagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PassagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return PassagesResourceWithStreamingResponse(self)

    def list(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PassageListResponse:
        """
        List all passages associated with a data source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            f"/v1/sources/{source_id}/passages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PassageListResponse,
        )


class AsyncPassagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPassagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPassagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPassagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncPassagesResourceWithStreamingResponse(self)

    async def list(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PassageListResponse:
        """
        List all passages associated with a data source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            f"/v1/sources/{source_id}/passages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PassageListResponse,
        )


class PassagesResourceWithRawResponse:
    def __init__(self, passages: PassagesResource) -> None:
        self._passages = passages

        self.list = to_raw_response_wrapper(
            passages.list,
        )


class AsyncPassagesResourceWithRawResponse:
    def __init__(self, passages: AsyncPassagesResource) -> None:
        self._passages = passages

        self.list = async_to_raw_response_wrapper(
            passages.list,
        )


class PassagesResourceWithStreamingResponse:
    def __init__(self, passages: PassagesResource) -> None:
        self._passages = passages

        self.list = to_streamed_response_wrapper(
            passages.list,
        )


class AsyncPassagesResourceWithStreamingResponse:
    def __init__(self, passages: AsyncPassagesResource) -> None:
        self._passages = passages

        self.list = async_to_streamed_response_wrapper(
            passages.list,
        )
