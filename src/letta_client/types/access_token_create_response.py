# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccessTokenCreateResponse", "Policy", "PolicyData"]


class PolicyData(BaseModel):
    id: str

    access: List[Literal["read_messages", "write_messages", "read_agent", "write_agent"]]

    type: Literal["agent"]


class Policy(BaseModel):
    data: List[PolicyData]

    version: Literal["1"]


class AccessTokenCreateResponse(BaseModel):
    token: str

    expires_at: str = FieldInfo(alias="expiresAt")

    hostname: str

    policy: Policy
