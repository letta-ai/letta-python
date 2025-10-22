# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TemplateRenameParams"]


class TemplateRenameParams(TypedDict, total=False):
    project: Required[str]

    new_name: Required[str]
    """The new name for the template"""
