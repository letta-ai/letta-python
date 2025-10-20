# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["DeploymentListEntitiesParams"]


class DeploymentListEntitiesParams(TypedDict, total=False):
    entity_types: Optional[SequenceNotStr[str]]
    """Filter by entity types (block, agent, group)"""
