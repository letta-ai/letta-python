# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .xai_model_settings import XaiModelSettings
from .groq_model_settings import GroqModelSettings
from .azure_model_settings import AzureModelSettings
from .text_response_format import TextResponseFormat
from .openai_model_settings import OpenAIModelSettings
from .bedrock_model_settings import BedrockModelSettings
from .deepseek_model_settings import DeepseekModelSettings
from .together_model_settings import TogetherModelSettings
from .anthropic_model_settings import AnthropicModelSettings
from .google_ai_model_settings import GoogleAIModelSettings
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat
from .google_vertex_model_settings import GoogleVertexModelSettings

__all__ = [
    "Conversation",
    "ModelSettings",
    "ModelSettingsSgLangModelSettings",
    "ModelSettingsSgLangModelSettingsReasoning",
    "ModelSettingsSgLangModelSettingsResponseFormat",
    "ModelSettingsMoonshotModelSettings",
    "ModelSettingsMoonshotModelSettingsResponseFormat",
    "ModelSettingsZaiModelSettings",
    "ModelSettingsZaiModelSettingsResponseFormat",
    "ModelSettingsZaiModelSettingsThinking",
    "ModelSettingsMoonshotCodingModelSettings",
    "ModelSettingsMoonshotCodingModelSettingsResponseFormat",
    "ModelSettingsMoonshotCodingModelSettingsThinking",
    "ModelSettingsBasetenModelSettings",
    "ModelSettingsOpenRouterModelSettings",
    "ModelSettingsOpenRouterModelSettingsResponseFormat",
    "ModelSettingsChatGptoAuthModelSettings",
    "ModelSettingsChatGptoAuthModelSettingsReasoning",
]


class ModelSettingsSgLangModelSettingsReasoning(BaseModel):
    """The reasoning configuration for the model."""

    reasoning_effort: Optional[Literal["none", "minimal", "low", "medium", "high", "xhigh"]] = None
    """The reasoning effort to use when generating text reasoning models"""


ModelSettingsSgLangModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelSettingsSgLangModelSettings(BaseModel):
    """
    SGLang model configuration (OpenAI-compatible runtime with SGLang-specific parsing).
    """

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["sglang"]] = None
    """The type of the provider."""

    reasoning: Optional[ModelSettingsSgLangModelSettingsReasoning] = None
    """The reasoning configuration for the model."""

    response_format: Optional[ModelSettingsSgLangModelSettingsResponseFormat] = None
    """The response format for the model."""

    strict: Optional[bool] = None
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: Optional[float] = None
    """The temperature of the model."""

    tool_call_parser: Optional[str] = None
    """SGLang tool call parser name (for example 'glm47', 'qwen25', or 'hermes')."""


ModelSettingsMoonshotModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelSettingsMoonshotModelSettings(BaseModel):
    """Moonshot/Kimi model configuration (OpenAI-compatible)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["moonshot"]] = None
    """The type of the provider."""

    response_format: Optional[ModelSettingsMoonshotModelSettingsResponseFormat] = None
    """The response format for the model."""

    strict: Optional[bool] = None
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelSettingsZaiModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelSettingsZaiModelSettingsThinking(BaseModel):
    """The thinking configuration for GLM-4.5+ models."""

    clear_thinking: Optional[bool] = None
    """If False, preserved thinking is used (recommended for agents)."""

    type: Optional[Literal["enabled", "disabled"]] = None
    """Whether thinking is enabled or disabled."""


class ModelSettingsZaiModelSettings(BaseModel):
    """Z.ai (ZhipuAI) model configuration (OpenAI-compatible)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["zai"]] = None
    """The type of the provider."""

    response_format: Optional[ModelSettingsZaiModelSettingsResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking: Optional[ModelSettingsZaiModelSettingsThinking] = None
    """The thinking configuration for GLM-4.5+ models."""


ModelSettingsMoonshotCodingModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelSettingsMoonshotCodingModelSettingsThinking(BaseModel):
    """The thinking configuration for the model."""

    budget_tokens: Optional[int] = None
    """The maximum number of tokens the model can use for extended thinking."""

    type: Optional[Literal["enabled", "disabled"]] = None
    """The type of thinking to use."""


class ModelSettingsMoonshotCodingModelSettings(BaseModel):
    """Kimi Code model configuration (Anthropic-compatible)."""

    effort: Optional[Literal["low", "medium", "high", "xhigh", "max"]] = None
    """Effort level for supported Anthropic models (controls token spending).

    'xhigh' and 'max' are available on Opus 4.6+. Not setting this gives similar
    performance to 'high'.
    """

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["moonshot_coding"]] = None
    """The type of the provider."""

    response_format: Optional[ModelSettingsMoonshotCodingModelSettingsResponseFormat] = None
    """The response format for the model."""

    strict: Optional[bool] = None
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking: Optional[ModelSettingsMoonshotCodingModelSettingsThinking] = None
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]] = None
    """Soft control for how verbose model output should be, used for GPT-5 models."""


