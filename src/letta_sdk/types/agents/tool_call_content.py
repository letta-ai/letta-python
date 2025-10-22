# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolCallContent"]


class ToolCallContent(BaseModel):
    id: str
    """A unique identifier for this specific tool call instance."""

    input: Dict[str, object]
    """
    The parameters being passed to the tool, structured as a dictionary of parameter
    names to values.
    """

    name: str
    """The name of the tool being called."""

    type: Optional[Literal["tool_call"]] = None
    """Indicates this content represents a tool call event."""
