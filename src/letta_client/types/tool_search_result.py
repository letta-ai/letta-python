# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .tool import Tool

from typing import Optional

__all__ = ["ToolSearchResult"]

class ToolSearchResult(BaseModel):
    """Result from a tool search operation."""
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