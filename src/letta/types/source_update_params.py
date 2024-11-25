# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .embeddingconfig_param import EmbeddingconfigParam

__all__ = ["SourceUpdateParams"]


class SourceUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """The description of the source."""

    embedding_config: Optional[EmbeddingconfigParam]
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

    metadata: Annotated[Optional[object], PropertyInfo(alias="metadata_")]
    """Metadata associated with the source."""

    name: Optional[str]
    """The name of the source."""
