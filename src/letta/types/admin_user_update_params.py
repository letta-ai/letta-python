# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AdminUserUpdateParams"]


class AdminUserUpdateParams(TypedDict, total=False):
    id: Required[str]
    """The id of the user to update."""

    name: Optional[str]
    """The new name of the user."""

    organization_id: Optional[str]
    """The new organization id of the user."""
