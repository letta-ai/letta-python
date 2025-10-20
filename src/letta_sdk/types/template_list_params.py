# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    exact: str
    """Whether to search for an exact name match"""

    limit: str

    name: str

    offset: Union[str, float]

    project_id: str

    project_slug: str

    search: str

    sort_by: Literal["updated_at", "created_at"]

    template_id: str

    version: str
    """
    Specify the version you want to return, otherwise will return the latest version
    """
