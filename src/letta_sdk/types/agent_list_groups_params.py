# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AgentListGroupsParams"]


class AgentListGroupsParams(TypedDict, total=False):
    manager_type: Optional[str]
    """Manager type to filter groups by"""
