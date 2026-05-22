# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentEnvironmentVariable"]


class AgentEnvironmentVariable(BaseModel):
    agent_id: str
    """The ID of the agent this environment variable belongs to."""

    key: str
    """The name of the environment variable."""

    value: str
    """The value of the environment variable."""

    id: Optional[str] = None
    """The human-friendly ID of the Agent-env"""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    description: Optional[str] = None
    """An optional description of the environment variable."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""

    value_enc: Optional[str] = None
    """Encrypted secret value (stored as encrypted string)"""
