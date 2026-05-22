# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .text_response_format_param import TextResponseFormatParam
from .json_object_response_format_param import JsonObjectResponseFormatParam
from .json_schema_response_format_param import JsonSchemaResponseFormatParam

__all__ = ["GroqModelSettingsParam", "ResponseFormat"]

ResponseFormat: TypeAlias = Union[TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam]


class GroqModelSettingsParam(TypedDict, total=False):
    """Groq model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["groq"]
    """The type of the provider."""

    response_format: Optional[ResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""
