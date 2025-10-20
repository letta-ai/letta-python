# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TemplateForkParams"]


class TemplateForkParams(TypedDict, total=False):
    project: Required[str]

    name: str
    """Optional custom name for the forked template.

    If not provided, a random name will be generated.
    """
