# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PassageCreateParams"]


class PassageCreateParams(TypedDict, total=False):
    text: Required[str]
    """The text content of the passage"""

    created_at: Optional[str]
    """Optional creation datetime for the passage (ISO 8601 format)"""

    metadata: Optional[Dict[str, object]]
    """Optional metadata for the passage"""

    tags: Optional[SequenceNotStr[str]]
    """Optional tags for categorizing the passage"""

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]
