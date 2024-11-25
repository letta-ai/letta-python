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
    "UnionMember1InternalMonologue",
    "UnionMember1FunctionCallMessage",
    "UnionMember1FunctionCallMessageFunctionCall",
    "UnionMember1FunctionCallMessageFunctionCallLettaSchemasLettaMessageFunctionCall",
    "UnionMember1FunctionCallMessageFunctionCallFunctionCallDelta",
    "UnionMember1FunctionReturn",
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
    """The time the message was created."""

    model: Optional[str] = None
    """The model used to make the function call."""

    name: Optional[str] = None
    """The name of the participant."""

    text: Optional[str] = None
    """The text of the message."""

    tool_call_id: Optional[str] = None
    """The id of the tool call."""

    tool_calls: Optional[List[UnionMember0ToolCall]] = None
    """The list of tool calls requested."""

    user_id: Optional[str] = None
    """The unique identifier of the user."""


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


class UnionMember1InternalMonologue(BaseModel):
    id: str

    date: datetime

    internal_monologue: str

    message_type: Optional[Literal["internal_monologue"]] = None


class UnionMember1FunctionCallMessageFunctionCallLettaSchemasLettaMessageFunctionCall(BaseModel):
    arguments: str

    function_call_id: str

    name: str


class UnionMember1FunctionCallMessageFunctionCallFunctionCallDelta(BaseModel):
    arguments: Optional[str] = None

    function_call_id: Optional[str] = None

    name: Optional[str] = None


UnionMember1FunctionCallMessageFunctionCall: TypeAlias = Union[
    UnionMember1FunctionCallMessageFunctionCallLettaSchemasLettaMessageFunctionCall,
    UnionMember1FunctionCallMessageFunctionCallFunctionCallDelta,
]


class UnionMember1FunctionCallMessage(BaseModel):
    id: str

    date: datetime

    function_call: UnionMember1FunctionCallMessageFunctionCall

    message_type: Optional[Literal["function_call"]] = None


class UnionMember1FunctionReturn(BaseModel):
    id: str

    date: datetime

    function_call_id: str

    function_return: str

    status: Literal["success", "error"]

    message_type: Optional[Literal["function_return"]] = None


class UnionMember1AssistantMessageOutput(BaseModel):
    id: str

    assistant_message: str

    date: datetime

    message_type: Optional[Literal["assistant_message"]] = None


UnionMember1: TypeAlias = Annotated[
    Union[
        UnionMember1SystemMessageOutput,
        UnionMember1UserMessageOutput,
        UnionMember1InternalMonologue,
        UnionMember1FunctionCallMessage,
        UnionMember1FunctionReturn,
        UnionMember1AssistantMessageOutput,
    ],
    PropertyInfo(discriminator="message_type"),
]

MessageListResponse: TypeAlias = Union[List[UnionMember0], List[UnionMember1]]
