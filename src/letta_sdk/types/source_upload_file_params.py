# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes
from .duplicate_file_handling import DuplicateFileHandling

__all__ = ["SourceUploadFileParams"]


class SourceUploadFileParams(TypedDict, total=False):
    file: Required[FileTypes]

    duplicate_handling: DuplicateFileHandling
    """How to handle duplicate filenames"""

    name: Optional[str]
    """Optional custom name to override the uploaded file's name"""
