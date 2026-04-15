# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ArchiveListParams"]


class ArchiveListParams(TypedDict, total=False):
    after: Optional[str]
    """Cursor for pagination (archive ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'archive-<uuid4>'
    """

    agent_id: Optional[str]
    """Only archives attached to this agent ID"""

    before: Optional[str]
    """Cursor for pagination (archive ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'archive-<uuid4>'
    """

    limit: Optional[int]
    """Maximum number of archives to return"""

    name: Optional[str]
    """Filter by archive name (exact match)"""

    order: Literal["asc", "desc"]
    """Sort order for archives by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""
