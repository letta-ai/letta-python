# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .embedding_config_param import EmbeddingConfigParam

__all__ = ["ArchiveCreateParams"]


class ArchiveCreateParams(TypedDict, total=False):
    embedding_config: Required[EmbeddingConfigParam]
    """Embedding configuration for the archive"""

    name: Required[str]

    description: Optional[str]
