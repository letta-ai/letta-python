# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TextContent"]


class TextContent(BaseModel):
    text: str
    """The text content of the message."""

    type: Optional[Literal["text"]] = None
    """The type of the message."""
