# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ApprovalReturn"]


class ApprovalReturn(BaseModel):
    approve: bool
    """Whether the tool has been approved"""

    tool_call_id: str
    """The ID of the tool call that corresponds to this approval"""

    reason: Optional[str] = None
    """An optional explanation for the provided approval status"""

    type: Optional[Literal["approval"]] = None
    """The message type to be created."""
