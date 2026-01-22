# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PassageSearchParams"]


class PassageSearchParams(TypedDict, total=False):
    agent_id: Optional[str]
    """Filter passages by agent ID"""

    archive_id: Optional[str]
    """Filter passages by archive ID"""

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter results to passages created before this datetime"""

    limit: int
    """Maximum number of results to return"""

    query: Optional[str]
    """Text query for semantic search"""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter results to passages created after this datetime"""

    tag_match_mode: Literal["any", "all"]
    """
    How to match tags - 'any' to match passages with any of the tags, 'all' to match
    only passages with all tags
    """

    tags: Optional[SequenceNotStr[str]]
    """Optional list of tags to filter search results"""
