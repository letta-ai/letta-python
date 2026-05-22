# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContinueToolRuleParam"]


class ContinueToolRuleParam(TypedDict, total=False):
    """
    Represents a tool rule configuration where if this tool gets called, it must continue the agent loop.
    """

    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str]
    """Optional template string (ignored)."""

    type: Literal["continue_loop"]
