# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ParentToolRule"]


class ParentToolRule(BaseModel):
    """
    A ToolRule that only allows a child tool to be called if the parent has been called.
    """

    children: List[str]
    """The children tools that can be invoked."""

    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str] = None
    """Optional template string (ignored)."""

    type: Optional[Literal["parent_last_tool"]] = None
