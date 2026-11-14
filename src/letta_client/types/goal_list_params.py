# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["GoalListParams"]


class GoalListParams(TypedDict, total=False):
    after: str

    agent_id: Optional[str]

    conversation_id: Optional[str]

    limit: int

    status: Literal["active", "completed", "cancelled"]
