# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .embedding_config_param import EmbeddingConfigParam

__all__ = ["FolderModifyParams"]


class FolderModifyParams(TypedDict, total=False):
    description: Optional[str]
    """The description of the source."""

    embedding_config: Optional[EmbeddingConfigParam]
    """Configuration for embedding model connection and processing parameters."""

    instructions: Optional[str]
    """Instructions for how to use the source."""

    metadata: Optional[Dict[str, object]]
    """Metadata associated with the source."""

    name: Optional[str]
    """The name of the source."""
