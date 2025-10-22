# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PipRequirementParam"]


class PipRequirementParam(TypedDict, total=False):
    name: Required[str]
    """Name of the pip package."""

    version: Optional[str]
    """Optional version of the package, following semantic versioning."""
