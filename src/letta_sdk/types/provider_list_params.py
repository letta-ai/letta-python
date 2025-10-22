# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .provider_type import ProviderType

__all__ = ["ProviderListParams"]


class ProviderListParams(TypedDict, total=False):
    after: Optional[str]
    """Provider ID cursor for pagination.

    Returns providers that come after this provider ID in the specified sort order
    """

    before: Optional[str]
    """Provider ID cursor for pagination.

    Returns providers that come before this provider ID in the specified sort order
    """

    limit: Optional[int]
    """Maximum number of providers to return"""

    name: Optional[str]
    """Filter providers by name"""

    order: Literal["asc", "desc"]
    """Sort order for providers by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    provider_type: Optional[ProviderType]
    """Filter providers by type"""
