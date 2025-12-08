# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["OmittedReasoningContentParam"]


class OmittedReasoningContentParam(TypedDict, total=False):
    """
    A placeholder for reasoning content we know is present, but isn't returned by the provider (e.g. OpenAI GPT-5 on ChatCompletions)
    """

    signature: Optional[str]
    """A unique identifier for this reasoning step."""

    type: Literal["omitted_reasoning"]
    """Indicates this is an omitted reasoning step."""
