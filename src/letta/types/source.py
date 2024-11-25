# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Source", "EmbeddingConfig"]


class EmbeddingConfig(BaseModel):
    embedding_dim: int
    """The dimension of the embedding."""

    embedding_endpoint_type: str
    """The endpoint type for the model."""

    embedding_model: str
    """The model for the embedding."""

    azure_deployment: Optional[str] = None
    """The Azure deployment for the model."""

    azure_endpoint: Optional[str] = None
    """The Azure endpoint for the model."""

    azure_version: Optional[str] = None
    """The Azure version for the model."""

    embedding_chunk_size: Optional[int] = None
    """The chunk size of the embedding."""

    embedding_endpoint: Optional[str] = None
    """The endpoint for the model (`None` if local)."""


class Source(BaseModel):
    embedding_config: EmbeddingConfig
    """The embedding configuration used by the source."""

    name: str
    """The name of the source."""

    id: Optional[str] = None
    """The human-friendly ID of the Source"""

    created_at: Optional[datetime] = None
    """The timestamp when the source was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    description: Optional[str] = None
    """The description of the source."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """Metadata associated with the source."""

    organization_id: Optional[str] = None
    """The ID of the organization that created the source."""

    updated_at: Optional[datetime] = None
    """The timestamp when the source was last updated."""
