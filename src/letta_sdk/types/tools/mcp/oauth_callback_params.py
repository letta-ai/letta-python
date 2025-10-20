# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["OAuthCallbackParams"]


class OAuthCallbackParams(TypedDict, total=False):
    code: Optional[str]
    """OAuth authorization code"""

    error: Optional[str]
    """OAuth error"""

    error_description: Optional[str]
    """OAuth error description"""

    state: Optional[str]
    """OAuth state parameter"""
