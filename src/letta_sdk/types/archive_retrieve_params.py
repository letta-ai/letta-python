# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ArchiveRetrieveParams"]


class ArchiveRetrieveParams(TypedDict, total=False):
    after: Optional[str]
    """Archive ID cursor for pagination.

    Returns archives that come after this archive ID in the specified sort order
    """

    agent_id: Optional[str]
    """Only archives attached to this agent ID"""

    before: Optional[str]
    """Archive ID cursor for pagination.

    Returns archives that come before this archive ID in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of archives to return"""

    name: Optional[str]
    """Filter by archive name (exact match)"""

    order: Literal["asc", "desc"]
    """Sort order for archives by creation time.

    'asc' for oldest first, 'desc' for newest first
    """
