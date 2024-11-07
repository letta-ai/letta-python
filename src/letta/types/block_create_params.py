# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BlockCreateParams"]


class BlockCreateParams(TypedDict, total=False):
    label: Required[str]
    """Label of the block."""

    description: Optional[str]
    """Description of the block."""

    limit: int
    """Character limit of the block."""

    metadata: Annotated[Optional[object], PropertyInfo(alias="metadata_")]
    """Metadata of the block."""

    name: Optional[str]
    """Name of the block if it is a template."""

    template: bool

    body_user_id: Annotated[Optional[str], PropertyInfo(alias="user_id")]
    """The unique identifier of the user associated with the block."""

    value: Optional[str]
    """Value of the block."""

    header_user_id: Annotated[str, PropertyInfo(alias="user_id")]
