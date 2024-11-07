# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AdminUserCreateParams"]


class AdminUserCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the user."""

    organization_id: Required[str]
    """The organization id of the user."""
