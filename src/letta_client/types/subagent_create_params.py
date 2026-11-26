# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SubagentCreateParams"]


class SubagentCreateParams(TypedDict, total=False):
    description: Required[str]

    harness: Required[str]

    parent_conversation_id: Required[str]

    agent_id: Optional[str]

    archived: bool

    computer: Optional[str]

    conversation_id: Optional[str]

    fork_context: bool

    mcp_config: Optional[Dict[str, object]]

    model_config: Optional[Dict[str, object]]

    parent_agent_id: str

    prompt: Optional[str]

    repositories: Optional[SequenceNotStr[str]]

    sandbox_size: Optional[str]

    status: Literal["running", "idle", "completed", "failed", "stopped"]

    subagent_type: Optional[str]

    worker_session_id: Optional[str]
