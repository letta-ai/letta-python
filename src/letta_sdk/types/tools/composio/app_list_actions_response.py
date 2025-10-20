# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "AppListActionsResponse",
    "AppListActionsResponseItem",
    "AppListActionsResponseItemParameters",
    "AppListActionsResponseItemResponse",
]


class AppListActionsResponseItemParameters(BaseModel):
    properties: Dict[str, object]

    title: str

    type: str

    examples: Optional[List[object]] = None

    required: Optional[List[str]] = None


class AppListActionsResponseItemResponse(BaseModel):
    properties: Dict[str, object]

    title: str

    type: str

    examples: Optional[List[object]] = None

    required: Optional[List[str]] = None


class AppListActionsResponseItem(BaseModel):
    app_id: str = FieldInfo(alias="appId")

    app_name: str = FieldInfo(alias="appName")

    available_versions: List[str]

    description: str

    name: str

    parameters: AppListActionsResponseItemParameters
    """Action parameter data models."""

    response: AppListActionsResponseItemResponse
    """Action response data model."""

    tags: List[str]

    version: str

    display_name: Optional[str] = None

    enabled: Optional[bool] = None

    logo: Optional[str] = None


AppListActionsResponse: TypeAlias = List[AppListActionsResponseItem]
