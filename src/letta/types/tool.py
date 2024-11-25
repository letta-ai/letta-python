# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Tool"]


class Tool(BaseModel):
    source_code: str
    """The source code of the function."""

    id: Optional[str] = None
    """The human-friendly ID of the Tool"""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    description: Optional[str] = None
    """The description of the tool."""

    json_schema: Optional[object] = None
    """The JSON schema of the function."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    module: Optional[str] = None
    """The module of the function."""

    name: Optional[str] = None
    """The name of the function."""

    organization_id: Optional[str] = None
    """The unique identifier of the organization associated with the tool."""

    source_type: Optional[str] = None
    """The type of the source code."""

    tags: Optional[List[str]] = None
    """Metadata tags."""
