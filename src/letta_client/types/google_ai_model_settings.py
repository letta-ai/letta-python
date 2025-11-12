# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_response_format import TextResponseFormat
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat

__all__ = ["GoogleAIModelSettings", "ResponseSchema", "ThinkingConfig"]

ResponseSchema: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ThinkingConfig(BaseModel):
    include_thoughts: Optional[bool] = None
    """Whether to include thoughts in the model's response."""

    thinking_budget: Optional[int] = None
    """The thinking budget for the model."""


class GoogleAIModelSettings(BaseModel):
    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["google_ai"]] = None
    """The type of the provider."""

    response_schema: Optional[ResponseSchema] = None
    """The response schema for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking_config: Optional[ThinkingConfig] = None
    """The thinking configuration for the model."""
