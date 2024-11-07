# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    key: str
    """The key value."""

    name: str
    """Name of the token."""

    user_id: str
    """The unique identifier of the user associated with the token."""

    id: Optional[str] = None
    """The human-friendly ID of the Sk"""
