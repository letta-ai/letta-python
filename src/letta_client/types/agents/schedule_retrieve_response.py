# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ScheduleRetrieveResponse",
    "Message",
    "MessageMessage",
    "MessageMessageContentUnionMember0",
    "MessageMessageContentUnionMember0UnionMember0",
    "MessageMessageContentUnionMember0UnionMember1",
    "MessageMessageContentUnionMember0UnionMember1Source",
    "Schedule",
    "ScheduleUnionMember0",
    "ScheduleUnionMember1",
]


class MessageMessageContentUnionMember0UnionMember0(BaseModel):
    text: str

    signature: Optional[str] = None

    type: Optional[Literal["text"]] = None


class MessageMessageContentUnionMember0UnionMember1Source(BaseModel):
    data: str

    media_type: str

    detail: Optional[str] = None

    type: Optional[Literal["base64"]] = None


class MessageMessageContentUnionMember0UnionMember1(BaseModel):
    source: MessageMessageContentUnionMember0UnionMember1Source

    type: Literal["image"]


MessageMessageContentUnionMember0: TypeAlias = Union[
    MessageMessageContentUnionMember0UnionMember0, MessageMessageContentUnionMember0UnionMember1
]


class MessageMessage(BaseModel):
    content: Union[List[MessageMessageContentUnionMember0], str]

    role: Literal["user", "assistant", "system"]

    name: Optional[str] = None

    otid: Optional[str] = None

    sender_id: Optional[str] = None

    type: Optional[Literal["message"]] = None


class Message(BaseModel):
    messages: List[MessageMessage]

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


class ScheduleUnionMember0(BaseModel):
    scheduled_at: float

    type: Optional[Literal["one-time"]] = None


class ScheduleUnionMember1(BaseModel):
    cron_expression: str

    type: Literal["recurring"]


Schedule: TypeAlias = Union[ScheduleUnionMember0, ScheduleUnionMember1]


class ScheduleRetrieveResponse(BaseModel):
    id: str

    agent_id: str

    message: Message

    next_scheduled_time: Optional[str] = None

    schedule: Schedule

    status: Literal["active", "paused", "completed"]

    use_sandbox: bool

    callback_url: Optional[str] = None

    context_window_limit: Optional[int] = None

    conversation_id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    model: Optional[str] = None

    api_model_settings: Optional[object] = FieldInfo(alias="model_settings", default=None)

    name: Optional[str] = None

    target_device_id: Optional[str] = None
