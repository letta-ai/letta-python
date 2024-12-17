# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AgentUpdateParams",
    "EmbeddingConfig",
    "LlmConfig",
    "ToolRule",
    "ToolRuleChildToolRule",
    "ToolRuleInitToolRule",
    "ToolRuleTerminalToolRule",
]


class AgentUpdateParams(TypedDict, total=False):
    block_ids: Optional[List[str]]
    """The ids of the blocks used by the agent."""

    description: Optional[str]
    """The description of the agent."""

    embedding_config: Optional[EmbeddingConfig]
    """Embedding model configuration.

    This object specifies all the information necessary to access an embedding model
    to usage with Letta, except for secret keys.

    Attributes: embedding_endpoint_type (str): The endpoint type for the model.
    embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
    model for the embedding. embedding_dim (int): The dimension of the embedding.
    embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
    (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
    azure_version (str): The Azure version for the model (Azure only).
    azure_deployment (str): The Azure deployment for the model (Azure only).
    """

    llm_config: Optional[LlmConfig]
    """Configuration for a Language Model (LLM) model.

    This object specifies all the information necessary to access an LLM model to
    usage with Letta, except for secret keys.

    Attributes: model (str): The name of the LLM model. model_endpoint_type (str):
    The endpoint type for the model. model_endpoint (str): The endpoint for the
    model. model_wrapper (str): The wrapper for the model. This is used to wrap
    additional text around the input/output of the model. This is useful for
    text-to-text completions, such as the Completions API in OpenAI. context_window
    (int): The context window size for the model. put_inner_thoughts_in_kwargs
    (bool): Puts `inner_thoughts` as a kwarg in the function call if this is set to
    True. This helps with function calling performance and also the generation of
    inner thoughts.
    """

    message_ids: Optional[List[str]]
    """The ids of the messages in the agent's in-context memory."""

    metadata: Annotated[Optional[object], PropertyInfo(alias="metadata_")]
    """The metadata of the agent."""

    name: Optional[str]
    """The name of the agent."""

    source_ids: Optional[List[str]]
    """The ids of the sources used by the agent."""

    system: Optional[str]
    """The system prompt used by the agent."""

    tags: Optional[List[str]]
    """The tags associated with the agent."""

    tool_ids: Optional[List[str]]
    """The ids of the tools used by the agent."""

    tool_rules: Optional[Iterable[ToolRule]]
    """The tool rules governing the agent."""


class EmbeddingConfig(TypedDict, total=False):
    embedding_dim: Required[int]
    """The dimension of the embedding."""

    embedding_endpoint_type: Required[
        Literal[
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
    ]
    """The endpoint type for the model."""

    embedding_model: Required[str]
    """The model for the embedding."""

    azure_deployment: Optional[str]
    """The Azure deployment for the model."""

    azure_endpoint: Optional[str]
    """The Azure endpoint for the model."""

    azure_version: Optional[str]
    """The Azure version for the model."""

    embedding_chunk_size: Optional[int]
    """The chunk size of the embedding."""

    embedding_endpoint: Optional[str]
    """The endpoint for the model (`None` if local)."""


class LlmConfig(TypedDict, total=False):
    context_window: Required[int]
    """The context window size for the model."""

    model: Required[str]
    """LLM model name."""

    model_endpoint_type: Required[
        Literal[
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
    ]
    """The endpoint type for the model."""

    model_endpoint: Optional[str]
    """The endpoint for the model."""

    model_wrapper: Optional[str]
    """The wrapper for the model."""

    put_inner_thoughts_in_kwargs: Optional[bool]
    """Puts 'inner_thoughts' as a kwarg in the function call if this is set to True.

    This helps with function calling performance and also the generation of inner
    thoughts.
    """


class ToolRuleChildToolRule(TypedDict, total=False):
    children: Required[List[str]]
    """The children tools that can be invoked."""

    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    type: Literal["InitToolRule", "TerminalToolRule", "continue_loop", "ToolRule", "require_parent_tools"]
    """Type of tool rule."""


class ToolRuleInitToolRule(TypedDict, total=False):
    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    type: Literal["InitToolRule", "TerminalToolRule", "continue_loop", "ToolRule", "require_parent_tools"]
    """Type of tool rule."""


class ToolRuleTerminalToolRule(TypedDict, total=False):
    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    type: Literal["InitToolRule", "TerminalToolRule", "continue_loop", "ToolRule", "require_parent_tools"]
    """Type of tool rule."""


ToolRule: TypeAlias = Union[ToolRuleChildToolRule, ToolRuleInitToolRule, ToolRuleTerminalToolRule]
