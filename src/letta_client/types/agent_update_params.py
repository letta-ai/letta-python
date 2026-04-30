# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .llm_config_param import LlmConfigParam
from .stop_reason_type import StopReasonType
from .init_tool_rule_param import InitToolRuleParam
from .child_tool_rule_param import ChildToolRuleParam
from .embedding_config_param import EmbeddingConfigParam
from .parent_tool_rule_param import ParentToolRuleParam
from .continue_tool_rule_param import ContinueToolRuleParam
from .terminal_tool_rule_param import TerminalToolRuleParam
from .xai_model_settings_param import XaiModelSettingsParam
from .groq_model_settings_param import GroqModelSettingsParam
from .azure_model_settings_param import AzureModelSettingsParam
from .text_response_format_param import TextResponseFormatParam
from .conditional_tool_rule_param import ConditionalToolRuleParam
from .openai_model_settings_param import OpenAIModelSettingsParam
from .bedrock_model_settings_param import BedrockModelSettingsParam
from .deepseek_model_settings_param import DeepseekModelSettingsParam
from .together_model_settings_param import TogetherModelSettingsParam
from .anthropic_model_settings_param import AnthropicModelSettingsParam
from .google_ai_model_settings_param import GoogleAIModelSettingsParam
from .json_object_response_format_param import JsonObjectResponseFormatParam
from .json_schema_response_format_param import JsonSchemaResponseFormatParam
from .requires_approval_tool_rule_param import RequiresApprovalToolRuleParam
from .google_vertex_model_settings_param import GoogleVertexModelSettingsParam
from .max_count_per_step_tool_rule_param import MaxCountPerStepToolRuleParam
from .required_before_exit_tool_rule_param import RequiredBeforeExitToolRuleParam

__all__ = [
    "AgentUpdateParams",
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
    "ResponseFormat",
    "ToolRule",
]


class AgentUpdateParams(TypedDict, total=False):
    base_template_id: Optional[str]
    """The base template id of the agent."""

    block_ids: Optional[SequenceNotStr[str]]
    """The ids of the blocks used by the agent."""

    compaction_settings: Optional[CompactionSettings]
    """Configuration for conversation compaction / summarization.

    Per-model settings (temperature, max tokens, etc.) are derived from the default
    configuration for that handle.
    """

    context_window_limit: Optional[int]
    """The context window limit used by the agent."""

    description: Optional[str]
    """The description of the agent."""

    embedding: Optional[str]
    """The embedding model handle used by the agent (format: provider/model-name)."""

    embedding_config: Optional[EmbeddingConfigParam]
    """Configuration for embedding model connection and processing parameters."""

    enable_sleeptime: Optional[bool]
    """If set to True, memory management will move to a background agent thread."""

    folder_ids: Optional[SequenceNotStr[str]]
    """The ids of the folders used by the agent."""

    hidden: Optional[bool]
    """If set to True, the agent will be hidden."""

    identity_ids: Optional[SequenceNotStr[str]]
    """The ids of the identities associated with this agent."""

    last_run_completion: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the agent last completed a run."""

    last_run_duration_ms: Optional[int]
    """The duration in milliseconds of the agent's last run."""

    last_stop_reason: Optional[StopReasonType]
    """The stop reason from the agent's last run."""

    llm_config: Optional[LlmConfigParam]
    """Configuration for Language Model (LLM) connection and generation parameters.

    .. deprecated:: LLMConfig is deprecated and should not be used as an input or
    return type in API calls. Use the schemas in letta.schemas.model (ModelSettings,
    OpenAIModelSettings, etc.) instead. For conversion, use the \\__to_model() method
    or Model.\\__from_llm_config() method.
    """

    max_files_open: Optional[int]
    """Maximum number of files that can be open at once for this agent.

    Setting this too high may exceed the context window, which will break the agent.
    """

    max_tokens: Optional[int]
    """Deprecated: Use `model` field to configure max output tokens instead.

    The maximum number of tokens to generate, including reasoning step.
    """

    message_buffer_autoclear: Optional[bool]
    """
    If set to True, the agent will not remember previous messages (though the agent
    will still retain state via core memory blocks and archival/recall memory). Not
    recommended unless you have an advanced use case.
    """

    message_ids: Optional[SequenceNotStr[str]]
    """The ids of the messages in the agent's in-context memory."""

    metadata: Optional[Dict[str, object]]
    """The metadata of the agent."""

    model: Optional[str]
    """The model handle used by the agent (format: provider/model-name)."""

    model_settings: Optional[ModelSettings]
    """The model settings for the agent."""

    name: Optional[str]
    """The name of the agent."""

    parallel_tool_calls: Optional[bool]
    """Deprecated: Use `model_settings` to configure parallel tool calls instead.

    If set to True, enables parallel tool calling.
    """

    per_file_view_window_char_limit: Optional[int]
    """The per-file view window character limit for this agent.

    Setting this too high may exceed the context window, which will break the agent.
    """

    project_id: Optional[str]
    """The id of the project the agent belongs to."""

    reasoning: Optional[bool]
    """Deprecated: Use `model` field to configure reasoning instead.

    Whether to enable reasoning for this agent.
    """

    response_format: Optional[ResponseFormat]
    """Deprecated: Use `model_settings` field to configure response format instead.

    The response format for the agent.
    """

    secrets: Optional[Dict[str, str]]
    """The environment variables for tool execution specific to this agent."""

    source_ids: Optional[SequenceNotStr[str]]
    """Deprecated: Use `folder_ids` field instead.

    The ids of the sources used by the agent.
    """

    system: Optional[str]
    """The system prompt used by the agent."""

    tags: Optional[SequenceNotStr[str]]
    """The tags associated with the agent."""

    template_id: Optional[str]
    """The id of the template the agent belongs to."""

    timezone: Optional[str]
    """The timezone of the agent (IANA format)."""

    tool_exec_environment_variables: Optional[Dict[str, str]]
    """Deprecated: use `secrets` field instead"""

    tool_ids: Optional[SequenceNotStr[str]]
    """The ids of the tools used by the agent."""

    tool_rules: Optional[Iterable[ToolRule]]
    """The tool rules governing the agent."""


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


