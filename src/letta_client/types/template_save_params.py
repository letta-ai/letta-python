# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TemplateSaveParams"]


class TemplateSaveParams(TypedDict, total=False):
    block_reconciliation_strategy: Literal["reconcile-all", "preserve-deleted"]
    """
    Strategy for reconciling memory blocks during migration: "reconcile-all" deletes
    blocks not in the template, "preserve-deleted" keeps them. Defaults to
    "preserve-deleted".
    """

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

    preserve_sources_on_migration: bool
    """
    If true, existing agent folders/sources will be preserved and merged with
    template sources during migration. If false, agent sources will be replaced with
    template sources.
    """
