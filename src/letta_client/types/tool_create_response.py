# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolCreateResponse"]


class ToolCreateResponse(BaseModel):
    name: str
    """The name of the function."""

    source_code: str
    """The source code of the function."""

    tags: List[str]
    """Metadata tags."""

    id: Optional[str] = None
    """The human-friendly ID of the Tool"""

    description: Optional[str] = None
    """The description of the tool."""

    json_schema: Optional[object] = None
    """The JSON schema of the function."""

    module: Optional[str] = None
    """The module of the function."""

    source_type: Optional[str] = None
    """The type of the source code."""

    user_id: Optional[str] = None
    """The unique identifier of the user associated with the function."""
