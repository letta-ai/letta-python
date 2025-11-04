# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EventMessage"]


class EventMessage(BaseModel):
    id: str

    date: datetime

    event_data: Dict[str, object]

    event_type: Literal["compaction"]

    is_err: Optional[bool] = None

    message_type: Optional[Literal["event"]] = None

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None
