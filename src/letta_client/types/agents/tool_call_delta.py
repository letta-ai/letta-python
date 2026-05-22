# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["ToolCallDelta"]

class ToolCallDelta(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None