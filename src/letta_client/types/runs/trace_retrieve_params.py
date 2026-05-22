# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TraceRetrieveParams"]


class TraceRetrieveParams(TypedDict, total=False):
    limit: int
    """Maximum number of spans to return"""
