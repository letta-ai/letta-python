# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .messageoutput import Messageoutput

__all__ = ["MessageRetrieveResponse"]

MessageRetrieveResponse: TypeAlias = List[Messageoutput]
