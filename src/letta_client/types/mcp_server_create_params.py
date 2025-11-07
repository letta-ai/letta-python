# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["McpServerCreateParams", "CreateStdioMcpServer", "CreateSseMcpServer", "CreateStreamableHTTPMcpServer"]


class CreateStdioMcpServer(TypedDict, total=False):
    args: Required[SequenceNotStr[str]]
    """The arguments to pass to the command"""

    command: Required[str]
    """The command to run (MCP 'local' client will run this command)"""

    server_name: Required[str]
    """The name of the server"""

    env: Optional[Dict[str, str]]
    """Environment variables to set"""

    type: Literal["sse", "stdio", "streamable_http"]


class CreateSseMcpServer(TypedDict, total=False):
    server_name: Required[str]
    """The name of the server"""

    server_url: Required[str]
    """The URL of the server"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom HTTP headers to include with requests"""

    type: Literal["sse", "stdio", "streamable_http"]


class CreateStreamableHTTPMcpServer(TypedDict, total=False):
    server_name: Required[str]
    """The name of the server"""

    server_url: Required[str]
    """The URL of the server"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom HTTP headers to include with requests"""

    type: Literal["sse", "stdio", "streamable_http"]


McpServerCreateParams: TypeAlias = Union[CreateStdioMcpServer, CreateSseMcpServer, CreateStreamableHTTPMcpServer]
