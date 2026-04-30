# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

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
    "ConversationRecompileParams",
    "CompactionSettings",
    "CompactionSettingsModelSettings",
    "CompactionSettingsModelSettingsSgLangModelSettings",
    "CompactionSettingsModelSettingsSgLangModelSettingsReasoning",
    "CompactionSettingsModelSettingsSgLangModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsMoonshotModelSettings",
    "CompactionSettingsModelSettingsMoonshotModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsZaiModelSettings",
    "CompactionSettingsModelSettingsZaiModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsZaiModelSettingsThinking",
    "CompactionSettingsModelSettingsMoonshotCodingModelSettings",
    "CompactionSettingsModelSettingsMoonshotCodingModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsMoonshotCodingModelSettingsThinking",
    "CompactionSettingsModelSettingsBasetenModelSettings",
    "CompactionSettingsModelSettingsOpenRouterModelSettings",
    "CompactionSettingsModelSettingsOpenRouterModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsChatGptoAuthModelSettings",
    "CompactionSettingsModelSettingsChatGptoAuthModelSettingsReasoning",
]


class ConversationRecompileParams(TypedDict, total=False):
    dry_run: bool
    """If True, do not persist changes; still returns the compiled system prompt."""

    agent_id: Optional[str]
    """Agent ID for agent-direct mode with 'default' conversation.

    Use with conversation_id='default' in the URL path.
    """

    compaction_settings: Optional[CompactionSettings]
    """Configuration for conversation compaction / summarization.

    Per-model settings (temperature, max tokens, etc.) are derived from the default
    configuration for that handle.
    """


class CompactionSettingsModelSettingsSgLangModelSettingsReasoning(TypedDict, total=False):
    """The reasoning configuration for the model."""

    reasoning_effort: Literal["none", "minimal", "low", "medium", "high", "xhigh"]
    """The reasoning effort to use when generating text reasoning models"""


CompactionSettingsModelSettingsSgLangModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class CompactionSettingsModelSettingsSgLangModelSettings(TypedDict, total=False):
    """
    SGLang model configuration (OpenAI-compatible runtime with SGLang-specific parsing).
    """

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["sglang"]
    """The type of the provider."""

    reasoning: CompactionSettingsModelSettingsSgLangModelSettingsReasoning
    """The reasoning configuration for the model."""

    response_format: Optional[CompactionSettingsModelSettingsSgLangModelSettingsResponseFormat]
    """The response format for the model."""

    strict: bool
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: float
    """The temperature of the model."""

    tool_call_parser: Optional[str]
    """SGLang tool call parser name (for example 'glm47', 'qwen25', or 'hermes')."""


CompactionSettingsModelSettingsMoonshotModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class CompactionSettingsModelSettingsMoonshotModelSettings(TypedDict, total=False):
    """Moonshot/Kimi model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["moonshot"]
    """The type of the provider."""

    response_format: Optional[CompactionSettingsModelSettingsMoonshotModelSettingsResponseFormat]
    """The response format for the model."""

    strict: bool
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: float
    """The temperature of the model."""


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


CompactionSettingsModelSettingsMoonshotCodingModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class CompactionSettingsModelSettingsMoonshotCodingModelSettingsThinking(TypedDict, total=False):
    """The thinking configuration for the model."""

    budget_tokens: int
    """The maximum number of tokens the model can use for extended thinking."""

    type: Literal["enabled", "disabled"]
    """The type of thinking to use."""


class CompactionSettingsModelSettingsMoonshotCodingModelSettings(TypedDict, total=False):
    """Kimi Code model configuration (Anthropic-compatible)."""

    effort: Optional[Literal["low", "medium", "high", "xhigh", "max"]]
    """Effort level for supported Anthropic models (controls token spending).

    'xhigh' and 'max' are available on Opus 4.6+. Not setting this gives similar
    performance to 'high'.
    """

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["moonshot_coding"]
    """The type of the provider."""

    response_format: Optional[CompactionSettingsModelSettingsMoonshotCodingModelSettingsResponseFormat]
    """The response format for the model."""

    strict: bool
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: float
    """The temperature of the model."""

    thinking: CompactionSettingsModelSettingsMoonshotCodingModelSettingsThinking
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]]
    """Soft control for how verbose model output should be, used for GPT-5 models."""


class CompactionSettingsModelSettingsBasetenModelSettings(TypedDict, total=False):
    """Baseten model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["baseten"]
    """The type of the provider."""

    temperature: float
    """The temperature of the model."""


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
    CompactionSettingsModelSettingsSgLangModelSettings,
    AnthropicModelSettingsParam,
    GoogleAIModelSettingsParam,
    GoogleVertexModelSettingsParam,
    AzureModelSettingsParam,
    XaiModelSettingsParam,
    CompactionSettingsModelSettingsMoonshotModelSettings,
    CompactionSettingsModelSettingsZaiModelSettings,
    CompactionSettingsModelSettingsMoonshotCodingModelSettings,
    GroqModelSettingsParam,
    DeepseekModelSettingsParam,
    TogetherModelSettingsParam,
    BedrockModelSettingsParam,
    CompactionSettingsModelSettingsBasetenModelSettings,
    CompactionSettingsModelSettingsOpenRouterModelSettings,
    CompactionSettingsModelSettingsChatGptoAuthModelSettings,
]


class CompactionSettings(TypedDict, total=False):
    """Configuration for conversation compaction / summarization.

    Per-model settings (temperature,
    max tokens, etc.) are derived from the default configuration for that handle.
    """

    clip_chars: Optional[int]
    """The maximum length of the summary in characters.

    If none, no clipping is performed.
    """

    mode: Literal["all", "sliding_window", "self_compact_all", "self_compact_sliding_window"]
    """The type of summarization technique use."""

    model: Optional[str]
    """
    Model handle to use for sliding_window/all summarization (format:
    provider/model-name). If None, uses lightweight provider-specific defaults.
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
    sliding window modes).
    """
