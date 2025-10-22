# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..agents.message_type import MessageType
from ..message_create_param import MessageCreateParam
from ..agents.approval_create_param import ApprovalCreateParam

__all__ = ["BatchCreateParams", "Request", "RequestMessage"]


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


RequestMessage: TypeAlias = Union[MessageCreateParam, ApprovalCreateParam]


class Request(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent to send this batch request for"""

    messages: Required[Iterable[RequestMessage]]
    """The messages to be sent to the agent."""

    assistant_message_tool_kwarg: str
    """The name of the message argument in the designated message tool."""

    assistant_message_tool_name: str
    """The name of the designated message tool."""

    enable_thinking: str
    """
    If set to True, enables reasoning before responses or tool calls from the agent.
    """

    include_return_message_types: Optional[List[MessageType]]
    """Only return specified message types in the response.

    If `None` (default) returns all messages.
    """

    max_steps: int
    """Maximum number of steps the agent should take to process the request."""

    use_assistant_message: bool
    """
    Whether the server should parse specific tool call arguments (default
    `send_message`) as `AssistantMessage` objects.
    """
