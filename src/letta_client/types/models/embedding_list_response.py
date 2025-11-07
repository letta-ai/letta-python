# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..provider_type import ProviderType

__all__ = ["EmbeddingListResponse", "EmbeddingListResponseItem"]


class EmbeddingListResponseItem(BaseModel):
    display_name: str
    """Display name for the model shown in UI"""

    embedding_dim: int
    """The dimension of the embedding"""

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
    """Deprecated: Use 'provider_type' field instead.

    The endpoint type for the embedding model.
    """

    embedding_model: str
    """Deprecated: Use 'name' field instead. Embedding model name."""

    name: str
    """The actual model name used by the provider"""

    provider_name: str
    """The name of the provider"""

    provider_type: ProviderType
    """The type of the provider"""

    azure_deployment: Optional[str] = None
    """Deprecated: The Azure deployment for the model."""

    azure_endpoint: Optional[str] = None
    """Deprecated: The Azure endpoint for the model."""

    azure_version: Optional[str] = None
    """Deprecated: The Azure version for the model."""

    batch_size: Optional[int] = None
    """Deprecated: The maximum batch size for processing embeddings."""

    embedding_chunk_size: Optional[int] = None
    """Deprecated: The chunk size of the embedding."""

    embedding_endpoint: Optional[str] = None
    """Deprecated: The endpoint for the model."""

    handle: Optional[str] = None
    """The handle for this config, in the format provider/model-name."""

    api_model_type: Optional[Literal["embedding"]] = FieldInfo(alias="model_type", default=None)
    """Type of model (llm or embedding)"""


EmbeddingListResponse: TypeAlias = List[EmbeddingListResponseItem]
