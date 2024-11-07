# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..embeddingconfig import Embeddingconfig

__all__ = ["Source"]


class Source(BaseModel):
    embedding_config: Embeddingconfig
    """The embedding configuration used by the source."""

    name: str
    """The name of the source."""

    user_id: str
    """The ID of the user that created the source."""

    id: Optional[str] = None
    """The human-friendly ID of the Source"""

    created_at: Optional[datetime] = None
    """The creation date of the source."""

    description: Optional[str] = None
    """The description of the source."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """Metadata associated with the source."""
