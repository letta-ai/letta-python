# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel
from ..embedding_config import EmbeddingConfig
from ..vector_db_provider import VectorDBProvider

__all__ = ["FolderListResponse"]


class FolderListResponse(BaseModel):
    """
    (Deprecated: Use Folder) Representation of a source, which is a collection of files and passages.
    """

    id: str
    """The human-friendly ID of the Source"""

    embedding_config: EmbeddingConfig
    """The embedding configuration used by the source."""

    name: str
    """The name of the source."""

    created_at: Optional[datetime] = None
    """The timestamp when the source was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    description: Optional[str] = None
    """The description of the source."""

    instructions: Optional[str] = None
    """Instructions for how to use the source."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    metadata: Optional[Dict[str, object]] = None
    """Metadata associated with the source."""

    updated_at: Optional[datetime] = None
    """The timestamp when the source was last updated."""

    vector_db_provider: Optional[VectorDBProvider] = None
    """The vector database provider used for this source's passages"""
