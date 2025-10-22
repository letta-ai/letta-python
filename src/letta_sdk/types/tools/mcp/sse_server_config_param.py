# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .mcp_server_type import McpServerType

__all__ = ["SseServerConfigParam"]


class SseServerConfigParam(TypedDict, total=False):
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
