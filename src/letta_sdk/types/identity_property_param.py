# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["IdentityPropertyParam"]


class IdentityPropertyParam(TypedDict, total=False):
    key: Required[str]
    """The key of the property"""

    type: Required[Literal["string", "number", "boolean", "json"]]
    """The type of the property"""

    value: Required[Union[str, float, bool, Dict[str, object]]]
    """The value of the property"""
