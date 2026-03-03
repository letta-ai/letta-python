# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FolderListParams"]


class FolderListParams(TypedDict, total=False):
    after: Optional[str]
    """Folder ID cursor for pagination.

    Returns folders that come after this folder ID in the specified sort order
    """

    before: Optional[str]
    """Folder ID cursor for pagination.

    Returns folders that come before this folder ID in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of folders to return"""

    name: Optional[str]
    """Folder name to filter by"""

    order: Literal["asc", "desc"]
    """Sort order for folders by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]
