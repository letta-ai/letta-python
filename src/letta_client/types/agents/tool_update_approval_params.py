# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ToolUpdateApprovalParams"]


class ToolUpdateApprovalParams(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent in the format 'agent-<uuid4>'"""

    body_requires_approval: Required[Annotated[bool, PropertyInfo(alias="requires_approval")]]
    """Whether the tool requires approval before execution"""

    query_requires_approval: Annotated[Optional[bool], PropertyInfo(alias="requires_approval")]
    """Whether the tool requires approval before execution"""
