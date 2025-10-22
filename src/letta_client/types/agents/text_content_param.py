# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextContentParam"]


class TextContentParam(TypedDict, total=False):
    text: Required[str]
    """The text content of the message."""

    signature: Optional[str]
    """Stores a unique identifier for any reasoning associated with this text content."""

    type: Literal["text"]
    """The type of the message."""
