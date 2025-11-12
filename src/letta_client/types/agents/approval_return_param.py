# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ApprovalReturnParam"]


class ApprovalReturnParam(TypedDict, total=False):
    approve: Required[bool]
    """Whether the tool has been approved"""

    tool_call_id: Required[str]
    """The ID of the tool call that corresponds to this approval"""

    reason: Optional[str]
    """An optional explanation for the provided approval status"""

    type: Literal["approval"]
    """The message type to be created."""
