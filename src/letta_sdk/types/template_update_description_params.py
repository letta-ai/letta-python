# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TemplateUpdateDescriptionParams"]


class TemplateUpdateDescriptionParams(TypedDict, total=False):
    project: Required[str]

    description: str
    """The new description for the template"""
