# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .stop_reason_type import StopReasonType

__all__ = ["AgentCountParams"]


class AgentCountParams(TypedDict, total=False):
    base_template_id: Optional[str]
    """Search agents by base template ID"""

    identifier_keys: Optional[SequenceNotStr[str]]
    """Search agents by identifier keys"""

    identity_id: Optional[str]
    """Search agents by identity ID"""

    last_stop_reason: Optional[StopReasonType]
    """Filter agents by their last stop reason."""

    match_all_tags: bool
    """If True, only counts agents that match ALL given tags.

    Otherwise, counts agents that have ANY of the passed-in tags.
    """

    name: Optional[str]
    """Name of the agent"""

    project_id: Optional[str]
    """
    Search agents by project ID - this will default to your default project on cloud
    """

    query_text: Optional[str]
    """Search agents by name"""

    tags: Optional[SequenceNotStr[str]]
    """List of tags to filter agents by"""

    template_id: Optional[str]
    """Search agents by template ID"""
