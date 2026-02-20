# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .tool import Tool
from .._utils import PropertyInfo
from .._models import BaseModel
from .agent_type import AgentType
from .llm_config import LlmConfig
from .agents.block import Block
from .init_tool_rule import InitToolRule
from .child_tool_rule import ChildToolRule
from .embedding_config import EmbeddingConfig
from .parent_tool_rule import ParentToolRule
from .stop_reason_type import StopReasonType
from .continue_tool_rule import ContinueToolRule
from .terminal_tool_rule import TerminalToolRule
from .vector_db_provider import VectorDBProvider
from .xai_model_settings import XaiModelSettings
from .groq_model_settings import GroqModelSettings
from .azure_model_settings import AzureModelSettings
from .text_response_format import TextResponseFormat
from .conditional_tool_rule import ConditionalToolRule
from .openai_model_settings import OpenAIModelSettings
from .bedrock_model_settings import BedrockModelSettings
from .deepseek_model_settings import DeepseekModelSettings
from .together_model_settings import TogetherModelSettings
from .anthropic_model_settings import AnthropicModelSettings
from .google_ai_model_settings import GoogleAIModelSettings
from .agent_environment_variable import AgentEnvironmentVariable
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat
from .requires_approval_tool_rule import RequiresApprovalToolRule
from .google_vertex_model_settings import GoogleVertexModelSettings
from .max_count_per_step_tool_rule import MaxCountPerStepToolRule
from .required_before_exit_tool_rule import RequiredBeforeExitToolRule
from .agents.approval_request_message import ApprovalRequestMessage

__all__ = [
    "AgentState",
    "Memory",
    "MemoryFileBlock",
    "Source",
    "CompactionSettings",
    "CompactionSettingsModelSettings",
    "CompactionSettingsModelSettingsZaiModelSettings",
    "CompactionSettingsModelSettingsZaiModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsZaiModelSettingsThinking",
    "CompactionSettingsModelSettingsOpenRouterModelSettings",
    "CompactionSettingsModelSettingsOpenRouterModelSettingsResponseFormat",
    "CompactionSettingsModelSettingsChatGptoAuthModelSettings",
    "CompactionSettingsModelSettingsChatGptoAuthModelSettingsReasoning",
    "Identity",
    "IdentityProperty",
    "ManagedGroup",
    "ModelSettings",
    "ModelSettingsZaiModelSettings",
    "ModelSettingsZaiModelSettingsResponseFormat",
    "ModelSettingsZaiModelSettingsThinking",
    "ModelSettingsOpenRouterModelSettings",
    "ModelSettingsOpenRouterModelSettingsResponseFormat",
    "ModelSettingsChatGptoAuthModelSettings",
    "ModelSettingsChatGptoAuthModelSettingsReasoning",
    "MultiAgentGroup",
    "ResponseFormat",
    "ToolRule",
]


class MemoryFileBlock(BaseModel):
    file_id: str
    """Unique identifier of the file."""

    is_open: bool
    """True if the agent currently has the file open."""

    source_id: str
    """Deprecated: Use `folder_id` field instead. Unique identifier of the source."""

    value: str
    """Value of the block."""

    id: Optional[str] = None
    """The human-friendly ID of the Block"""

    base_template_id: Optional[str] = None
    """The base template id of the block."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Block."""

    deployment_id: Optional[str] = None
    """The id of the deployment."""

    description: Optional[str] = None
    """Description of the block."""

    entity_id: Optional[str] = None
    """The id of the entity within the template."""

    hidden: Optional[bool] = None
    """If set to True, the block will be hidden."""

    is_template: Optional[bool] = None
    """Whether the block is a template (e.g. saved human/persona options)."""

    label: Optional[str] = None
    """Label of the block (e.g. 'human', 'persona') in the context window."""

    last_accessed_at: Optional[datetime] = None
    """UTC timestamp of the agent’s most recent access to this file.

    Any operations from the open, close, or search tools will update this field.
    """

    last_updated_by_id: Optional[str] = None
    """The id of the user that last updated this Block."""

    limit: Optional[int] = None
    """Character limit of the block."""

    metadata: Optional[Dict[str, object]] = None
    """Metadata of the block."""

    preserve_on_migration: Optional[bool] = None
    """Preserve the block on template migration."""

    project_id: Optional[str] = None
    """The associated project id."""

    read_only: Optional[bool] = None
    """Whether the agent has read-only access to the block."""

    tags: Optional[List[str]] = None
    """The tags associated with the block."""

    template_id: Optional[str] = None
    """The id of the template."""

    template_name: Optional[str] = None
    """Name of the block if it is a template."""


