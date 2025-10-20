# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectListResponse", "Project"]


class Project(BaseModel):
    id: str

    name: str

    slug: str


class ProjectListResponse(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    projects: List[Project]
