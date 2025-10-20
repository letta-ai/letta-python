# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConditionalToolRuleParam"]


class ConditionalToolRuleParam(TypedDict, total=False):
    child_output_mapping: Required[Dict[str, str]]
    """The output case to check for mapping"""

    tool_name: Required[str]
    """The name of the tool. Must exist in the database for the user's organization."""

    default_child: Optional[str]
    """The default child tool to be called. If None, any tool can be called."""

    prompt_template: Optional[str]
    """Optional template string (ignored)."""

    require_output_mapping: bool
    """Whether to throw an error when output doesn't match any case"""

    type: Literal["conditional"]
