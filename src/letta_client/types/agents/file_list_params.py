# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: Optional[str]
    """File ID cursor for pagination.

    Returns files that come after this file ID in the specified sort order
    """

    before: Optional[str]
    """File ID cursor for pagination.

    Returns files that come before this file ID in the specified sort order
    """

    cursor: Optional[str]
    """Pagination cursor from previous response (deprecated, use before/after)"""

    is_open: Optional[bool]
    """Filter by open status (true for open files, false for closed files)"""

    limit: Optional[int]
    """Maximum number of files to return"""

    order: Literal["asc", "desc"]
    """Sort order for files by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""
