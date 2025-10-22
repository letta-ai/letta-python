# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RequiredBeforeExitToolRuleParam"]


class RequiredBeforeExitToolRuleParam(TypedDict, total=False):
    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str]
    """Optional template string (ignored)."""

    type: Literal["required_before_exit"]
