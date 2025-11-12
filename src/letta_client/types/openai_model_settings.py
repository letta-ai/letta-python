# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_response_format import TextResponseFormat
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat

__all__ = ["OpenAIModelSettings", "Reasoning", "ResponseFormat"]


class Reasoning(BaseModel):
    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] = None
    """The reasoning effort to use when generating text reasoning models"""


ResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class OpenAIModelSettings(BaseModel):
    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["openai"]] = None
    """The type of the provider."""

    reasoning: Optional[Reasoning] = None
    """The reasoning configuration for the model."""

    response_format: Optional[ResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""
