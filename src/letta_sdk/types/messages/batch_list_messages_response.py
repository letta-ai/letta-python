# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..agents.message import Message

__all__ = ["BatchListMessagesResponse"]


class BatchListMessagesResponse(BaseModel):
    messages: List[Message]
