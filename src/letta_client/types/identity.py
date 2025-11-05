# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .identity_type import IdentityType
from .identity_property import IdentityProperty

__all__ = ["Identity"]


class Identity(BaseModel):
    id: str
    """The human-friendly ID of the Identity"""

    agent_ids: List[str]
    """The IDs of the agents associated with the identity."""

    block_ids: List[str]
    """The IDs of the blocks associated with the identity."""

    identifier_key: str
    """External, user-generated identifier key of the identity."""

    identity_type: IdentityType
    """The type of the identity."""

    name: str
    """The name of the identity."""

    project_id: Optional[str] = None
    """The project id of the identity, if applicable."""

    properties: Optional[List[IdentityProperty]] = None
    """List of properties associated with the identity"""
