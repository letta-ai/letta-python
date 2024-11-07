# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Block"]


class Block(BaseModel):
    value: str
    """Value of the block."""

    id: Optional[str] = None
    """The human-friendly ID of the Block"""

    description: Optional[str] = None
    """Description of the block."""

    label: Optional[str] = None
    """Label of the block (e.g. 'human', 'persona') in the context window."""

    limit: Optional[int] = None
    """Character limit of the block."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """Metadata of the block."""

    template: Optional[bool] = None
    """Whether the block is a template (e.g. saved human/persona options)."""

    template_name: Optional[str] = None
    """Name of the block if it is a template."""

    user_id: Optional[str] = None
    """The unique identifier of the user associated with the block."""
