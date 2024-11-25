# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Llmconfig"]


class Llmconfig(BaseModel):
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
