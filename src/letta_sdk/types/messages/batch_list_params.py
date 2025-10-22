# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["BatchListParams"]


class BatchListParams(TypedDict, total=False):
    after: Optional[str]
    """Job ID cursor for pagination.

    Returns jobs that come after this job ID in the specified sort order
    """

    before: Optional[str]
    """Job ID cursor for pagination.

    Returns jobs that come before this job ID in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of jobs to return"""

    order: Literal["asc", "desc"]
    """Sort order for jobs by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""