class Memory(BaseModel):
    """Deprecated: Use `blocks` field instead. The in-context memory of the agent."""

    blocks: List[Block]
    """Memory blocks contained in the agent's in-context memory"""

    agent_type: Union[AgentType, str, None] = None
    """Agent type controlling prompt rendering."""

    file_blocks: Optional[List[MemoryFileBlock]] = None
    """Special blocks representing the agent's in-context memory of an attached file"""

    git_enabled: Optional[bool] = None
    """Whether this agent uses git-backed memory with structured labels."""

    prompt_template: Optional[str] = None
    """Deprecated. Ignored for performance."""


class Source(BaseModel):
    """
    (Deprecated: Use Folder) Representation of a source, which is a collection of files and passages.
    """

    id: str
    """The human-friendly ID of the Source"""

    embedding_config: EmbeddingConfig
    """The embedding configuration used by the source."""

    name: str
    """The name of the source."""

    created_at: Optional[datetime] = None
    """The timestamp when the source was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    description: Optional[str] = None
    """The description of the source."""

    instructions: Optional[str] = None
    """Instructions for how to use the source."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    metadata: Optional[Dict[str, object]] = None
    """Metadata associated with the source."""

    updated_at: Optional[datetime] = None
    """The timestamp when the source was last updated."""

    vector_db_provider: Optional[VectorDBProvider] = None
    """The vector database provider used for this source's passages"""


CompactionSettingsModelSettingsZaiModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class CompactionSettingsModelSettingsZaiModelSettingsThinking(BaseModel):
    """The thinking configuration for GLM-4.5+ models."""

    clear_thinking: Optional[bool] = None
    """If False, preserved thinking is used (recommended for agents)."""

    type: Optional[Literal["enabled", "disabled"]] = None
    """Whether thinking is enabled or disabled."""


