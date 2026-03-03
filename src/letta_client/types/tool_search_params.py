# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ToolSearchParams"]


class ToolSearchParams(TypedDict, total=False):
    limit: int
    """Maximum number of results to return."""

    query: Optional[str]
    """Text query for semantic search."""

    search_mode: Literal["vector", "fts", "hybrid"]
    """Search mode: vector, fts, or hybrid."""

    tags: Optional[SequenceNotStr[str]]
    """Filter by tags (match any)."""

    tool_types: Optional[SequenceNotStr[str]]
    """Filter by tool types (e.g., 'custom', 'letta_core')."""

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]
