# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "TemplateGetSnapshotResponse",
    "Agent",
    "AgentMemoryVariables",
    "AgentMemoryVariablesData",
    "AgentProperties",
    "AgentToolRule",
    "AgentToolRuleUnionMember0",
    "AgentToolRuleUnionMember1",
    "AgentToolRuleUnionMember2",
    "AgentToolRuleUnionMember3",
    "AgentToolRuleUnionMember4",
    "AgentToolRuleUnionMember5",
    "AgentToolRuleUnionMember6",
    "AgentToolRuleUnionMember7",
    "AgentToolRuleUnionMember8",
    "AgentToolVariables",
    "AgentToolVariablesData",
    "Block",
    "Configuration",
]


class AgentMemoryVariablesData(BaseModel):
    key: str

    type: str

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)


class AgentMemoryVariables(BaseModel):
    data: List[AgentMemoryVariablesData]

    version: str


class AgentProperties(BaseModel):
    context_window_limit: Optional[float] = None

    enable_reasoner: Optional[bool] = None

    max_files_open: Optional[float] = None

    max_reasoning_tokens: Optional[float] = None

    max_tokens: Optional[float] = None

    message_buffer_autoclear: Optional[bool] = None

    per_file_view_window_char_limit: Optional[float] = None

    put_inner_thoughts_in_kwargs: Optional[bool] = None

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] = None

    temperature: Optional[float] = None

    verbosity_level: Optional[Literal["low", "medium", "high"]] = None


class AgentToolRuleUnionMember0(BaseModel):
    children: List[str]

    tool_name: str

    prompt_template: Optional[str] = None

    type: Optional[Literal["constrain_child_tools"]] = None


class AgentToolRuleUnionMember1(BaseModel):
    tool_name: str

    prompt_template: Optional[str] = None

    type: Optional[Literal["run_first"]] = None


class AgentToolRuleUnionMember2(BaseModel):
    tool_name: str

    prompt_template: Optional[str] = None

    type: Optional[Literal["exit_loop"]] = None


class AgentToolRuleUnionMember3(BaseModel):
    child_output_mapping: Dict[str, str]

    tool_name: str

    default_child: Optional[str] = None

    prompt_template: Optional[str] = None

    require_output_mapping: Optional[bool] = None

    type: Optional[Literal["conditional"]] = None


class AgentToolRuleUnionMember4(BaseModel):
    tool_name: str

    prompt_template: Optional[str] = None

    type: Optional[Literal["continue_loop"]] = None


class AgentToolRuleUnionMember5(BaseModel):
    tool_name: str

    prompt_template: Optional[str] = None

    type: Optional[Literal["required_before_exit"]] = None


class AgentToolRuleUnionMember6(BaseModel):
    max_count_limit: float

    tool_name: str

    prompt_template: Optional[str] = None

    type: Optional[Literal["max_count_per_step"]] = None


class AgentToolRuleUnionMember7(BaseModel):
    children: List[str]

    tool_name: str

    prompt_template: Optional[str] = None

    type: Optional[Literal["parent_last_tool"]] = None


class AgentToolRuleUnionMember8(BaseModel):
    tool_name: str

    prompt_template: Optional[str] = None

    type: Optional[Literal["requires_approval"]] = None


AgentToolRule: TypeAlias = Union[
    AgentToolRuleUnionMember0,
    AgentToolRuleUnionMember1,
    AgentToolRuleUnionMember2,
    AgentToolRuleUnionMember3,
    AgentToolRuleUnionMember4,
    AgentToolRuleUnionMember5,
    AgentToolRuleUnionMember6,
    AgentToolRuleUnionMember7,
    AgentToolRuleUnionMember8,
]


class AgentToolVariablesData(BaseModel):
    key: str

    type: str

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)


class AgentToolVariables(BaseModel):
    data: List[AgentToolVariablesData]

    version: str


class Agent(BaseModel):
    agent_type: Literal[
        "memgpt_agent",
        "memgpt_v2_agent",
        "react_agent",
        "workflow_agent",
        "split_thread_agent",
        "sleeptime_agent",
        "voice_convo_agent",
        "voice_sleeptime_agent",
    ] = FieldInfo(alias="agentType")

    entity_id: str = FieldInfo(alias="entityId")

    identity_ids: Optional[List[str]] = FieldInfo(alias="identityIds", default=None)

    memory_variables: Optional[AgentMemoryVariables] = FieldInfo(alias="memoryVariables", default=None)

    model: str

    name: str

    properties: Optional[AgentProperties] = None

    source_ids: Optional[List[str]] = FieldInfo(alias="sourceIds", default=None)

    system_prompt: str = FieldInfo(alias="systemPrompt")

    tags: Optional[List[str]] = None

    tool_ids: Optional[List[str]] = FieldInfo(alias="toolIds", default=None)

    tool_rules: Optional[List[AgentToolRule]] = FieldInfo(alias="toolRules", default=None)

    tool_variables: Optional[AgentToolVariables] = FieldInfo(alias="toolVariables", default=None)


class Block(BaseModel):
    description: str

    label: str

    limit: float

    preserve_on_migration: Optional[bool] = FieldInfo(alias="preserveOnMigration", default=None)

    read_only: bool = FieldInfo(alias="readOnly")

    value: str


class Configuration(BaseModel):
    manager_agent_entity_id: Optional[str] = FieldInfo(alias="managerAgentEntityId", default=None)

    manager_type: Optional[str] = FieldInfo(alias="managerType", default=None)

    max_message_buffer_length: Optional[float] = FieldInfo(alias="maxMessageBufferLength", default=None)

    max_turns: Optional[float] = FieldInfo(alias="maxTurns", default=None)

    min_message_buffer_length: Optional[float] = FieldInfo(alias="minMessageBufferLength", default=None)

    sleeptime_agent_frequency: Optional[float] = FieldInfo(alias="sleeptimeAgentFrequency", default=None)

    termination_token: Optional[str] = FieldInfo(alias="terminationToken", default=None)


class TemplateGetSnapshotResponse(BaseModel):
    agents: List[Agent]

    blocks: List[Block]

    configuration: Configuration

    type: Literal["classic", "cluster", "sleeptime", "round_robin", "supervisor", "dynamic", "voice_sleeptime"]

    version: str
