# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["TemplateListVersionsParams"]


class TemplateListVersionsParams(TypedDict, total=False):
    project_slug: Required[str]

    limit: str

    offset: Union[str, float]
