# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .letta_user_message_content_union import LettaUserMessageContentUnion

__all__ = ["UserMessage"]


class UserMessage(BaseModel):
    id: str

    content: Union[List[LettaUserMessageContentUnion], str]
    """
    The message content sent by the user (can be a string or an array of multi-modal
    content parts)
    """

    date: datetime

    is_err: Optional[bool] = None

    message_type: Optional[Literal["user_message"]] = None
    """The type of the message."""

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None
