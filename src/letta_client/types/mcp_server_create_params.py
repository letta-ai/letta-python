# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .create_sse_mcp_server_param import CreateSseMcpServerParam
from .create_stdio_mcp_server_param import CreateStdioMcpServerParam
from .create_streamable_http_mcp_server_param import CreateStreamableHTTPMcpServerParam

__all__ = ["McpServerCreateParams", "Config"]


class McpServerCreateParams(TypedDict, total=False):
    config: Required[Config]
    """The MCP server configuration (Stdio, SSE, or Streamable HTTP)"""

    server_name: Required[str]
    """The name of the MCP server"""


Config: TypeAlias = Union[CreateStdioMcpServerParam, CreateSseMcpServerParam, CreateStreamableHTTPMcpServerParam]
