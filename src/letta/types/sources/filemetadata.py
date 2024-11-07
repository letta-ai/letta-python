# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Filemetadata"]


class Filemetadata(BaseModel):
    source_id: str
    """The unique identifier of the source associated with the document."""

    user_id: str
    """The unique identifier of the user associated with the document."""

    id: Optional[str] = None
    """The human-friendly ID of the File"""

    created_at: Optional[datetime] = None
    """The creation date of this file metadata object."""

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

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