class CompactionSettingsModelSettingsZaiModelSettings(BaseModel):
    """Z.ai (ZhipuAI) model configuration (OpenAI-compatible)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["zai"]] = None
    """The type of the provider."""

    response_format: Optional[CompactionSettingsModelSettingsZaiModelSettingsResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking: Optional[CompactionSettingsModelSettingsZaiModelSettingsThinking] = None
    """The thinking configuration for GLM-4.5+ models."""


CompactionSettingsModelSettingsOpenRouterModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class CompactionSettingsModelSettingsOpenRouterModelSettings(BaseModel):
    """OpenRouter model configuration (OpenAI-compatible)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["openrouter"]] = None
    """The type of the provider."""

    response_format: Optional[CompactionSettingsModelSettingsOpenRouterModelSettingsResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


class CompactionSettingsModelSettingsChatGptoAuthModelSettingsReasoning(BaseModel):
    """The reasoning configuration for the model."""

    reasoning_effort: Optional[Literal["none", "low", "medium", "high", "xhigh"]] = None
    """The reasoning effort level for GPT-5.x and o-series models."""


class CompactionSettingsModelSettingsChatGptoAuthModelSettings(BaseModel):
    """ChatGPT OAuth model configuration (uses ChatGPT backend API)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["chatgpt_oauth"]] = None
    """The type of the provider."""

    reasoning: Optional[CompactionSettingsModelSettingsChatGptoAuthModelSettingsReasoning] = None
    """The reasoning configuration for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


CompactionSettingsModelSettings: TypeAlias = Annotated[
    Union[
        OpenAIModelSettings,
        AnthropicModelSettings,
        GoogleAIModelSettings,
        GoogleVertexModelSettings,
        AzureModelSettings,
        XaiModelSettings,
        CompactionSettingsModelSettingsZaiModelSettings,
        GroqModelSettings,
        DeepseekModelSettings,
        TogetherModelSettings,
        BedrockModelSettings,
        CompactionSettingsModelSettingsOpenRouterModelSettings,
        CompactionSettingsModelSettingsChatGptoAuthModelSettings,
        None,
    ],
    PropertyInfo(discriminator="provider_type"),
]


class CompactionSettings(BaseModel):
    """Configuration for conversation compaction / summarization.

    ``model`` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. ``"openai/gpt-4o-mini"``). Per-model settings (temperature,
    max tokens, etc.) are derived from the default configuration for that handle.
    """

    clip_chars: Optional[int] = None
    """The maximum length of the summary in characters.

    If none, no clipping is performed.
    """

    mode: Optional[Literal["all", "sliding_window", "self"]] = None
    """The type of summarization technique use."""

    model: Optional[str] = None
    """Model handle to use for summarization (format: provider/model-name).

    If None, uses lightweight provider-specific defaults.
    """

    api_model_settings: Optional[CompactionSettingsModelSettings] = FieldInfo(alias="model_settings", default=None)
    """Optional model settings used to override defaults for the summarizer model."""

    prompt: Optional[str] = None
    """The prompt to use for summarization. If None, uses mode-specific default."""

    prompt_acknowledgement: Optional[bool] = None
    """
    Whether to include an acknowledgement post-prompt (helps prevent non-summary
    outputs).
    """

    sliding_window_percentage: Optional[float] = None
    """
    The percentage of the context window to keep post-summarization (only used in
    sliding window mode).
    """


class IdentityProperty(BaseModel):
    """A property of an identity"""

    key: str
    """The key of the property"""

    type: Literal["string", "number", "boolean", "json"]
    """The type of the property"""

    value: Union[str, float, bool, Dict[str, object]]
    """The value of the property"""


class Identity(BaseModel):
    id: str
    """The human-friendly ID of the Identity"""

    agent_ids: List[str]
    """The IDs of the agents associated with the identity."""

    block_ids: List[str]
    """The IDs of the blocks associated with the identity."""

    identifier_key: str
    """External, user-generated identifier key of the identity."""

    identity_type: Literal["org", "user", "other"]
    """The type of the identity."""

    name: str
    """The name of the identity."""

    project_id: Optional[str] = None
    """The project id of the identity, if applicable."""

    properties: Optional[List[IdentityProperty]] = None
    """List of properties associated with the identity"""


class ManagedGroup(BaseModel):
    """The multi-agent group that this agent manages"""

    id: str
    """The id of the group. Assigned by the database."""

    agent_ids: List[str]

    description: str

    manager_type: Literal["round_robin", "supervisor", "dynamic", "sleeptime", "voice_sleeptime", "swarm"]

    base_template_id: Optional[str] = None
    """The base template id."""

    deployment_id: Optional[str] = None
    """The id of the deployment."""

    hidden: Optional[bool] = None
    """If set to True, the group will be hidden."""

    last_processed_message_id: Optional[str] = None

    manager_agent_id: Optional[str] = None

    max_message_buffer_length: Optional[int] = None
    """The desired maximum length of messages in the context window of the convo agent.

    This is a best effort, and may be off slightly due to user/assistant
    interleaving.
    """

    max_turns: Optional[int] = None

    min_message_buffer_length: Optional[int] = None
    """The desired minimum length of messages in the context window of the convo agent.

    This is a best effort, and may be off-by-one due to user/assistant interleaving.
    """

    project_id: Optional[str] = None
    """The associated project id."""

    shared_block_ids: Optional[List[str]] = None

    sleeptime_agent_frequency: Optional[int] = None

    template_id: Optional[str] = None
    """The id of the template."""

    termination_token: Optional[str] = None

    turns_counter: Optional[int] = None


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
        AnthropicModelSettings,
        GoogleAIModelSettings,
        GoogleVertexModelSettings,
        AzureModelSettings,
        XaiModelSettings,
        ModelSettingsZaiModelSettings,
        GroqModelSettings,
        DeepseekModelSettings,
        TogetherModelSettings,
        BedrockModelSettings,
        ModelSettingsOpenRouterModelSettings,
        ModelSettingsChatGptoAuthModelSettings,
        None,
    ],
    PropertyInfo(discriminator="provider_type"),
]


class MultiAgentGroup(BaseModel):
    """Deprecated: Use `managed_group` field instead.

    The multi-agent group that this agent manages.
    """

    id: str
    """The id of the group. Assigned by the database."""

    agent_ids: List[str]

    description: str

    manager_type: Literal["round_robin", "supervisor", "dynamic", "sleeptime", "voice_sleeptime", "swarm"]

    base_template_id: Optional[str] = None
    """The base template id."""

    deployment_id: Optional[str] = None
    """The id of the deployment."""

    hidden: Optional[bool] = None
    """If set to True, the group will be hidden."""

    last_processed_message_id: Optional[str] = None

    manager_agent_id: Optional[str] = None

    max_message_buffer_length: Optional[int] = None
    """The desired maximum length of messages in the context window of the convo agent.

    This is a best effort, and may be off slightly due to user/assistant
    interleaving.
    """

    max_turns: Optional[int] = None

    min_message_buffer_length: Optional[int] = None
    """The desired minimum length of messages in the context window of the convo agent.

    This is a best effort, and may be off-by-one due to user/assistant interleaving.
    """

    project_id: Optional[str] = None
    """The associated project id."""

    shared_block_ids: Optional[List[str]] = None

    sleeptime_agent_frequency: Optional[int] = None

    template_id: Optional[str] = None
    """The id of the template."""

    termination_token: Optional[str] = None

    turns_counter: Optional[int] = None


ResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]

ToolRule: TypeAlias = Annotated[
    Union[
        ChildToolRule,
        InitToolRule,
        TerminalToolRule,
        ConditionalToolRule,
        ContinueToolRule,
        RequiredBeforeExitToolRule,
        MaxCountPerStepToolRule,
        ParentToolRule,
        RequiresApprovalToolRule,
    ],
    PropertyInfo(discriminator="type"),
]


