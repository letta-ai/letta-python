# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    after: Optional[str]
    """Message ID cursor for pagination.

    Returns messages that come after this message ID in the conversation
    """

    before: Optional[str]
    """Message ID cursor for pagination.

    Returns messages that come before this message ID in the conversation
    """

    limit: Optional[int]
    """Maximum number of messages to return"""
