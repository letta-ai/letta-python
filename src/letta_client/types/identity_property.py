# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IdentityProperty"]


class IdentityProperty(BaseModel):
    """A property of an identity"""

    key: str
    """The key of the property"""

    type: Literal["string", "number", "boolean", "json"]
    """The type of the property"""

    value: Union[str, float, bool, Dict[str, object]]
    """The value of the property"""
