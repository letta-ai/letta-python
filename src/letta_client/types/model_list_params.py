# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .provider_type import ProviderType
from .provider_category import ProviderCategory

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    provider_category: Optional[List[ProviderCategory]]

    provider_name: Optional[str]

    provider_type: Optional[ProviderType]
