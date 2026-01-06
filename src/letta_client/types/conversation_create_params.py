# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConversationCreateParams"]


class ConversationCreateParams(TypedDict, total=False):
    agent_id: Required[str]
    """The agent ID to create a conversation for"""

    summary: Optional[str]
    """A summary of the conversation."""
