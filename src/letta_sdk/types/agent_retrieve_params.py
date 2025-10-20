# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AgentRetrieveParams"]


class AgentRetrieveParams(TypedDict, total=False):
    include_relationships: Optional[SequenceNotStr[str]]
    """
    Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
    in the response. If not provided, all relationships are loaded by default. Using
    this can optimize performance by reducing unnecessary joins.
    """
