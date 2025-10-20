# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolModifyApprovalParams"]


class ToolModifyApprovalParams(TypedDict, total=False):
    agent_id: Required[str]

    requires_approval: Required[bool]
