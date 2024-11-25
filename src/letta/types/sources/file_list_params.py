# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Pagination cursor to fetch the next set of results"""

    limit: int
    """Number of files to return"""
