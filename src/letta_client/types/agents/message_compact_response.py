# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MessageCompactResponse"]


class MessageCompactResponse(BaseModel):
    num_messages_after: int

    num_messages_before: int

    summary: str
