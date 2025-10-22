# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NpmRequirement"]


class NpmRequirement(BaseModel):
    name: str
    """Name of the npm package."""

    version: Optional[str] = None
    """Optional version of the package, following semantic versioning."""
