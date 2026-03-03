# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageStreamParams"]


class MessageStreamParams(TypedDict, total=False):
    batch_size: Optional[int]
    """Number of entries to read per batch."""

    include_pings: Optional[bool]
    """
    Whether to include periodic keepalive ping messages in the stream to prevent
    connection timeouts.
    """

    poll_interval: Optional[float]
    """Seconds to wait between polls when no new data."""

    starting_after: int
    """Sequence id to use as a cursor for pagination.

    Response will start streaming after this chunk sequence id
    """

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]
