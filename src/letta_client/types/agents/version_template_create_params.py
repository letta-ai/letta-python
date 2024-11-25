# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VersionTemplateCreateParams"]


class VersionTemplateCreateParams(TypedDict, total=False):
    body: Required[object]

    return_agent_id: Annotated[bool, PropertyInfo(alias="returnAgentId")]
