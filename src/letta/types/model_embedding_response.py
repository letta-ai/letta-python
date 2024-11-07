# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .embeddingconfig import Embeddingconfig

__all__ = ["ModelEmbeddingResponse"]

ModelEmbeddingResponse: TypeAlias = List[Embeddingconfig]
