# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "McpServerListResponse",
    "McpServerListResponseItem",
    "McpServerListResponseItemStdioMcpServer",
    "McpServerListResponseItemSsemcpServer",
    "McpServerListResponseItemStreamableHttpmcpServer",
]


class McpServerListResponseItemStdioMcpServer(BaseModel):
    args: List[str]
    """The arguments to pass to the command"""

    command: str
    """The command to run (MCP 'local' client will run this command)"""

    server_name: str
    """The name of the server"""

    id: Optional[str] = None
    """The human-friendly ID of the Mcp_server"""

    env: Optional[Dict[str, str]] = None
    """Environment variables to set"""

    type: Optional[Literal["sse", "stdio", "streamable_http"]] = None


class McpServerListResponseItemSsemcpServer(BaseModel):
    server_name: str
    """The name of the server"""

    server_url: str
    """The URL of the server"""

    id: Optional[str] = None
    """The human-friendly ID of the Mcp_server"""

    auth_header: Optional[str] = None
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str] = None
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]] = None
    """Custom HTTP headers to include with requests"""

    type: Optional[Literal["sse", "stdio", "streamable_http"]] = None


class McpServerListResponseItemStreamableHttpmcpServer(BaseModel):
    server_name: str
    """The name of the server"""

    server_url: str
    """The URL of the server"""

    id: Optional[str] = None
    """The human-friendly ID of the Mcp_server"""

    auth_header: Optional[str] = None
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str] = None
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]] = None
    """Custom HTTP headers to include with requests"""

    type: Optional[Literal["sse", "stdio", "streamable_http"]] = None


McpServerListResponseItem: TypeAlias = Union[
    McpServerListResponseItemStdioMcpServer,
    McpServerListResponseItemSsemcpServer,
    McpServerListResponseItemStreamableHttpmcpServer,
]

McpServerListResponse: TypeAlias = List[McpServerListResponseItem]
