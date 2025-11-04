# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .user_message import UserMessage
from .event_message import EventMessage
from .system_message import SystemMessage
from .summary_message import SummaryMessage
from .assistant_message import AssistantMessage
from .reasoning_message import ReasoningMessage
from .tool_call_message import ToolCallMessage
from ..tool_return_message import ToolReturnMessage
from .approval_request_message import ApprovalRequestMessage
from .hidden_reasoning_message import HiddenReasoningMessage
from .approval_response_message import ApprovalResponseMessage

__all__ = ["MessageModifyResponse"]

MessageModifyResponse: TypeAlias = Annotated[
    Union[
        SystemMessage,
        UserMessage,
        ReasoningMessage,
        HiddenReasoningMessage,
        ToolCallMessage,
        ToolReturnMessage,
        AssistantMessage,
        ApprovalRequestMessage,
        ApprovalResponseMessage,
        SummaryMessage,
        EventMessage,
    ],
    PropertyInfo(discriminator="message_type"),
]
