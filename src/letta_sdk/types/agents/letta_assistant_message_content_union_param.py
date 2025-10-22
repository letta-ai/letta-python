# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LettaAssistantMessageContentUnionParam"]


class LettaAssistantMessageContentUnionParam(TypedDict, total=False):
    text: Required[str]
    """The text content of the message."""

    type: Literal["text"]
    """The type of the message."""
