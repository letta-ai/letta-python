# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional, List

from .provider_category import ProviderCategory

from .provider_type import ProviderType

__all__ = ["ModelListParams"]

class ModelListParams(TypedDict, total=False):
    provider_category: Optional[List[ProviderCategory]]

    provider_name: Optional[str]

    provider_type: Optional[ProviderType]