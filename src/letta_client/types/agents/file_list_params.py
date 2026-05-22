# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional

__all__ = ["FileListParams"]

class FileListParams(TypedDict, total=False):
    after: Optional[str]
    """Cursor for pagination (file ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'file-<uuid4>'
    """

    before: Optional[str]
    """Cursor for pagination (file ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'file-<uuid4>'
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