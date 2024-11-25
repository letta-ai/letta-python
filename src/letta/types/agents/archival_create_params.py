# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ArchivalCreateParams"]


class ArchivalCreateParams(TypedDict, total=False):
    text: Required[str]
    """Text to write to archival memory."""
