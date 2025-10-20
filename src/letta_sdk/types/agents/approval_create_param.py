# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ApprovalCreateParam"]


class ApprovalCreateParam(TypedDict, total=False):
    approval_request_id: Required[str]
    """The message ID of the approval request"""

    approve: Required[bool]
    """Whether the tool has been approved"""

    reason: Optional[str]
    """An optional explanation for the provided approval status"""

    type: Literal["approval"]
    """The message type to be created."""
