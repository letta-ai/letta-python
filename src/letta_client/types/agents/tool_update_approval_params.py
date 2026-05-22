# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from ..._utils import PropertyInfo

from typing import Optional

__all__ = ["ToolUpdateApprovalParams"]

class ToolUpdateApprovalParams(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent in the format 'agent-<uuid4>'"""

    body_requires_approval: Required[Annotated[bool, PropertyInfo(alias="requires_approval")]]
    """Whether the tool requires approval before execution"""

    query_requires_approval: Annotated[Optional[bool], PropertyInfo(alias="requires_approval")]
    """Whether the tool requires approval before execution"""