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

    created_by_id: Optional[str] = None
    """The id of the user that made this Block."""

    description: Optional[str] = None
    """Description of the block."""

    is_template: Optional[bool] = None
    """Whether the block is a template (e.g. saved human/persona options)."""

    label: Optional[str] = None
    """Label of the block (e.g. 'human', 'persona') in the context window."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that last updated this Block."""

    limit: Optional[int] = None
    """Character limit of the block."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """Metadata of the block."""

    name: Optional[str] = None
    """Name of the block if it is a template."""

    organization_id: Optional[str] = None
    """The unique identifier of the organization associated with the block."""
