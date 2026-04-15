# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .agents.message_type import MessageType

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    after: Optional[str]
    """Cursor for pagination (message ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'message-<uuid4>'
    """

    before: Optional[str]
    """Cursor for pagination (message ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'message-<uuid4>'
    """

    conversation_id: Optional[str]
    """Conversation ID to filter messages by"""

    include_return_message_types: Optional[List[MessageType]]
    """Message types to include in response.

    When null, all message types are returned.
    """

    limit: Optional[int]
    """Maximum number of messages to return"""

    order: Literal["asc", "desc"]
    """Sort order for messages by creation time.

    'asc' for oldest first, 'desc' for newest first
    """
