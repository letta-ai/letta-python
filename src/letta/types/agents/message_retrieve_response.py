# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .messageoutput import Messageoutput

__all__ = [
    "MessageRetrieveResponse",
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

MessageRetrieveResponse: TypeAlias = Union[List[Messageoutput], List[UnionMember1]]
