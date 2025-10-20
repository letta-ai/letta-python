# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Optional, cast
from typing_extensions import overload

import httpx

from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import required_args, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....types.tool import Tool
from ....._base_client import make_request_options
from .....types.tools.mcp import (
    McpServerType,
    server_add_params,
    server_test_params,
    server_resync_params,
    server_update_params,
    server_connect_params,
)
from .....types.tools.mcp.mcp_server_type import McpServerType
from .....types.tools.mcp.server_add_response import ServerAddResponse
from .....types.tools.mcp.server_list_response import ServerListResponse
from .....types.tools.mcp.server_delete_response import ServerDeleteResponse
from .....types.tools.mcp.server_update_response import ServerUpdateResponse
from .....types.tools.mcp.stdio_server_config_param import StdioServerConfigParam

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(SyncAPIResource):
    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return ServersResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        mcp_server_name: str,
        *,
        stdio_config: Optional[StdioServerConfigParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          stdio_config: The configuration for the server (MCP 'local' client will run this command)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        mcp_server_name: str,
        *,
        token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          token: The access token or API key for the MCP server (used for SSE authentication)

          custom_headers: Custom authentication headers as key-value pairs

          server_url: The URL of the server (MCP SSE client will connect to this URL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        mcp_server_name: str,
        *,
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
    ) -> ServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom authentication headers as key-value pairs

          server_url: The URL path for the streamable HTTP server (e.g., 'example/mcp')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        mcp_server_name: str,
        *,
        stdio_config: Optional[StdioServerConfigParam] | Omit = omit,
        token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateResponse:
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        return cast(
            ServerUpdateResponse,
            self._patch(
                f"/v1/tools/mcp/servers/{mcp_server_name}",
                body=maybe_transform(
                    {
                        "stdio_config": stdio_config,
                        "token": token,
                        "custom_headers": custom_headers,
                        "server_url": server_url,
                        "auth_header": auth_header,
                        "auth_token": auth_token,
                    },
                    server_update_params.ServerUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ServerUpdateResponse
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
    ) -> ServerListResponse:
        """Get a list of all configured MCP servers"""
        return self._get(
            "/v1/tools/mcp/servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerListResponse,
        )

    def delete(
        self,
        mcp_server_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerDeleteResponse:
        """
        Delete a MCP server configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        return self._delete(
            f"/v1/tools/mcp/servers/{mcp_server_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerDeleteResponse,
        )

    @overload
    def add(
        self,
        *,
        args: SequenceNotStr[str],
        command: str,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerAddResponse:
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
    def add(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerAddResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          server_name: The name of the server

          server_url: The URL of the server (MCP SSE client will connect to this URL)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with SSE requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def add(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerAddResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          server_name: The name of the server

          server_url: The URL path for the streamable HTTP server (e.g., 'example/mcp')

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with streamable HTTP requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["args", "command", "server_name"], ["server_name", "server_url"])
    def add(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
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
    ) -> ServerAddResponse:
        return self._put(
            "/v1/tools/mcp/servers",
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
                server_add_params.ServerAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerAddResponse,
        )

    @overload
    def connect(
        self,
        *,
        args: SequenceNotStr[str],
        command: str,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Connect to an MCP server with support for OAuth via SSE.

        Returns a stream of
        events handling authorization state and exchange if OAuth is required.

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
    def connect(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Connect to an MCP server with support for OAuth via SSE.

        Returns a stream of
        events handling authorization state and exchange if OAuth is required.

        Args:
          server_name: The name of the server

          server_url: The URL of the server (MCP SSE client will connect to this URL)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with SSE requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def connect(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Connect to an MCP server with support for OAuth via SSE.

        Returns a stream of
        events handling authorization state and exchange if OAuth is required.

        Args:
          server_name: The name of the server

          server_url: The URL path for the streamable HTTP server (e.g., 'example/mcp')

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with streamable HTTP requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["args", "command", "server_name"], ["server_name", "server_url"])
    def connect(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
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
    ) -> object:
        return self._post(
            "/v1/tools/mcp/servers/connect",
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
                server_connect_params.ServerConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def register_tool(
        self,
        mcp_tool_name: str,
        *,
        mcp_server_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Register a new MCP tool as a Letta server by MCP server + tool name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        if not mcp_tool_name:
            raise ValueError(f"Expected a non-empty value for `mcp_tool_name` but received {mcp_tool_name!r}")
        return self._post(
            f"/v1/tools/mcp/servers/{mcp_server_name}/{mcp_tool_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    def resync(
        self,
        mcp_server_name: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Resync tools for an MCP server by:

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
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        return self._post(
            f"/v1/tools/mcp/servers/{mcp_server_name}/resync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, server_resync_params.ServerResyncParams),
            ),
            cast_to=object,
        )

    @overload
    def test(
        self,
        *,
        args: SequenceNotStr[str],
        command: str,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Test connection to an MCP server without adding it.

        Returns the list of
        available tools if successful.

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
    def test(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Test connection to an MCP server without adding it.

        Returns the list of
        available tools if successful.

        Args:
          server_name: The name of the server

          server_url: The URL of the server (MCP SSE client will connect to this URL)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with SSE requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def test(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Test connection to an MCP server without adding it.

        Returns the list of
        available tools if successful.

        Args:
          server_name: The name of the server

          server_url: The URL path for the streamable HTTP server (e.g., 'example/mcp')

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with streamable HTTP requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["args", "command", "server_name"], ["server_name", "server_url"])
    def test(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
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
    ) -> object:
        return self._post(
            "/v1/tools/mcp/servers/test",
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
                server_test_params.ServerTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncServersResource(AsyncAPIResource):
    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AsyncServersResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        mcp_server_name: str,
        *,
        stdio_config: Optional[StdioServerConfigParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          stdio_config: The configuration for the server (MCP 'local' client will run this command)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        mcp_server_name: str,
        *,
        token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          token: The access token or API key for the MCP server (used for SSE authentication)

          custom_headers: Custom authentication headers as key-value pairs

          server_url: The URL of the server (MCP SSE client will connect to this URL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        mcp_server_name: str,
        *,
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
    ) -> ServerUpdateResponse:
        """
        Update an existing MCP server configuration

        Args:
          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom authentication headers as key-value pairs

          server_url: The URL path for the streamable HTTP server (e.g., 'example/mcp')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        mcp_server_name: str,
        *,
        stdio_config: Optional[StdioServerConfigParam] | Omit = omit,
        token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateResponse:
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        return cast(
            ServerUpdateResponse,
            await self._patch(
                f"/v1/tools/mcp/servers/{mcp_server_name}",
                body=await async_maybe_transform(
                    {
                        "stdio_config": stdio_config,
                        "token": token,
                        "custom_headers": custom_headers,
                        "server_url": server_url,
                        "auth_header": auth_header,
                        "auth_token": auth_token,
                    },
                    server_update_params.ServerUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ServerUpdateResponse
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
    ) -> ServerListResponse:
        """Get a list of all configured MCP servers"""
        return await self._get(
            "/v1/tools/mcp/servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerListResponse,
        )

    async def delete(
        self,
        mcp_server_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerDeleteResponse:
        """
        Delete a MCP server configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        return await self._delete(
            f"/v1/tools/mcp/servers/{mcp_server_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerDeleteResponse,
        )

    @overload
    async def add(
        self,
        *,
        args: SequenceNotStr[str],
        command: str,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerAddResponse:
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
    async def add(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerAddResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          server_name: The name of the server

          server_url: The URL of the server (MCP SSE client will connect to this URL)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with SSE requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def add(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerAddResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Args:
          server_name: The name of the server

          server_url: The URL path for the streamable HTTP server (e.g., 'example/mcp')

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with streamable HTTP requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["args", "command", "server_name"], ["server_name", "server_url"])
    async def add(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
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
    ) -> ServerAddResponse:
        return await self._put(
            "/v1/tools/mcp/servers",
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
                server_add_params.ServerAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerAddResponse,
        )

    @overload
    async def connect(
        self,
        *,
        args: SequenceNotStr[str],
        command: str,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Connect to an MCP server with support for OAuth via SSE.

        Returns a stream of
        events handling authorization state and exchange if OAuth is required.

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
    async def connect(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Connect to an MCP server with support for OAuth via SSE.

        Returns a stream of
        events handling authorization state and exchange if OAuth is required.

        Args:
          server_name: The name of the server

          server_url: The URL of the server (MCP SSE client will connect to this URL)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with SSE requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def connect(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Connect to an MCP server with support for OAuth via SSE.

        Returns a stream of
        events handling authorization state and exchange if OAuth is required.

        Args:
          server_name: The name of the server

          server_url: The URL path for the streamable HTTP server (e.g., 'example/mcp')

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with streamable HTTP requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["args", "command", "server_name"], ["server_name", "server_url"])
    async def connect(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
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
    ) -> object:
        return await self._post(
            "/v1/tools/mcp/servers/connect",
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
                server_connect_params.ServerConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def register_tool(
        self,
        mcp_tool_name: str,
        *,
        mcp_server_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Register a new MCP tool as a Letta server by MCP server + tool name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        if not mcp_tool_name:
            raise ValueError(f"Expected a non-empty value for `mcp_tool_name` but received {mcp_tool_name!r}")
        return await self._post(
            f"/v1/tools/mcp/servers/{mcp_server_name}/{mcp_tool_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    async def resync(
        self,
        mcp_server_name: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Resync tools for an MCP server by:

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
        if not mcp_server_name:
            raise ValueError(f"Expected a non-empty value for `mcp_server_name` but received {mcp_server_name!r}")
        return await self._post(
            f"/v1/tools/mcp/servers/{mcp_server_name}/resync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"agent_id": agent_id}, server_resync_params.ServerResyncParams),
            ),
            cast_to=object,
        )

    @overload
    async def test(
        self,
        *,
        args: SequenceNotStr[str],
        command: str,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Test connection to an MCP server without adding it.

        Returns the list of
        available tools if successful.

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
    async def test(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Test connection to an MCP server without adding it.

        Returns the list of
        available tools if successful.

        Args:
          server_name: The name of the server

          server_url: The URL of the server (MCP SSE client will connect to this URL)

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with SSE requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def test(
        self,
        *,
        server_name: str,
        server_url: str,
        auth_header: Optional[str] | Omit = omit,
        auth_token: Optional[str] | Omit = omit,
        custom_headers: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Test connection to an MCP server without adding it.

        Returns the list of
        available tools if successful.

        Args:
          server_name: The name of the server

          server_url: The URL path for the streamable HTTP server (e.g., 'example/mcp')

          auth_header: The name of the authentication header (e.g., 'Authorization')

          auth_token: The authentication token or API key value

          custom_headers: Custom HTTP headers to include with streamable HTTP requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["args", "command", "server_name"], ["server_name", "server_url"])
    async def test(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        server_name: str,
        env: Optional[Dict[str, str]] | Omit = omit,
        type: McpServerType | Omit = omit,
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
    ) -> object:
        return await self._post(
            "/v1/tools/mcp/servers/test",
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
                server_test_params.ServerTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ServersResourceWithRawResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.update = to_raw_response_wrapper(
            servers.update,
        )
        self.list = to_raw_response_wrapper(
            servers.list,
        )
        self.delete = to_raw_response_wrapper(
            servers.delete,
        )
        self.add = to_raw_response_wrapper(
            servers.add,
        )
        self.connect = to_raw_response_wrapper(
            servers.connect,
        )
        self.register_tool = to_raw_response_wrapper(
            servers.register_tool,
        )
        self.resync = to_raw_response_wrapper(
            servers.resync,
        )
        self.test = to_raw_response_wrapper(
            servers.test,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._servers.tools)


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.update = async_to_raw_response_wrapper(
            servers.update,
        )
        self.list = async_to_raw_response_wrapper(
            servers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            servers.delete,
        )
        self.add = async_to_raw_response_wrapper(
            servers.add,
        )
        self.connect = async_to_raw_response_wrapper(
            servers.connect,
        )
        self.register_tool = async_to_raw_response_wrapper(
            servers.register_tool,
        )
        self.resync = async_to_raw_response_wrapper(
            servers.resync,
        )
        self.test = async_to_raw_response_wrapper(
            servers.test,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._servers.tools)


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.update = to_streamed_response_wrapper(
            servers.update,
        )
        self.list = to_streamed_response_wrapper(
            servers.list,
        )
        self.delete = to_streamed_response_wrapper(
            servers.delete,
        )
        self.add = to_streamed_response_wrapper(
            servers.add,
        )
        self.connect = to_streamed_response_wrapper(
            servers.connect,
        )
        self.register_tool = to_streamed_response_wrapper(
            servers.register_tool,
        )
        self.resync = to_streamed_response_wrapper(
            servers.resync,
        )
        self.test = to_streamed_response_wrapper(
            servers.test,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._servers.tools)


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.update = async_to_streamed_response_wrapper(
            servers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            servers.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            servers.add,
        )
        self.connect = async_to_streamed_response_wrapper(
            servers.connect,
        )
        self.register_tool = async_to_streamed_response_wrapper(
            servers.register_tool,
        )
        self.resync = async_to_streamed_response_wrapper(
            servers.resync,
        )
        self.test = async_to_streamed_response_wrapper(
            servers.test,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._servers.tools)
