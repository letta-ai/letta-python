# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .agents.message_type import MessageType
from .message_create_param import MessageCreateParam
from .agents.text_content_param import TextContentParam
from .agents.image_content_param import ImageContentParam
from .agents.approval_create_param import ApprovalCreateParam
from .agents.reasoning_content_param import ReasoningContentParam
from .agents.tool_call_content_param import ToolCallContentParam
from .agents.tool_return_content_param import ToolReturnContentParam
from .agents.omitted_reasoning_content_param import OmittedReasoningContentParam
from .agents.redacted_reasoning_content_param import RedactedReasoningContentParam

__all__ = [
    "BatchCreateParams",
    "Request",
    "RequestInputUnionMember1",
    "RequestInputUnionMember1SummarizedReasoningContent",
    "RequestInputUnionMember1SummarizedReasoningContentSummary",
    "RequestMessage",
]


class BatchCreateParams(TypedDict, total=False):
    requests: Required[Iterable[Request]]
    """List of requests to be processed in batch."""

    callback_url: Optional[str]
    """Optional URL to call via POST when the batch completes.

    The callback payload will be a JSON object with the following fields: {'job_id':
    string, 'status': string, 'completed_at': string}. Where 'job_id' is the unique
    batch job identifier, 'status' is the final batch status (e.g., 'completed',
    'failed'), and 'completed_at' is an ISO 8601 timestamp indicating when the batch
    job completed.
    """


class RequestInputUnionMember1SummarizedReasoningContentSummary(TypedDict, total=False):
    index: Required[int]
    """The index of the summary part."""

    text: Required[str]
    """The text of the summary part."""


class RequestInputUnionMember1SummarizedReasoningContent(TypedDict, total=False):
    """The style of reasoning content returned by the OpenAI Responses API"""

    id: Required[str]
    """The unique identifier for this reasoning step."""

    summary: Required[Iterable[RequestInputUnionMember1SummarizedReasoningContentSummary]]
    """Summaries of the reasoning content."""

    encrypted_content: str
    """The encrypted reasoning content."""

    type: Literal["summarized_reasoning"]
    """Indicates this is a summarized reasoning step."""


RequestInputUnionMember1: TypeAlias = Union[
    TextContentParam,
    ImageContentParam,
    ToolCallContentParam,
    ToolReturnContentParam,
    ReasoningContentParam,
    RedactedReasoningContentParam,
    OmittedReasoningContentParam,
    RequestInputUnionMember1SummarizedReasoningContent,
]

RequestMessage: TypeAlias = Union[MessageCreateParam, ApprovalCreateParam]


class Request(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent to send this batch request for"""

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

    enable_thinking: str
    """
    If set to True, enables reasoning before responses or tool calls from the agent.
    """

    include_return_message_types: Optional[List[MessageType]]
    """Only return specified message types in the response.

    If `None` (default) returns all messages.
    """

    input: Union[str, Iterable[RequestInputUnionMember1], None]
    """Syntactic sugar for a single user message.

    Equivalent to messages=[{'role': 'user', 'content': input}].
    """

    max_steps: int
    """Maximum number of steps the agent should take to process the request."""

    messages: Optional[Iterable[RequestMessage]]
    """The messages to be sent to the agent."""

    use_assistant_message: bool
    """
    Whether the server should parse specific tool call arguments (default
    `send_message`) as `AssistantMessage` objects. Still supported for legacy agent
    types, but deprecated for letta_v1_agent onward.
    """
