# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing_extensions import Literal

__all__ = ["TerminalToolRule"]

class TerminalToolRule(BaseModel):
    """
    Represents a terminal tool rule configuration where if this tool gets called, it must end the agent loop.
    """
    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str] = None
    """Optional template string (ignored)."""

    type: Optional[Literal["exit_loop"]] = None