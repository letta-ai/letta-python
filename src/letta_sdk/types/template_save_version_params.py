# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TemplateSaveVersionParams"]


class TemplateSaveVersionParams(TypedDict, total=False):
    project: Required[str]

    message: str
    """A message to describe the changes made in this template version"""

    migrate_agents: bool
    """
    If true, existing agents attached to this template will be migrated to the new
    template version
    """

    preserve_core_memories_on_migration: bool
    """
    If true, the core memories will be preserved in the template version when
    migrating agents
    """

    preserve_environment_variables_on_migration: bool
    """
    If true, the environment variables will be preserved in the template version
    when migrating agents
    """
