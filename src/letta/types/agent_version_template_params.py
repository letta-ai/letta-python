# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentVersionTemplateParams"]


class AgentVersionTemplateParams(TypedDict, total=False):
    return_agent_id: Annotated[bool, PropertyInfo(alias="returnAgentId")]

    migrate_deployed_agents: bool
