# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolUpdateApprovalParams"]


class ToolUpdateApprovalParams(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent in the format 'agent-<uuid4>'"""

    requires_approval: Required[bool]
