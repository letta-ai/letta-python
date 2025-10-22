# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ToolReturnParam"]


class ToolReturnParam(TypedDict, total=False):
    status: Required[Literal["success", "error"]]

    tool_call_id: Required[str]

    tool_return: Required[str]

    stderr: Optional[SequenceNotStr[str]]

    stdout: Optional[SequenceNotStr[str]]

    type: Literal["tool"]
    """The message type to be created."""
