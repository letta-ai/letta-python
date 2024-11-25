# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LimitUpdateParams"]


class LimitUpdateParams(TypedDict, total=False):
    label: Required[str]
    """Label of the block."""

    limit: Required[int]
    """New limit of the block."""
