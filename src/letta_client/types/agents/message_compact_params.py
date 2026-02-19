# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from ..xai_model_settings_param import XaiModelSettingsParam
from ..groq_model_settings_param import GroqModelSettingsParam
from ..azure_model_settings_param import AzureModelSettingsParam
from ..text_response_format_param import TextResponseFormatParam
from ..openai_model_settings_param import OpenAIModelSettingsParam
from ..bedrock_model_settings_param import BedrockModelSettingsParam
from ..deepseek_model_settings_param import DeepseekModelSettingsParam
from ..together_model_settings_param import TogetherModelSettingsParam
from ..anthropic_model_settings_param import AnthropicModelSettingsParam
from ..google_ai_model_settings_param import GoogleAIModelSettingsParam
from ..json_object_response_format_param import JsonObjectResponseFormatParam
from ..json_schema_response_format_param import JsonSchemaResponseFormatParam
from ..google_vertex_model_settings_param import GoogleVertexModelSettingsParam

__all__ = [
    "MessageCompactParams",
    "CompactionSettings",
    "CompactionSettingsModelSettings",
    "CompactionSettingsModelSettingsZaiModelSettings",
    "CompactionSettingsModelSettingsZaiModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsZaiModelSettingsThinking",
    "CompactionSettingsModelSettingsOpenRouterModelSettings",
    "CompactionSettingsModelSettingsOpenRouterModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsChatGptoAuthModelSettings",
    "CompactionSettingsModelSettingsChatGptoAuthModelSettingsReasoning",
]


class MessageCompactParams(TypedDict, total=False):
    compaction_settings: Optional[CompactionSettings]
    """Configuration for conversation compaction / summarization.

    `model` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. `"openai/gpt-4o-mini"`). Per-model settings (temperature, max
    tokens, etc.) are derived from the default configuration for that handle.
    """


CompactionSettingsModelSettingsZaiModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class CompactionSettingsModelSettingsZaiModelSettingsThinking(TypedDict, total=False):
    """The thinking configuration for GLM-4.5+ models."""

    clear_thinking: bool
    """If False, preserved thinking is used (recommended for agents)."""

    type: Literal["enabled", "disabled"]
    """Whether thinking is enabled or disabled."""


class CompactionSettingsModelSettingsZaiModelSettings(TypedDict, total=False):
    """Z.ai (ZhipuAI) model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["zai"]
    """The type of the provider."""

    response_format: Optional[CompactionSettingsModelSettingsZaiModelSettingsResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""

    thinking: CompactionSettingsModelSettingsZaiModelSettingsThinking
    """The thinking configuration for GLM-4.5+ models."""


CompactionSettingsModelSettingsOpenRouterModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class CompactionSettingsModelSettingsOpenRouterModelSettings(TypedDict, total=False):
    """OpenRouter model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["openrouter"]
    """The type of the provider."""

    response_format: Optional[CompactionSettingsModelSettingsOpenRouterModelSettingsResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


class CompactionSettingsModelSettingsChatGptoAuthModelSettingsReasoning(TypedDict, total=False):
    """The reasoning configuration for the model."""

    reasoning_effort: Literal["none", "low", "medium", "high", "xhigh"]
    """The reasoning effort level for GPT-5.x and o-series models."""


class CompactionSettingsModelSettingsChatGptoAuthModelSettings(TypedDict, total=False):
    """ChatGPT OAuth model configuration (uses ChatGPT backend API)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["chatgpt_oauth"]
    """The type of the provider."""

    reasoning: CompactionSettingsModelSettingsChatGptoAuthModelSettingsReasoning
    """The reasoning configuration for the model."""

    temperature: float
    """The temperature of the model."""


CompactionSettingsModelSettings: TypeAlias = Union[
    OpenAIModelSettingsParam,
    AnthropicModelSettingsParam,
    GoogleAIModelSettingsParam,
    GoogleVertexModelSettingsParam,
    AzureModelSettingsParam,
    XaiModelSettingsParam,
    CompactionSettingsModelSettingsZaiModelSettings,
    GroqModelSettingsParam,
    DeepseekModelSettingsParam,
    TogetherModelSettingsParam,
    BedrockModelSettingsParam,
    CompactionSettingsModelSettingsOpenRouterModelSettings,
    CompactionSettingsModelSettingsChatGptoAuthModelSettings,
]


class CompactionSettings(TypedDict, total=False):
    """Configuration for conversation compaction / summarization.

    ``model`` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. ``"openai/gpt-4o-mini"``). Per-model settings (temperature,
    max tokens, etc.) are derived from the default configuration for that handle.
    """

    clip_chars: Optional[int]
    """The maximum length of the summary in characters.

    If none, no clipping is performed.
    """

    mode: Literal["all", "sliding_window", "self"]
    """The type of summarization technique use."""

    model: Optional[str]
    """Model handle to use for summarization (format: provider/model-name).

    If None, uses lightweight provider-specific defaults.
    """

    model_settings: Optional[CompactionSettingsModelSettings]
    """Optional model settings used to override defaults for the summarizer model."""

    prompt: Optional[str]
    """The prompt to use for summarization. If None, uses mode-specific default."""

    prompt_acknowledgement: bool
    """
    Whether to include an acknowledgement post-prompt (helps prevent non-summary
    outputs).
    """

    sliding_window_percentage: float
    """
    The percentage of the context window to keep post-summarization (only used in
    sliding window mode).
    """
