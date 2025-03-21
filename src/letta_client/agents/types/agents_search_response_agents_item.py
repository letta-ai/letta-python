# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .agents_search_response_agents_item_created_by_id import AgentsSearchResponseAgentsItemCreatedById
from .agents_search_response_agents_item_last_updated_by_id import AgentsSearchResponseAgentsItemLastUpdatedById
from .agents_search_response_agents_item_created_at import AgentsSearchResponseAgentsItemCreatedAt
from .agents_search_response_agents_item_updated_at import AgentsSearchResponseAgentsItemUpdatedAt
from .agents_search_response_agents_item_tool_rules import AgentsSearchResponseAgentsItemToolRules
from .agents_search_response_agents_item_message_ids import AgentsSearchResponseAgentsItemMessageIds
from .agents_search_response_agents_item_agent_type import AgentsSearchResponseAgentsItemAgentType
from .agents_search_response_agents_item_llm_config import AgentsSearchResponseAgentsItemLlmConfig
from .agents_search_response_agents_item_embedding_config import AgentsSearchResponseAgentsItemEmbeddingConfig
from .agents_search_response_agents_item_organization_id import AgentsSearchResponseAgentsItemOrganizationId
from .agents_search_response_agents_item_description import AgentsSearchResponseAgentsItemDescription
from .agents_search_response_agents_item_metadata import AgentsSearchResponseAgentsItemMetadata
from .agents_search_response_agents_item_memory import AgentsSearchResponseAgentsItemMemory
from .agents_search_response_agents_item_tools_item import AgentsSearchResponseAgentsItemToolsItem
from .agents_search_response_agents_item_sources_item import AgentsSearchResponseAgentsItemSourcesItem
from .agents_search_response_agents_item_tool_exec_environment_variables import (
    AgentsSearchResponseAgentsItemToolExecEnvironmentVariables,
)
from .agents_search_response_agents_item_project_id import AgentsSearchResponseAgentsItemProjectId
from .agents_search_response_agents_item_template_id import AgentsSearchResponseAgentsItemTemplateId
from .agents_search_response_agents_item_base_template_id import AgentsSearchResponseAgentsItemBaseTemplateId
from .agents_search_response_agents_item_identity_ids import AgentsSearchResponseAgentsItemIdentityIds
from .agents_search_response_agents_item_message_buffer_autoclear import (
    AgentsSearchResponseAgentsItemMessageBufferAutoclear,
)
from .agents_search_response_agents_item_multi_agent_group import AgentsSearchResponseAgentsItemMultiAgentGroup
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AgentsSearchResponseAgentsItem(UncheckedBaseModel):
    created_by_id: typing.Optional[AgentsSearchResponseAgentsItemCreatedById] = None
    last_updated_by_id: typing.Optional[AgentsSearchResponseAgentsItemLastUpdatedById] = None
    created_at: typing.Optional[AgentsSearchResponseAgentsItemCreatedAt] = None
    updated_at: typing.Optional[AgentsSearchResponseAgentsItemUpdatedAt] = None
    id: str
    name: str
    tool_rules: typing.Optional[AgentsSearchResponseAgentsItemToolRules] = None
    message_ids: typing.Optional[AgentsSearchResponseAgentsItemMessageIds] = None
    system: str
    agent_type: AgentsSearchResponseAgentsItemAgentType
    llm_config: AgentsSearchResponseAgentsItemLlmConfig
    embedding_config: AgentsSearchResponseAgentsItemEmbeddingConfig
    organization_id: typing.Optional[AgentsSearchResponseAgentsItemOrganizationId] = None
    description: typing.Optional[AgentsSearchResponseAgentsItemDescription] = None
    metadata: typing.Optional[AgentsSearchResponseAgentsItemMetadata] = None
    memory: AgentsSearchResponseAgentsItemMemory
    tools: typing.List[AgentsSearchResponseAgentsItemToolsItem]
    sources: typing.List[AgentsSearchResponseAgentsItemSourcesItem]
    tags: typing.List[str]
    tool_exec_environment_variables: typing.Optional[AgentsSearchResponseAgentsItemToolExecEnvironmentVariables] = None
    project_id: typing.Optional[AgentsSearchResponseAgentsItemProjectId] = None
    template_id: typing.Optional[AgentsSearchResponseAgentsItemTemplateId] = None
    base_template_id: typing.Optional[AgentsSearchResponseAgentsItemBaseTemplateId] = None
    identity_ids: typing.Optional[AgentsSearchResponseAgentsItemIdentityIds] = None
    message_buffer_autoclear: typing.Optional[AgentsSearchResponseAgentsItemMessageBufferAutoclear] = None
    multi_agent_group: typing.Optional[AgentsSearchResponseAgentsItemMultiAgentGroup] = None
    template: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
