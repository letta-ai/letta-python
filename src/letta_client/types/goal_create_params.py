# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GoalCreateParams"]


class GoalCreateParams(TypedDict, total=False):
    description: Required[str]

    agent_id: Optional[str]

    conversation_id: Optional[str]

    status: Literal["active", "completed", "cancelled"]
