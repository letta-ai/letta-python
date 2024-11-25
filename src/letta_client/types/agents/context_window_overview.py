# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ContextWindowOverview", "Message", "MessageToolCall", "MessageToolCallFunction"]


class MessageToolCallFunction(BaseModel):
    arguments: str
    """The arguments to pass to the function (JSON dump)"""

    name: str
    """The name of the function to call"""


class MessageToolCall(BaseModel):
    id: str
    """The ID of the tool call"""

    function: MessageToolCallFunction
    """The arguments and name for the function"""

    type: Optional[str] = None


class Message(BaseModel):
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

    tool_calls: Optional[List[MessageToolCall]] = None
    """The list of tool calls requested."""

    user_id: Optional[str] = None
    """The unique identifier of the user."""


class ContextWindowOverview(BaseModel):
    context_window_size_current: int
    """The current number of tokens in the context window."""

    context_window_size_max: int
    """The maximum amount of tokens the context window can hold."""

    core_memory: str
    """The content of the core memory."""

    messages: List[Message]
    """The messages in the context window."""

    num_archival_memory: int
    """The number of messages in the archival memory."""

    num_messages: int
    """The number of messages in the context window."""

    num_recall_memory: int
    """The number of messages in the recall memory."""

    num_tokens_core_memory: int
    """The number of tokens in the core memory."""

    num_tokens_external_memory_summary: int
    """
    The number of tokens in the external memory summary (archival + recall
    metadata).
    """

    num_tokens_messages: int
    """The number of tokens in the messages list."""

    num_tokens_summary_memory: int
    """The number of tokens in the summary memory."""

    num_tokens_system: int
    """The number of tokens in the system prompt."""

    system_prompt: str
    """The content of the system prompt."""

    summary_memory: Optional[str] = None
    """The content of the summary memory."""
