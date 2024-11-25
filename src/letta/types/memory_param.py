# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .shared_params.block import Block

__all__ = ["MemoryParam"]


class MemoryParam(TypedDict, total=False):
    memory: Dict[str, Block]
    """Mapping from memory block section to memory block."""

    prompt_template: str
    """Jinja2 template for compiling memory blocks into a prompt string"""
