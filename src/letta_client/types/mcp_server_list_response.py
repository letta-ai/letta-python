# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, List

from .stdio_mcp_server import StdioMcpServer

from .sse_mcp_server import SseMcpServer

from .streamable_http_mcp_server import StreamableHTTPMcpServer

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["McpServerListResponse", "McpServerListResponseItem"]

McpServerListResponseItem: TypeAlias = Union[StdioMcpServer, SseMcpServer, StreamableHTTPMcpServer]

McpServerListResponse: TypeAlias = List[McpServerListResponseItem]