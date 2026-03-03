# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BlockListParams"]


class BlockListParams(TypedDict, total=False):
    after: Optional[str]
    """Block ID cursor for pagination.

    Returns blocks that come after this block ID in the specified sort order
    """

    before: Optional[str]
    """Block ID cursor for pagination.

    Returns blocks that come before this block ID in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of blocks to return"""

    order: Literal["asc", "desc"]
    """Sort order for blocks by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]
