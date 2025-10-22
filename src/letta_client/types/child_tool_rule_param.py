# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ChildToolRuleParam", "ChildArgNode"]


class ChildArgNode(TypedDict, total=False):
    name: Required[str]
    """The name of the child tool to invoke next."""

    args: Optional[Dict[str, object]]
    """Optional prefilled arguments for this child tool.

    Keys must match the tool's parameter names and values must satisfy the tool's
    JSON schema. Supports partial prefill; non-overlapping parameters are left to
    the model.
    """


class ChildToolRuleParam(TypedDict, total=False):
    children: Required[SequenceNotStr[str]]
    """The children tools that can be invoked."""

    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    child_arg_nodes: Optional[Iterable[ChildArgNode]]
    """Optional list of typed child argument overrides.

    Each node must reference a child in 'children'.
    """

    prompt_template: Optional[str]
    """Optional template string (ignored)."""

    type: Literal["constrain_child_tools"]
