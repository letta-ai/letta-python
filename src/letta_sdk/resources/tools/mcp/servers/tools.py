# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.tools.mcp.servers import tool_execute_params
from .....types.tools.mcp.servers.tool_list_response import ToolListResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def list(
        self,
        mcp_server_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        Get a list of all tools for a specific MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        return self._get(
            f"/v1/tools/mcp/servers/{mcp_server_name}/tools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolListResponse,
        )

    def execute(
        self,
        tool_name: str,
        *,
        mcp_server_name: str,
        args: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Execute a specific MCP tool from a configured server.

        Returns the tool execution
        result.

        Args:
          args: Arguments to pass to the MCP tool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        if not tool_name:
            raise ValueError(f"Expected a non-empty value for `tool_name` but received {tool_name!r}")
        return self._post(
            f"/v1/tools/mcp/servers/{mcp_server_name}/tools/{tool_name}/execute",
            body=maybe_transform({"args": args}, tool_execute_params.ToolExecuteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def list(
        self,
        mcp_server_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        Get a list of all tools for a specific MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        return await self._get(
            f"/v1/tools/mcp/servers/{mcp_server_name}/tools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolListResponse,
        )

    async def execute(
        self,
        tool_name: str,
        *,
        mcp_server_name: str,
        args: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Execute a specific MCP tool from a configured server.

        Returns the tool execution
        result.

        Args:
          args: Arguments to pass to the MCP tool

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        if not tool_name:
            raise ValueError(f"Expected a non-empty value for `tool_name` but received {tool_name!r}")
        return await self._post(
            f"/v1/tools/mcp/servers/{mcp_server_name}/tools/{tool_name}/execute",
            body=await async_maybe_transform({"args": args}, tool_execute_params.ToolExecuteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.execute = to_raw_response_wrapper(
            tools.execute,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.execute = async_to_raw_response_wrapper(
            tools.execute,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.execute = to_streamed_response_wrapper(
            tools.execute,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.execute = async_to_streamed_response_wrapper(
            tools.execute,
        )
