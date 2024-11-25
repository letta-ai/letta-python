# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LabelUpdateParams"]


class LabelUpdateParams(TypedDict, total=False):
    current_label: Required[str]
    """Current label of the block."""

    new_label: Required[str]
    """New label of the block."""

    user_id: str
