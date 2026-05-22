# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .agents.message import Message

__all__ = ["MessageRetrieveResponse"]

MessageRetrieveResponse: TypeAlias = List[Message]
