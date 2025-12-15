# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RequiresApprovalToolRuleParam"]


class RequiresApprovalToolRuleParam(TypedDict, total=False):
    """
    Represents a tool rule configuration which requires approval before the tool can be invoked.
    """

    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str]
    """Optional template string (ignored).

    Rendering uses fast built-in formatting for performance.
    """

    type: Literal["requires_approval"]
