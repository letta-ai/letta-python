# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PipRequirement"]


class PipRequirement(BaseModel):
    name: str
    """Name of the pip package."""

    version: Optional[str] = None
    """Optional version of the package, following semantic versioning."""
