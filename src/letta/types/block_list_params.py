# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BlockListParams"]


class BlockListParams(TypedDict, total=False):
    label: Optional[str]
    """Labels to include (e.g. human, persona)"""

    name: Optional[str]
    """Name of the block"""

    templates_only: bool
    """Whether to include only templates"""
