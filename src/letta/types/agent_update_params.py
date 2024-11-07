# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .memory_param import MemoryParam
from .llm_config_param import LlmConfigParam
from .embedding_config_param import EmbeddingConfigParam

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    id: Required[str]
    """The id of the agent."""

    description: Optional[str]
    """The description of the agent."""

    embedding_config: Optional[EmbeddingConfigParam]
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

    llm_config: Optional[LlmConfigParam]
    """Configuration for a Language Model (LLM) model.

    This object specifies all the information necessary to access an LLM model to
    usage with Letta, except for secret keys.

    Attributes: model (str): The name of the LLM model. model_endpoint_type (str):
    The endpoint type for the model. model_endpoint (str): The endpoint for the
    model. model_wrapper (str): The wrapper for the model. This is used to wrap
    additional text around the input/output of the model. This is useful for
    text-to-text completions, such as the Completions API in OpenAI. context_window
    (int): The context window size for the model. put_inner_thoughts_in_kwargs
    (bool): Puts 'inner_thoughts' as a kwarg in the function call if this is set to
    True. This helps with function calling performance and also the generation of
    inner thoughts.
    """

    memory: Optional[MemoryParam]
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

    tools: Optional[List[str]]
    """The tools used by the agent."""

    body_user_id: Annotated[Optional[str], PropertyInfo(alias="user_id")]
    """The user id of the agent."""

    header_user_id: Annotated[str, PropertyInfo(alias="user_id")]
