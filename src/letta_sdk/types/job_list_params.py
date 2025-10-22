# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    active: bool
    """Filter for active jobs."""

    after: Optional[str]
    """Cursor for pagination"""

    ascending: bool
    """
    Whether to sort jobs oldest to newest (True, default) or newest to oldest
    (False)
    """

    before: Optional[str]
    """Cursor for pagination"""

    limit: Optional[int]
    """Limit for pagination"""

    source_id: Optional[str]
    """Only list jobs associated with the source."""
