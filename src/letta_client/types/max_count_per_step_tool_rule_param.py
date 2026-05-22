# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MaxCountPerStepToolRuleParam"]


class MaxCountPerStepToolRuleParam(TypedDict, total=False):
    """
    Represents a tool rule configuration which constrains the total number of times this tool can be invoked in a single step.
    """

    max_count_limit: Required[int]
    """
    The max limit for the total number of times this tool can be invoked in a single
    step.
    """

    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str]
    """Optional template string (ignored)."""

    type: Literal["max_count_per_step"]
