# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MaxCountPerStepToolRule"]


class MaxCountPerStepToolRule(BaseModel):
    max_count_limit: int
    """
    The max limit for the total number of times this tool can be invoked in a single
    step.
    """

    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str] = None
    """Optional template string (ignored)."""

    type: Optional[Literal["max_count_per_step"]] = None
