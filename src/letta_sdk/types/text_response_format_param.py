# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TextResponseFormatParam"]


class TextResponseFormatParam(TypedDict, total=False):
    type: Literal["text"]
    """The type of the response format."""
