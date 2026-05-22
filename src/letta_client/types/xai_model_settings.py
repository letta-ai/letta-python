# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from .text_response_format import TextResponseFormat

from .json_schema_response_format import JsonSchemaResponseFormat

from .json_object_response_format import JsonObjectResponseFormat

from .._utils import PropertyInfo

from typing_extensions import Annotated, TypeAliasType, TypeAlias, Literal

from .._models import BaseModel

__all__ = ["XaiModelSettings", "ResponseFormat"]

ResponseFormat: TypeAlias = Annotated[Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None], PropertyInfo(discriminator="type")]

class XaiModelSettings(BaseModel):
    """xAI model configuration (OpenAI-compatible)."""
    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["xai"]] = None
    """The type of the provider."""

    response_format: Optional[ResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""