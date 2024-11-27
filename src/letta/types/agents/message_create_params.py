# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "MessageCreateParams",
    "MessagesUnionMember0",
    "MessagesUnionMember1",
    "MessagesUnionMember1ToolCall",
    "MessagesUnionMember1ToolCallFunction",
]


class MessageCreateParams(TypedDict, total=False):
    messages: Required[Union[Iterable[MessagesUnionMember0], Iterable[MessagesUnionMember1]]]
    """The messages to be sent to the agent."""

    assistant_message_tool_kwarg: str
    """The name of the message argument in the designated message tool."""

    assistant_message_tool_name: str
    """The name of the designated message tool."""


class MessagesUnionMember0(TypedDict, total=False):
    role: Required[Literal["user", "system"]]
    """The role of the participant."""

    text: Required[str]
    """The text of the message."""

    name: Optional[str]
    """The name of the participant."""


class MessagesUnionMember1ToolCallFunction(TypedDict, total=False):
    arguments: Required[str]
    """The arguments to pass to the function (JSON dump)"""

    name: Required[str]
    """The name of the function to call"""


class MessagesUnionMember1ToolCall(TypedDict, total=False):
    id: Required[str]
    """The ID of the tool call"""

    function: Required[MessagesUnionMember1ToolCallFunction]
    """The arguments and name for the function"""

    type: str


class MessagesUnionMember1(TypedDict, total=False):
    role: Required[Literal["assistant", "user", "tool", "function", "system"]]
    """The role of the participant."""

    id: str
    """The human-friendly ID of the Message"""

    agent_id: Optional[str]
    """The unique identifier of the agent."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time the message was created."""

    model: Optional[str]
    """The model used to make the function call."""

    name: Optional[str]
    """The name of the participant."""

    text: Optional[str]
    """The text of the message."""

    tool_call_id: Optional[str]
    """The id of the tool call."""

    tool_calls: Optional[Iterable[MessagesUnionMember1ToolCall]]
    """The list of tool calls requested."""

    user_id: Optional[str]
    """The unique identifier of the user."""
