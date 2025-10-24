# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SleeptimeManagerParam"]


class SleeptimeManagerParam(TypedDict, total=False):
    manager_agent_id: Required[str]

    manager_type: Literal["sleeptime"]

    sleeptime_agent_frequency: Optional[int]
