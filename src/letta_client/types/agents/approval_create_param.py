# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .tool_return_param import ToolReturnParam
from .approval_return_param import ApprovalReturnParam

__all__ = ["ApprovalCreateParam", "Approval"]

Approval: TypeAlias = Union[ApprovalReturnParam, ToolReturnParam]


class ApprovalCreateParam(TypedDict, total=False):
    approval_request_id: Optional[str]
    """The message ID of the approval request"""

    approvals: Optional[Iterable[Approval]]
    """The list of approval responses"""

    approve: Optional[bool]
    """Whether the tool has been approved"""

    group_id: Optional[str]
    """The multi-agent group that the message was sent in"""

    reason: Optional[str]
    """An optional explanation for the provided approval status"""

    type: Literal["approval"]
    """The message type to be created."""
