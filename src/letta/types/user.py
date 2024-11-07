# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    name: str
    """The name of the user."""

    id: Optional[str] = None
    """The human-friendly ID of the User"""

    created_at: Optional[datetime] = None
    """The creation date of the user."""

    is_deleted: Optional[bool] = None
    """Whether this user is deleted or not."""

    organization_id: Optional[str] = None
    """The organization id of the user"""

    updated_at: Optional[datetime] = None
    """The update date of the user."""
