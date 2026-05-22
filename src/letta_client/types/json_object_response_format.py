# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JsonObjectResponseFormat"]


class JsonObjectResponseFormat(BaseModel):
    """Response format for JSON object responses."""

    type: Optional[Literal["json_object"]] = None
    """The type of the response format."""
