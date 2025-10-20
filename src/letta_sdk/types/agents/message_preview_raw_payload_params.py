# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .message_type import MessageType
from ..message_create_param import MessageCreateParam
from .approval_create_param import ApprovalCreateParam

__all__ = [
    "MessagePreviewRawPayloadParams",
    "LettaRequest",
    "LettaRequestMessage",
    "LettaStreamingRequest",
    "LettaStreamingRequestMessage",
]


class LettaRequest(TypedDict, total=False):
    messages: Required[Iterable[LettaRequestMessage]]
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


LettaRequestMessage: TypeAlias = Union[MessageCreateParam, ApprovalCreateParam]


class LettaStreamingRequest(TypedDict, total=False):
    messages: Required[Iterable[LettaStreamingRequestMessage]]
    """The messages to be sent to the agent."""

    assistant_message_tool_kwarg: str
    """The name of the message argument in the designated message tool."""

    assistant_message_tool_name: str
    """The name of the designated message tool."""

    background: bool
    """Whether to process the request in the background."""

    enable_thinking: str
    """
    If set to True, enables reasoning before responses or tool calls from the agent.
    """

    include_pings: bool
    """
    Whether to include periodic keepalive ping messages in the stream to prevent
    connection timeouts.
    """

    include_return_message_types: Optional[List[MessageType]]
    """Only return specified message types in the response.

    If `None` (default) returns all messages.
    """

    max_steps: int
    """Maximum number of steps the agent should take to process the request."""

    stream_tokens: bool
    """
    Flag to determine if individual tokens should be streamed, rather than streaming
    per step.
    """

    use_assistant_message: bool
    """
    Whether the server should parse specific tool call arguments (default
    `send_message`) as `AssistantMessage` objects.
    """


LettaStreamingRequestMessage: TypeAlias = Union[MessageCreateParam, ApprovalCreateParam]

MessagePreviewRawPayloadParams: TypeAlias = Union[LettaRequest, LettaStreamingRequest]
