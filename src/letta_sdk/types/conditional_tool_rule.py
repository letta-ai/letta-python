# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConditionalToolRule"]


class ConditionalToolRule(BaseModel):
    child_output_mapping: Dict[str, str]
    """The output case to check for mapping"""

    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    default_child: Optional[str] = None
    """The default child tool to be called. If None, any tool can be called."""

    prompt_template: Optional[str] = None
    """Optional template string (ignored)."""

    require_output_mapping: Optional[bool] = None
    """Whether to throw an error when output doesn't match any case"""

    type: Optional[Literal["conditional"]] = None
