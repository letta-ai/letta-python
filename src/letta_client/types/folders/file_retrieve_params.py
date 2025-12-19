# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileRetrieveParams"]


class FileRetrieveParams(TypedDict, total=False):
    folder_id: Required[str]
    """The ID of the source in the format 'source-<uuid4>'"""

    include_content: bool
    """Whether to include full file content"""
