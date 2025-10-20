# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .embedding_config import EmbeddingConfig

__all__ = ["ModelListEmbeddingResponse"]

ModelListEmbeddingResponse: TypeAlias = List[EmbeddingConfig]
