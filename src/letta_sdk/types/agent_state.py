# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from .tool import Tool
from .group import Group
from .source import Source
from .._utils import PropertyInfo
from .._models import BaseModel
from .agent_type import AgentType
from .llm_config import LlmConfig
from .agents.memory import Memory
from .init_tool_rule import InitToolRule
from .child_tool_rule import ChildToolRule
from .embedding_config import EmbeddingConfig
from .parent_tool_rule import ParentToolRule
from .continue_tool_rule import ContinueToolRule
from .terminal_tool_rule import TerminalToolRule
from .text_response_format import TextResponseFormat
from .conditional_tool_rule import ConditionalToolRule
from .agent_environment_variable import AgentEnvironmentVariable
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat
from .requires_approval_tool_rule import RequiresApprovalToolRule
from .max_count_per_step_tool_rule import MaxCountPerStepToolRule
from .required_before_exit_tool_rule import RequiredBeforeExitToolRule

__all__ = ["AgentState", "ResponseFormat", "ToolRule"]

ResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]

ToolRule: TypeAlias = Annotated[
    Union[
        ChildToolRule,
        InitToolRule,
        TerminalToolRule,
        ConditionalToolRule,
        ContinueToolRule,
        RequiredBeforeExitToolRule,
        MaxCountPerStepToolRule,
        ParentToolRule,
        RequiresApprovalToolRule,
    ],
    PropertyInfo(discriminator="type"),
]


class AgentState(BaseModel):
    id: str
    """The id of the agent. Assigned by the database."""

    agent_type: AgentType
    """The type of agent."""

    embedding_config: EmbeddingConfig
    """The embedding configuration used by the agent."""

    llm_config: LlmConfig
    """The LLM configuration used by the agent."""

    memory: Memory
    """The in-context memory of the agent."""

    name: str
    """The name of the agent."""

    sources: List[Source]
    """The sources used by the agent."""

    system: str
    """The system prompt used by the agent."""

    tags: List[str]
    """The tags associated with the agent."""

    tools: List[Tool]
    """The tools used by the agent."""

    base_template_id: Optional[str] = None
    """The base template id of the agent."""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    deployment_id: Optional[str] = None
    """The id of the deployment."""

    description: Optional[str] = None
    """The description of the agent."""

    enable_sleeptime: Optional[bool] = None
    """If set to True, memory management will move to a background agent thread."""

    entity_id: Optional[str] = None
    """The id of the entity within the template."""

    hidden: Optional[bool] = None
    """If set to True, the agent will be hidden."""

    identity_ids: Optional[List[str]] = None
    """The ids of the identities associated with this agent."""

    last_run_completion: Optional[datetime] = None
    """The timestamp when the agent last completed a run."""

    last_run_duration_ms: Optional[int] = None
    """The duration in milliseconds of the agent's last run."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    max_files_open: Optional[int] = None
    """Maximum number of files that can be open at once for this agent.

    Setting this too high may exceed the context window, which will break the agent.
    """

    message_buffer_autoclear: Optional[bool] = None
    """
    If set to True, the agent will not remember previous messages (though the agent
    will still retain state via core memory blocks and archival/recall memory). Not
    recommended unless you have an advanced use case.
    """

    message_ids: Optional[List[str]] = None
    """The ids of the messages in the agent's in-context memory."""

    metadata: Optional[Dict[str, object]] = None
    """The metadata of the agent."""

    multi_agent_group: Optional[Group] = None
    """The multi-agent group that this agent manages"""

    per_file_view_window_char_limit: Optional[int] = None
    """The per-file view window character limit for this agent.

    Setting this too high may exceed the context window, which will break the agent.
    """

    project_id: Optional[str] = None
    """The id of the project the agent belongs to."""

    response_format: Optional[ResponseFormat] = None
    """The response format used by the agent when returning from `send_message`."""

    secrets: Optional[List[AgentEnvironmentVariable]] = None
    """The environment variables for tool execution specific to this agent."""

    template_id: Optional[str] = None
    """The id of the template the agent belongs to."""

    timezone: Optional[str] = None
    """The timezone of the agent (IANA format)."""

    tool_exec_environment_variables: Optional[List[AgentEnvironmentVariable]] = None
    """Deprecated: use `secrets` field instead."""

    tool_rules: Optional[List[ToolRule]] = None
    """The list of tool rules."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
