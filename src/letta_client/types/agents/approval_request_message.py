# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from . import tool_call
from ..._models import BaseModel
from .tool_call_delta import ToolCallDelta

__all__ = ["ApprovalRequestMessage", "ToolCall", "ToolCalls"]

ToolCall: TypeAlias = Union[tool_call.ToolCall, ToolCallDelta]

ToolCalls: TypeAlias = Union[List[tool_call.ToolCall], ToolCallDelta, None]


class ApprovalRequestMessage(BaseModel):
    id: str

    date: datetime

    tool_call: ToolCall
    """The tool call that has been requested by the llm to run"""

    is_err: Optional[bool] = None

    message_type: Optional[Literal["approval_request_message"]] = None
    """The type of the message."""

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None

    tool_calls: Optional[ToolCalls] = None
    """
    The tool calls that have been requested by the llm to run, which are pending
    approval
    """
