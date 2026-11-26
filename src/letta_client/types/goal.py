# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Goal"]


class Goal(BaseModel):
    agent_id: Optional[str] = None

    conversation_id: Optional[str] = None

    created_at: datetime

    description: str

    goal_id: str

    status: Literal["active", "completed", "cancelled"]

    updated_at: datetime
