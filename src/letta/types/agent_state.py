# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AgentState",
    "EmbeddingConfig",
    "LlmConfig",
    "Memory",
    "MemoryBlock",
    "Source",
    "SourceEmbeddingConfig",
    "Tool",
    "ToolRule",
    "ToolRuleChildToolRule",
    "ToolRuleInitToolRule",
    "ToolRuleTerminalToolRule",
]


class EmbeddingConfig(BaseModel):
    embedding_dim: int
    """The dimension of the embedding."""

    embedding_endpoint_type: Literal[
        "openai",
        "anthropic",
        "cohere",
        "google_ai",
        "azure",
        "groq",
        "ollama",
        "webui",
        "webui-legacy",
        "lmstudio",
        "lmstudio-legacy",
        "llamacpp",
        "koboldcpp",
        "vllm",
        "hugging-face",
        "mistral",
        "together",
    ]
    """The endpoint type for the model."""

    embedding_model: str
    """The model for the embedding."""

    azure_deployment: Optional[str] = None
    """The Azure deployment for the model."""

    azure_endpoint: Optional[str] = None
    """The Azure endpoint for the model."""

    azure_version: Optional[str] = None
    """The Azure version for the model."""

    embedding_chunk_size: Optional[int] = None
    """The chunk size of the embedding."""

    embedding_endpoint: Optional[str] = None
    """The endpoint for the model (`None` if local)."""


class LlmConfig(BaseModel):
    context_window: int
    """The context window size for the model."""

    model: str
    """LLM model name."""

    api_model_endpoint_type: Literal[
        "openai",
        "anthropic",
        "cohere",
        "google_ai",
        "azure",
        "groq",
        "ollama",
        "webui",
        "webui-legacy",
        "lmstudio",
        "lmstudio-legacy",
        "llamacpp",
        "koboldcpp",
        "vllm",
        "hugging-face",
        "mistral",
        "together",
    ] = FieldInfo(alias="model_endpoint_type")
    """The endpoint type for the model."""

    api_model_endpoint: Optional[str] = FieldInfo(alias="model_endpoint", default=None)
    """The endpoint for the model."""

    api_model_wrapper: Optional[str] = FieldInfo(alias="model_wrapper", default=None)
    """The wrapper for the model."""

    put_inner_thoughts_in_kwargs: Optional[bool] = None
    """Puts 'inner_thoughts' as a kwarg in the function call if this is set to True.

    This helps with function calling performance and also the generation of inner
    thoughts.
    """


class MemoryBlock(BaseModel):
    value: str
    """Value of the block."""

    id: Optional[str] = None
    """The human-friendly ID of the Block"""

    created_by_id: Optional[str] = None
    """The id of the user that made this Block."""

    description: Optional[str] = None
    """Description of the block."""

    is_template: Optional[bool] = None
    """Whether the block is a template (e.g. saved human/persona options)."""

    label: Optional[str] = None
    """Label of the block (e.g. 'human', 'persona') in the context window."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that last updated this Block."""

    limit: Optional[int] = None
    """Character limit of the block."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """Metadata of the block."""

    name: Optional[str] = None
    """Name of the block if it is a template."""

    organization_id: Optional[str] = None
    """The unique identifier of the organization associated with the block."""


class Memory(BaseModel):
    blocks: List[MemoryBlock]
    """Memory blocks contained in the agent's in-context memory"""

    prompt_template: Optional[str] = None
    """Jinja2 template for compiling memory blocks into a prompt string"""


class SourceEmbeddingConfig(BaseModel):
    embedding_dim: int
    """The dimension of the embedding."""

    embedding_endpoint_type: Literal[
        "openai",
        "anthropic",
        "cohere",
        "google_ai",
        "azure",
        "groq",
        "ollama",
        "webui",
        "webui-legacy",
        "lmstudio",
        "lmstudio-legacy",
        "llamacpp",
        "koboldcpp",
        "vllm",
        "hugging-face",
        "mistral",
        "together",
    ]
    """The endpoint type for the model."""

    embedding_model: str
    """The model for the embedding."""

    azure_deployment: Optional[str] = None
    """The Azure deployment for the model."""

    azure_endpoint: Optional[str] = None
    """The Azure endpoint for the model."""

    azure_version: Optional[str] = None
    """The Azure version for the model."""

    embedding_chunk_size: Optional[int] = None
    """The chunk size of the embedding."""

    embedding_endpoint: Optional[str] = None
    """The endpoint for the model (`None` if local)."""


class Source(BaseModel):
    embedding_config: SourceEmbeddingConfig
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

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """Metadata associated with the source."""

    organization_id: Optional[str] = None
    """The ID of the organization that created the source."""

    updated_at: Optional[datetime] = None
    """The timestamp when the source was last updated."""


class Tool(BaseModel):
    source_code: str
    """The source code of the function."""

    id: Optional[str] = None
    """The human-friendly ID of the Tool"""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    description: Optional[str] = None
    """The description of the tool."""

    json_schema: Optional[object] = None
    """The JSON schema of the function."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    module: Optional[str] = None
    """The module of the function."""

    name: Optional[str] = None
    """The name of the function."""

    organization_id: Optional[str] = None
    """The unique identifier of the organization associated with the tool."""

    return_char_limit: Optional[int] = None
    """The maximum number of characters in the response."""

    source_type: Optional[str] = None
    """The type of the source code."""

    tags: Optional[List[str]] = None
    """Metadata tags."""


class ToolRuleChildToolRule(BaseModel):
    children: List[str]
    """The children tools that can be invoked."""

    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    type: Optional[Literal["InitToolRule", "TerminalToolRule", "continue_loop", "ToolRule", "require_parent_tools"]] = (
        None
    )
    """Type of tool rule."""


class ToolRuleInitToolRule(BaseModel):
    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    type: Optional[Literal["InitToolRule", "TerminalToolRule", "continue_loop", "ToolRule", "require_parent_tools"]] = (
        None
    )
    """Type of tool rule."""


class ToolRuleTerminalToolRule(BaseModel):
    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    type: Optional[Literal["InitToolRule", "TerminalToolRule", "continue_loop", "ToolRule", "require_parent_tools"]] = (
        None
    )
    """Type of tool rule."""


ToolRule: TypeAlias = Union[ToolRuleChildToolRule, ToolRuleInitToolRule, ToolRuleTerminalToolRule]


class AgentState(BaseModel):
    id: str
    """The id of the agent. Assigned by the database."""

    agent_type: Literal["memgpt_agent", "split_thread_agent", "o1_agent", "offline_memory_agent", "chat_only_agent"]
    """The type of agent."""

    embedding_config: EmbeddingConfig
    """The embedding configuration used by the agent."""

    llm_config: LlmConfig
    """The LLM configuration used by the agent."""

    memory: Memory
    """The in-context memory of the agent."""

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

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    description: Optional[str] = None
    """The description of the agent."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    message_ids: Optional[List[str]] = None
    """The ids of the messages in the agent's in-context memory."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """The metadata of the agent."""

    organization_id: Optional[str] = None
    """The unique identifier of the organization associated with the agent."""

    tool_rules: Optional[List[ToolRule]] = None
    """The list of tool rules."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
