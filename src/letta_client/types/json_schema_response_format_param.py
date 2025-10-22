# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["JsonSchemaResponseFormatParam"]


class JsonSchemaResponseFormatParam(TypedDict, total=False):
    json_schema: Required[Dict[str, object]]
    """The JSON schema of the response."""

    type: Literal["json_schema"]
    """The type of the response format."""
