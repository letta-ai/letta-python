# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentUpdateParams", "EmbeddingConfig", "LlmConfig", "Memory", "MemoryMemory"]


class AgentUpdateParams(TypedDict, total=False):
    id: Required[str]
    """The id of the agent."""

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

    memory: Optional[Memory]
    """Represents the in-context memory of the agent.

    This includes both the `Block` objects (labelled by sections), as well as tools
    to edit the blocks.

    Attributes: memory (Dict[str, Block]): Mapping from memory block section to
    memory block.
    """

    message_ids: Optional[List[str]]
    """The ids of the messages in the agent's in-context memory."""

    metadata: Annotated[Optional[object], PropertyInfo(alias="metadata_")]
    """The metadata of the agent."""

    name: Optional[str]
    """The name of the agent."""

    system: Optional[str]
    """The system prompt used by the agent."""

    tags: Optional[List[str]]
    """The tags associated with the agent."""

    tools: Optional[List[str]]
    """The tools used by the agent."""

    user_id: Optional[str]
    """The user id of the agent."""


class EmbeddingConfig(TypedDict, total=False):
    embedding_dim: Required[int]
    """The dimension of the embedding."""

    embedding_endpoint_type: Required[str]
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


class MemoryMemory(TypedDict, total=False):
    value: Required[str]
    """Value of the block."""

    id: str
    """The human-friendly ID of the Block"""

    created_by_id: Optional[str]
    """The id of the user that made this Block."""

    description: Optional[str]
    """Description of the block."""

    is_template: bool
    """Whether the block is a template (e.g. saved human/persona options)."""

    label: Optional[str]
    """Label of the block (e.g. 'human', 'persona') in the context window."""

    last_updated_by_id: Optional[str]
    """The id of the user that last updated this Block."""

    limit: int
    """Character limit of the block."""

    metadata: Annotated[Optional[object], PropertyInfo(alias="metadata_")]
    """Metadata of the block."""

    name: Optional[str]
    """Name of the block if it is a template."""

    organization_id: Optional[str]
    """The unique identifier of the organization associated with the block."""


class Memory(TypedDict, total=False):
    memory: Dict[str, MemoryMemory]
    """Mapping from memory block section to memory block."""

    prompt_template: str
    """Jinja2 template for compiling memory blocks into a prompt string"""
