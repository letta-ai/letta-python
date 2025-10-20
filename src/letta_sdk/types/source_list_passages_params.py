# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SourceListPassagesParams"]


class SourceListPassagesParams(TypedDict, total=False):
    after: Optional[str]
    """Message after which to retrieve the returned messages."""

    before: Optional[str]
    """Message before which to retrieve the returned messages."""

    limit: int
    """Maximum number of messages to retrieve."""
