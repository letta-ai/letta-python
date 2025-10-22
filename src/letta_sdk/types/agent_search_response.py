# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_state import AgentState

__all__ = ["AgentSearchResponse"]


class AgentSearchResponse(BaseModel):
    agents: List[AgentState]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
