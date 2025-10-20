# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .agents.job_type import JobType
from .stop_reason_type import StopReasonType
from .agents.job_status import JobStatus

__all__ = ["Job"]


class Job(BaseModel):
    id: Optional[str] = None
    """The human-friendly ID of the Job"""

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
    """The type of the job."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    metadata: Optional[Dict[str, object]] = None
    """The metadata of the job."""

    status: Optional[JobStatus] = None
    """The status of the job."""

    stop_reason: Optional[StopReasonType] = None
    """The reason why the job was stopped."""

    total_duration_ns: Optional[int] = None
    """Total run duration in nanoseconds"""

    ttft_ns: Optional[int] = None
    """Time to first token for a run in nanoseconds"""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
