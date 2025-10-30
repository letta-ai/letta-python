# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ..._base_client import make_request_options
from ...types.mcp_servers import refresh_trigger_params

__all__ = ["RefreshResource", "AsyncRefreshResource"]


class RefreshResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefreshResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return RefreshResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefreshResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return RefreshResourceWithStreamingResponse(self)

    def trigger(
        self,
        mcp_server_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Refresh tools for an MCP server by:

        1.

        Fetching current tools from the MCP server
        2. Deleting tools that no longer exist on the server
        3. Updating schemas for existing tools
        4. Adding new tools from the server

        Returns a summary of changes made.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return self._patch(
            f"/v1/mcp-servers/{mcp_server_id}/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, refresh_trigger_params.RefreshTriggerParams),
            ),
            cast_to=object,
        )


class AsyncRefreshResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefreshResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRefreshResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefreshResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncRefreshResourceWithStreamingResponse(self)

    async def trigger(
        self,
        mcp_server_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Refresh tools for an MCP server by:

        1.

        Fetching current tools from the MCP server
        2. Deleting tools that no longer exist on the server
        3. Updating schemas for existing tools
        4. Adding new tools from the server

        Returns a summary of changes made.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return await self._patch(
            f"/v1/mcp-servers/{mcp_server_id}/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"agent_id": agent_id}, refresh_trigger_params.RefreshTriggerParams),
            ),
            cast_to=object,
        )


class RefreshResourceWithRawResponse:
    def __init__(self, refresh: RefreshResource) -> None:
        self._refresh = refresh

        self.trigger = to_raw_response_wrapper(
            refresh.trigger,
        )


class AsyncRefreshResourceWithRawResponse:
    def __init__(self, refresh: AsyncRefreshResource) -> None:
        self._refresh = refresh

        self.trigger = async_to_raw_response_wrapper(
            refresh.trigger,
        )


class RefreshResourceWithStreamingResponse:
    def __init__(self, refresh: RefreshResource) -> None:
        self._refresh = refresh

        self.trigger = to_streamed_response_wrapper(
            refresh.trigger,
        )


class AsyncRefreshResourceWithStreamingResponse:
    def __init__(self, refresh: AsyncRefreshResource) -> None:
        self._refresh = refresh

        self.trigger = async_to_streamed_response_wrapper(
            refresh.trigger,
        )
