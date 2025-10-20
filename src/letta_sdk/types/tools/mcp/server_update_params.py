# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .stdio_server_config_param import StdioServerConfigParam

__all__ = ["ServerUpdateParams", "UpdateStdioMcpServer", "UpdateSsemcpServer", "UpdateStreamableHttpmcpServer"]


class UpdateStdioMcpServer(TypedDict, total=False):
    stdio_config: Optional[StdioServerConfigParam]
    """The configuration for the server (MCP 'local' client will run this command)"""


class UpdateSsemcpServer(TypedDict, total=False):
    token: Optional[str]
    """The access token or API key for the MCP server (used for SSE authentication)"""

    custom_headers: Optional[Dict[str, str]]
    """Custom authentication headers as key-value pairs"""

    server_url: Optional[str]
    """The URL of the server (MCP SSE client will connect to this URL)"""


class UpdateStreamableHttpmcpServer(TypedDict, total=False):
    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom authentication headers as key-value pairs"""

    server_url: Optional[str]
    """The URL path for the streamable HTTP server (e.g., 'example/mcp')"""


ServerUpdateParams: TypeAlias = Union[UpdateStdioMcpServer, UpdateSsemcpServer, UpdateStreamableHttpmcpServer]
