# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChildToolRule"]


class ChildToolRule(BaseModel):
    children: List[str]
    """The children tools that can be invoked."""

    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str] = None
    """Optional template string (ignored)."""

    type: Optional[Literal["constrain_child_tools"]] = None
