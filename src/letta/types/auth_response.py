# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthResponse"]


class AuthResponse(BaseModel):
    uuid: str
    """UUID of the user"""

    is_admin: Optional[bool] = None
    """Whether the user is an admin"""
