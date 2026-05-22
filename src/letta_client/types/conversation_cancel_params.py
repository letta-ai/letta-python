# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

__all__ = ["ConversationCancelParams"]

class ConversationCancelParams(TypedDict, total=False):
    agent_id: Optional[str]
    """Agent ID for agent-direct mode with 'default' conversation"""