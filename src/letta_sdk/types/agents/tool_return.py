# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolReturn"]


class ToolReturn(BaseModel):
    status: Literal["success", "error"]
    """The status of the tool call"""

    stderr: Optional[List[str]] = None
    """Captured stderr from the tool invocation"""

    stdout: Optional[List[str]] = None
    """Captured stdout (e.g. prints, logs) from the tool invocation"""
