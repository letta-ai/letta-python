# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SupervisorManagerParam"]


class SupervisorManagerParam(TypedDict, total=False):
    manager_agent_id: Required[str]

    manager_type: Literal["supervisor"]
