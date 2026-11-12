# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GoalUpdateParams"]


class GoalUpdateParams(TypedDict, total=False):
    description: str

    status: Literal["active", "completed", "cancelled"]
