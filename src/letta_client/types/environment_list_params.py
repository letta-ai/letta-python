# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentListParams"]


class EnvironmentListParams(TypedDict, total=False):
    after: str

    limit: str

    online_only: Annotated[str, PropertyInfo(alias="onlineOnly")]

    source: Literal["local", "remote"]

    user_id: Annotated[str, PropertyInfo(alias="userId")]
