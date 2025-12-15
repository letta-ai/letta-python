# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .tool_return import ToolReturn
from .approval_return import ApprovalReturn

__all__ = ["ApprovalResponseMessage", "Approval"]

Approval: TypeAlias = Annotated[Union[ApprovalReturn, ToolReturn], PropertyInfo(discriminator="type")]


class ApprovalResponseMessage(BaseModel):
    """
    A message representing a response form the user indicating whether a tool has been approved to run.

    Args:
        id (str): The ID of the message
        date (datetime): The date the message was created in ISO format
        name (Optional[str]): The name of the sender of the message
        approve: (bool) Whether the tool has been approved
        approval_request_id: The ID of the approval request
        reason: (Optional[str]) An optional explanation for the provided approval status
    """

    id: str

    date: datetime

    approval_request_id: Optional[str] = None
    """The message ID of the approval request"""

    approvals: Optional[List[Approval]] = None
    """The list of approval responses"""

    approve: Optional[bool] = None
    """Whether the tool has been approved"""

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
