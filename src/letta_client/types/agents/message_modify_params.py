# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .letta_user_message_content_union_param import LettaUserMessageContentUnionParam
from .letta_assistant_message_content_union_param import LettaAssistantMessageContentUnionParam

__all__ = [
    "MessageModifyParams",
    "UpdateSystemMessage",
    "UpdateUserMessage",
    "UpdateReasoningMessage",
    "UpdateAssistantMessage",
]


class UpdateSystemMessage(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent in the format 'agent-<uuid4>'"""

    content: Required[str]
    """
    The message content sent by the system (can be a string or an array of
    multi-modal content parts)
    """

    message_type: Literal["system_message"]


class UpdateUserMessage(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent in the format 'agent-<uuid4>'"""

    content: Required[Union[Iterable[LettaUserMessageContentUnionParam], str]]
    """
    The message content sent by the user (can be a string or an array of multi-modal
    content parts)
    """

    message_type: Literal["user_message"]


class UpdateReasoningMessage(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent in the format 'agent-<uuid4>'"""

    reasoning: Required[str]

    message_type: Literal["reasoning_message"]


class UpdateAssistantMessage(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent in the format 'agent-<uuid4>'"""

    content: Required[Union[Iterable[LettaAssistantMessageContentUnionParam], str]]
    """
    The message content sent by the assistant (can be a string or an array of
    content parts)
    """

    message_type: Literal["assistant_message"]


MessageModifyParams: TypeAlias = Union[
    UpdateSystemMessage, UpdateUserMessage, UpdateReasoningMessage, UpdateAssistantMessage
]
