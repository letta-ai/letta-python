# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .text_response_format_param import TextResponseFormatParam
from .json_object_response_format_param import JsonObjectResponseFormatParam
from .json_schema_response_format_param import JsonSchemaResponseFormatParam

__all__ = ["OpenAIModelSettingsParam", "Reasoning", "ResponseFormat"]


class Reasoning(TypedDict, total=False):
    reasoning_effort: Literal["none", "minimal", "low", "medium", "high"]
    """The reasoning effort to use when generating text reasoning models"""


ResponseFormat: TypeAlias = Union[TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam]


class OpenAIModelSettingsParam(TypedDict, total=False):
    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["openai"]
    """The type of the provider."""

    reasoning: Reasoning
    """The reasoning configuration for the model."""

    response_format: Optional[ResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""
