# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .identity_type import IdentityType
from .identity_property_param import IdentityPropertyParam

__all__ = ["IdentityUpsertParams"]


class IdentityUpsertParams(TypedDict, total=False):
    identifier_key: Required[str]
    """External, user-generated identifier key of the identity."""

    identity_type: Required[IdentityType]
    """The type of the identity."""

    name: Required[str]
    """The name of the identity."""

    agent_ids: Optional[SequenceNotStr[str]]
    """The agent ids that are associated with the identity."""

    block_ids: Optional[SequenceNotStr[str]]
    """The IDs of the blocks associated with the identity."""

    project_id: Optional[str]
    """The project id of the identity, if applicable."""

    properties: Optional[Iterable[IdentityPropertyParam]]
    """List of properties associated with the identity."""

    x_project: Annotated[str, PropertyInfo(alias="X-Project")]
    """The project slug to associate with the identity (cloud only)."""
