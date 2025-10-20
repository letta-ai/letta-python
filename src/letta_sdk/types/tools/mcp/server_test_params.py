# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from .mcp_server_type import McpServerType

__all__ = ["ServerTestParams", "StdioServerConfig", "SseServerConfig", "StreamableHTTPServerConfig"]


class StdioServerConfig(TypedDict, total=False):
    args: Required[SequenceNotStr[str]]
    """The arguments to pass to the command"""

    command: Required[str]
    """The command to run (MCP 'local' client will run this command)"""

    server_name: Required[str]
    """The name of the server"""

    env: Optional[Dict[str, str]]
    """Environment variables to set"""

    type: McpServerType


class SseServerConfig(TypedDict, total=False):
    server_name: Required[str]
    """The name of the server"""

    server_url: Required[str]
    """The URL of the server (MCP SSE client will connect to this URL)"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom HTTP headers to include with SSE requests"""

    type: McpServerType


class StreamableHTTPServerConfig(TypedDict, total=False):
    server_name: Required[str]
    """The name of the server"""

    server_url: Required[str]
    """The URL path for the streamable HTTP server (e.g., 'example/mcp')"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom HTTP headers to include with streamable HTTP requests"""

    type: McpServerType


ServerTestParams: TypeAlias = Union[StdioServerConfig, SseServerConfig, StreamableHTTPServerConfig]
