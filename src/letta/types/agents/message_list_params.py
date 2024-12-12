# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    assistant_message_tool_kwarg: str
    """The name of the message argument in the designated message tool."""

    assistant_message_tool_name: str
    """The name of the designated message tool."""

    before: Optional[str]
    """Message before which to retrieve the returned messages."""

    limit: int
    """Maximum number of messages to retrieve."""

    msg_object: bool
    """If true, returns Message objects. If false, return LettaMessage objects."""
