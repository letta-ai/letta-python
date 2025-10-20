# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: Optional[str]
    """Pagination cursor to fetch the next set of results"""

    check_status_updates: bool
    """Whether to check and update file processing status (from the vector db service).

    If False, will not fetch and update the status, which may lead to performance
    gains.
    """

    include_content: bool
    """Whether to include full file content"""

    limit: int
    """Number of files to return"""
