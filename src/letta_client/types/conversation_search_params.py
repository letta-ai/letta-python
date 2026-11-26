# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConversationSearchParams"]


class ConversationSearchParams(TypedDict, total=False):
    query: Required[str]
    """Text query for searching conversation summaries or generated descriptions."""

    agent_id: Optional[str]
    """Filter conversations by agent ID."""

    archive_status: Literal["unarchived", "archived", "all"]
    """
    Whether to search unarchived conversations only, archived conversations only, or
    all conversations.
    """

    limit: int
    """Maximum number of results to return."""

    search_mode: Literal["vector", "fts", "hybrid"]
    """Search mode to use."""

    search_target: Literal["summary", "description"]
    """
    Which conversation text field to search: the user-facing summary/title or the
    generated conversation description.
    """
