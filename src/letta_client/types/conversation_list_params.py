# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    after: Optional[str]
    """Cursor for pagination (conversation ID)"""

    agent_id: Optional[str]
    """
    The agent ID to list conversations for (optional - returns all conversations if
    not provided)
    """

    limit: int
    """Maximum number of conversations to return"""

    order: Literal["asc", "desc"]
    """Sort order for conversations. 'asc' for oldest first, 'desc' for newest first"""

    order_by: Literal["created_at", "last_run_completion"]
    """Field to sort by"""

    summary_search: Optional[str]
    """Search for text within conversation summaries"""
