# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OrganizationSourcesStats", "Source", "SourceFile"]


class SourceFile(BaseModel):
    file_id: str
    """Unique identifier of the file"""

    file_name: str
    """Name of the file"""

    file_size: Optional[int] = None
    """Size of the file in bytes"""


class Source(BaseModel):
    source_id: str
    """Unique identifier of the source"""

    source_name: str
    """Name of the source"""

    file_count: Optional[int] = None
    """Number of files in the source"""

    files: Optional[List[SourceFile]] = None
    """List of file statistics"""

    total_size: Optional[int] = None
    """Total size of all files in bytes"""


class OrganizationSourcesStats(BaseModel):
    sources: Optional[List[Source]] = None
    """List of source metadata"""

    total_files: Optional[int] = None
    """Total number of files across all sources"""

    total_size: Optional[int] = None
    """Total size of all files in bytes"""

    total_sources: Optional[int] = None
    """Total number of sources"""
