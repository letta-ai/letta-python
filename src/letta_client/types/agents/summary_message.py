# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SummaryMessage"]


class SummaryMessage(BaseModel):
    """A message representing a summary of the conversation.

    Sent to the LLM as a user or system message depending on the provider.
    """

    id: str

    date: datetime

    summary: str

    is_err: Optional[bool] = None

    message_type: Optional[Literal["summary_message"]] = None

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None
