# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..embedding_model import EmbeddingModel

__all__ = ["EmbeddingListResponse"]

EmbeddingListResponse: TypeAlias = List[EmbeddingModel]
