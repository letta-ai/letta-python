# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .embeddingconfig import Embeddingconfig

__all__ = ["Source"]


class Source(BaseModel):
    embedding_config: Embeddingconfig
    """The embedding configuration used by the source."""

    name: str
    """The name of the source."""

    id: Optional[str] = None
    """The human-friendly ID of the Source"""

    created_at: Optional[datetime] = None
    """The timestamp when the source was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    description: Optional[str] = None
    """The description of the source."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """Metadata associated with the source."""

    organization_id: Optional[str] = None
    """The ID of the organization that created the source."""

    updated_at: Optional[datetime] = None
    """The timestamp when the source was last updated."""
