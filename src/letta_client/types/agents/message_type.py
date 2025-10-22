# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["MessageType"]

MessageType: TypeAlias = Literal[
    "system_message",
    "user_message",
    "assistant_message",
    "reasoning_message",
    "hidden_reasoning_message",
    "tool_call_message",
    "tool_return_message",
    "approval_request_message",
    "approval_response_message",
]
