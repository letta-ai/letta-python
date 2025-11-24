# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AnthropicModelSettingsParam", "Thinking"]


class Thinking(TypedDict, total=False):
    budget_tokens: int
    """The maximum number of tokens the model can use for extended thinking."""

    type: Literal["enabled", "disabled"]
    """The type of thinking to use."""


class AnthropicModelSettingsParam(TypedDict, total=False):
    effort: Optional[Literal["low", "medium", "high"]]
    """Effort level for Opus 4.5 model (controls token conservation).

    Not setting this gives similar performance to 'high'.
    """

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: bool
    """Whether to enable parallel tool calling."""

    provider_type: Literal["anthropic"]
    """The type of the provider."""

    temperature: float
    """The temperature of the model."""

    thinking: Thinking
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]]
    """Soft control for how verbose model output should be, used for GPT-5 models."""
