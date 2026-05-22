# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Union

from typing_extensions import Literal, Annotated, TypeAliasType, TypeAlias

from .text_response_format import TextResponseFormat

from .json_schema_response_format import JsonSchemaResponseFormat

from .json_object_response_format import JsonObjectResponseFormat

from .._utils import PropertyInfo

__all__ = ["OpenAIModelSettings", "Reasoning", "ResponseFormat"]

class Reasoning(BaseModel):
    """The reasoning configuration for the model."""
    reasoning_effort: Optional[Literal["none", "minimal", "low", "medium", "high", "xhigh"]] = None
    """The reasoning effort to use when generating text reasoning models"""

ResponseFormat: TypeAlias = Annotated[Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None], PropertyInfo(discriminator="type")]

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

    strict: Optional[bool] = None
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: Optional[float] = None
    """The temperature of the model."""