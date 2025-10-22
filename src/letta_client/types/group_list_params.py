# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .manager_type import ManagerType

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    after: Optional[str]
    """Group ID cursor for pagination.

    Returns groups that come after this group ID in the specified sort order
    """

    before: Optional[str]
    """Group ID cursor for pagination.

    Returns groups that come before this group ID in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of groups to return"""

    manager_type: Optional[ManagerType]
    """Search groups by manager type"""

    order: Literal["asc", "desc"]
    """Sort order for groups by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    project_id: Optional[str]
    """Search groups by project id"""
