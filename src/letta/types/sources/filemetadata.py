# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Filemetadata"]


class Filemetadata(BaseModel):
    source_id: str
    """The unique identifier of the source associated with the document."""

    id: Optional[str] = None
    """The human-friendly ID of the File"""

    created_at: Optional[datetime] = None
    """The creation date of the file."""

    file_creation_date: Optional[str] = None
    """The creation date of the file."""

    file_last_modified_date: Optional[str] = None
    """The last modified date of the file."""

    file_name: Optional[str] = None
    """The name of the file."""

    file_path: Optional[str] = None
    """The path to the file."""

    file_size: Optional[int] = None
    """The size of the file in bytes."""

    file_type: Optional[str] = None
    """The type of the file (MIME type)."""

    is_deleted: Optional[bool] = None
    """Whether this file is deleted or not."""

    organization_id: Optional[str] = None
    """The unique identifier of the organization associated with the document."""

    updated_at: Optional[datetime] = None
    """The update date of the file."""
