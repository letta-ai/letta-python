# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JsonSchemaResponseFormat"]


class JsonSchemaResponseFormat(BaseModel):
    json_schema: Dict[str, object]
    """The JSON schema of the response."""

    type: Optional[Literal["json_schema"]] = None
    """The type of the response format."""
