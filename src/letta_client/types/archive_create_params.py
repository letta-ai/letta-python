# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .embedding_config_param import EmbeddingConfigParam

__all__ = ["ArchiveCreateParams"]


class ArchiveCreateParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    embedding: Optional[str]
    """Embedding model handle for the archive"""

    embedding_config: Optional[EmbeddingConfigParam]
    """Configuration for embedding model connection and processing parameters."""
