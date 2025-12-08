# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InitToolRule"]


class InitToolRule(BaseModel):
    """Represents the initial tool rule configuration."""

    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""

    args: Optional[Dict[str, object]] = None
    """Optional prefilled arguments for this tool.

    When present, these values will override any LLM-provided arguments with the
    same keys during invocation. Keys must match the tool's parameter names and
    values must satisfy the tool's JSON schema. Supports partial prefill;
    non-overlapping parameters are left to the model.
    """

    prompt_template: Optional[str] = None
    """Optional template string (ignored).

    Rendering uses fast built-in formatting for performance.
    """

    type: Optional[Literal["run_first"]] = None
