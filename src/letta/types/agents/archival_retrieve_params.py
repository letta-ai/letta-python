# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ArchivalRetrieveParams"]


class ArchivalRetrieveParams(TypedDict, total=False):
    after: Optional[int]
    """Unique ID of the memory to start the query range at."""

    before: Optional[int]
    """Unique ID of the memory to end the query range at."""

    limit: Optional[int]
    """How many results to include in the response."""

    user_id: str
