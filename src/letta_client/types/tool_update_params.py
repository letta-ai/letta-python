# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .npm_requirement_param import NpmRequirementParam
from .pip_requirement_param import PipRequirementParam

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    args_json_schema: Optional[Dict[str, object]]
    """The args JSON schema of the function."""

    default_requires_approval: Optional[bool]
    """Whether or not to require approval before executing this tool."""

    description: Optional[str]
    """The description of the tool."""

    enable_parallel_execution: Optional[bool]
    """
    If set to True, then this tool will potentially be executed concurrently with
    other tools. Default False.
    """

    json_schema: Optional[Dict[str, object]]
    """
    The JSON schema of the function (auto-generated from source_code if not
    provided)
    """

    metadata: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="metadata_")]
    """A dictionary of additional metadata for the tool."""

    npm_requirements: Optional[Iterable[NpmRequirementParam]]
    """Optional list of npm packages required by this tool."""

    pip_requirements: Optional[Iterable[PipRequirementParam]]
    """Optional list of pip packages required by this tool."""

    return_char_limit: Optional[int]
    """The maximum number of characters in the response."""

    source_code: Optional[str]
    """The source code of the function."""

    source_type: Optional[str]
    """The type of the source code."""

    tags: Optional[SequenceNotStr[str]]
    """Metadata tags."""
