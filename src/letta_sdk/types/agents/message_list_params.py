# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    after: Optional[str]
    """Message after which to retrieve the returned messages."""

    assistant_message_tool_kwarg: str
    """The name of the message argument."""

    assistant_message_tool_name: str
    """The name of the designated message tool."""

    before: Optional[str]
    """Message before which to retrieve the returned messages."""

    group_id: Optional[str]
    """Group ID to filter messages by."""

    include_err: Optional[bool]
    """Whether to include error messages and error statuses.

    For debugging purposes only.
    """

    limit: int
    """Maximum number of messages to retrieve."""

    use_assistant_message: bool
    """Whether to use assistant messages"""
