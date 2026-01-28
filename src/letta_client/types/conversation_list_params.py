# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    agent_id: Required[str]
    """The agent ID to list conversations for"""

    after: Optional[str]
    """Cursor for pagination (conversation ID)"""

    limit: int
    """Maximum number of conversations to return"""

    summary_search: Optional[str]
    """Search for text within conversation summaries"""
