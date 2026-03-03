# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TagListParams"]


class TagListParams(TypedDict, total=False):
    after: Optional[str]
    """Tag cursor for pagination.

    Returns tags that come after this tag in the specified sort order
    """

    before: Optional[str]
    """Tag cursor for pagination.

    Returns tags that come before this tag in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of tags to return"""

    name: Optional[str]
    """Filter tags by name"""

    order: Literal["asc", "desc"]
    """Sort order for tags.

    'asc' for alphabetical order, 'desc' for reverse alphabetical order
    """

    order_by: Literal["name"]
    """Field to sort by"""

    query_text: Optional[str]
    """Filter tags by text search. Deprecated, please use name field instead"""

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]
