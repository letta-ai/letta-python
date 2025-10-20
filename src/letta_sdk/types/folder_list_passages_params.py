# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FolderListPassagesParams"]


class FolderListPassagesParams(TypedDict, total=False):
    after: Optional[str]
    """Passage ID cursor for pagination.

    Returns passages that come after this passage ID in the specified sort order
    """

    before: Optional[str]
    """Passage ID cursor for pagination.

    Returns passages that come before this passage ID in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of passages to return"""

    order: Literal["asc", "desc"]
    """Sort order for passages by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""
