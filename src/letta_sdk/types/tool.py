# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_type import ToolType
from .npm_requirement import NpmRequirement
from .pip_requirement import PipRequirement

__all__ = ["Tool"]


class Tool(BaseModel):
    id: Optional[str] = None
    """The human-friendly ID of the Tool"""

    args_json_schema: Optional[Dict[str, object]] = None
    """The args JSON schema of the function."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    default_requires_approval: Optional[bool] = None
    """Default value for whether or not executing this tool requires approval."""

    description: Optional[str] = None
    """The description of the tool."""

    json_schema: Optional[Dict[str, object]] = None
    """The JSON schema of the function."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    metadata: Optional[Dict[str, object]] = FieldInfo(alias="metadata_", default=None)
    """A dictionary of additional metadata for the tool."""

    name: Optional[str] = None
    """The name of the function."""

    npm_requirements: Optional[List[NpmRequirement]] = None
    """Optional list of npm packages required by this tool."""

    pip_requirements: Optional[List[PipRequirement]] = None
    """Optional list of pip packages required by this tool."""

    return_char_limit: Optional[int] = None
    """The maximum number of characters in the response."""

    source_code: Optional[str] = None
    """The source code of the function."""

    source_type: Optional[str] = None
    """The type of the source code."""

    tags: Optional[List[str]] = None
    """Metadata tags."""

    tool_type: Optional[ToolType] = None
    """The type of the tool."""
