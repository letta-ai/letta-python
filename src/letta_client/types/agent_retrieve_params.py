# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["AgentRetrieveParams"]


class AgentRetrieveParams(TypedDict, total=False):
    include: List[
        Literal[
            "agent.blocks",
            "agent.identities",
            "agent.managed_group",
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
