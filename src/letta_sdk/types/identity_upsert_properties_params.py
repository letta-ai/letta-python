# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .identity_property_param import IdentityPropertyParam

__all__ = ["IdentityUpsertPropertiesParams"]


class IdentityUpsertPropertiesParams(TypedDict, total=False):
    body: Required[Iterable[IdentityPropertyParam]]
