# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .text_response_format_param import TextResponseFormatParam
from .json_object_response_format_param import JsonObjectResponseFormatParam
from .json_schema_response_format_param import JsonSchemaResponseFormatParam

__all__ = ["GoogleAIModelSettingsParam", "ResponseSchema", "ThinkingConfig"]

ResponseSchema: TypeAlias = Union[TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam]


class ThinkingConfig(TypedDict, total=False):
    include_thoughts: bool
    """Whether to include thoughts in the model's response."""

    thinking_budget: int
    """The thinking budget for the model."""


class GoogleAIModelSettingsParam(TypedDict, total=False):
    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["google_ai"]
    """The type of the provider."""

    response_schema: Optional[ResponseSchema]
    """The response schema for the model."""

    temperature: float
    """The temperature of the model."""

    thinking_config: ThinkingConfig
    """The thinking configuration for the model."""
