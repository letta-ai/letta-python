# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "AgentSearchParams",
    "Search",
    "SearchUnionMember0",
    "SearchUnionMember1",
    "SearchUnionMember2",
    "SearchUnionMember3",
    "SearchUnionMember4",
]


class AgentSearchParams(TypedDict, total=False):
    after: Optional[str]

    ascending: bool

    combinator: Literal["AND"]

    limit: float

    project_id: str

    search: Iterable[Search]

    sort_by: Annotated[Literal["created_at", "last_run_completion"], PropertyInfo(alias="sortBy")]


class SearchUnionMember0(TypedDict, total=False):
    field: Required[Literal["version"]]

    value: Required[str]


class SearchUnionMember1(TypedDict, total=False):
    field: Required[Literal["name"]]

    operator: Required[Literal["eq", "contains"]]

    value: Required[str]


class SearchUnionMember2(TypedDict, total=False):
    field: Required[Literal["tags"]]

    operator: Required[Literal["contains"]]

    value: Required[SequenceNotStr[str]]


class SearchUnionMember3(TypedDict, total=False):
    field: Required[Literal["identity"]]

    operator: Required[Literal["eq"]]

    value: Required[str]


class SearchUnionMember4(TypedDict, total=False):
    field: Required[Literal["templateName"]]

    operator: Required[Literal["eq"]]

    value: Required[str]


Search: TypeAlias = Union[
    SearchUnionMember0, SearchUnionMember1, SearchUnionMember2, SearchUnionMember3, SearchUnionMember4
]
