# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .npm_requirement_param import NpmRequirementParam
from .pip_requirement_param import PipRequirementParam

__all__ = ["ToolRunParams"]


class ToolRunParams(TypedDict, total=False):
    args: Required[Dict[str, object]]
    """The arguments to pass to the tool."""

    source_code: Required[str]
    """The source code of the function."""

    args_json_schema: Optional[Dict[str, object]]
    """The args JSON schema of the function."""

    env_vars: Dict[str, str]
    """The environment variables to pass to the tool."""

    json_schema: Optional[Dict[str, object]]
    """
    The JSON schema of the function (auto-generated from source_code if not
    provided)
    """

    name: Optional[str]
    """The name of the tool to run."""

    npm_requirements: Optional[Iterable[NpmRequirementParam]]
    """Optional list of npm packages required by this tool."""

    pip_requirements: Optional[Iterable[PipRequirementParam]]
    """Optional list of pip packages required by this tool."""

    source_type: Optional[str]
    """The type of the source code."""
