# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..agents.letta_message_union import LettaMessageUnion

__all__ = ["MessageListResponse"]

MessageListResponse: TypeAlias = List[LettaMessageUnion]
