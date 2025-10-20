# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TemplateListVersionsResponse", "Version"]


class Version(BaseModel):
    created_at: str
    """When the version was created"""

    is_latest: bool
    """Whether this is the latest version"""

    version: str
    """The version number"""

    message: Optional[str] = None
    """Version description message"""


class TemplateListVersionsResponse(BaseModel):
    has_next_page: bool

    total_count: float

    versions: List[Version]
