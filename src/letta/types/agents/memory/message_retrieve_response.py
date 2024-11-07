# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "MessageRetrieveResponse",
    "MessageRetrieveResponseItem",
    "MessageRetrieveResponseItemToolCall",
    "MessageRetrieveResponseItemToolCallFunction",
]


class MessageRetrieveResponseItemToolCallFunction(BaseModel):
    arguments: str
    """The arguments to pass to the function (JSON dump)"""

    name: str
    """The name of the function to call"""


class MessageRetrieveResponseItemToolCall(BaseModel):
    id: str
    """The ID of the tool call"""

    function: MessageRetrieveResponseItemToolCallFunction
    """The arguments and name for the function"""

    type: Optional[str] = None


class MessageRetrieveResponseItem(BaseModel):
    role: Literal["assistant", "user", "tool", "function", "system"]
    """The role of the participant."""

    id: Optional[str] = None
    """The human-friendly ID of the Message"""

    agent_id: Optional[str] = None
    """The unique identifier of the agent."""

    created_at: Optional[datetime] = None
    """The time the message was created."""

    model: Optional[str] = None
    """The model used to make the function call."""

    name: Optional[str] = None
    """The name of the participant."""

    text: Optional[str] = None
    """The text of the message."""

    tool_call_id: Optional[str] = None
    """The id of the tool call."""

    tool_calls: Optional[List[MessageRetrieveResponseItemToolCall]] = None
    """The list of tool calls requested."""

    user_id: Optional[str] = None
    """The unique identifier of the user."""


MessageRetrieveResponse: TypeAlias = List[MessageRetrieveResponseItem]
