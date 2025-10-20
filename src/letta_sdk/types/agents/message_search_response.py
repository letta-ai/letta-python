# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .message import Message
from ..._models import BaseModel

__all__ = ["MessageSearchResponse", "MessageSearchResponseItem"]


class MessageSearchResponseItem(BaseModel):
    embedded_text: str
    """The embedded content (LLM-friendly)"""

    message: Message
    """The raw message object"""

    rrf_score: float
    """Reciprocal Rank Fusion combined score"""

    fts_rank: Optional[int] = None
    """Full-text search rank position if FTS was used"""

    vector_rank: Optional[int] = None
    """Vector search rank position if vector search was used"""


MessageSearchResponse: TypeAlias = List[MessageSearchResponseItem]
