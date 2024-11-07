# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BlockUpdateParams"]


class BlockUpdateParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the block."""

    description: Optional[str]
    """Description of the block."""

    label: str
    """Label of the block (e.g. 'human', 'persona') in the context window."""

    limit: Optional[int]
    """Character limit of the block."""

    metadata: Annotated[Optional[object], PropertyInfo(alias="metadata_")]
    """Metadata of the block."""

    template: bool
    """Whether the block is a template (e.g. saved human/persona options)."""

    template_name: Optional[str]
    """Name of the block if it is a template."""

    user_id: Optional[str]
    """The unique identifier of the user associated with the block."""

    value: Optional[str]
    """Value of the block."""
