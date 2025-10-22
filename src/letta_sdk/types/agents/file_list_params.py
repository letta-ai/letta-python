# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Pagination cursor from previous response"""

    is_open: Optional[bool]
    """Filter by open status (true for open files, false for closed files)"""

    limit: int
    """Number of items to return (1-100)"""
