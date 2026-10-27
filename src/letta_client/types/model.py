# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .provider_type import ProviderType
from .provider_category import ProviderCategory
from .text_response_format import TextResponseFormat
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat

__all__ = ["Model", "ReasoningCapabilities", "ResponseFormat"]


class ReasoningCapabilities(BaseModel):
    """Provider-reported reasoning capabilities for a model."""

    mandatory: bool
    """Whether reasoning is mandatory for this model."""

    default_effort: Optional[str] = None
    """The provider's default effort when reasoning is enabled."""

    default_enabled: Optional[bool] = None
    """Whether the provider enables reasoning by default."""

    supported_efforts: Optional[List[str]] = None
    """Reasoning effort levels accepted by the provider for this model.

    Null means all gateway-supported effort levels are accepted.
    """

    supports_max_tokens: Optional[bool] = None
    """Whether the provider accepts an explicit reasoning token budget for this model."""


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
        "baseten",
        "minimax",
        "moonshot",
        "moonshot_coding",
        "mistral",
        "together",
        "bedrock",
        "deepseek",
        "xai",
        "zai",
        "zai_coding",
        "openrouter",
        "chatgpt_oauth",
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

    effort: Optional[Literal["low", "medium", "high", "xhigh", "max"]] = None
    """The effort level for Anthropic models that support it (Opus 4.5+).

    Controls token spending and thinking behavior. Not setting this gives similar
    performance to 'high'.
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

    reasoning_capabilities: Optional[ReasoningCapabilities] = None
    """Provider-reported reasoning capabilities for a model."""

    reasoning_effort: Optional[Literal["none", "minimal", "low", "medium", "high", "xhigh", "max"]] = None
    """Deprecated: The reasoning effort to use when generating text reasoning models.

    'max' is supported only by GPT-5.6 models.
    """

    response_format: Optional[ResponseFormat] = None
    """The response format for the model's output.

    Supports text, json_object, and json_schema (structured outputs). Can be set via
    model_settings.
    """

    return_logprobs: Optional[bool] = None
    """Whether to return log probabilities of the output tokens.

    Useful for RL training.
    """

    return_token_ids: Optional[bool] = None
    """Whether to return token IDs for all LLM generations via SGLang native endpoint.

    Required for multi-turn RL training with loss masking. Only works with SGLang
    provider.
    """

    strict: Optional[bool] = None
    """Enable strict mode for tool calling.

    When true, tool schemas include strict: true and additionalProperties: false,
    guaranteeing tool outputs match JSON schemas.
    """

    supports_structured_outputs: Optional[bool] = None
    """Whether this model supports request-scoped structured outputs."""

    temperature: Optional[float] = None
    """Deprecated: The temperature to use when generating text with the model."""

    tier: Optional[str] = None
    """Deprecated: The cost tier for the model (cloud only)."""

    tool_call_parser: Optional[str] = None
    """SGLang tool call parser name (e.g.

    'glm47', 'qwen25', 'hermes'). Used by the SGLang native adapter to parse tool
    calls from raw model output.
    """

    top_logprobs: Optional[int] = None
    """Number of most likely tokens to return at each position (0-20).

    Requires return_logprobs=True.
    """

    verbosity: Optional[Literal["low", "medium", "high"]] = None
    """Deprecated: Soft control for how verbose model output should be."""
