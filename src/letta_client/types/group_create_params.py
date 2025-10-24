# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .dynamic_manager_param import DynamicManagerParam
from .sleeptime_manager_param import SleeptimeManagerParam
from .supervisor_manager_param import SupervisorManagerParam
from .round_robin_manager_param import RoundRobinManagerParam
from .voice_sleeptime_manager_param import VoiceSleeptimeManagerParam

__all__ = ["GroupCreateParams", "ManagerConfig"]


class GroupCreateParams(TypedDict, total=False):
    agent_ids: Required[SequenceNotStr[str]]

    description: Required[str]

    hidden: Optional[bool]
    """If set to True, the group will be hidden."""

    manager_config: ManagerConfig

    project_id: Optional[str]
    """The associated project id."""

    shared_block_ids: SequenceNotStr[str]

    x_project: Annotated[str, PropertyInfo(alias="X-Project")]
    """The project slug to associate with the group (cloud only)."""


ManagerConfig: TypeAlias = Union[
    RoundRobinManagerParam,
    SupervisorManagerParam,
    DynamicManagerParam,
    SleeptimeManagerParam,
    VoiceSleeptimeManagerParam,
]
