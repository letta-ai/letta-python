# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentListParams"]


class EnvironmentListParams(TypedDict, total=False):
    after: str

    connection_name: Annotated[str, PropertyInfo(alias="connectionName")]
    """Filter by exact computer name."""

    device_id: Annotated[str, PropertyInfo(alias="deviceId")]
    """Filter by the stable device identifier."""

    instance_id: Annotated[str, PropertyInfo(alias="instanceId")]
    """Filter by the stable listener instance identifier."""

    limit: str

    online_only: Annotated[str, PropertyInfo(alias="onlineOnly")]

    pagination_order: Annotated[Literal["id"], PropertyInfo(alias="paginationOrder")]

    search: str
    """Filter by computer name (case-insensitive substring)."""

    source: Literal["local", "remote"]

    user_id: Annotated[str, PropertyInfo(alias="userId")]
