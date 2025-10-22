# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .provider_category import ProviderCategory

__all__ = ["LlmConfigParam"]


class LlmConfigParam(TypedDict, total=False):
    context_window: Required[int]
    """The context window size for the model."""

    model: Required[str]
    """LLM model name."""

    model_endpoint_type: Required[
        Literal[
            "openai",
            "anthropic",
            "google_ai",
            "google_vertex",
            "azure",
            "groq",
            "ollama",
            "webui",
            "webui-legacy",
            "lmstudio",
            "lmstudio-legacy",
            "lmstudio-chatcompletions",
            "llamacpp",
            "koboldcpp",
            "vllm",
            "hugging-face",
            "mistral",
            "together",
            "bedrock",
            "deepseek",
            "xai",
        ]
    ]
    """The endpoint type for the model."""

    compatibility_type: Optional[Literal["gguf", "mlx"]]
    """The framework compatibility type for the model."""

    enable_reasoner: bool
    """
    Whether or not the model should use extended thinking if it is a 'reasoning'
    style model
    """

    frequency_penalty: Optional[float]
    """
    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    From OpenAI: Number between -2.0 and 2.0.
    """

    handle: Optional[str]
    """The handle for this config, in the format provider/model-name."""

    max_reasoning_tokens: int
    """Configurable thinking budget for extended thinking.

    Used for enable_reasoner and also for Google Vertex models like Gemini 2.5
    Flash. Minimum value is 1024 when used with enable_reasoner.
    """

    max_tokens: Optional[int]
    """The maximum number of tokens to generate.

    If not set, the model will use its default value.
    """

    model_endpoint: Optional[str]
    """The endpoint for the model."""

    model_wrapper: Optional[str]
    """The wrapper for the model."""

    provider_category: Optional[ProviderCategory]
    """The provider category for the model."""

    provider_name: Optional[str]
    """The provider name for the model."""

    put_inner_thoughts_in_kwargs: Optional[bool]
    """Puts 'inner_thoughts' as a kwarg in the function call if this is set to True.

    This helps with function calling performance and also the generation of inner
    thoughts.
    """

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]]
    """The reasoning effort to use when generating text reasoning models"""

    temperature: float
    """The temperature to use when generating text with the model.

    A higher temperature will result in more random text.
    """

    tier: Optional[str]
    """The cost tier for the model (cloud only)."""

    verbosity: Optional[Literal["low", "medium", "high"]]
    """Soft control for how verbose model output should be, used for GPT-5 models."""
