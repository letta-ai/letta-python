# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ToolCreateParams"]


class ToolCreateParams(TypedDict, total=False):
    source_code: Required[str]
    """The source code of the function."""

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
    """The name of the function (auto-generated from source_code if not provided)."""

    source_type: str
    """The source type of the function."""

    tags: List[str]
    """Metadata tags."""

    user_id: str
