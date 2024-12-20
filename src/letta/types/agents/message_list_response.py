# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "MessageListResponse",
    "UnionMember0",
    "UnionMember0ToolCall",
    "UnionMember0ToolCallFunction",
    "UnionMember1",
    "UnionMember1SystemMessageOutput",
    "UnionMember1UserMessageOutput",
    "UnionMember1ReasoningMessage",
    "UnionMember1ToolCallMessage",
    "UnionMember1ToolCallMessageToolCall",
    "UnionMember1ToolCallMessageToolCallLettaSchemasLettaMessageToolCall",
    "UnionMember1ToolCallMessageToolCallToolCallDelta",
    "UnionMember1ToolReturnMessage",
    "UnionMember1AssistantMessageOutput",
]


class UnionMember0ToolCallFunction(BaseModel):
    arguments: str
    """The arguments to pass to the function (JSON dump)"""

    name: str
    """The name of the function to call"""


class UnionMember0ToolCall(BaseModel):
    id: str
    """The ID of the tool call"""

    function: UnionMember0ToolCallFunction
    """The arguments and name for the function"""

    type: Optional[str] = None


class UnionMember0(BaseModel):
    role: Literal["assistant", "user", "tool", "function", "system"]
    """The role of the participant."""

    id: Optional[str] = None
    """The human-friendly ID of the Message"""

    agent_id: Optional[str] = None
    """The unique identifier of the agent."""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    model: Optional[str] = None
    """The model used to make the function call."""

    name: Optional[str] = None
    """The name of the participant."""

    organization_id: Optional[str] = None
    """The unique identifier of the organization."""

    text: Optional[str] = None
    """The text of the message."""

    tool_call_id: Optional[str] = None
    """The id of the tool call."""

    tool_calls: Optional[List[UnionMember0ToolCall]] = None
    """The list of tool calls requested."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""


class UnionMember1SystemMessageOutput(BaseModel):
    id: str

    date: datetime

    message: str

    message_type: Optional[Literal["system_message"]] = None


class UnionMember1UserMessageOutput(BaseModel):
    id: str

    date: datetime

    message: str

    message_type: Optional[Literal["user_message"]] = None


class UnionMember1ReasoningMessage(BaseModel):
    id: str

    date: datetime

    reasoning: str

    message_type: Optional[Literal["reasoning_message"]] = None


class UnionMember1ToolCallMessageToolCallLettaSchemasLettaMessageToolCall(BaseModel):
    arguments: str

    name: str

    tool_call_id: str


class UnionMember1ToolCallMessageToolCallToolCallDelta(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None


UnionMember1ToolCallMessageToolCall: TypeAlias = Union[
    UnionMember1ToolCallMessageToolCallLettaSchemasLettaMessageToolCall,
    UnionMember1ToolCallMessageToolCallToolCallDelta,
]


class UnionMember1ToolCallMessage(BaseModel):
    id: str

    date: datetime

    tool_call: UnionMember1ToolCallMessageToolCall

    message_type: Optional[Literal["tool_call_message"]] = None


class UnionMember1ToolReturnMessage(BaseModel):
    id: str

    date: datetime

    status: Literal["success", "error"]

    tool_call_id: str

    tool_return: str

    message_type: Optional[Literal["tool_return_message"]] = None

    stderr: Optional[List[str]] = None

    stdout: Optional[List[str]] = None


class UnionMember1AssistantMessageOutput(BaseModel):
    id: str

    assistant_message: str

    date: datetime

    message_type: Optional[Literal["assistant_message"]] = None


UnionMember1: TypeAlias = Annotated[
    Union[
        UnionMember1SystemMessageOutput,
        UnionMember1UserMessageOutput,
        UnionMember1ReasoningMessage,
        UnionMember1ToolCallMessage,
        UnionMember1ToolReturnMessage,
        UnionMember1AssistantMessageOutput,
    ],
    PropertyInfo(discriminator="message_type"),
]

MessageListResponse: TypeAlias = Union[List[UnionMember0], List[UnionMember1]]
