# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolReturnContent"]


class ToolReturnContent(BaseModel):
    content: str
    """The content returned by the tool execution."""

    is_error: bool
    """Indicates whether the tool execution resulted in an error."""

    tool_call_id: str
    """References the ID of the ToolCallContent that initiated this tool call."""

    type: Optional[Literal["tool_return"]] = None
    """Indicates this content represents a tool return event."""
