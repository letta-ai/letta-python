# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentSummarizeParams"]


class AgentSummarizeParams(TypedDict, total=False):
    max_message_length: Required[int]
    """Maximum number of messages to retain after summarization."""
