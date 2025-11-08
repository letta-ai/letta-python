# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .agent_state import AgentState

__all__ = ["ToolExecutionResult"]


class ToolExecutionResult(BaseModel):
    status: Literal["success", "error"]
    """The status of the tool execution and return object"""

    agent_state: Optional[AgentState] = None
    """Representation of an agent's state.

    This is the state of the agent at a given time, and is persisted in the DB
    backend. The state has all the information needed to recreate a persisted agent.
    """

    func_return: Optional[object] = None
    """The function return object"""

    sandbox_config_fingerprint: Optional[str] = None
    """The fingerprint of the config for the sandbox"""

    stderr: Optional[List[str]] = None
    """Captured stderr from the function invocation"""

    stdout: Optional[List[str]] = None
    """Captured stdout (prints, logs) from function invocation"""
