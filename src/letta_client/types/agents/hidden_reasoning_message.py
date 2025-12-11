# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HiddenReasoningMessage"]


class HiddenReasoningMessage(BaseModel):
    """
    Representation of an agent's internal reasoning where reasoning content
    has been hidden from the response.

    Args:
        id (str): The ID of the message
        date (datetime): The date the message was created in ISO format
        name (Optional[str]): The name of the sender of the message
        state (Literal["redacted", "omitted"]): Whether the reasoning
            content was redacted by the provider or simply omitted by the API
        hidden_reasoning (Optional[str]): The internal reasoning of the agent
    """

    id: str

    date: datetime

    state: Literal["redacted", "omitted"]

    hidden_reasoning: Optional[str] = None

    is_err: Optional[bool] = None

    message_type: Optional[Literal["hidden_reasoning_message"]] = None
    """The type of the message."""

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None
