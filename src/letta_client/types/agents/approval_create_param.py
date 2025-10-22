# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ApprovalCreateParam", "Approval", "ApprovalApprovalReturn", "ApprovalLettaSchemasLettaMessageToolReturn"]


class ApprovalApprovalReturn(TypedDict, total=False):
    approve: Required[bool]
    """Whether the tool has been approved"""

    tool_call_id: Required[str]
    """The ID of the tool call that corresponds to this approval"""

    reason: Optional[str]
    """An optional explanation for the provided approval status"""

    type: Literal["approval"]
    """The message type to be created."""


class ApprovalLettaSchemasLettaMessageToolReturn(TypedDict, total=False):
    status: Required[Literal["success", "error"]]

    tool_call_id: Required[str]

    tool_return: Required[str]

    stderr: Optional[SequenceNotStr[str]]

    stdout: Optional[SequenceNotStr[str]]

    type: Literal["tool"]
    """The message type to be created."""


Approval: TypeAlias = Union[ApprovalApprovalReturn, ApprovalLettaSchemasLettaMessageToolReturn]


class ApprovalCreateParam(TypedDict, total=False):
    approval_request_id: Optional[str]
    """The message ID of the approval request"""

    approvals: Optional[Iterable[Approval]]
    """The list of approval responses"""

    approve: Optional[bool]
    """Whether the tool has been approved"""

    reason: Optional[str]
    """An optional explanation for the provided approval status"""

    type: Literal["approval"]
    """The message type to be created."""
