# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .text_response_format_param import TextResponseFormatParam
from .json_object_response_format_param import JsonObjectResponseFormatParam
from .json_schema_response_format_param import JsonSchemaResponseFormatParam

__all__ = ["AnthropicModelSettingsParam", "OutputFormat", "Thinking"]

OutputFormat: TypeAlias = Union[TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam]


class Thinking(TypedDict, total=False):
    budget_tokens: int
    """The maximum number of tokens the model can use for extended thinking."""

    type: Literal["enabled", "disabled"]
    """The type of thinking to use."""


class AnthropicModelSettingsParam(TypedDict, total=False):
    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    output_format: Optional[OutputFormat]
    """The structured output format for the model."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["anthropic"]
    """The type of the provider."""

    temperature: float
    """The temperature of the model."""

    thinking: Thinking
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]]
    """Soft control for how verbose model output should be, used for GPT-5 models."""
