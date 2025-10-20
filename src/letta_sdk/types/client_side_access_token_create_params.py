# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClientSideAccessTokenCreateParams", "Policy"]


class ClientSideAccessTokenCreateParams(TypedDict, total=False):
    hostname: Required[str]
    """The hostname of the client side application.

    Please specify the full URL including the protocol (http or https).
    """

    policy: Required[Iterable[Policy]]

    expires_at: str
    """The expiration date of the token.

    If not provided, the token will expire in 5 minutes
    """


class Policy(TypedDict, total=False):
    id: Required[str]

    access: Required[List[Literal["read_messages", "write_messages", "read_agent", "write_agent"]]]

    type: Required[Literal["agent"]]
