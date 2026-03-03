# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    after: Optional[str]
    """Message ID cursor for pagination.

    Returns messages that come after this message ID in the specified sort order
    """

    before: Optional[str]
    """Message ID cursor for pagination.

    Returns messages that come before this message ID in the specified sort order
    """

    group_id: Optional[str]
    """Group ID to filter messages by."""

    include_err: Optional[bool]
    """Whether to include error messages and error statuses.

    For debugging purposes only.
    """

    limit: Optional[int]
    """Maximum number of messages to return"""

    order: Literal["asc", "desc"]
    """Sort order for messages by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]
