# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .identity_type import IdentityType
from .identity_property_param import IdentityPropertyParam

__all__ = ["IdentityModifyParams"]


class IdentityModifyParams(TypedDict, total=False):
    agent_ids: Optional[SequenceNotStr[str]]
    """The agent ids that are associated with the identity."""

    block_ids: Optional[SequenceNotStr[str]]
    """The IDs of the blocks associated with the identity."""

    identifier_key: Optional[str]
    """External, user-generated identifier key of the identity."""

    identity_type: Optional[IdentityType]
    """Enum to represent the type of the identity."""

    name: Optional[str]
    """The name of the identity."""

    properties: Optional[Iterable[IdentityPropertyParam]]
    """List of properties associated with the identity."""
