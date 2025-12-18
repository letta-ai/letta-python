# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..xai_model_settings_param import XaiModelSettingsParam
from ..groq_model_settings_param import GroqModelSettingsParam
from ..azure_model_settings_param import AzureModelSettingsParam
from ..openai_model_settings_param import OpenAIModelSettingsParam
from ..bedrock_model_settings_param import BedrockModelSettingsParam
from ..deepseek_model_settings_param import DeepseekModelSettingsParam
from ..together_model_settings_param import TogetherModelSettingsParam
from ..anthropic_model_settings_param import AnthropicModelSettingsParam
from ..google_ai_model_settings_param import GoogleAIModelSettingsParam
from ..google_vertex_model_settings_param import GoogleVertexModelSettingsParam

__all__ = ["MessageCompactParams", "CompactionSettings", "CompactionSettingsModelSettings"]


class MessageCompactParams(TypedDict, total=False):
    compaction_settings: Optional[CompactionSettings]
    """Configuration for conversation compaction / summarization.

    `model` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. `"openai/gpt-4o-mini"`). Per-model settings (temperature, max
    tokens, etc.) are derived from the default configuration for that handle.
    """


CompactionSettingsModelSettings: TypeAlias = Union[
    OpenAIModelSettingsParam,
    AnthropicModelSettingsParam,
    GoogleAIModelSettingsParam,
    GoogleVertexModelSettingsParam,
    AzureModelSettingsParam,
    XaiModelSettingsParam,
    GroqModelSettingsParam,
    DeepseekModelSettingsParam,
    TogetherModelSettingsParam,
    BedrockModelSettingsParam,
]


class CompactionSettings(TypedDict, total=False):
    """Configuration for conversation compaction / summarization.

    ``model`` is the only required user-facing field – it specifies the summarizer
    model handle (e.g. ``"openai/gpt-4o-mini"``). Per-model settings (temperature,
    max tokens, etc.) are derived from the default configuration for that handle.
    """

    model: Required[str]
    """Model handle to use for summarization (format: provider/model-name)."""

    clip_chars: Optional[int]
    """The maximum length of the summary in characters.

    If none, no clipping is performed.
    """

    mode: Literal["all", "sliding_window"]
    """The type of summarization technique use."""

    model_settings: Optional[CompactionSettingsModelSettings]
    """Optional model settings used to override defaults for the summarizer model."""

    prompt: str
    """The prompt to use for summarization."""

    prompt_acknowledgement: bool
    """
    Whether to include an acknowledgement post-prompt (helps prevent non-summary
    outputs).
    """

    sliding_window_percentage: float
    """
    The percentage of the context window to keep post-summarization (only used in
    sliding window mode).
    """
