# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RunListStepsParams"]


class RunListStepsParams(TypedDict, total=False):
    after: Optional[str]
    """Cursor for pagination"""

    before: Optional[str]
    """Cursor for pagination"""

    limit: Optional[int]
    """Maximum number of messages to return"""

    order: str
    """Sort order by the created_at timestamp of the objects.

    asc for ascending order and desc for descending order.
    """
