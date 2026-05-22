# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ToolCallDelta"]


class ToolCallDelta(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None
