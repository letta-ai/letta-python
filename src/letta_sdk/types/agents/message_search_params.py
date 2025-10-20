# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from .message_role import MessageRole

__all__ = ["MessageSearchParams"]


class MessageSearchParams(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter messages created on or before this date"""

    limit: int
    """Maximum number of results to return"""

    project_id: Optional[str]
    """Filter messages by project ID"""

    query: Optional[str]
    """Text query for full-text search"""

    roles: Optional[List[MessageRole]]
    """Filter messages by role"""

    search_mode: Literal["vector", "fts", "hybrid"]
    """Search mode to use"""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter messages created after this date"""

    template_id: Optional[str]
    """Filter messages by template ID"""
