# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSearchParams"]


class MessageSearchParams(TypedDict, total=False):
    query: Required[str]
    """Text query for full-text search"""

    agent_id: Optional[str]
    """Filter messages by agent ID"""

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter messages created on or before this date"""

    limit: int
    """Maximum number of results to return"""

    search_mode: Literal["vector", "fts", "hybrid"]
    """Search mode to use"""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter messages created after this date"""
