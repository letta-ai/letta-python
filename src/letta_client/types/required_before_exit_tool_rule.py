# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing_extensions import Literal

__all__ = ["RequiredBeforeExitToolRule"]

class RequiredBeforeExitToolRule(BaseModel):
    """
    Represents a tool rule configuration where this tool must be called before the agent loop can exit.
    """
    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str] = None
    """Optional template string (ignored)."""

    type: Optional[Literal["required_before_exit"]] = None