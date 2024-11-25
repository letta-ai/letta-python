# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LlmconfigParam"]


class LlmconfigParam(TypedDict, total=False):
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
