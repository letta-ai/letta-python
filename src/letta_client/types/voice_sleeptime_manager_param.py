# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VoiceSleeptimeManagerParam"]


class VoiceSleeptimeManagerParam(TypedDict, total=False):
    manager_agent_id: Required[str]

    manager_type: Literal["voice_sleeptime"]

    max_message_buffer_length: Optional[int]
    """The desired maximum length of messages in the context window of the convo agent.

    This is a best effort, and may be off slightly due to user/assistant
    interleaving.
    """

    min_message_buffer_length: Optional[int]
    """The desired minimum length of messages in the context window of the convo agent.

    This is a best effort, and may be off-by-one due to user/assistant interleaving.
    """
