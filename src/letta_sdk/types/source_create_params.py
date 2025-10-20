# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .embedding_config_param import EmbeddingConfigParam

__all__ = ["SourceCreateParams"]


class SourceCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the source."""

    description: Optional[str]
    """The description of the source."""

    embedding: Optional[str]
    """The handle for the embedding config used by the source."""

    embedding_chunk_size: Optional[int]
    """The chunk size of the embedding."""

    embedding_config: Optional[EmbeddingConfigParam]
    """Configuration for embedding model connection and processing parameters."""

    instructions: Optional[str]
    """Instructions for how to use the source."""

    metadata: Optional[Dict[str, object]]
    """Metadata associated with the source."""
