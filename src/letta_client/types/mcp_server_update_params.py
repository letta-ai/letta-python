# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["McpServerUpdateParams", "UpdateStdioMcpServer", "UpdateSseMcpServer", "UpdateStreamableHTTPMcpServer"]


class UpdateStdioMcpServer(TypedDict, total=False):
    args: Optional[SequenceNotStr[str]]
    """The arguments to pass to the command"""

    command: Optional[str]
    """The command to run the MCP server"""

    env: Optional[Dict[str, str]]
    """Environment variables to set"""

    server_name: Optional[str]
    """The name of the MCP server"""


class UpdateSseMcpServer(TypedDict, total=False):
    token: Optional[str]
    """The authentication token (internal)"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom headers to send with requests"""

    server_name: Optional[str]
    """The name of the MCP server"""

    server_url: Optional[str]
    """The URL of the SSE MCP server"""


class UpdateStreamableHTTPMcpServer(TypedDict, total=False):
    token: Optional[str]
    """The authentication token (internal)"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom headers to send with requests"""

    server_name: Optional[str]
    """The name of the MCP server"""

    server_url: Optional[str]
    """The URL of the Streamable HTTP MCP server"""


McpServerUpdateParams: TypeAlias = Union[UpdateStdioMcpServer, UpdateSseMcpServer, UpdateStreamableHTTPMcpServer]
