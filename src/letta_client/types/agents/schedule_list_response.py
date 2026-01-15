# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ScheduleListResponse",
    "ScheduledMessage",
    "ScheduledMessageMessage",
    "ScheduledMessageMessageMessage",
    "ScheduledMessageMessageMessageContentUnionMember0",
    "ScheduledMessageMessageMessageContentUnionMember0UnionMember0",
    "ScheduledMessageMessageMessageContentUnionMember0UnionMember1",
    "ScheduledMessageMessageMessageContentUnionMember0UnionMember1Source",
    "ScheduledMessageSchedule",
    "ScheduledMessageScheduleUnionMember0",
    "ScheduledMessageScheduleUnionMember1",
]


class ScheduledMessageMessageMessageContentUnionMember0UnionMember0(BaseModel):
    text: str

    signature: Optional[str] = None

    type: Optional[Literal["text"]] = None


class ScheduledMessageMessageMessageContentUnionMember0UnionMember1Source(BaseModel):
    data: str

    media_type: str

    detail: Optional[str] = None

    type: Optional[Literal["base64"]] = None


class ScheduledMessageMessageMessageContentUnionMember0UnionMember1(BaseModel):
    source: ScheduledMessageMessageMessageContentUnionMember0UnionMember1Source

    type: Literal["image"]


ScheduledMessageMessageMessageContentUnionMember0: TypeAlias = Union[
    ScheduledMessageMessageMessageContentUnionMember0UnionMember0,
    ScheduledMessageMessageMessageContentUnionMember0UnionMember1,
]


class ScheduledMessageMessageMessage(BaseModel):
    content: Union[List[ScheduledMessageMessageMessageContentUnionMember0], str]

    role: Literal["user", "assistant", "system"]

    name: Optional[str] = None

    otid: Optional[str] = None

    sender_id: Optional[str] = None

    type: Optional[Literal["message"]] = None


class ScheduledMessageMessage(BaseModel):
    messages: List[ScheduledMessageMessageMessage]

    callback_url: Optional[str] = None

    include_return_message_types: Optional[
        List[
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
    ] = None

    max_steps: Optional[float] = None


class ScheduledMessageScheduleUnionMember0(BaseModel):
    scheduled_at: float

    type: Optional[Literal["one-time"]] = None


class ScheduledMessageScheduleUnionMember1(BaseModel):
    cron_expression: str

    type: Literal["recurring"]


ScheduledMessageSchedule: TypeAlias = Union[ScheduledMessageScheduleUnionMember0, ScheduledMessageScheduleUnionMember1]


class ScheduledMessage(BaseModel):
    id: str

    agent_id: str

    message: ScheduledMessageMessage

    next_scheduled_time: Optional[str] = None

    schedule: ScheduledMessageSchedule


class ScheduleListResponse(BaseModel):
    has_next_page: bool

    scheduled_messages: List[ScheduledMessage]
