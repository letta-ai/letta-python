# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .agents.user_message import UserMessage
from .tool_return_message import ToolReturnMessage
from .agents.system_message import SystemMessage
from .agents.assistant_message import AssistantMessage
from .agents.reasoning_message import ReasoningMessage
from .agents.tool_call_message import ToolCallMessage
from .agents.approval_request_message import ApprovalRequestMessage
from .agents.hidden_reasoning_message import HiddenReasoningMessage
from .agents.approval_response_message import ApprovalResponseMessage

__all__ = ["StepListMessagesResponse", "StepListMessagesResponseItem"]

StepListMessagesResponseItem: TypeAlias = Annotated[
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
    ],
    PropertyInfo(discriminator="message_type"),
]

StepListMessagesResponse: TypeAlias = List[StepListMessagesResponseItem]
