# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .stop_reason_type import StopReasonType

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    active: bool
    """Filter for active runs."""

    after: Optional[str]
    """Cursor for pagination (run ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'run-<uuid4>'
    """

    agent_id: Optional[str]
    """The unique identifier of the agent associated with the run."""

    agent_ids: Optional[SequenceNotStr[str]]
    """The unique identifiers of the agents associated with the run.

    Deprecated in favor of agent_id field.
    """

    ascending: bool
    """
    Whether to sort agents oldest to newest (True) or newest to oldest (False,
    default). Deprecated in favor of order field.
    """

    background: Optional[bool]
    """If True, filters for runs that were created in background mode."""

    before: Optional[str]
    """Cursor for pagination (run ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'run-<uuid4>'
    """

    conversation_id: Optional[str]
    """Filter runs by conversation ID."""

    limit: Optional[int]
    """Maximum number of runs to return"""

    order: Literal["asc", "desc"]
    """Sort order for runs by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    statuses: Optional[SequenceNotStr[str]]
    """Filter runs by status. Can specify multiple statuses."""

    stop_reason: Optional[StopReasonType]
    """Filter runs by stop reason."""
