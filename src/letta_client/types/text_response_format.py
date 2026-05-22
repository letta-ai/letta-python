# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing_extensions import Literal

__all__ = ["TextResponseFormat"]

class TextResponseFormat(BaseModel):
    """Response format for plain text responses."""
    type: Optional[Literal["text"]] = None
    """The type of the response format."""