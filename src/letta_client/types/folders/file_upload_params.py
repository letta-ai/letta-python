# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    duplicate_handling: Literal["skip", "error", "suffix", "replace"]
    """How to handle duplicate filenames"""

    name: Optional[str]
    """Optional custom name to override the uploaded file's name"""
