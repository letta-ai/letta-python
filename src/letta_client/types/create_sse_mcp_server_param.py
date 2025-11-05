# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CreateSseMcpServerParam"]


class CreateSseMcpServerParam(TypedDict, total=False):
    server_name: Required[str]
    """The name of the server"""

    server_url: Required[str]
    """The URL of the server"""

    auth_header: Optional[str]
    """The name of the authentication header (e.g., 'Authorization')"""

    auth_token: Optional[str]
    """The authentication token or API key value"""

    custom_headers: Optional[Dict[str, str]]
    """Custom HTTP headers to include with requests"""

    type: Literal["sse", "stdio", "streamable_http"]
