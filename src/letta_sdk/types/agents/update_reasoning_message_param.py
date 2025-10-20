# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UpdateReasoningMessageParam"]


class UpdateReasoningMessageParam(TypedDict, total=False):
    reasoning: Required[str]

    message_type: Literal["reasoning_message"]
