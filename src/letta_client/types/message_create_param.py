# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .letta_message_content_union_param import LettaMessageContentUnionParam

__all__ = ["MessageCreateParam"]


class MessageCreateParam(TypedDict, total=False):
    """Request to create a message"""

    content: Required[Union[Iterable[LettaMessageContentUnionParam], str]]
    """The content of the message."""

    role: Required[Literal["user", "system", "assistant"]]
    """The role of the participant."""

    batch_item_id: Optional[str]
    """The id of the LLMBatchItem that this message is associated with"""

    group_id: Optional[str]
    """The multi-agent group that the message was sent in"""

    name: Optional[str]
    """The name of the participant."""

    otid: Optional[str]
    """The offline threading id associated with this message"""

    sender_id: Optional[str]
    """The id of the sender of the message, can be an identity id or agent id"""

    type: Optional[Literal["message"]]
    """The message type to be created."""
