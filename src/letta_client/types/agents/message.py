# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .system_message import SystemMessage

from .user_message import UserMessage

from .reasoning_message import ReasoningMessage

from .hidden_reasoning_message import HiddenReasoningMessage

from .tool_call_message import ToolCallMessage

from ..tool_return_message import ToolReturnMessage

from .assistant_message import AssistantMessage

from .approval_request_message import ApprovalRequestMessage

from .approval_response_message import ApprovalResponseMessage

from .summary_message import SummaryMessage

from .event_message import EventMessage

from ..._utils import PropertyInfo

from typing_extensions import Annotated, TypeAliasType, TypeAlias

__all__ = ["Message"]

Message: TypeAlias = Annotated[Union[SystemMessage, UserMessage, ReasoningMessage, HiddenReasoningMessage, ToolCallMessage, ToolReturnMessage, AssistantMessage, ApprovalRequestMessage, ApprovalResponseMessage, SummaryMessage, EventMessage], PropertyInfo(discriminator="message_type")]