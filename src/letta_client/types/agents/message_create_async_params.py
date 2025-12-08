# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .message_type import MessageType
from .text_content_param import TextContentParam
from .image_content_param import ImageContentParam
from ..message_create_param import MessageCreateParam
from .approval_create_param import ApprovalCreateParam
from .reasoning_content_param import ReasoningContentParam
from .tool_call_content_param import ToolCallContentParam
from .tool_return_content_param import ToolReturnContentParam
from .omitted_reasoning_content_param import OmittedReasoningContentParam
from .redacted_reasoning_content_param import RedactedReasoningContentParam

__all__ = [
    "MessageCreateAsyncParams",
    "InputUnionMember1",
    "InputUnionMember1SummarizedReasoningContent",
    "InputUnionMember1SummarizedReasoningContentSummary",
    "Message",
]


class MessageCreateAsyncParams(TypedDict, total=False):
    assistant_message_tool_kwarg: str
    """The name of the message argument in the designated message tool.

    Still supported for legacy agent types, but deprecated for letta_v1_agent
    onward.
    """

    assistant_message_tool_name: str
    """The name of the designated message tool.

    Still supported for legacy agent types, but deprecated for letta_v1_agent
    onward.
    """

    callback_url: Optional[str]
    """Optional callback URL to POST to when the job completes"""

    enable_thinking: str
    """
    If set to True, enables reasoning before responses or tool calls from the agent.
    """

    include_return_message_types: Optional[List[MessageType]]
    """Only return specified message types in the response.

    If `None` (default) returns all messages.
    """

    input: Union[str, Iterable[InputUnionMember1], None]
    """Syntactic sugar for a single user message.

    Equivalent to messages=[{'role': 'user', 'content': input}].
    """

    max_steps: int
    """Maximum number of steps the agent should take to process the request."""

    messages: Optional[Iterable[Message]]
    """The messages to be sent to the agent."""

    use_assistant_message: bool
    """
    Whether the server should parse specific tool call arguments (default
    `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
    types, but deprecated for letta_v1_agent onward.
    """


class InputUnionMember1SummarizedReasoningContentSummary(TypedDict, total=False):
    index: Required[int]
    """The index of the summary part."""

    text: Required[str]
    """The text of the summary part."""


class InputUnionMember1SummarizedReasoningContent(TypedDict, total=False):
    """The style of reasoning content returned by the OpenAI Responses API"""

    id: Required[str]
    """The unique identifier for this reasoning step."""

    summary: Required[Iterable[InputUnionMember1SummarizedReasoningContentSummary]]
    """Summaries of the reasoning content."""

    encrypted_content: str
    """The encrypted reasoning content."""

    type: Literal["summarized_reasoning"]
    """Indicates this is a summarized reasoning step."""


InputUnionMember1: TypeAlias = Union[
    TextContentParam,
    ImageContentParam,
    ToolCallContentParam,
    ToolReturnContentParam,
    ReasoningContentParam,
    RedactedReasoningContentParam,
    OmittedReasoningContentParam,
    InputUnionMember1SummarizedReasoningContent,
]

Message: TypeAlias = Union[MessageCreateParam, ApprovalCreateParam]
