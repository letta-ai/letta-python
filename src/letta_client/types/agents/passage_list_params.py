# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PassageListParams"]


class PassageListParams(TypedDict, total=False):
    after: Optional[str]
    """Unique ID of the memory to start the query range at."""

    ascending: Optional[bool]
    """
    Whether to sort passages oldest to newest (True, default) or newest to oldest
    (False)
    """

    before: Optional[str]
    """Unique ID of the memory to end the query range at."""

    limit: Optional[int]
    """How many results to include in the response."""

    search: Optional[str]
    """Search passages by text"""
