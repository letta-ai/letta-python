# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ParentToolRuleParam"]


class ParentToolRuleParam(TypedDict, total=False):
    """
    A ToolRule that only allows a child tool to be called if the parent has been called.
    """

    children: Required[SequenceNotStr[str]]
    """The children tools that can be invoked."""

    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str]
    """Optional template string (ignored)."""

    type: Literal["parent_last_tool"]
