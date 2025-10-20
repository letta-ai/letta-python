# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmbeddingConfigParam"]


class EmbeddingConfigParam(TypedDict, total=False):
    embedding_dim: Required[int]
    """The dimension of the embedding."""

    embedding_endpoint_type: Required[
        Literal[
            "openai",
            "anthropic",
            "bedrock",
            "google_ai",
            "google_vertex",
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
            "pinecone",
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

    batch_size: int
    """The maximum batch size for processing embeddings."""

    embedding_chunk_size: Optional[int]
    """The chunk size of the embedding."""

    embedding_endpoint: Optional[str]
    """The endpoint for the model (`None` if local)."""

    handle: Optional[str]
    """The handle for this config, in the format provider/model-name."""
