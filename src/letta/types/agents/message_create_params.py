# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageCreateParams", "Message"]


class MessageCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The messages to be sent to the agent."""

    assistant_message_tool_kwarg: str
    """The name of the message argument in the designated message tool."""

    assistant_message_tool_name: str
    """The name of the designated message tool."""


class Message(TypedDict, total=False):
    role: Required[Literal["user", "system"]]
    """The role of the participant."""

    text: Required[str]
    """The text of the message."""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the object was created."""

    created_by_id: Optional[str]
    """The id of the user that made this object."""

    last_updated_by_id: Optional[str]
    """The id of the user that made this object."""

    name: Optional[str]
    """The name of the participant."""

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the object was last updated."""
