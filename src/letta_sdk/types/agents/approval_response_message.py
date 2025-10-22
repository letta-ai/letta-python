# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ApprovalResponseMessage"]


class ApprovalResponseMessage(BaseModel):
    id: str

    approval_request_id: str
    """The message ID of the approval request"""

    approve: bool
    """Whether the tool has been approved"""

    date: datetime

    is_err: Optional[bool] = None

    message_type: Optional[Literal["approval_response_message"]] = None
    """The type of the message."""

    name: Optional[str] = None

    otid: Optional[str] = None

    reason: Optional[str] = None
    """An optional explanation for the provided approval status"""

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None
