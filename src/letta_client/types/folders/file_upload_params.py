# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from ..._types import FileTypes

from typing import Optional

__all__ = ["FileUploadParams"]

class FileUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    duplicate_handling: Literal["skip", "error", "suffix", "replace"]
    """How to handle duplicate filenames"""

    name: Optional[str]
    """Optional custom name to override the uploaded file's name"""