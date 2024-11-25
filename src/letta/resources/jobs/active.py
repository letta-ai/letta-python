# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.jobs.active_list_response import ActiveListResponse

__all__ = ["ActiveResource", "AsyncActiveResource"]


class ActiveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return ActiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return ActiveResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActiveListResponse:
        """
        List all active jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._get(
            "/v1/jobs/active",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveListResponse,
        )


class AsyncActiveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncActiveResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActiveListResponse:
        """
        List all active jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/jobs/active",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveListResponse,
        )


class ActiveResourceWithRawResponse:
    def __init__(self, active: ActiveResource) -> None:
        self._active = active

        self.list = to_raw_response_wrapper(
            active.list,
        )


class AsyncActiveResourceWithRawResponse:
    def __init__(self, active: AsyncActiveResource) -> None:
        self._active = active

        self.list = async_to_raw_response_wrapper(
            active.list,
        )


class ActiveResourceWithStreamingResponse:
    def __init__(self, active: ActiveResource) -> None:
        self._active = active

        self.list = to_streamed_response_wrapper(
            active.list,
        )


class AsyncActiveResourceWithStreamingResponse:
    def __init__(self, active: AsyncActiveResource) -> None:
        self._active = active

        self.list = async_to_streamed_response_wrapper(
            active.list,
        )
