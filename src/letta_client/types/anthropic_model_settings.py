# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_response_format import TextResponseFormat
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat

__all__ = ["AnthropicModelSettings", "ResponseFormat", "Thinking"]

ResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class Thinking(BaseModel):
    """The thinking configuration for the model."""

    budget_tokens: Optional[int] = None
    """The maximum number of tokens the model can use for extended thinking."""

    type: Optional[Literal["enabled", "disabled"]] = None
    """The type of thinking to use."""


class AnthropicModelSettings(BaseModel):
    effort: Optional[Literal["low", "medium", "high"]] = None
    """Effort level for Opus 4.5 model (controls token conservation).

    Not setting this gives similar performance to 'high'.
    """

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["anthropic"]] = None
    """The type of the provider."""

    response_format: Optional[ResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking: Optional[Thinking] = None
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]] = None
    """Soft control for how verbose model output should be, used for GPT-5 models."""
