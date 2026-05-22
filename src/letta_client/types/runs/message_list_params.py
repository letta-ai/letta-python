# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional

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

    limit: Optional[int]
    """Maximum number of messages to return"""

    order: Literal["asc", "desc"]
    """Sort order for messages by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""