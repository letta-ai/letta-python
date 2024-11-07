# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..embeddingconfig import Embeddingconfig

__all__ = ["Passage"]


class Passage(BaseModel):
    embedding: Optional[List[float]] = None
    """The embedding of the passage."""

    embedding_config: Optional[Embeddingconfig] = None
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

    text: str
    """The text of the passage."""

    id: Optional[str] = None
    """The human-friendly ID of the Passage"""

    agent_id: Optional[str] = None
    """The unique identifier of the agent associated with the passage."""

    created_at: Optional[datetime] = None
    """The creation date of the passage."""

    file_id: Optional[str] = None
    """The unique identifier of the file associated with the passage."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """The metadata of the passage."""

    source_id: Optional[str] = None
    """The data source of the passage."""

    user_id: Optional[str] = None
    """The unique identifier of the user associated with the passage."""
