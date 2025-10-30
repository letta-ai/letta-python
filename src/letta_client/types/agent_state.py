# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .tool import Tool
from .group import Group
from .._utils import PropertyInfo
from .._models import BaseModel
from .identity import Identity
from .agent_type import AgentType
from .llm_config import LlmConfig
from .agents.block import Block
from .init_tool_rule import InitToolRule
from .child_tool_rule import ChildToolRule
from .embedding_config import EmbeddingConfig
from .parent_tool_rule import ParentToolRule
from .continue_tool_rule import ContinueToolRule
from .terminal_tool_rule import TerminalToolRule
from .vector_db_provider import VectorDBProvider
from .text_response_format import TextResponseFormat
from .conditional_tool_rule import ConditionalToolRule
from .agent_environment_variable import AgentEnvironmentVariable
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat
from .requires_approval_tool_rule import RequiresApprovalToolRule
from .max_count_per_step_tool_rule import MaxCountPerStepToolRule
from .required_before_exit_tool_rule import RequiredBeforeExitToolRule

__all__ = [
    "AgentState",
    "Memory",
    "MemoryFileBlock",
    "Source",
    "Embedding",
    "Model",
    "ModelOpenAIModel",
    "ModelOpenAIModelReasoning",
    "ModelOpenAIModelResponseFormat",
    "ModelAnthropicModel",
    "ModelAnthropicModelThinking",
    "ModelGoogleAIModel",
    "ModelGoogleAIModelResponseSchema",
    "ModelGoogleAIModelThinkingConfig",
    "ModelGoogleVertexModel",
    "ModelGoogleVertexModelResponseSchema",
    "ModelGoogleVertexModelThinkingConfig",
    "ModelAzureModel",
    "ModelAzureModelResponseFormat",
    "ModelXaiModel",
    "ModelXaiModelResponseFormat",
    "ModelGroqModel",
    "ModelGroqModelResponseFormat",
    "ModelDeepseekModel",
    "ModelDeepseekModelResponseFormat",
    "ModelTogetherModel",
    "ModelTogetherModelResponseFormat",
    "ModelBedrockModel",
    "ModelBedrockModelResponseFormat",
    "ResponseFormat",
    "ToolRule",
]


class MemoryFileBlock(BaseModel):
    file_id: str
    """Unique identifier of the file."""

    is_open: bool
    """True if the agent currently has the file open."""

    source_id: str
    """Unique identifier of the source."""

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

    template_id: Optional[str] = None
    """The id of the template."""

    template_name: Optional[str] = None
    """Name of the block if it is a template."""


class Memory(BaseModel):
    blocks: List[Block]
    """Memory blocks contained in the agent's in-context memory"""

    agent_type: Union[AgentType, str, None] = None
    """Agent type controlling prompt rendering."""

    file_blocks: Optional[List[MemoryFileBlock]] = None
    """Special blocks representing the agent's in-context memory of an attached file"""

    prompt_template: Optional[str] = None
    """Deprecated. Ignored for performance."""


class Source(BaseModel):
    embedding_config: EmbeddingConfig
    """The embedding configuration used by the source."""

    name: str
    """The name of the source."""

    id: Optional[str] = None
    """The human-friendly ID of the Source"""

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


class Embedding(BaseModel):
    model: str
    """The name of the model."""

    provider: Literal["openai", "ollama"]
    """The provider of the model."""


class ModelOpenAIModelReasoning(BaseModel):
    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] = None
    """The reasoning effort to use when generating text reasoning models"""


ModelOpenAIModelResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelOpenAIModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["openai"]] = None
    """The provider of the model."""

    reasoning: Optional[ModelOpenAIModelReasoning] = None
    """The reasoning configuration for the model."""

    response_format: Optional[ModelOpenAIModelResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


class ModelAnthropicModelThinking(BaseModel):
    budget_tokens: Optional[int] = None
    """The maximum number of tokens the model can use for extended thinking."""

    type: Optional[Literal["enabled", "disabled"]] = None
    """The type of thinking to use."""


class ModelAnthropicModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["anthropic"]] = None
    """The provider of the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking: Optional[ModelAnthropicModelThinking] = None
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]] = None
    """Soft control for how verbose model output should be, used for GPT-5 models."""


ModelGoogleAIModelResponseSchema: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelGoogleAIModelThinkingConfig(BaseModel):
    include_thoughts: Optional[bool] = None
    """Whether to include thoughts in the model's response."""

    thinking_budget: Optional[int] = None
    """The thinking budget for the model."""


class ModelGoogleAIModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["google_ai"]] = None
    """The provider of the model."""

    response_schema: Optional[ModelGoogleAIModelResponseSchema] = None
    """The response schema for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking_config: Optional[ModelGoogleAIModelThinkingConfig] = None
    """The thinking configuration for the model."""


ModelGoogleVertexModelResponseSchema: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelGoogleVertexModelThinkingConfig(BaseModel):
    include_thoughts: Optional[bool] = None
    """Whether to include thoughts in the model's response."""

    thinking_budget: Optional[int] = None
    """The thinking budget for the model."""


class ModelGoogleVertexModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["google_vertex"]] = None
    """The provider of the model."""

    response_schema: Optional[ModelGoogleVertexModelResponseSchema] = None
    """The response schema for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking_config: Optional[ModelGoogleVertexModelThinkingConfig] = None
    """The thinking configuration for the model."""


ModelAzureModelResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelAzureModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["azure"]] = None
    """The provider of the model."""

    response_format: Optional[ModelAzureModelResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelXaiModelResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelXaiModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["xai"]] = None
    """The provider of the model."""

    response_format: Optional[ModelXaiModelResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelGroqModelResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelGroqModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["groq"]] = None
    """The provider of the model."""

    response_format: Optional[ModelGroqModelResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelDeepseekModelResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelDeepseekModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["deepseek"]] = None
    """The provider of the model."""

    response_format: Optional[ModelDeepseekModelResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelTogetherModelResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelTogetherModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["together"]] = None
    """The provider of the model."""

    response_format: Optional[ModelTogetherModelResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelBedrockModelResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelBedrockModel(BaseModel):
    model: str
    """The name of the model."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    provider: Optional[Literal["bedrock"]] = None
    """The provider of the model."""

    response_format: Optional[ModelBedrockModelResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


Model: TypeAlias = Annotated[
    Union[
        ModelOpenAIModel,
        ModelAnthropicModel,
        ModelGoogleAIModel,
        ModelGoogleVertexModel,
        ModelAzureModel,
        ModelXaiModel,
        ModelGroqModel,
        ModelDeepseekModel,
        ModelTogetherModel,
        ModelBedrockModel,
        None,
    ],
    PropertyInfo(discriminator="provider"),
]

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
    id: str
    """The id of the agent. Assigned by the database."""

    agent_type: AgentType
    """The type of agent."""

    blocks: List[Block]
    """The memory blocks used by the agent."""

    embedding_config: EmbeddingConfig
    """Deprecated: Use `embedding` field instead.

    The embedding configuration used by the agent.
    """

    llm_config: LlmConfig
    """Deprecated: Use `model` field instead. The LLM configuration used by the agent."""

    memory: Memory
    """Deprecated: Use `blocks` field instead. The in-context memory of the agent."""

    name: str
    """The name of the agent."""

    sources: List[Source]
    """The sources used by the agent."""

    system: str
    """The system prompt used by the agent."""

    tags: List[str]
    """The tags associated with the agent."""

    tools: List[Tool]
    """The tools used by the agent."""

    base_template_id: Optional[str] = None
    """The base template id of the agent."""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    deployment_id: Optional[str] = None
    """The id of the deployment."""

    description: Optional[str] = None
    """The description of the agent."""

    embedding: Optional[Embedding] = None
    """The embedding model used by the agent."""

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

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    managed_group: Optional[Group] = None
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

    model: Optional[Model] = None
    """The model used by the agent."""

    multi_agent_group: Optional[Group] = None
    """Deprecated: Use `managed_group` field instead.

    The multi-agent group that this agent manages.
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
