# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    after: Optional[str]
    """Cursor for pagination"""

    ascending: bool
    """
    Whether to sort agents oldest to newest (True) or newest to oldest (False,
    default)
    """

    base_template_id: Optional[str]
    """Search agents by base template ID"""

    before: Optional[str]
    """Cursor for pagination"""

    identifier_keys: Optional[SequenceNotStr[str]]
    """Search agents by identifier keys"""

    identity_id: Optional[str]
    """Search agents by identity ID"""

    include_relationships: Optional[SequenceNotStr[str]]
    """
    Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
    in the response. If not provided, all relationships are loaded by default. Using
    this can optimize performance by reducing unnecessary joins.
    """

    limit: Optional[int]
    """Limit for pagination"""

    match_all_tags: bool
    """If True, only returns agents that match ALL given tags.

    Otherwise, return agents that have ANY of the passed-in tags.
    """

    name: Optional[str]
    """Name of the agent"""

    order: Literal["asc", "desc"]
    """Sort order for agents by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at", "last_run_completion"]
    """Field to sort by"""

    project_id: Optional[str]
    """
    Search agents by project ID - this will default to your default project on cloud
    """

    query_text: Optional[str]
    """Search agents by name"""

    sort_by: Optional[str]
    """Field to sort by. Options: 'created_at' (default), 'last_run_completion'"""

    tags: Optional[SequenceNotStr[str]]
    """List of tags to filter agents by"""

    template_id: Optional[str]
    """Search agents by template ID"""
