# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileUploadResponse"]


class FileUploadResponse(BaseModel):
    source_id: str
    """The unique identifier of the source associated with the document."""

    id: Optional[str] = None
    """The human-friendly ID of the File"""

    chunks_embedded: Optional[int] = None
    """Number of chunks that have been embedded."""

    content: Optional[str] = None
    """
    Optional full-text content of the file; only populated on demand due to its
    size.
    """

    created_at: Optional[datetime] = None
    """The creation date of the file."""

    error_message: Optional[str] = None
    """Optional error message if the file failed processing."""

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

    original_file_name: Optional[str] = None
    """The original name of the file as uploaded."""

    processing_status: Optional[Literal["pending", "parsing", "embedding", "completed", "error"]] = None
    """The current processing status of the file (e.g.

    pending, parsing, embedding, completed, error).
    """

    total_chunks: Optional[int] = None
    """Total number of chunks for the file."""

    updated_at: Optional[datetime] = None
    """The update date of the file."""
