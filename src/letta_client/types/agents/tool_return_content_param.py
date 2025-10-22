# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolReturnContentParam"]


class ToolReturnContentParam(TypedDict, total=False):
    content: Required[str]
    """The content returned by the tool execution."""

    is_error: Required[bool]
    """Indicates whether the tool execution resulted in an error."""

    tool_call_id: Required[str]
    """References the ID of the ToolCallContent that initiated this tool call."""

    type: Literal["tool_return"]
    """Indicates this content represents a tool return event."""
