# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ScheduleCreateResponse"]


class ScheduleCreateResponse(BaseModel):
    id: str

    next_scheduled_at: Optional[str] = None
