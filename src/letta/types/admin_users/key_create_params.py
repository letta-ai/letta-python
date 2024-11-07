# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    user_id: Required[str]
    """The unique identifier of the user associated with the token."""

    name: Optional[str]
    """Name of the token."""
