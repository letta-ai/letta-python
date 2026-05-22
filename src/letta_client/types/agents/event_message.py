# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EventMessage"]


class EventMessage(BaseModel):
    """A message for notifying the developer that an event that has occured (e.g.

    a compaction). Events are NOT part of the context window.
    """

    id: str

    date: datetime

    event_data: Dict[str, object]

    event_type: Literal["compaction"]

    is_err: Optional[bool] = None

    message_type: Optional[Literal["event_message"]] = None

    name: Optional[str] = None

    otid: Optional[str] = None
    """The offline threading id (OTID).

    Set by the client to deduplicate requests. Used for idempotency in background
    streaming mode — each message in a request must have a unique OTID. Retries of
    the same request should reuse the same OTIDs.
    """

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None
