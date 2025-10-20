# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .provider_type import ProviderType
from .provider_category import ProviderCategory

__all__ = ["Provider"]


class Provider(BaseModel):
    name: str
    """The name of the provider"""

    provider_category: ProviderCategory
    """The category of the provider (base or byok)"""

    provider_type: ProviderType
    """The type of the provider"""

    id: Optional[str] = None
    """The id of the provider, lazily created by the database manager."""

    access_key: Optional[str] = None
    """Access key used for requests to the provider."""

    api_key: Optional[str] = None
    """API key or secret key used for requests to the provider."""

    api_version: Optional[str] = None
    """API version used for requests to the provider."""

    base_url: Optional[str] = None
    """Base URL for the provider."""

    region: Optional[str] = None
    """Region used for requests to the provider."""

    updated_at: Optional[datetime] = None
    """The last update timestamp of the provider."""