class AgentState(BaseModel):
    """Representation of an agent's state.

    This is the state of the agent at a given time, and is persisted in the DB backend. The state has all the information needed to recreate a persisted agent.
    """

    id: str
    """The id of the agent. Assigned by the database."""

    agent_type: AgentType
    """The type of agent."""

    blocks: List[Block]
    """The memory blocks used by the agent."""

    llm_config: LlmConfig
    """Deprecated: Use `model` field instead. The LLM configuration used by the agent."""

    memory: Memory
    """Deprecated: Use `blocks` field instead. The in-context memory of the agent."""

    name: str
    """The name of the agent."""

    sources: List[Source]
    """Deprecated: Use `folders` field instead. The sources used by the agent."""

    system: str
    """The system prompt used by the agent."""

    tags: List[str]
    """The tags associated with the agent."""

    tools: List[Tool]
    """The tools used by the agent."""

    base_template_id: Optional[str] = None
    """The base template id of the agent."""

    compaction_settings: Optional[CompactionSettings] = None
    """Configuration for conversation compaction / summarization.

    `model` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. `"openai/gpt-4o-mini"`). Per-model settings (temperature, max
    tokens, etc.) are derived from the default configuration for that handle.
    """

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    deployment_id: Optional[str] = None
    """The id of the deployment."""

    description: Optional[str] = None
    """The description of the agent."""

    embedding: Optional[str] = None
    """The embedding model handle used by the agent (format: provider/model-name)."""

    embedding_config: Optional[EmbeddingConfig] = None
    """Configuration for embedding model connection and processing parameters."""

    enable_sleeptime: Optional[bool] = None
    """If set to True, memory management will move to a background agent thread."""

    entity_id: Optional[str] = None
    """The id of the entity within the template."""

    hidden: Optional[bool] = None
    """If set to True, the agent will be hidden."""

    identities: Optional[List[Identity]] = None
    """The identities associated with this agent."""

    identity_ids: Optional[List[str]] = None
    """Deprecated: Use `identities` field instead.

    The ids of the identities associated with this agent.
    """

    last_run_completion: Optional[datetime] = None
    """The timestamp when the agent last completed a run."""

    last_run_duration_ms: Optional[int] = None
    """The duration in milliseconds of the agent's last run."""

    last_stop_reason: Optional[StopReasonType] = None
    """The stop reason from the agent's last run."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    managed_group: Optional[ManagedGroup] = None
    """The multi-agent group that this agent manages"""

    max_files_open: Optional[int] = None
    """Maximum number of files that can be open at once for this agent.

    Setting this too high may exceed the context window, which will break the agent.
    """

    message_buffer_autoclear: Optional[bool] = None
    """
    If set to True, the agent will not remember previous messages (though the agent
    will still retain state via core memory blocks and archival/recall memory). Not
    recommended unless you have an advanced use case.
    """

    message_ids: Optional[List[str]] = None
    """The ids of the messages in the agent's in-context memory."""

    metadata: Optional[Dict[str, object]] = None
    """The metadata of the agent."""

    model: Optional[str] = None
    """The model handle used by the agent (format: provider/model-name)."""

    api_model_settings: Optional[ModelSettings] = FieldInfo(alias="model_settings", default=None)
    """The model settings used by the agent."""

    multi_agent_group: Optional[MultiAgentGroup] = None
    """Deprecated: Use `managed_group` field instead.

    The multi-agent group that this agent manages.
    """

    pending_approval: Optional[ApprovalRequestMessage] = None
    """
    A message representing a request for approval to call a tool (generated by the
    LLM to trigger tool execution).

    Args: id (str): The ID of the message date (datetime): The date the message was
    created in ISO format name (Optional[str]): The name of the sender of the
    message tool_call (ToolCall): The tool call
    """

    per_file_view_window_char_limit: Optional[int] = None
    """The per-file view window character limit for this agent.

    Setting this too high may exceed the context window, which will break the agent.
    """

    project_id: Optional[str] = None
    """The id of the project the agent belongs to."""

    response_format: Optional[ResponseFormat] = None
    """The response format used by the agent"""

    secrets: Optional[List[AgentEnvironmentVariable]] = None
    """The environment variables for tool execution specific to this agent."""

    template_id: Optional[str] = None
    """The id of the template the agent belongs to."""

    timezone: Optional[str] = None
    """The timezone of the agent (IANA format)."""

    tool_exec_environment_variables: Optional[List[AgentEnvironmentVariable]] = None
    """Deprecated: use `secrets` field instead."""

    tool_rules: Optional[List[ToolRule]] = None
    """The list of tool rules."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
