# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .npm_requirement_param import NpmRequirementParam
from .pip_requirement_param import PipRequirementParam

__all__ = ["ToolUpsertParams"]


class ToolUpsertParams(TypedDict, total=False):
    source_code: Required[str]
    """The source code of the function."""

    args_json_schema: Optional[Dict[str, object]]
    """The args JSON schema of the function."""

    default_requires_approval: Optional[bool]
    """Whether or not to require approval before executing this tool."""

    description: Optional[str]
    """The description of the tool."""

    json_schema: Optional[Dict[str, object]]
    """
    The JSON schema of the function (auto-generated from source_code if not
    provided)
    """

    npm_requirements: Optional[Iterable[NpmRequirementParam]]
    """Optional list of npm packages required by this tool."""

    pip_requirements: Optional[Iterable[PipRequirementParam]]
    """Optional list of pip packages required by this tool."""

    return_char_limit: int
    """The maximum number of characters in the response."""

    source_type: str
    """The source type of the function."""

    tags: Optional[SequenceNotStr[str]]
    """Metadata tags."""
