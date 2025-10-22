# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ReasoningMessage"]


class ReasoningMessage(BaseModel):
    id: str

    date: datetime

    reasoning: str

    is_err: Optional[bool] = None

    message_type: Optional[Literal["reasoning_message"]] = None
    """The type of the message."""

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    signature: Optional[str] = None

    source: Optional[Literal["reasoner_model", "non_reasoner_model"]] = None

    step_id: Optional[str] = None
