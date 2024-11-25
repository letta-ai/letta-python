# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
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

    before: Optional[str]
    """Message before which to retrieve the returned messages."""

    limit: int
    """Maximum number of messages to retrieve."""

    msg_object: bool
    """If true, returns Message objects. If false, return LettaMessage objects."""

    use_assistant_message: bool
    """
    [Only applicable if msg_object is False] If true, returns AssistantMessage
    objects when the agent calls a designated message tool. If false, return
    FunctionCallMessage objects for all tool calls.
    """
