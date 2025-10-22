# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["RoundRobinManagerParam"]


class RoundRobinManagerParam(TypedDict, total=False):
    manager_type: Literal["round_robin"]

    max_turns: Optional[int]
