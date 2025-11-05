# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .sse_mcp_server import SseMcpServer
from .stdio_mcp_server import StdioMcpServer
from .streamable_http_mcp_server import StreamableHTTPMcpServer

__all__ = ["McpServerModifyResponse"]

McpServerModifyResponse: TypeAlias = Union[StdioMcpServer, SseMcpServer, StreamableHTTPMcpServer]
