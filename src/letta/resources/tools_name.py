# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ToolsNameResource", "AsyncToolsNameResource"]


class ToolsNameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return ToolsNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return ToolsNameResourceWithStreamingResponse(self)

    def retrieve(
        self,
        tool_name: str,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get a tool ID by name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_name:
            raise ValueError(f"Expected a non-empty value for `tool_name` but received {tool_name!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._get(
            f"/v1/tools/name/{tool_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncToolsNameResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncToolsNameResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        tool_name: str,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get a tool ID by name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_name:
            raise ValueError(f"Expected a non-empty value for `tool_name` but received {tool_name!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._get(
            f"/v1/tools/name/{tool_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ToolsNameResourceWithRawResponse:
    def __init__(self, tools_name: ToolsNameResource) -> None:
        self._tools_name = tools_name

        self.retrieve = to_raw_response_wrapper(
            tools_name.retrieve,
        )


class AsyncToolsNameResourceWithRawResponse:
    def __init__(self, tools_name: AsyncToolsNameResource) -> None:
        self._tools_name = tools_name

        self.retrieve = async_to_raw_response_wrapper(
            tools_name.retrieve,
        )


class ToolsNameResourceWithStreamingResponse:
    def __init__(self, tools_name: ToolsNameResource) -> None:
        self._tools_name = tools_name

        self.retrieve = to_streamed_response_wrapper(
            tools_name.retrieve,
        )


class AsyncToolsNameResourceWithStreamingResponse:
    def __init__(self, tools_name: AsyncToolsNameResource) -> None:
        self._tools_name = tools_name

        self.retrieve = async_to_streamed_response_wrapper(
            tools_name.retrieve,
        )
