# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageCreateParams", "Message"]


class MessageCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The messages to be sent to the agent."""

    assistant_message_tool_kwarg: str
    """The name of the message argument in the designated message tool."""

    assistant_message_tool_name: str
    """The name of the designated message tool."""

    user_id: str


class Message(TypedDict, total=False):
    role: Required[Literal["user", "system"]]
    """The role of the participant."""

    text: Required[str]
    """The text of the message."""

    name: Optional[str]
    """The name of the participant."""
