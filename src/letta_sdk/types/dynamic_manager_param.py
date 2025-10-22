# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DynamicManagerParam"]


class DynamicManagerParam(TypedDict, total=False):
    manager_agent_id: Required[str]

    manager_type: Literal["dynamic"]

    max_turns: Optional[int]

    termination_token: Optional[str]
