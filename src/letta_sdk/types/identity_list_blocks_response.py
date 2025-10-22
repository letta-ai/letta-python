# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .agents.core_memory.block import Block

__all__ = ["IdentityListBlocksResponse"]

IdentityListBlocksResponse: TypeAlias = List[Block]
