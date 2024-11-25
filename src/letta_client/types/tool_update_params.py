# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the tool."""

    description: Optional[str]
    """The description of the tool."""

    json_schema: Optional[object]
    """The JSON schema of the function."""

    module: Optional[str]
    """The module of the function."""

    name: Optional[str]
    """The name of the function."""

    source_code: Optional[str]
    """The source code of the function."""

    source_type: Optional[str]
    """The type of the source code."""

    tags: Optional[List[str]]
    """Metadata tags."""

    terminal: Optional[bool]
    """Whether the tool is a terminal tool (allow requesting heartbeats)."""

    body_user_id: Annotated[Optional[str], PropertyInfo(alias="user_id")]
    """The unique identifier of the user associated with the function."""

    header_user_id: Annotated[str, PropertyInfo(alias="user_id")]
