# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Job"]


class Job(BaseModel):
    user_id: str
    """The unique identifier of the user associated with the job."""

    id: Optional[str] = None
    """The human-friendly ID of the Job"""

    completed_at: Optional[datetime] = None
    """The unix timestamp of when the job was completed."""

    created_at: Optional[datetime] = None
    """The unix timestamp of when the job was created."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """The metadata of the job."""

    status: Optional[Literal["created", "running", "completed", "failed", "pending"]] = None
    """The status of the job."""
