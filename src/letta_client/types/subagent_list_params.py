# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SubagentListParams"]


class SubagentListParams(TypedDict, total=False):
    after: str

    archived: Literal["true", "false"]

    limit: int

    parent_agent_id: str

    parent_conversation_id: str

    status: Literal["running", "idle", "completed", "failed", "stopped"]
