# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ToolCall"]


class ToolCall(BaseModel):
    arguments: str

    name: str

    tool_call_id: str
