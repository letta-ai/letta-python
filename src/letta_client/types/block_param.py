# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BlockParam"]


class BlockParam(TypedDict, total=False):
    value: Required[str]
    """Value of the block."""

    id: str
    """The human-friendly ID of the Block"""

    description: Optional[str]
    """Description of the block."""

    label: Optional[str]
    """Label of the block (e.g. 'human', 'persona')."""

    limit: int
    """Character limit of the block."""

    metadata: Annotated[Optional[object], PropertyInfo(alias="metadata_")]
    """Metadata of the block."""

    name: Optional[str]
    """Name of the block."""

    template: bool
    """Whether the block is a template (e.g. saved human/persona options)."""

    user_id: Optional[str]
    """The unique identifier of the user associated with the block."""
