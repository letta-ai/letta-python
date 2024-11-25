# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """The description of the tool."""

    json_schema: Optional[object]
    """
    The JSON schema of the function (auto-generated from source_code if not
    provided)
    """

    module: Optional[str]
    """The source code of the function."""

    name: Optional[str]
    """The name of the function."""

    source_code: Optional[str]
    """The source code of the function."""

    source_type: Optional[str]
    """The type of the source code."""

    tags: Optional[List[str]]
    """Metadata tags."""
