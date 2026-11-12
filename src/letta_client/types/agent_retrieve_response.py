# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .agent_state import AgentState

__all__ = ["AgentRetrieveResponse", "AgentRetrieveResponseVariable", "AgentRetrieveResponseVariableCreatedBy"]


class AgentRetrieveResponseVariableCreatedBy(BaseModel):
    id: str

    name: Optional[str] = None


class AgentRetrieveResponseVariable(BaseModel):
    key: str

    value: str

    created_by: Optional[AgentRetrieveResponseVariableCreatedBy] = None

    is_private: Optional[bool] = None


class AgentRetrieveResponse(AgentState):
    """Representation of an agent's state.

    This is the state of the agent at a given time, and is persisted in the DB backend. The state has all the information needed to recreate a persisted agent.
    """

    variables: Optional[List[AgentRetrieveResponseVariable]] = None
