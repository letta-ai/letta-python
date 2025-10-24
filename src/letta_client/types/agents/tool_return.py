# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolReturn"]


class ToolReturn(BaseModel):
    status: Literal["success", "error"]

    tool_call_id: str

    tool_return: str

    stderr: Optional[List[str]] = None

    stdout: Optional[List[str]] = None

    type: Optional[Literal["tool"]] = None
    """The message type to be created."""
