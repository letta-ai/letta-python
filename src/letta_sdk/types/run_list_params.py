# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .stop_reason_type import StopReasonType

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    active: bool
    """Filter for active runs."""

    after: Optional[str]
    """Cursor for pagination"""

    agent_ids: Optional[SequenceNotStr[str]]
    """The unique identifier of the agent associated with the run."""

    ascending: bool
    """
    Whether to sort agents oldest to newest (True) or newest to oldest (False,
    default)
    """

    background: Optional[bool]
    """If True, filters for runs that were created in background mode."""

    before: Optional[str]
    """Cursor for pagination"""

    limit: Optional[int]
    """Maximum number of runs to return"""

    stop_reason: Optional[StopReasonType]
    """Filter runs by stop reason."""
