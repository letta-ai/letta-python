# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    name: Optional[str]
    """Name of the agent"""

    tags: Optional[List[str]]
    """List of tags to filter agents by"""

    user_id: str
