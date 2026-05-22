# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAliasType, TypeAlias

from typing import Optional, Union

from .update_stdio_mcp_server_param import UpdateStdioMcpServerParam

from .update_sse_mcp_server_param import UpdateSseMcpServerParam

from .update_streamable_http_mcp_server_param import UpdateStreamableHTTPMcpServerParam

__all__ = ["McpServerUpdateParams", "Config"]

class McpServerUpdateParams(TypedDict, total=False):
    config: Required[Config]
    """The MCP server configuration updates (Stdio, SSE, or Streamable HTTP)"""

    server_name: Optional[str]
    """The name of the MCP server"""

Config: TypeAlias = Union[UpdateStdioMcpServerParam, UpdateSseMcpServerParam, UpdateStreamableHTTPMcpServerParam]