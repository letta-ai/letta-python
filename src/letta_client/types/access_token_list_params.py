# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccessTokenListParams"]


class AccessTokenListParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """The agent ID to filter tokens by.

    If provided, only tokens for this agent will be returned.
    """

    limit: float
    """The number of tokens to return per page. Defaults to 10."""

    offset: float
    """The offset for pagination. Defaults to 0."""
