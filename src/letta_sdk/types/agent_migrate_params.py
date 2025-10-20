# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentMigrateParams"]


class AgentMigrateParams(TypedDict, total=False):
    preserve_core_memories: Required[bool]

    to_template: Required[str]

    preserve_tool_variables: bool
    """
    If true, preserves the existing agent's tool environment variables instead of
    using the template's variables
    """
