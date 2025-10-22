# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolCallContentParam"]


class ToolCallContentParam(TypedDict, total=False):
    id: Required[str]
    """A unique identifier for this specific tool call instance."""

    input: Required[Dict[str, object]]
    """
    The parameters being passed to the tool, structured as a dictionary of parameter
    names to values.
    """

    name: Required[str]
    """The name of the tool being called."""

    signature: Optional[str]
    """Stores a unique identifier for any reasoning associated with this tool call."""

    type: Literal["tool_call"]
    """Indicates this content represents a tool call event."""
