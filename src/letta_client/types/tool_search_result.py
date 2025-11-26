# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .tool import Tool
from .._models import BaseModel

__all__ = ["ToolSearchResult"]


class ToolSearchResult(BaseModel):
    combined_score: float
    """Combined relevance score (RRF for hybrid mode)."""

    tool: Tool
    """The matched tool."""

    embedded_text: Optional[str] = None
    """The embedded text content used for matching."""

    fts_rank: Optional[int] = None
    """Full-text search rank position."""

    vector_rank: Optional[int] = None
    """Vector search rank position."""
