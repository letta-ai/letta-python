# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_response_format import TextResponseFormat
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat

__all__ = ["AnthropicModelSettings", "OutputFormat", "Thinking"]

OutputFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class Thinking(BaseModel):
    budget_tokens: Optional[int] = None
    """The maximum number of tokens the model can use for extended thinking."""

    type: Optional[Literal["enabled", "disabled"]] = None
    """The type of thinking to use."""


class AnthropicModelSettings(BaseModel):
    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    output_format: Optional[OutputFormat] = None
    """The structured output format for the model."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["anthropic"]] = None
    """The type of the provider."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking: Optional[Thinking] = None
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]] = None
    """Soft control for how verbose model output should be, used for GPT-5 models."""
