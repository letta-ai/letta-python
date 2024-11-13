# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "MessageRetrieveResponse",
    "MessageListResponse",
    "MessageListResponseToolCall",
    "MessageListResponseToolCallFunction",
    "LettaMessageListResponse",
    "LettaMessageListResponseSystemMessageOutput",
    "LettaMessageListResponseUserMessageOutput",
    "LettaMessageListResponseInternalMonologue",
    "LettaMessageListResponseFunctionCallMessage",
    "LettaMessageListResponseFunctionCallMessageFunctionCall",
    "LettaMessageListResponseFunctionCallMessageFunctionCallLettaSchemasLettaMessageFunctionCall",
    "LettaMessageListResponseFunctionCallMessageFunctionCallFunctionCallDelta",
    "LettaMessageListResponseFunctionReturn",
    "LettaMessageListResponseAssistantMessageOutput",
]


class MessageListResponseToolCallFunction(BaseModel):
    arguments: str
    """The arguments to pass to the function (JSON dump)"""

    name: str
    """The name of the function to call"""


class MessageListResponseToolCall(BaseModel):
    id: str
    """The ID of the tool call"""

    function: MessageListResponseToolCallFunction
    """The arguments and name for the function"""

    type: Optional[str] = None


class MessageListResponse(BaseModel):
    role: Literal["assistant", "user", "tool", "function", "system"]
    """The role of the participant."""

    id: Optional[str] = None
    """The human-friendly ID of the Message"""

    agent_id: Optional[str] = None
    """The unique identifier of the agent."""

    created_at: Optional[datetime] = None
    """The time the message was created."""

    model: Optional[str] = None
    """The model used to make the function call."""

    name: Optional[str] = None
    """The name of the participant."""

    text: Optional[str] = None
    """The text of the message."""

    tool_call_id: Optional[str] = None
    """The id of the tool call."""

    tool_calls: Optional[List[MessageListResponseToolCall]] = None
    """The list of tool calls requested."""

    user_id: Optional[str] = None
    """The unique identifier of the user."""


class LettaMessageListResponseSystemMessageOutput(BaseModel):
    id: str

    date: datetime

    message: str

    message_type: Optional[Literal["system_message"]] = None


class LettaMessageListResponseUserMessageOutput(BaseModel):
    id: str

    date: datetime

    message: str

    message_type: Optional[Literal["user_message"]] = None


class LettaMessageListResponseInternalMonologue(BaseModel):
    id: str

    date: datetime

    internal_monologue: str

    message_type: Optional[Literal["internal_monologue"]] = None


class LettaMessageListResponseFunctionCallMessageFunctionCallLettaSchemasLettaMessageFunctionCall(BaseModel):
    arguments: str

    function_call_id: str

    name: str


class LettaMessageListResponseFunctionCallMessageFunctionCallFunctionCallDelta(BaseModel):
    arguments: Optional[str] = None

    function_call_id: Optional[str] = None

    name: Optional[str] = None


LettaMessageListResponseFunctionCallMessageFunctionCall: TypeAlias = Union[
    LettaMessageListResponseFunctionCallMessageFunctionCallLettaSchemasLettaMessageFunctionCall,
    LettaMessageListResponseFunctionCallMessageFunctionCallFunctionCallDelta,
]


class LettaMessageListResponseFunctionCallMessage(BaseModel):
    id: str

    date: datetime

    function_call: LettaMessageListResponseFunctionCallMessageFunctionCall

    message_type: Optional[Literal["function_call"]] = None


class LettaMessageListResponseFunctionReturn(BaseModel):
    id: str

    date: datetime

    function_call_id: str

    function_return: str

    status: Literal["success", "error"]

    message_type: Optional[Literal["function_return"]] = None


class LettaMessageListResponseAssistantMessageOutput(BaseModel):
    id: str

    assistant_message: str

    date: datetime

    message_type: Optional[Literal["assistant_message"]] = None


LettaMessageListResponse: TypeAlias = Annotated[
    Union[
        LettaMessageListResponseSystemMessageOutput,
        LettaMessageListResponseUserMessageOutput,
        LettaMessageListResponseInternalMonologue,
        LettaMessageListResponseFunctionCallMessage,
        LettaMessageListResponseFunctionReturn,
        LettaMessageListResponseAssistantMessageOutput,
    ],
    PropertyInfo(discriminator="message_type"),
]

MessageRetrieveResponse: TypeAlias = Union[List[MessageListResponse], List[LettaMessageListResponse]]
