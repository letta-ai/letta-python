# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .message_type import MessageType
from ..stop_reason_type import StopReasonType

__all__ = ["Run", "RequestConfig"]


class RequestConfig(BaseModel):
    assistant_message_tool_kwarg: Optional[str] = None
    """The name of the message argument in the designated message tool."""

    assistant_message_tool_name: Optional[str] = None
    """The name of the designated message tool."""

    include_return_message_types: Optional[List[MessageType]] = None
    """Only return specified message types in the response.

    If `None` (default) returns all messages.
    """

    use_assistant_message: Optional[bool] = None
    """
    Whether the server should parse specific tool call arguments (default
    `send_message`) as `AssistantMessage` objects.
    """


class Run(BaseModel):
    agent_id: str
    """The unique identifier of the agent associated with the run."""

    id: Optional[str] = None
    """The human-friendly ID of the Run"""

    background: Optional[bool] = None
    """Whether the run was created in background mode."""

    base_template_id: Optional[str] = None
    """The base template ID that the run belongs to."""

    callback_error: Optional[str] = None
    """Optional error message from attempting to POST the callback endpoint."""

    callback_sent_at: Optional[datetime] = None
    """Timestamp when the callback was last attempted."""

    callback_status_code: Optional[int] = None
    """HTTP status code returned by the callback endpoint."""

    callback_url: Optional[str] = None
    """If set, POST to this URL when the run completes."""

    completed_at: Optional[datetime] = None
    """The timestamp when the run was completed."""

    created_at: Optional[datetime] = None
    """The timestamp when the run was created."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata for the run."""

    request_config: Optional[RequestConfig] = None
    """The request configuration for the run."""

    status: Optional[Literal["created", "running", "completed", "failed", "cancelled"]] = None
    """The current status of the run."""

    stop_reason: Optional[StopReasonType] = None
    """The reason why the run was stopped."""

    total_duration_ns: Optional[int] = None
    """Total run duration in nanoseconds"""

    ttft_ns: Optional[int] = None
    """Time to first token for a run in nanoseconds"""
