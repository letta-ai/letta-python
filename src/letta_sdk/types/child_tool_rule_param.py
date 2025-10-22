# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ChildToolRuleParam"]


class ChildToolRuleParam(TypedDict, total=False):
    children: Required[SequenceNotStr[str]]
    """The children tools that can be invoked."""

    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str]
    """Optional template string (ignored)."""

    type: Literal["constrain_child_tools"]
