# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ToolCountParams"]


class ToolCountParams(TypedDict, total=False):
    exclude_letta_tools: Optional[bool]
    """Exclude built-in Letta tools from the count"""

    exclude_tool_types: Optional[SequenceNotStr[str]]
    """Tool type(s) to exclude - accepts repeated params or comma-separated values"""

    name: Optional[str]

    names: Optional[SequenceNotStr[str]]
    """Filter by specific tool names"""

    return_only_letta_tools: Optional[bool]
    """Count only tools with tool*type starting with 'letta*'"""

    search: Optional[str]
    """Search tool names (case-insensitive partial match)"""

    tool_ids: Optional[SequenceNotStr[str]]
    """Filter by specific tool IDs - accepts repeated params or comma-separated values"""

    tool_types: Optional[SequenceNotStr[str]]
    """Filter by tool type(s) - accepts repeated params or comma-separated values"""
