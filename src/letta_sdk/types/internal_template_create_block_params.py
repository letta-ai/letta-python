# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["InternalTemplateCreateBlockParams"]


class InternalTemplateCreateBlockParams(TypedDict, total=False):
    base_template_id: Required[str]
    """The id of the base template."""

    deployment_id: Required[str]
    """The id of the deployment."""

    entity_id: Required[str]
    """The id of the entity within the template."""

    label: Required[str]
    """Label of the block."""

    template_id: Required[str]
    """The id of the template."""

    value: Required[str]
    """Value of the block."""

    description: Optional[str]
    """Description of the block."""

    hidden: Optional[bool]
    """If set to True, the block will be hidden."""

    is_template: bool

    limit: int
    """Character limit of the block."""

    metadata: Optional[Dict[str, object]]
    """Metadata of the block."""

    name: Optional[str]
    """Name of the block if it is a template."""

    preserve_on_migration: Optional[bool]
    """Preserve the block on template migration."""

    project_id: Optional[str]
    """The associated project id."""

    read_only: bool
    """Whether the agent has read-only access to the block."""
