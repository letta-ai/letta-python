# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .provider_type import ProviderType
from .provider_category import ProviderCategory
from .text_response_format import TextResponseFormat
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat

__all__ = ["Model", "ResponseFormat"]

ResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class Model(BaseModel):
    context_window: int
    """Deprecated: Use 'max_context_window' field instead.

    The context window size for the model.
    """

    max_context_window: int
    """The maximum context window for the model"""

    model: str
    """Deprecated: Use 'name' field instead. LLM model name."""

    api_model_endpoint_type: Literal[
        "openai",
        "anthropic",
        "google_ai",
        "google_vertex",
        "azure",
        "groq",
        "ollama",
        "webui",
        "webui-legacy",
        "lmstudio",
        "lmstudio-legacy",
        "lmstudio-chatcompletions",
        "llamacpp",
        "koboldcpp",
        "vllm",
        "hugging-face",
        "mistral",
        "together",
        "bedrock",
        "deepseek",
        "xai",
        "zai",
    ] = FieldInfo(alias="model_endpoint_type")
    """Deprecated: Use 'provider_type' field instead. The endpoint type for the model."""

    name: str
    """The actual model name used by the provider"""

    provider_type: ProviderType
    """The type of the provider"""

    compatibility_type: Optional[Literal["gguf", "mlx"]] = None
    """Deprecated: The framework compatibility type for the model."""

    display_name: Optional[str] = None
    """A human-friendly display name for the model."""

    effort: Optional[Literal["low", "medium", "high"]] = None
    """The effort level for Anthropic Opus 4.5 model (controls token spending).

    Not setting this gives similar performance to 'high'.
    """

    enable_reasoner: Optional[bool] = None
    """
    Deprecated: Whether or not the model should use extended thinking if it is a
    'reasoning' style model.
    """

    frequency_penalty: Optional[float] = None
    """
    Deprecated: Positive values penalize new tokens based on their existing
    frequency in the text so far.
    """

    handle: Optional[str] = None
    """The handle for this config, in the format provider/model-name."""

    max_reasoning_tokens: Optional[int] = None
    """Deprecated: Configurable thinking budget for extended thinking."""

    max_tokens: Optional[int] = None
    """Deprecated: The maximum number of tokens to generate."""

    api_model_endpoint: Optional[str] = FieldInfo(alias="model_endpoint", default=None)
    """Deprecated: The endpoint for the model."""

    api_model_type: Optional[Literal["llm"]] = FieldInfo(alias="model_type", default=None)
    """Type of model (llm or embedding)"""

    api_model_wrapper: Optional[str] = FieldInfo(alias="model_wrapper", default=None)
    """Deprecated: The wrapper for the model."""

    parallel_tool_calls: Optional[bool] = None
    """Deprecated: If set to True, enables parallel tool calling."""

    provider_category: Optional[ProviderCategory] = None
    """Deprecated: The provider category for the model."""

    provider_name: Optional[str] = None
    """The provider name for the model."""

    put_inner_thoughts_in_kwargs: Optional[bool] = None
    """Deprecated: Puts 'inner_thoughts' as a kwarg in the function call."""

    reasoning_effort: Optional[Literal["none", "minimal", "low", "medium", "high", "xhigh"]] = None
    """Deprecated: The reasoning effort to use when generating text reasoning models."""

    response_format: Optional[ResponseFormat] = None
    """The response format for the model's output.

    Supports text, json_object, and json_schema (structured outputs). Can be set via
    model_settings.
    """

    strict: Optional[bool] = None
    """Enable strict mode for tool calling.

    When true, tool schemas include strict: true and additionalProperties: false,
    guaranteeing tool outputs match JSON schemas.
    """

    temperature: Optional[float] = None
    """Deprecated: The temperature to use when generating text with the model."""

    tier: Optional[str] = None
    """Deprecated: The cost tier for the model (cloud only)."""

    verbosity: Optional[Literal["low", "medium", "high"]] = None
    """Deprecated: Soft control for how verbose model output should be."""
