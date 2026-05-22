# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

__all__ = ["PipRequirement"]

class PipRequirement(BaseModel):
    name: str
    """Name of the pip package."""

    version: Optional[str] = None
    """Optional version of the package, following semantic versioning."""