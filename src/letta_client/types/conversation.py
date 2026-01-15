# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Conversation"]


class Conversation(BaseModel):
    """Represents a conversation on an agent for concurrent messaging."""

    id: str
    """The unique identifier of the conversation."""

    agent_id: str
    """The ID of the agent this conversation belongs to."""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    in_context_message_ids: Optional[List[str]] = None
    """The IDs of in-context messages for the conversation."""

    isolated_block_ids: Optional[List[str]] = None
    """
    IDs of blocks that are isolated (specific to this conversation, overriding agent
    defaults).
    """

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    summary: Optional[str] = None
    """A summary of the conversation."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
