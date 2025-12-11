# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RedactedReasoningContentParam"]


class RedactedReasoningContentParam(TypedDict, total=False):
    """Sent via the Anthropic Messages API"""

    data: Required[str]
    """The redacted or filtered intermediate reasoning content."""

    type: Literal["redacted_reasoning"]
    """Indicates this is a redacted thinking step."""
