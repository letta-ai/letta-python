# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .mcp_server_type import McpServerType

__all__ = ["StreamableHTTPServerConfigParam"]


class StreamableHTTPServerConfigParam(TypedDict, total=False):
    server_name: Required[str]
    """The name of the server"""

    server_url: Required[str]
    """The URL path for the streamable HTTP server (e.g., 'example/mcp')"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom HTTP headers to include with streamable HTTP requests"""

    type: McpServerType
