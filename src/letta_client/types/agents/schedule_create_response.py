# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["ScheduleCreateResponse"]

class ScheduleCreateResponse(BaseModel):
    id: str

    next_scheduled_at: Optional[str] = None