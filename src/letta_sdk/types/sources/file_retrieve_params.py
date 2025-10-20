# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileRetrieveParams"]


class FileRetrieveParams(TypedDict, total=False):
    source_id: Required[str]

    include_content: bool
    """Whether to include full file content"""
