# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmbeddingConfig"]


class EmbeddingConfig(BaseModel):
    """Configuration for embedding model connection and processing parameters."""

    embedding_dim: int
    """The dimension of the embedding."""

    embedding_endpoint_type: Literal[
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
    """The endpoint type for the model."""

    embedding_model: str
    """The model for the embedding."""

    azure_deployment: Optional[str] = None
    """The Azure deployment for the model."""

    azure_endpoint: Optional[str] = None
    """The Azure endpoint for the model."""

    azure_version: Optional[str] = None
    """The Azure version for the model."""

    batch_size: Optional[int] = None
    """The maximum batch size for processing embeddings."""

    embedding_chunk_size: Optional[int] = None
    """The chunk size of the embedding."""

    embedding_endpoint: Optional[str] = None
    """The endpoint for the model (`None` if local)."""

    handle: Optional[str] = None
    """The handle for this config, in the format provider/model-name."""
