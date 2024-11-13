# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageCreateParams", "Message"]


class MessageCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The messages to be sent to the agent."""

    assistant_message_function_kwarg: str
    """
    [Only applicable if use_assistant_message is True] The name of the message
    argument in the designated message tool.
    """

    assistant_message_function_name: str
    """
    [Only applicable if use_assistant_message is True] The name of the designated
    message tool.
    """

    return_message_object: bool
    """Set True to return the raw Message object.

    Set False to return the Message in the format of the Letta API.
    """

    run_async: bool
    """Whether to asynchronously send the messages to the agent."""

    stream_steps: bool
    """Flag to determine if the response should be streamed.

    Set to True for streaming agent steps.
    """

    stream_tokens: bool
    """Flag to determine if individual tokens should be streamed.

    Set to True for token streaming (requires stream_steps = True).
    """

    use_assistant_message: bool
    """
    [Only applicable if return_message_object is False] If true, returns
    AssistantMessage objects when the agent calls a designated message tool. If
    false, return FunctionCallMessage objects for all tool calls.
    """

    user_id: str


class Message(TypedDict, total=False):
    role: Required[Literal["user", "system"]]
    """The role of the participant."""

    text: Required[str]
    """The text of the message."""

    name: Optional[str]
    """The name of the participant."""
