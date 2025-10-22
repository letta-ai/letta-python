# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .apps import (
    AppsResource,
    AsyncAppsResource,
    AppsResourceWithRawResponse,
    AsyncAppsResourceWithRawResponse,
    AppsResourceWithStreamingResponse,
    AsyncAppsResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.tool import Tool
from ...._base_client import make_request_options

__all__ = ["ComposioResource", "AsyncComposioResource"]


class ComposioResource(SyncAPIResource):
    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ComposioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ComposioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComposioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ComposioResourceWithStreamingResponse(self)

    def add(
        self,
        composio_action_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Add a new Composio tool by action name (Composio refers to each tool as an
        `Action`)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not composio_action_name:
            raise ValueError(
                f"Expected a non-empty value for `composio_action_name` but received {composio_action_name!r}"
            )
        return self._post(
            f"/v1/tools/composio/{composio_action_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )


class AsyncComposioResource(AsyncAPIResource):
    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncComposioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComposioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComposioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncComposioResourceWithStreamingResponse(self)

    async def add(
        self,
        composio_action_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Add a new Composio tool by action name (Composio refers to each tool as an
        `Action`)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not composio_action_name:
            raise ValueError(
                f"Expected a non-empty value for `composio_action_name` but received {composio_action_name!r}"
            )
        return await self._post(
            f"/v1/tools/composio/{composio_action_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )


class ComposioResourceWithRawResponse:
    def __init__(self, composio: ComposioResource) -> None:
        self._composio = composio

        self.add = to_raw_response_wrapper(
            composio.add,
        )

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._composio.apps)


class AsyncComposioResourceWithRawResponse:
    def __init__(self, composio: AsyncComposioResource) -> None:
        self._composio = composio

        self.add = async_to_raw_response_wrapper(
            composio.add,
        )

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._composio.apps)


class ComposioResourceWithStreamingResponse:
    def __init__(self, composio: ComposioResource) -> None:
        self._composio = composio

        self.add = to_streamed_response_wrapper(
            composio.add,
        )

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._composio.apps)


class AsyncComposioResourceWithStreamingResponse:
    def __init__(self, composio: AsyncComposioResource) -> None:
        self._composio = composio

        self.add = async_to_streamed_response_wrapper(
            composio.add,
        )

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._composio.apps)
