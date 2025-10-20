# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    after: Optional[str]
    """Message ID cursor for pagination.

    Returns messages that come after this message ID in the specified sort order
    """

    assistant_message_tool_kwarg: str
    """The name of the message argument."""

    assistant_message_tool_name: str
    """The name of the designated message tool."""

    before: Optional[str]
    """Message ID cursor for pagination.

    Returns messages that come before this message ID in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of messages to retrieve"""

    order: Literal["asc", "desc"]
    """Sort order for messages by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    use_assistant_message: bool
    """Whether to use assistant messages"""
