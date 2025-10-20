# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TemplateCreateAgentsParams", "InitialMessageSequence"]


class TemplateCreateAgentsParams(TypedDict, total=False):
    project: Required[str]

    agent_name: str
    """The name of the agent, optional otherwise a random one will be assigned"""

    identity_ids: SequenceNotStr[str]
    """The identity ids to assign to the agent"""

    initial_message_sequence: Iterable[InitialMessageSequence]
    """
    Set an initial sequence of messages, if not provided, the agent will start with
    the default message sequence, if an empty array is provided, the agent will
    start with no messages
    """

    memory_variables: Dict[str, str]
    """The memory variables to assign to the agent"""

    tags: SequenceNotStr[str]
    """The tags to assign to the agent"""

    tool_variables: Dict[str, str]
    """The tool variables to assign to the agent"""


class InitialMessageSequence(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["user", "system", "assistant"]]

    batch_item_id: Optional[str]

    group_id: Optional[str]

    name: Optional[str]

    otid: Optional[str]

    sender_id: Optional[str]
