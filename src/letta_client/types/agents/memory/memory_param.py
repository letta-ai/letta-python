# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from ...block_param import BlockParam

__all__ = ["MemoryParam"]


class MemoryParam(TypedDict, total=False):
    memory: Dict[str, BlockParam]
    """Mapping from memory block section to memory block."""

    prompt_template: str
    """Jinja2 template for compiling memory blocks into a prompt string"""
