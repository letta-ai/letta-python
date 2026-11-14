# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Monitor"]


class Monitor(BaseModel):
    agent_id: Optional[str] = None

    command: str

    conversation_id: Optional[str] = None

    created_at: datetime

    description: str

    device_id: Optional[str] = None

    exit_code: Optional[int] = None

    kind: Literal["command", "websocket", "script", "github_pull_request"]

    monitor_id: str

    output_file: Optional[str] = None

    persistent: bool

    started_at: Optional[datetime] = None

    status: Literal["running", "completed", "failed"]

    updated_at: datetime
