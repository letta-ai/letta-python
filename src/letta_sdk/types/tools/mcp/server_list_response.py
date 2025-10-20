# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import TypeAlias

from .sse_server_config import SseServerConfig
from .stdio_server_config import StdioServerConfig
from .streamable_http_server_config import StreamableHTTPServerConfig

__all__ = ["ServerListResponse", "ServerListResponseItem"]

ServerListResponseItem: TypeAlias = Union[SseServerConfig, StdioServerConfig, StreamableHTTPServerConfig]

ServerListResponse: TypeAlias = Dict[str, ServerListResponseItem]
