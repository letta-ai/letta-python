# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .memory import Memory
from .._models import BaseModel
from .llm_config import LlmConfig
from .embedding_config import EmbeddingConfig

__all__ = ["AgentState", "ToolRule"]


class ToolRule(BaseModel):
    tool_name: str
    """The name of the tool. Must exist in the database for the user's organization."""


class AgentState(BaseModel):
    agent_type: Literal["memgpt_agent", "split_thread_agent", "o1_agent"]
    """The type of agent."""

    embedding_config: EmbeddingConfig
    """The embedding configuration used by the agent."""

    llm_config: LlmConfig
    """The LLM configuration used by the agent."""

    name: str
    """The name of the agent."""

    system: str
    """The system prompt used by the agent."""

    tools: List[str]
    """The tools used by the agent."""

    id: Optional[str] = None
    """The human-friendly ID of the Agent"""

    created_at: Optional[datetime] = None
    """The datetime the agent was created."""

    description: Optional[str] = None
    """The description of the agent."""

    memory: Optional[Memory] = None
    """Represents the in-context memory of the agent.

    This includes both the `Block` objects (labelled by sections), as well as tools
    to edit the blocks.

    Attributes: memory (Dict[str, Block]): Mapping from memory block section to
    memory block.
    """

    message_ids: Optional[List[str]] = None
    """The ids of the messages in the agent's in-context memory."""

    metadata: Optional[object] = FieldInfo(alias="metadata_", default=None)
    """The metadata of the agent."""

    tags: Optional[List[str]] = None
    """The tags associated with the agent."""

    tool_rules: Optional[List[ToolRule]] = None
    """The list of tool rules."""

    user_id: Optional[str] = None
    """The user id of the agent."""
