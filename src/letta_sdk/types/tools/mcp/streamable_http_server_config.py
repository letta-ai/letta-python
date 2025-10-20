# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel
from .mcp_server_type import McpServerType

__all__ = ["StreamableHTTPServerConfig"]


class StreamableHTTPServerConfig(BaseModel):
    server_name: str
    """The name of the server"""

    server_url: str
    """The URL path for the streamable HTTP server (e.g., 'example/mcp')"""

    auth_header: Optional[str] = None
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str] = None
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]] = None
    """Custom HTTP headers to include with streamable HTTP requests"""

    type: Optional[McpServerType] = None
