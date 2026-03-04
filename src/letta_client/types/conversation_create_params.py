# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .xai_model_settings_param import XaiModelSettingsParam
from .groq_model_settings_param import GroqModelSettingsParam
from .azure_model_settings_param import AzureModelSettingsParam
from .text_response_format_param import TextResponseFormatParam
from .openai_model_settings_param import OpenAIModelSettingsParam
from .bedrock_model_settings_param import BedrockModelSettingsParam
from .deepseek_model_settings_param import DeepseekModelSettingsParam
from .together_model_settings_param import TogetherModelSettingsParam
from .anthropic_model_settings_param import AnthropicModelSettingsParam
from .google_ai_model_settings_param import GoogleAIModelSettingsParam
from .json_object_response_format_param import JsonObjectResponseFormatParam
from .json_schema_response_format_param import JsonSchemaResponseFormatParam
from .google_vertex_model_settings_param import GoogleVertexModelSettingsParam

__all__ = [
    "ConversationCreateParams",
    "ModelSettings",
    "ModelSettingsZaiModelSettings",
    "ModelSettingsZaiModelSettingsResponseFormat",
    "ModelSettingsZaiModelSettingsThinking",
    "ModelSettingsOpenRouterModelSettings",
    "ModelSettingsOpenRouterModelSettingsResponseFormat",
    "ModelSettingsChatGptoAuthModelSettings",
    "ModelSettingsChatGptoAuthModelSettingsReasoning",
]


class ConversationCreateParams(TypedDict, total=False):
    agent_id: Required[str]
    """The agent ID to create a conversation for"""

    isolated_block_labels: Optional[SequenceNotStr[str]]
    """
    List of block labels that should be isolated (conversation-specific) rather than
    shared across conversations. New blocks will be created as copies of the agent's
    blocks with these labels.
    """

    model: Optional[str]
    """The model handle for this conversation (overrides agent's model).

    Format: provider/model-name.
    """

    model_settings: Optional[ModelSettings]
    """The model settings for this conversation (overrides agent's model settings)."""

    summary: Optional[str]
    """A summary of the conversation."""


ModelSettingsZaiModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelSettingsZaiModelSettingsThinking(TypedDict, total=False):
    """The thinking configuration for GLM-4.5+ models."""

    clear_thinking: bool
    """If False, preserved thinking is used (recommended for agents)."""

    type: Literal["enabled", "disabled"]
    """Whether thinking is enabled or disabled."""


class ModelSettingsZaiModelSettings(TypedDict, total=False):
    """Z.ai (ZhipuAI) model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["zai"]
    """The type of the provider."""

    response_format: Optional[ModelSettingsZaiModelSettingsResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""

    thinking: ModelSettingsZaiModelSettingsThinking
    """The thinking configuration for GLM-4.5+ models."""


ModelSettingsOpenRouterModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelSettingsOpenRouterModelSettings(TypedDict, total=False):
    """OpenRouter model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["openrouter"]
    """The type of the provider."""

    response_format: Optional[ModelSettingsOpenRouterModelSettingsResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


class ModelSettingsChatGptoAuthModelSettingsReasoning(TypedDict, total=False):
    """The reasoning configuration for the model."""

    reasoning_effort: Literal["none", "low", "medium", "high", "xhigh"]
    """The reasoning effort level for GPT-5.x and o-series models."""


class ModelSettingsChatGptoAuthModelSettings(TypedDict, total=False):
    """ChatGPT OAuth model configuration (uses ChatGPT backend API)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["chatgpt_oauth"]
    """The type of the provider."""

    reasoning: ModelSettingsChatGptoAuthModelSettingsReasoning
    """The reasoning configuration for the model."""

    temperature: float
    """The temperature of the model."""


ModelSettings: TypeAlias = Union[
    OpenAIModelSettingsParam,
    AnthropicModelSettingsParam,
    GoogleAIModelSettingsParam,
    GoogleVertexModelSettingsParam,
    AzureModelSettingsParam,
    XaiModelSettingsParam,
    ModelSettingsZaiModelSettings,
    GroqModelSettingsParam,
    DeepseekModelSettingsParam,
    TogetherModelSettingsParam,
    BedrockModelSettingsParam,
    ModelSettingsOpenRouterModelSettings,
    ModelSettingsChatGptoAuthModelSettings,
]
