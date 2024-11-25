# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    cursor: Optional[str]

    limit: Optional[int]

    user_id: str
