# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    after: Optional[str]
    """Agent ID cursor for pagination.

    Returns agents that come after this agent ID in the specified sort order
    """

    before: Optional[str]
    """Agent ID cursor for pagination.

    Returns agents that come before this agent ID in the specified sort order
    """

    include: List[
        Literal[
            "agent.blocks",
            "agent.identities",
            "agent.managed_group",
            "agent.pending_approval",
            "agent.secrets",
            "agent.sources",
            "agent.tags",
            "agent.tools",
        ]
    ]
    """Specify which relational fields to include in the response.

    No relationships are included by default.
    """

    include_relationships: Optional[SequenceNotStr[str]]
    """
    Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
    in the response. If not provided, all relationships are loaded by default. Using
    this can optimize performance by reducing unnecessary joins.This is a legacy
    parameter, and no longer supported after 1.0.0 SDK versions.
    """

    limit: Optional[int]
    """Maximum number of agents to return"""

    order: Literal["asc", "desc"]
    """Sort order for agents by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""
