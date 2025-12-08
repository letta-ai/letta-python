# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .embedding_config import EmbeddingConfig
from .vector_db_provider import VectorDBProvider

__all__ = ["Archive"]


class Archive(BaseModel):
    """
    Representation of an archive - a collection of archival passages that can be shared between agents.
    """

    id: str
    """The human-friendly ID of the Archive"""

    created_at: datetime
    """The creation date of the archive"""

    embedding_config: EmbeddingConfig
    """Embedding configuration for passages in this archive"""

    name: str
    """The name of the archive"""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    description: Optional[str] = None
    """A description of the archive"""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata"""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""

    vector_db_provider: Optional[VectorDBProvider] = None
    """The vector database provider used for this archive's passages"""
