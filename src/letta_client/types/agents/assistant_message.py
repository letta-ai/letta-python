# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .letta_assistant_message_content_union import LettaAssistantMessageContentUnion

__all__ = ["AssistantMessage"]


class AssistantMessage(BaseModel):
    """A message sent by the LLM in response to user input. Used in the LLM context.

    Args:
        id (str): The ID of the message
        date (datetime): The date the message was created in ISO format
        name (Optional[str]): The name of the sender of the message
        content (Union[str, List[LettaAssistantMessageContentUnion]]): The message content sent by the agent (can be a string or an array of content parts)
    """

    id: str

    content: Union[List[LettaAssistantMessageContentUnion], str]
    """
    The message content sent by the agent (can be a string or an array of content
    parts)
    """

    date: datetime

    is_err: Optional[bool] = None

    message_type: Optional[Literal["assistant_message"]] = None
    """The type of the message."""

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None
