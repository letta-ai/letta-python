# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..embedding_model import EmbeddingModel

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["EmbeddingListResponse"]

EmbeddingListResponse: TypeAlias = List[EmbeddingModel]