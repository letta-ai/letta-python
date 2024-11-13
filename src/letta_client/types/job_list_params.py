# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    source_id: Optional[str]
    """Only list jobs associated with the source."""

    user_id: str
