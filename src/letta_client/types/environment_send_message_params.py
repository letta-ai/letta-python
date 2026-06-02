# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "EnvironmentSendMessageParams",
    "Message",
    "MessageUnionMember0",
    "MessageUnionMember0ContentUnionMember1",
    "MessageUnionMember1",
    "MessageUnionMember1Approval",
    "MessageUnionMember1ApprovalUnionMember0",
    "MessageUnionMember1ApprovalUnionMember0ToolReturnUnionMember1",
    "MessageUnionMember1ApprovalUnionMember1",
]


class EnvironmentSendMessageParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    conversation_id: Annotated[Optional[str], PropertyInfo(alias="conversationId")]


class MessageUnionMember0ContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageUnionMember0(TypedDict, total=False):
    client_message_id: Required[str]

    content: Required[Union[str, Iterable[MessageUnionMember0ContentUnionMember1]]]

    role: Required[Literal["user"]]

    otid: str


class MessageUnionMember1ApprovalUnionMember0ToolReturnUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageUnionMember1ApprovalUnionMember0(TypedDict, total=False):
    status: Required[Literal["success", "error"]]

    tool_call_id: Required[str]

    tool_return: Required[Union[str, Iterable[MessageUnionMember1ApprovalUnionMember0ToolReturnUnionMember1]]]

    stderr: Optional[SequenceNotStr[str]]

    stdout: Optional[SequenceNotStr[str]]

    type: Literal["tool"]


class MessageUnionMember1ApprovalUnionMember1(TypedDict, total=False):
    approve: Required[bool]

    tool_call_id: Required[str]

    reason: Optional[str]

    type: Literal["approval"]

    updated_input: Optional[Dict[str, object]]


MessageUnionMember1Approval: TypeAlias = Union[
    MessageUnionMember1ApprovalUnionMember0, MessageUnionMember1ApprovalUnionMember1
]


class MessageUnionMember1(TypedDict, total=False):
    approvals: Required[Iterable[MessageUnionMember1Approval]]

    type: Required[Literal["approval"]]


Message: TypeAlias = Union[MessageUnionMember0, MessageUnionMember1]
