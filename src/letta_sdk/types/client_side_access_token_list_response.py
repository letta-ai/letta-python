# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ClientSideAccessTokenListResponse", "Token", "TokenPolicy", "TokenPolicyData"]


class TokenPolicyData(BaseModel):
    id: str

    access: List[Literal["read_messages", "write_messages", "read_agent", "write_agent"]]

    type: Literal["agent"]


class TokenPolicy(BaseModel):
    data: List[TokenPolicyData]

    version: Literal["1"]


class Token(BaseModel):
    token: str

    expires_at: str = FieldInfo(alias="expiresAt")

    hostname: str

    policy: TokenPolicy


class ClientSideAccessTokenListResponse(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    tokens: List[Token]
