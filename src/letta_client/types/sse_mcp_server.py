# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SseMcpServer"]


class SseMcpServer(BaseModel):
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
