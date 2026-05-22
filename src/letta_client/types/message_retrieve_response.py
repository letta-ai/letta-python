# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .agents.message import Message

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["MessageRetrieveResponse"]

MessageRetrieveResponse: TypeAlias = List[Message]