# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .block import Block
from .._models import BaseModel

__all__ = ["Memory"]


class Memory(BaseModel):
    memory: Optional[Dict[str, Block]] = None
    """Mapping from memory block section to memory block."""

    prompt_template: Optional[str] = None
    """Jinja2 template for compiling memory blocks into a prompt string"""
