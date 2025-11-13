# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, overload

import httpx

from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...types import mcp_server_create_params, mcp_server_update_params, mcp_server_refresh_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.mcp_server_list_response import McpServerListResponse
from ...types.mcp_server_create_response import McpServerCreateResponse
from ...types.mcp_server_update_response import McpServerUpdateResponse
from ...types.mcp_server_retrieve_response import McpServerRetrieveResponse

__all__ = ["McpServersResource", "AsyncMcpServersResource"]


class McpServersResource(SyncAPIResource):
    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> McpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return McpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return McpServersResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        args: SequenceNotStr[str],
        command: str,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: Literal["sse", "stdio", "streamable_http"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          args: The arguments to pass to the command

          command: The command to run (MCP 'local' client will run this command)

          server_name: The name of the server

          env: Environment variables to set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: Literal["sse", "stdio", "streamable_http"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          server_name: The name of the server

          server_url: The URL of the server

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: Literal["sse", "stdio", "streamable_http"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          server_name: The name of the server

          server_url: The URL of the server

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["args", "command", "server_name"], ["server_name", "server_url"])
    def create(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: Literal["sse", "stdio", "streamable_http"] | Omit = omit,
        server_url: str | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        return cast(
            McpServerCreateResponse,
            self._post(
                "/v1/mcp-servers/",
                body=maybe_transform(
                    {
                        "args": args,
                        "command": command,
                        "server_name": server_name,
                        "env": env,
                        "type": type,
                        "server_url": server_url,
                        "auth_header": auth_header,
                        "auth_token": auth_token,
                        "custom_headers": custom_headers,
                    },
                    mcp_server_create_params.McpServerCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, McpServerCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        mcp_server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerRetrieveResponse:
        """
        Get a specific MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return cast(
            McpServerRetrieveResponse,
            self._get(
                f"/v1/mcp-servers/{mcp_server_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, McpServerRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        mcp_server_id: str,
        *,
        args: Optional[SequenceNotStr[str]] | Omit = omit,
        command: Optional[str] | Omit = omit,
        env: Optional[Dict[str, str]] | Omit = omit,
        server_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          args: The arguments to pass to the command

          command: The command to run the MCP server

          env: Environment variables to set

          server_name: The name of the MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        mcp_server_id: str,
        *,
        token: Optional[str] | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_name: Optional[str] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          token: The authentication token (internal)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom headers to send with requests

          server_name: The name of the MCP server

          server_url: The URL of the SSE MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        mcp_server_id: str,
        *,
        token: Optional[str] | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_name: Optional[str] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          token: The authentication token (internal)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom headers to send with requests

          server_name: The name of the MCP server

          server_url: The URL of the Streamable HTTP MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        mcp_server_id: str,
        *,
        args: Optional[SequenceNotStr[str]] | Omit = omit,
        command: Optional[str] | Omit = omit,
        env: Optional[Dict[str, str]] | Omit = omit,
        server_name: Optional[str] | Omit = omit,
        token: Optional[str] | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return cast(
            McpServerUpdateResponse,
            self._patch(
                f"/v1/mcp-servers/{mcp_server_id}",
                body=maybe_transform(
                    {
                        "args": args,
                        "command": command,
                        "env": env,
                        "server_name": server_name,
                        "token": token,
                        "auth_header": auth_header,
                        "auth_token": auth_token,
                        "custom_headers": custom_headers,
                        "server_url": server_url,
                    },
                    mcp_server_update_params.McpServerUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, McpServerUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerListResponse:
        """Get a list of all configured MCP servers"""
        return self._get(
            "/v1/mcp-servers/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerListResponse,
        )

    def delete(
        self,
        mcp_server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an MCP server by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/mcp-servers/{mcp_server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def refresh(
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
                query=maybe_transform({"agent_id": agent_id}, mcp_server_refresh_params.McpServerRefreshParams),
            ),
            cast_to=object,
        )


class AsyncMcpServersResource(AsyncAPIResource):
    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMcpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncMcpServersResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        args: SequenceNotStr[str],
        command: str,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: Literal["sse", "stdio", "streamable_http"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          args: The arguments to pass to the command

          command: The command to run (MCP 'local' client will run this command)

          server_name: The name of the server

          env: Environment variables to set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: Literal["sse", "stdio", "streamable_http"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          server_name: The name of the server

          server_url: The URL of the server

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: Literal["sse", "stdio", "streamable_http"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          server_name: The name of the server

          server_url: The URL of the server

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["args", "command", "server_name"], ["server_name", "server_url"])
    async def create(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: Literal["sse", "stdio", "streamable_http"] | Omit = omit,
        server_url: str | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        return cast(
            McpServerCreateResponse,
            await self._post(
                "/v1/mcp-servers/",
                body=await async_maybe_transform(
                    {
                        "args": args,
                        "command": command,
                        "server_name": server_name,
                        "env": env,
                        "type": type,
                        "server_url": server_url,
                        "auth_header": auth_header,
                        "auth_token": auth_token,
                        "custom_headers": custom_headers,
                    },
                    mcp_server_create_params.McpServerCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, McpServerCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        mcp_server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerRetrieveResponse:
        """
        Get a specific MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return cast(
            McpServerRetrieveResponse,
            await self._get(
                f"/v1/mcp-servers/{mcp_server_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, McpServerRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        mcp_server_id: str,
        *,
        args: Optional[SequenceNotStr[str]] | Omit = omit,
        command: Optional[str] | Omit = omit,
        env: Optional[Dict[str, str]] | Omit = omit,
        server_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          args: The arguments to pass to the command

          command: The command to run the MCP server

          env: Environment variables to set

          server_name: The name of the MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        mcp_server_id: str,
        *,
        token: Optional[str] | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_name: Optional[str] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          token: The authentication token (internal)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom headers to send with requests

          server_name: The name of the MCP server

          server_url: The URL of the SSE MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        mcp_server_id: str,
        *,
        token: Optional[str] | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_name: Optional[str] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          token: The authentication token (internal)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom headers to send with requests

          server_name: The name of the MCP server

          server_url: The URL of the Streamable HTTP MCP server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        mcp_server_id: str,
        *,
        args: Optional[SequenceNotStr[str]] | Omit = omit,
        command: Optional[str] | Omit = omit,
        env: Optional[Dict[str, str]] | Omit = omit,
        server_name: Optional[str] | Omit = omit,
        token: Optional[str] | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return cast(
            McpServerUpdateResponse,
            await self._patch(
                f"/v1/mcp-servers/{mcp_server_id}",
                body=await async_maybe_transform(
                    {
                        "args": args,
                        "command": command,
                        "env": env,
                        "server_name": server_name,
                        "token": token,
                        "auth_header": auth_header,
                        "auth_token": auth_token,
                        "custom_headers": custom_headers,
                        "server_url": server_url,
                    },
                    mcp_server_update_params.McpServerUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, McpServerUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerListResponse:
        """Get a list of all configured MCP servers"""
        return await self._get(
            "/v1/mcp-servers/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerListResponse,
        )

    async def delete(
        self,
        mcp_server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an MCP server by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/mcp-servers/{mcp_server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def refresh(
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
                query=await async_maybe_transform(
                    {"agent_id": agent_id}, mcp_server_refresh_params.McpServerRefreshParams
                ),
            ),
            cast_to=object,
        )


class McpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = to_raw_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mcp_servers.update,
        )
        self.list = to_raw_response_wrapper(
            mcp_servers.list,
        )
        self.delete = to_raw_response_wrapper(
            mcp_servers.delete,
        )
        self.refresh = to_raw_response_wrapper(
            mcp_servers.refresh,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._mcp_servers.tools)


class AsyncMcpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = async_to_raw_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mcp_servers.update,
        )
        self.list = async_to_raw_response_wrapper(
            mcp_servers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mcp_servers.delete,
        )
        self.refresh = async_to_raw_response_wrapper(
            mcp_servers.refresh,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._mcp_servers.tools)


class McpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = to_streamed_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mcp_servers.update,
        )
        self.list = to_streamed_response_wrapper(
            mcp_servers.list,
        )
        self.delete = to_streamed_response_wrapper(
            mcp_servers.delete,
        )
        self.refresh = to_streamed_response_wrapper(
            mcp_servers.refresh,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._mcp_servers.tools)


class AsyncMcpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = async_to_streamed_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mcp_servers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mcp_servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mcp_servers.delete,
        )
        self.refresh = async_to_streamed_response_wrapper(
            mcp_servers.refresh,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._mcp_servers.tools)
