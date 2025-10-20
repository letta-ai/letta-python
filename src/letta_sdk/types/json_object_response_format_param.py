# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["JsonObjectResponseFormatParam"]


class JsonObjectResponseFormatParam(TypedDict, total=False):
    type: Literal["json_object"]
    """The type of the response format."""