class ModelSettingsBasetenModelSettings(BaseModel):
    """Baseten model configuration (OpenAI-compatible)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["baseten"]] = None
    """The type of the provider."""

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelSettingsOpenRouterModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelSettingsOpenRouterModelSettings(BaseModel):
    """OpenRouter model configuration (OpenAI-compatible)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["openrouter"]] = None
    """The type of the provider."""

    response_format: Optional[ModelSettingsOpenRouterModelSettingsResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


class ModelSettingsChatGptoAuthModelSettingsReasoning(BaseModel):
    """The reasoning configuration for the model."""

    reasoning_effort: Optional[Literal["none", "low", "medium", "high", "xhigh"]] = None
    """The reasoning effort level for GPT-5.x and o-series models."""


class ModelSettingsChatGptoAuthModelSettings(BaseModel):
    """ChatGPT OAuth model configuration (uses ChatGPT backend API)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["chatgpt_oauth"]] = None
    """The type of the provider."""

    reasoning: Optional[ModelSettingsChatGptoAuthModelSettingsReasoning] = None
    """The reasoning configuration for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelSettings: TypeAlias = Annotated[
    Union[
        OpenAIModelSettings,
        ModelSettingsSgLangModelSettings,
        AnthropicModelSettings,
        GoogleAIModelSettings,
        GoogleVertexModelSettings,
        AzureModelSettings,
        XaiModelSettings,
        ModelSettingsMoonshotModelSettings,
        ModelSettingsZaiModelSettings,
        ModelSettingsMoonshotCodingModelSettings,
        GroqModelSettings,
        DeepseekModelSettings,
        TogetherModelSettings,
        BedrockModelSettings,
        ModelSettingsBasetenModelSettings,
        ModelSettingsOpenRouterModelSettings,
        ModelSettingsChatGptoAuthModelSettings,
        None,
    ],
    PropertyInfo(discriminator="provider_type"),
]


class Conversation(BaseModel):
    """Represents a conversation on an agent for concurrent messaging."""

    id: str
    """The unique identifier of the conversation."""

    agent_id: str
    """The ID of the agent this conversation belongs to."""

    archived: Optional[bool] = None
    """Whether the conversation is archived."""

    archived_at: Optional[datetime] = None
    """Timestamp of when the conversation was archived."""

    context_window_limit: Optional[int] = None
    """
    The context window limit for this conversation (overrides agent's context
    window).
    """

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    in_context_message_ids: Optional[List[str]] = None
    """The IDs of in-context messages for the conversation.

    Null means this field was not retrieved/hydrated for this response.
    """

    last_message_at: Optional[datetime] = None
    """Timestamp of the most recent message request sent to this conversation."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    model: Optional[str] = None
    """The model handle for this conversation (overrides agent's model).

    Format: provider/model-name.
    """

    api_model_settings: Optional[ModelSettings] = FieldInfo(alias="model_settings", default=None)
    """The model settings for this conversation (overrides agent's model settings)."""

    summary: Optional[str] = None
    """A summary of the conversation."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
