# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TextContent"]


class TextContent(BaseModel):
    text: str
    """The text content of the message."""

    signature: Optional[str] = None
    """Stores a unique identifier for any reasoning associated with this text content."""

    type: Optional[Literal["text"]] = None
    """The type of the message."""
