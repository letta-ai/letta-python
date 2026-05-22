# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    after: Optional[str]
    """Cursor for pagination (tool ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'tool-<uuid4>'
    """

    before: Optional[str]
    """Cursor for pagination (tool ID).

    Returns results relative to this ID in the specified sort order. Expected
    format: 'tool-<uuid4>'
    """

    exclude_tool_types: Optional[SequenceNotStr[str]]
    """Tool type(s) to exclude - accepts repeated params or comma-separated values"""

    limit: Optional[int]
    """Maximum number of tools to return"""

    name: Optional[str]
    """Filter by single tool name"""

    names: Optional[SequenceNotStr[str]]
    """Filter by specific tool names"""

    order: Literal["asc", "desc"]
    """Sort order for tools by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    return_only_letta_tools: Optional[bool]
    """Return only tools with tool*type starting with 'letta*'"""

    search: Optional[str]
    """Search tool names (case-insensitive partial match)"""

    tool_ids: Optional[SequenceNotStr[str]]
    """Filter by specific tool IDs - accepts repeated params or comma-separated values"""

    tool_types: Optional[SequenceNotStr[str]]
    """Filter by tool type(s) - accepts repeated params or comma-separated values"""
