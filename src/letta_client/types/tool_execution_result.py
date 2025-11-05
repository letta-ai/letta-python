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

    Parameters: id (str): The unique identifier of the agent. name (str): The name
    of the agent (must be unique to the user). created_at (datetime): The datetime
    the agent was created. message_ids (List[str]): The ids of the messages in the
    agent's in-context memory. memory (Memory): The in-context memory of the agent.
    tools (List[str]): The tools used by the agent. This includes any memory editing
    functions specified in `memory`. system (str): The system prompt used by the
    agent. llm_config (LLMConfig): The LLM configuration used by the agent.
    embedding_config (EmbeddingConfig): The embedding configuration used by the
    agent.
    """

    func_return: Optional[object] = None
    """The function return object"""

    sandbox_config_fingerprint: Optional[str] = None
    """The fingerprint of the config for the sandbox"""

    stderr: Optional[List[str]] = None
    """Captured stderr from the function invocation"""

    stdout: Optional[List[str]] = None
    """Captured stdout (prints, logs) from function invocation"""
