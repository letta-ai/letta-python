# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .identity_type import IdentityType

__all__ = ["IdentityListParams"]


class IdentityListParams(TypedDict, total=False):
    after: Optional[str]
    """Identity ID cursor for pagination.

    Returns identities that come after this identity ID in the specified sort order
    """

    before: Optional[str]
    """Identity ID cursor for pagination.

    Returns identities that come before this identity ID in the specified sort order
    """

    identifier_key: Optional[str]

    identity_type: Optional[IdentityType]
    """Enum to represent the type of the identity."""

    limit: Optional[int]
    """Maximum number of identities to return"""

    name: Optional[str]

    order: Literal["asc", "desc"]
    """Sort order for identities by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    project_id: Optional[str]
