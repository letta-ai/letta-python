# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScheduleCreateResponse"]


class ScheduleCreateResponse(BaseModel):
    id: str

    next_scheduled_at: Optional[str] = None

    status: Literal["active", "paused", "completed"]

    use_sandbox: bool

    callback_url: Optional[str] = None

    context_window_limit: Optional[int] = None

    model: Optional[str] = None

    api_model_settings: Optional[object] = FieldInfo(alias="model_settings", default=None)

    target_device_id: Optional[str] = None
