# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["UpdateStreamableHTTPMcpServerParam"]


class UpdateStreamableHTTPMcpServerParam(TypedDict, total=False):
    token: Optional[str]
    """The authentication token (internal)"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom headers to send with requests"""

    server_name: Optional[str]
    """The name of the MCP server"""

    server_url: Optional[str]
    """The URL of the Streamable HTTP MCP server"""
