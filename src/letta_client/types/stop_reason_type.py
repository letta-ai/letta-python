# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["StopReasonType"]

StopReasonType: TypeAlias = Literal[
    "end_turn",
    "error",
    "llm_api_error",
    "invalid_llm_response",
    "invalid_tool_call",
    "max_steps",
    "max_tokens_exceeded",
    "no_tool_call",
    "tool_rule",
    "cancelled",
    "insufficient_credits",
    "requires_approval",
    "context_window_overflow_in_system_prompt",
]
