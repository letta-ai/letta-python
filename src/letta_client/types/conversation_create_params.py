# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ConversationCreateParams"]


class ConversationCreateParams(TypedDict, total=False):
    agent_id: Required[str]
    """The agent ID to create a conversation for"""

    isolated_block_labels: Optional[SequenceNotStr[str]]
    """
    List of block labels that should be isolated (conversation-specific) rather than
    shared across conversations. New blocks will be created as copies of the agent's
    blocks with these labels.
    """

    summary: Optional[str]
    """A summary of the conversation."""
