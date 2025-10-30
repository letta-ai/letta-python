# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["FileListResponse", "File"]


class File(BaseModel):
    id: str
    """Unique identifier of the file-agent relationship"""

    file_id: str
    """Unique identifier of the file"""

    file_name: str
    """Name of the file"""

    folder_id: str
    """Unique identifier of the folder/source"""

    folder_name: str
    """Name of the folder/source"""

    is_open: bool
    """Whether the file is currently open in the agent's context"""

    end_line: Optional[int] = None
    """Ending line number if file was opened with line range"""

    last_accessed_at: Optional[datetime] = None
    """Timestamp of last access by the agent"""

    start_line: Optional[int] = None
    """Starting line number if file was opened with line range"""

    visible_content: Optional[str] = None
    """Portion of the file visible to the agent if open"""


class FileListResponse(BaseModel):
    files: List[File]
    """List of file attachments for the agent"""

    has_more: bool
    """Whether more results exist after this page"""

    next_cursor: Optional[str] = None
    """Cursor for fetching the next page (file-agent relationship ID)"""
