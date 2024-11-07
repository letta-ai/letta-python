# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .llm_config import LlmConfig

__all__ = ["ModelListResponse"]

ModelListResponse: TypeAlias = List[LlmConfig]
