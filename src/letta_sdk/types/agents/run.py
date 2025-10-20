# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .job_type import JobType
from ..._models import BaseModel
from .job_status import JobStatus
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
    id: Optional[str] = None
    """The human-friendly ID of the Run"""

    callback_error: Optional[str] = None
    """Optional error message from attempting to POST the callback endpoint."""

    callback_sent_at: Optional[datetime] = None
    """Timestamp when the callback was last attempted."""

    callback_status_code: Optional[int] = None
    """HTTP status code returned by the callback endpoint."""

    callback_url: Optional[str] = None
    """If set, POST to this URL when the job completes."""

    completed_at: Optional[datetime] = None
    """The unix timestamp of when the job was completed."""

    created_at: Optional[datetime] = None
    """The unix timestamp of when the job was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    job_type: Optional[JobType] = None

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    metadata: Optional[Dict[str, object]] = None
    """The metadata of the job."""

    request_config: Optional[RequestConfig] = None
    """The request configuration for the run."""

    status: Optional[JobStatus] = None
    """The status of the job."""

    stop_reason: Optional[StopReasonType] = None
    """The reason why the run was stopped."""

    total_duration_ns: Optional[int] = None
    """Total run duration in nanoseconds"""

    ttft_ns: Optional[int] = None
    """Time to first token for a run in nanoseconds"""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
