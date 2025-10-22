# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .provider_type import ProviderType

__all__ = ["ProviderCreateParams"]


class ProviderCreateParams(TypedDict, total=False):
    api_key: Required[str]
    """API key or secret key used for requests to the provider."""

    name: Required[str]
    """The name of the provider."""

    provider_type: Required[ProviderType]
    """The type of the provider."""

    access_key: Optional[str]
    """Access key used for requests to the provider."""

    api_version: Optional[str]
    """API version used for requests to the provider."""

    base_url: Optional[str]
    """Base URL used for requests to the provider."""

    region: Optional[str]
    """Region used for requests to the provider."""
