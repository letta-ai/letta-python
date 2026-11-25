# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SubagentUpdateParams"]


class SubagentUpdateParams(TypedDict, total=False):
    agent_id: Optional[str]

    archived: bool

    conversation_id: Optional[str]

    status: Literal["running", "idle", "completed", "failed", "stopped"]

    worker_session_id: Optional[str]
