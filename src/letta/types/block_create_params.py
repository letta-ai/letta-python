# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BlockCreateParams"]


class BlockCreateParams(TypedDict, total=False):
    label: Required[str]
    """Label of the block."""

    value: Required[str]
    """Value of the block."""

    description: Optional[str]
    """Description of the block."""

    is_template: bool

    limit: int
    """Character limit of the block."""

    metadata: Annotated[Optional[object], PropertyInfo(alias="metadata_")]
    """Metadata of the block."""

    name: Optional[str]
    """Name of the block if it is a template."""
