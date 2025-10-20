# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .embedding_config import EmbeddingConfig

__all__ = ["Passage"]


class Passage(BaseModel):
    embedding: Optional[List[float]] = None
    """The embedding of the passage."""

    embedding_config: Optional[EmbeddingConfig] = None
    """Configuration for embedding model connection and processing parameters."""

    text: str
    """The text of the passage."""

    id: Optional[str] = None
    """The human-friendly ID of the Passage"""

    archive_id: Optional[str] = None
    """The unique identifier of the archive containing this passage."""

    created_at: Optional[datetime] = None
    """The creation date of the passage."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    file_id: Optional[str] = None
    """The unique identifier of the file associated with the passage."""

    file_name: Optional[str] = None
    """The name of the file (only for source passages)."""

    is_deleted: Optional[bool] = None
    """Whether this passage is deleted or not."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    metadata: Optional[Dict[str, object]] = None
    """The metadata of the passage."""

    source_id: Optional[str] = None
    """The data source of the passage."""

    tags: Optional[List[str]] = None
    """Tags associated with this passage."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
