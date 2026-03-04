# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["StepListParams"]


class StepListParams(TypedDict, total=False):
    after: Optional[str]
    """Return steps after this step ID"""

    agent_id: Optional[str]
    """Filter by the ID of the agent that performed the step"""

    before: Optional[str]
    """Return steps before this step ID"""

    end_date: Optional[str]
    """Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")"""

    feedback: Optional[Literal["positive", "negative"]]
    """Filter by feedback"""

    has_feedback: Optional[bool]
    """Filter by whether steps have feedback (true) or not (false)"""

    limit: Optional[int]
    """Maximum number of steps to return"""

    model: Optional[str]
    """Filter by the name of the model used for the step"""

    order: Literal["asc", "desc"]
    """Sort order for steps by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    project_id: Optional[str]
    """Filter by the project ID that is associated with the step (cloud only)."""

    start_date: Optional[str]
    """Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")"""

    tags: Optional[SequenceNotStr[str]]
    """Filter by tags"""

    trace_ids: Optional[SequenceNotStr[str]]
    """Filter by trace ids returned by the server"""
