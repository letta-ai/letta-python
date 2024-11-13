# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceDetachParams"]


class SourceDetachParams(TypedDict, total=False):
    agent_id: Required[str]
    """The unique identifier of the agent to detach the source from."""

    user_id: str
