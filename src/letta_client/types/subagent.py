# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Subagent"]


class Subagent(BaseModel):
    agent_id: Optional[str] = None

    archived: bool

    computer: Optional[str] = None

    conversation_id: Optional[str] = None

    created_at: datetime

    description: str

    fork_context: bool

    harness: str

    mcp_config: Optional[Dict[str, object]] = None

    api_model_config: Optional[Dict[str, object]] = FieldInfo(alias="model_config", default=None)

    parent_agent_id: str

    parent_conversation_id: str

    prompt: Optional[str] = None

    repositories: Optional[List[str]] = None

    sandbox_size: Optional[str] = None

    status: Literal["running", "idle", "completed", "failed", "stopped"]

    subagent_id: str

    subagent_type: Optional[str] = None

    updated_at: datetime

    worker_session_id: Optional[str] = None
