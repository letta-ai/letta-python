# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "AppListResponse",
    "AppListResponseItem",
    "AppListResponseItemAuthScheme",
    "AppListResponseItemAuthSchemeField",
]


class AppListResponseItemAuthSchemeField(BaseModel):
    description: str

    name: str

    type: str

    default: Optional[str] = None

    display_name: Optional[str] = None

    expected_from_customer: Optional[bool] = None

    get_current_user_endpoint: Optional[str] = None

    required: Optional[bool] = None


class AppListResponseItemAuthScheme(BaseModel):
    auth_mode: Literal[
        "OAUTH2",
        "OAUTH1",
        "API_KEY",
        "BASIC",
        "BEARER_TOKEN",
        "BASIC_WITH_JWT",
        "GOOGLE_SERVICE_ACCOUNT",
        "GOOGLEADS_AUTH",
        "NO_AUTH",
        "CALCOM_AUTH",
    ]

    fields: List[AppListResponseItemAuthSchemeField]

    scheme_name: str

    authorization_url: Optional[str] = None

    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    default_scopes: Optional[List[object]] = None

    proxy: Optional[Dict[str, object]] = None

    token_response_metadata: Optional[List[object]] = None

    token_url: Optional[str] = None


class AppListResponseItem(BaseModel):
    app_id: str = FieldInfo(alias="appId")

    categories: List[str]

    description: str

    key: str

    meta: Dict[str, object]

    name: str

    auth_schemes: Optional[List[AppListResponseItemAuthScheme]] = None

    configuration_docs_text: Optional[str] = None

    docs: Optional[str] = None

    documentation_doc_text: Optional[str] = None

    enabled: Optional[bool] = None

    group: Optional[str] = None

    logo: Optional[str] = None

    no_auth: Optional[bool] = None

    status: Optional[str] = None

    test_connectors: Optional[List[Dict[str, object]]] = FieldInfo(alias="testConnectors", default=None)


AppListResponse: TypeAlias = List[AppListResponseItem]
