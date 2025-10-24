# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequiresApprovalToolRule"]


class RequiresApprovalToolRule(BaseModel):
    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    prompt_template: Optional[str] = None
    """Optional template string (ignored).

    Rendering uses fast built-in formatting for performance.
    """

    type: Optional[Literal["requires_approval"]] = None
