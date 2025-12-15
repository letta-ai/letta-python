# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChildToolRule", "ChildArgNode"]


class ChildArgNode(BaseModel):
    """Typed child override for prefilled arguments.

    When used in a ChildToolRule, if this child is selected next, its `args` will be
    applied as prefilled arguments (overriding overlapping LLM-provided values).
    """

    name: str
    """The name of the child tool to invoke next."""

    args: Optional[Dict[str, object]] = None
    """Optional prefilled arguments for this child tool.

    Keys must match the tool's parameter names and values must satisfy the tool's
    JSON schema. Supports partial prefill; non-overlapping parameters are left to
    the model.
    """


class ChildToolRule(BaseModel):
    """A ToolRule represents a tool that can be invoked by the agent."""

    children: List[str]
    """The children tools that can be invoked."""

    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    child_arg_nodes: Optional[List[ChildArgNode]] = None
    """Optional list of typed child argument overrides.

    Each node must reference a child in 'children'.
    """

    prompt_template: Optional[str] = None
    """Optional template string (ignored)."""

    type: Optional[Literal["constrain_child_tools"]] = None
