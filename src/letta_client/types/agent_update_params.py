# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

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
    "CompactionSettingsModelSettingsZaiModelSettings",
    "CompactionSettingsModelSettingsZaiModelSettingsResponseFormat",
    "ModelSettings",
    "ModelSettingsZaiModelSettings",
    "ModelSettingsZaiModelSettingsResponseFormat",
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

    `model` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. `"openai/gpt-4o-mini"`). Per-model settings (temperature, max
    tokens, etc.) are derived from the default configuration for that handle.
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


CompactionSettingsModelSettingsZaiModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


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
]


class CompactionSettings(TypedDict, total=False):
    """Configuration for conversation compaction / summarization.

    ``model`` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. ``"openai/gpt-4o-mini"``). Per-model settings (temperature,
    max tokens, etc.) are derived from the default configuration for that handle.
    """

    model: Required[str]
    """Model handle to use for summarization (format: provider/model-name)."""

    clip_chars: Optional[int]
    """The maximum length of the summary in characters.

    If none, no clipping is performed.
    """

    mode: Literal["all", "sliding_window"]
    """The type of summarization technique use."""

    model_settings: Optional[CompactionSettingsModelSettings]
    """Optional model settings used to override defaults for the summarizer model."""

    prompt: str
    """The prompt to use for summarization."""

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


ModelSettingsZaiModelSettingsResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


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
