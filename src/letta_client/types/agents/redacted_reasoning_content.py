# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

__all__ = ["RedactedReasoningContent"]

class RedactedReasoningContent(BaseModel):
    """Sent via the Anthropic Messages API"""
    data: str
    """The redacted or filtered intermediate reasoning content."""

    type: Optional[Literal["redacted_reasoning"]] = None
    """Indicates this is a redacted thinking step."""