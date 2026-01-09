# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ScheduleCreateParams",
    "Message",
    "MessageContentUnionMember0",
    "MessageContentUnionMember0UnionMember0",
    "MessageContentUnionMember0UnionMember1",
    "MessageContentUnionMember0UnionMember1Source",
    "Schedule",
    "ScheduleUnionMember0",
    "ScheduleUnionMember1",
]


class ScheduleCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    schedule: Required[Schedule]

    callback_url: str

    include_return_message_types: List[
        Literal[
            "system_message",
            "user_message",
            "assistant_message",
            "reasoning_message",
            "hidden_reasoning_message",
            "tool_call_message",
            "tool_return_message",
            "approval_request_message",
            "approval_response_message",
        ]
    ]

    max_steps: float


class MessageContentUnionMember0UnionMember0(TypedDict, total=False):
    text: Required[str]

    signature: Optional[str]

    type: Literal["text"]


class MessageContentUnionMember0UnionMember1Source(TypedDict, total=False):
    data: Required[str]

    media_type: Required[str]

    detail: str

    type: Literal["base64"]


class MessageContentUnionMember0UnionMember1(TypedDict, total=False):
    source: Required[MessageContentUnionMember0UnionMember1Source]

    type: Required[Literal["image"]]


MessageContentUnionMember0: TypeAlias = Union[
    MessageContentUnionMember0UnionMember0, MessageContentUnionMember0UnionMember1
]


class Message(TypedDict, total=False):
    content: Required[Union[Iterable[MessageContentUnionMember0], str]]

    role: Required[Literal["user", "assistant", "system"]]

    name: str

    otid: str

    sender_id: str

    type: Literal["message"]


class ScheduleUnionMember0(TypedDict, total=False):
    scheduled_at: Required[float]

    type: Literal["one-time"]


class ScheduleUnionMember1(TypedDict, total=False):
    cron_expression: Required[str]

    type: Required[Literal["recurring"]]


Schedule: TypeAlias = Union[ScheduleUnionMember0, ScheduleUnionMember1]
