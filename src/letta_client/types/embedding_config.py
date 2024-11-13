# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EmbeddingConfig"]


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
