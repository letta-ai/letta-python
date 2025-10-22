# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["RunListActiveParams"]


class RunListActiveParams(TypedDict, total=False):
    agent_ids: Optional[SequenceNotStr[str]]
    """The unique identifier of the agent associated with the run."""

    background: Optional[bool]
    """If True, filters for runs that were created in background mode."""
