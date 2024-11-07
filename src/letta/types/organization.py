# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Organization"]


class Organization(BaseModel):
    id: Optional[str] = None
    """The human-friendly ID of the Org"""

    created_at: Optional[datetime] = None
    """The creation date of the organization."""

    name: Optional[str] = None
    """The name of the organization."""
