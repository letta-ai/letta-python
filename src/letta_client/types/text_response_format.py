# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TextResponseFormat"]


class TextResponseFormat(BaseModel):
    type: Optional[Literal["text"]] = None
    """The type of the response format."""
