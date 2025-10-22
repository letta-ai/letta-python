# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolReturnMessage", "ToolReturn"]


class ToolReturn(BaseModel):
    status: Literal["success", "error"]

    tool_call_id: str

    tool_return: str

    stderr: Optional[List[str]] = None

    stdout: Optional[List[str]] = None

    type: Optional[Literal["tool"]] = None
    """The message type to be created."""


class ToolReturnMessage(BaseModel):
    id: str

    date: datetime

    status: Literal["success", "error"]

    tool_call_id: str

    tool_return: str

    is_err: Optional[bool] = None

    message_type: Optional[Literal["tool_return_message"]] = None
    """The type of the message."""

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    stderr: Optional[List[str]] = None

    stdout: Optional[List[str]] = None

    step_id: Optional[str] = None

    tool_returns: Optional[List[ToolReturn]] = None
