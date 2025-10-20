# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "GroupUpdateParams",
    "ManagerConfig",
    "ManagerConfigRoundRobinManagerUpdate",
    "ManagerConfigSupervisorManagerUpdate",
    "ManagerConfigDynamicManagerUpdate",
    "ManagerConfigSleeptimeManagerUpdate",
    "ManagerConfigVoiceSleeptimeManagerUpdate",
]


class GroupUpdateParams(TypedDict, total=False):
    agent_ids: Optional[SequenceNotStr[str]]

    description: Optional[str]

    manager_config: Optional[ManagerConfig]

    project_id: Optional[str]
    """The associated project id."""

    shared_block_ids: Optional[SequenceNotStr[str]]

    x_project: Annotated[str, PropertyInfo(alias="X-Project")]
    """The project slug to associate with the group (cloud only)."""


class ManagerConfigRoundRobinManagerUpdate(TypedDict, total=False):
    manager_type: Literal["round_robin"]

    max_turns: Optional[int]


class ManagerConfigSupervisorManagerUpdate(TypedDict, total=False):
    manager_agent_id: Required[Optional[str]]

    manager_type: Literal["supervisor"]


class ManagerConfigDynamicManagerUpdate(TypedDict, total=False):
    manager_agent_id: Optional[str]

    manager_type: Literal["dynamic"]

    max_turns: Optional[int]

    termination_token: Optional[str]


class ManagerConfigSleeptimeManagerUpdate(TypedDict, total=False):
    manager_agent_id: Optional[str]

    manager_type: Literal["sleeptime"]

    sleeptime_agent_frequency: Optional[int]


class ManagerConfigVoiceSleeptimeManagerUpdate(TypedDict, total=False):
    manager_agent_id: Optional[str]

    manager_type: Literal["voice_sleeptime"]

    max_message_buffer_length: Optional[int]
    """The desired maximum length of messages in the context window of the convo agent.

    This is a best effort, and may be off slightly due to user/assistant
    interleaving.
    """

    min_message_buffer_length: Optional[int]
    """The desired minimum length of messages in the context window of the convo agent.

    This is a best effort, and may be off-by-one due to user/assistant interleaving.
    """


ManagerConfig: TypeAlias = Union[
    ManagerConfigRoundRobinManagerUpdate,
    ManagerConfigSupervisorManagerUpdate,
    ManagerConfigDynamicManagerUpdate,
    ManagerConfigSleeptimeManagerUpdate,
    ManagerConfigVoiceSleeptimeManagerUpdate,
]