class ModelSettingsSgLangModelSettingsReasoning(TypedDict, total=False):
    """The reasoning configuration for the model."""

    reasoning_effort: Literal["none", "minimal", "low", "medium", "high", "xhigh"]
    """The reasoning effort to use when generating text reasoning models"""


ModelSettingsSgLangModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelSettingsSgLangModelSettings(TypedDict, total=False):
    """
    SGLang model configuration (OpenAI-compatible runtime with SGLang-specific parsing).
    """

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["sglang"]
    """The type of the provider."""

    reasoning: ModelSettingsSgLangModelSettingsReasoning
    """The reasoning configuration for the model."""

    response_format: Optional[ModelSettingsSgLangModelSettingsResponseFormat]
    """The response format for the model."""

    strict: bool
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: float
    """The temperature of the model."""

    tool_call_parser: Optional[str]
    """SGLang tool call parser name (for example 'glm47', 'qwen25', or 'hermes')."""


ModelSettingsMoonshotModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelSettingsMoonshotModelSettings(TypedDict, total=False):
    """Moonshot/Kimi model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["moonshot"]
    """The type of the provider."""

    response_format: Optional[ModelSettingsMoonshotModelSettingsResponseFormat]
    """The response format for the model."""

    strict: bool
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: float
    """The temperature of the model."""


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


ModelSettingsMoonshotCodingModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelSettingsMoonshotCodingModelSettingsThinking(TypedDict, total=False):
    """The thinking configuration for the model."""

    budget_tokens: int
    """The maximum number of tokens the model can use for extended thinking."""

    type: Literal["enabled", "disabled"]
    """The type of thinking to use."""


class ModelSettingsMoonshotCodingModelSettings(TypedDict, total=False):
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

    response_format: Optional[ModelSettingsMoonshotCodingModelSettingsResponseFormat]
    """The response format for the model."""

    strict: bool
    """Enable strict mode for tool calling.

    When true, tool outputs are guaranteed to match JSON schemas.
    """

    temperature: float
    """The temperature of the model."""

    thinking: ModelSettingsMoonshotCodingModelSettingsThinking
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]]
    """Soft control for how verbose model output should be, used for GPT-5 models."""


class ModelSettingsBasetenModelSettings(TypedDict, total=False):
    """Baseten model configuration (OpenAI-compatible)."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["baseten"]
    """The type of the provider."""

    temperature: float
    """The temperature of the model."""


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
    ModelSettingsSgLangModelSettings,
    AnthropicModelSettingsParam,
    GoogleAIModelSettingsParam,
    GoogleVertexModelSettingsParam,
    AzureModelSettingsParam,
    XaiModelSettingsParam,
    ModelSettingsMoonshotModelSettings,
    ModelSettingsZaiModelSettings,
    ModelSettingsMoonshotCodingModelSettings,
    GroqModelSettingsParam,
    DeepseekModelSettingsParam,
    TogetherModelSettingsParam,
    BedrockModelSettingsParam,
    ModelSettingsBasetenModelSettings,
    ModelSettingsOpenRouterModelSettings,
    ModelSettingsChatGptoAuthModelSettings,
]

ResponseFormat: TypeAlias = Union[TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam]

ToolRule: TypeAlias = Union[
    ChildToolRuleParam,
    InitToolRuleParam,
    TerminalToolRuleParam,
    ConditionalToolRuleParam,
    ContinueToolRuleParam,
    RequiredBeforeExitToolRuleParam,
    MaxCountPerStepToolRuleParam,
    ParentToolRuleParam,
    RequiresApprovalToolRuleParam,
]
