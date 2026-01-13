# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BlockCreateParams"]


class BlockCreateParams(TypedDict, total=False):
    label: Required[str]
    """Label of the block."""

    value: Required[str]
    """Value of the block."""

    base_template_id: Optional[str]
    """The base template id of the block."""

    deployment_id: Optional[str]
    """The id of the deployment."""

    description: Optional[str]
    """Description of the block."""

    entity_id: Optional[str]
    """The id of the entity within the template."""

    hidden: Optional[bool]
    """If set to True, the block will be hidden."""

    is_template: bool

    limit: int
    """Character limit of the block."""

    metadata: Optional[Dict[str, object]]
    """Metadata of the block."""

    preserve_on_migration: Optional[bool]
    """Preserve the block on template migration."""

    project_id: Optional[str]
    """The associated project id."""

    read_only: bool
    """Whether the agent has read-only access to the block."""

    tags: Optional[SequenceNotStr[str]]
    """The tags to associate with the block."""

    template_id: Optional[str]
    """The id of the template."""

    template_name: Optional[str]
    """Name of the block if it is a template."""
