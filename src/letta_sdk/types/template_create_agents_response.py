# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .agent_state import AgentState

__all__ = ["TemplateCreateAgentsResponse"]


class TemplateCreateAgentsResponse(BaseModel):
    agents: List[AgentState]
