# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .embedding_config import EmbeddingConfig

__all__ = ["Folder"]


class Folder(BaseModel):
    embedding_config: EmbeddingConfig
    """The embedding configuration used by the folder."""

    name: str
    """The name of the folder."""

    id: Optional[str] = None
    """The human-friendly ID of the Source"""

    created_at: Optional[datetime] = None
    """The timestamp when the folder was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    description: Optional[str] = None
    """The description of the folder."""

    instructions: Optional[str] = None
    """Instructions for how to use the folder."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    metadata: Optional[Dict[str, object]] = None
    """Metadata associated with the folder."""

    updated_at: Optional[datetime] = None
    """The timestamp when the folder was last updated."""
