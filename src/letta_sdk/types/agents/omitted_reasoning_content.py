# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OmittedReasoningContent"]


class OmittedReasoningContent(BaseModel):
    type: Optional[Literal["omitted_reasoning"]] = None
    """Indicates this is an omitted reasoning step."""
