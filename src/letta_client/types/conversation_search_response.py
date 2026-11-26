# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .conversation import Conversation

__all__ = ["ConversationSearchResponse", "ConversationSearchResponseItem"]


class ConversationSearchResponseItem(BaseModel):
    """Result from a conversation search operation with scoring details."""

    conversation: Conversation
    """The matched conversation."""

    embedded_text: str
    """The embedded text content used for matching."""

    rrf_score: float
    """Reciprocal Rank Fusion combined score."""

    fts_rank: Optional[int] = None
    """Full-text search rank position if FTS was used."""

    vector_rank: Optional[int] = None
    """Vector search rank position if vector search was used."""


ConversationSearchResponse: TypeAlias = List[ConversationSearchResponseItem]
