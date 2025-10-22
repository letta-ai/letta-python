# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContinueToolRule"]


class ContinueToolRule(BaseModel):
    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str] = None
    """Optional template string (ignored)."""

    type: Optional[Literal["continue_loop"]] = None
