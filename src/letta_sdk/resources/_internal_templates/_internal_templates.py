# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ...types import (
    AgentType,
    internal_template_create_agent_params,
    internal_template_create_block_params,
    internal_template_create_group_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .deployment import (
    DeploymentResource,
    AsyncDeploymentResource,
    DeploymentResourceWithRawResponse,
    AsyncDeploymentResourceWithRawResponse,
    DeploymentResourceWithStreamingResponse,
    AsyncDeploymentResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.group import Group
from ..._base_client import make_request_options
from ...types.agent_type import AgentType
from ...types.agent_state import AgentState
from ...types.llm_config_param import LlmConfigParam
from ...types.create_block_param import CreateBlockParam
from ...types.message_create_param import MessageCreateParam
from ...types.embedding_config_param import EmbeddingConfigParam
from ...types.agents.core_memory.block import Block

__all__ = ["_InternalTemplatesResource", "AsyncInternalTemplatesResource"]


class _InternalTemplatesResource(SyncAPIResource):
    @cached_property
    def deployment(self) -> DeploymentResource:
        return DeploymentResource(self._client)

    @cached_property
    def with_raw_response(self) -> _InternalTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return _InternalTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> _InternalTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return _InternalTemplatesResourceWithStreamingResponse(self)

    def create_agent(
        self,
        *,
        base_template_id: str,
        deployment_id: str,
        entity_id: str,
        template_id: str,
        agent_type: AgentType | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        context_window_limit: Optional[int] | Omit = omit,
        description: Optional[str] | Omit = omit,
        embedding: Optional[str] | Omit = omit,
        embedding_chunk_size: Optional[int] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        enable_reasoner: Optional[bool] | Omit = omit,
        enable_sleeptime: Optional[bool] | Omit = omit,
        from_template: Optional[str] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        identity_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_base_tool_rules: Optional[bool] | Omit = omit,
        include_base_tools: bool | Omit = omit,
        include_default_source: bool | Omit = omit,
        include_multi_agent_tools: bool | Omit = omit,
        initial_message_sequence: Optional[Iterable[MessageCreateParam]] | Omit = omit,
        llm_config: Optional[LlmConfigParam] | Omit = omit,
        max_files_open: Optional[int] | Omit = omit,
        max_reasoning_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        memory_blocks: Optional[Iterable[CreateBlockParam]] | Omit = omit,
        memory_variables: Optional[Dict[str, str]] | Omit = omit,
        message_buffer_autoclear: bool | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        per_file_view_window_char_limit: Optional[int] | Omit = omit,
        project: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        reasoning: Optional[bool] | Omit = omit,
        response_format: Optional[internal_template_create_agent_params.ResponseFormat] | Omit = omit,
        secrets: Optional[Dict[str, str]] | Omit = omit,
        source_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template: bool | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        tool_exec_environment_variables: Optional[Dict[str, str]] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_rules: Optional[Iterable[internal_template_create_agent_params.ToolRule]] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Create a new agent with template-related fields.

        Args:
          base_template_id: The id of the base template.

          deployment_id: The id of the deployment.

          entity_id: The id of the entity within the template.

          template_id: The id of the template.

          agent_type: The type of agent.

          block_ids: The ids of the blocks used by the agent.

          context_window_limit: The context window limit used by the agent.

          description: The description of the agent.

          embedding: The embedding configuration handle used by the agent, specified in the format
              provider/model-name.

          embedding_chunk_size: The embedding chunk size used by the agent.

          embedding_config: Configuration for embedding model connection and processing parameters.

          enable_reasoner: Whether to enable internal extended thinking step for a reasoner model.

          enable_sleeptime: If set to True, memory management will move to a background agent thread.

          from_template: The template id used to configure the agent

          hidden: If set to True, the agent will be hidden.

          identity_ids: The ids of the identities associated with this agent.

          include_base_tool_rules: If true, attaches the Letta base tool rules (e.g. deny all tools not explicitly
              allowed).

          include_base_tools: If true, attaches the Letta core tools (e.g. core_memory related functions).

          include_default_source: If true, automatically creates and attaches a default data source for this
              agent.

          include_multi_agent_tools: If true, attaches the Letta multi-agent tools (e.g. sending a message to another
              agent).

          initial_message_sequence: The initial set of messages to put in the agent's in-context memory.

          llm_config: Configuration for Language Model (LLM) connection and generation parameters.

          max_files_open: Maximum number of files that can be open at once for this agent. Setting this
              too high may exceed the context window, which will break the agent.

          max_reasoning_tokens: The maximum number of tokens to generate for reasoning step. If not set, the
              model will use its default value.

          max_tokens: The maximum number of tokens to generate, including reasoning step. If not set,
              the model will use its default value.

          memory_blocks: The blocks to create in the agent's in-context memory.

          memory_variables: The variables that should be set for the agent.

          message_buffer_autoclear: If set to True, the agent will not remember previous messages (though the agent
              will still retain state via core memory blocks and archival/recall memory). Not
              recommended unless you have an advanced use case.

          metadata: The metadata of the agent.

          model: The LLM configuration handle used by the agent, specified in the format
              provider/model-name, as an alternative to specifying llm_config.

          name: The name of the agent.

          per_file_view_window_char_limit: The per-file view window character limit for this agent. Setting this too high
              may exceed the context window, which will break the agent.

          project: Deprecated: Project should now be passed via the X-Project header instead of in
              the request body. If using the sdk, this can be done via the new x_project field
              below.

          project_id: The id of the project the agent belongs to.

          reasoning: Whether to enable reasoning for this agent.

          response_format: The response format for the agent.

          secrets: The environment variables for tool execution specific to this agent.

          source_ids: The ids of the sources used by the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          template: Whether the agent is a template

          timezone: The timezone of the agent (IANA format).

          tool_exec_environment_variables: Deprecated: use `secrets` field instead.

          tool_ids: The ids of the tools used by the agent.

          tool_rules: The tool rules governing the agent.

          tools: The tools used by the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/_internal_templates/agents",
            body=maybe_transform(
                {
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "entity_id": entity_id,
                    "template_id": template_id,
                    "agent_type": agent_type,
                    "block_ids": block_ids,
                    "context_window_limit": context_window_limit,
                    "description": description,
                    "embedding": embedding,
                    "embedding_chunk_size": embedding_chunk_size,
                    "embedding_config": embedding_config,
                    "enable_reasoner": enable_reasoner,
                    "enable_sleeptime": enable_sleeptime,
                    "from_template": from_template,
                    "hidden": hidden,
                    "identity_ids": identity_ids,
                    "include_base_tool_rules": include_base_tool_rules,
                    "include_base_tools": include_base_tools,
                    "include_default_source": include_default_source,
                    "include_multi_agent_tools": include_multi_agent_tools,
                    "initial_message_sequence": initial_message_sequence,
                    "llm_config": llm_config,
                    "max_files_open": max_files_open,
                    "max_reasoning_tokens": max_reasoning_tokens,
                    "max_tokens": max_tokens,
                    "memory_blocks": memory_blocks,
                    "memory_variables": memory_variables,
                    "message_buffer_autoclear": message_buffer_autoclear,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                    "per_file_view_window_char_limit": per_file_view_window_char_limit,
                    "project": project,
                    "project_id": project_id,
                    "reasoning": reasoning,
                    "response_format": response_format,
                    "secrets": secrets,
                    "source_ids": source_ids,
                    "system": system,
                    "tags": tags,
                    "template": template,
                    "timezone": timezone,
                    "tool_exec_environment_variables": tool_exec_environment_variables,
                    "tool_ids": tool_ids,
                    "tool_rules": tool_rules,
                    "tools": tools,
                },
                internal_template_create_agent_params.InternalTemplateCreateAgentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def create_block(
        self,
        *,
        base_template_id: str,
        deployment_id: str,
        entity_id: str,
        label: str,
        template_id: str,
        value: str,
        description: Optional[str] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        is_template: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preserve_on_migration: Optional[bool] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        read_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Create a new block with template-related fields.

        Args:
          base_template_id: The id of the base template.

          deployment_id: The id of the deployment.

          entity_id: The id of the entity within the template.

          label: Label of the block.

          template_id: The id of the template.

          value: Value of the block.

          description: Description of the block.

          hidden: If set to True, the block will be hidden.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: Name of the block if it is a template.

          preserve_on_migration: Preserve the block on template migration.

          project_id: The associated project id.

          read_only: Whether the agent has read-only access to the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/_internal_templates/blocks",
            body=maybe_transform(
                {
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "entity_id": entity_id,
                    "label": label,
                    "template_id": template_id,
                    "value": value,
                    "description": description,
                    "hidden": hidden,
                    "is_template": is_template,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "preserve_on_migration": preserve_on_migration,
                    "project_id": project_id,
                    "read_only": read_only,
                },
                internal_template_create_block_params.InternalTemplateCreateBlockParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    def create_group(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        base_template_id: str,
        deployment_id: str,
        description: str,
        template_id: str,
        hidden: Optional[bool] | Omit = omit,
        manager_config: internal_template_create_group_params.ManagerConfig | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        shared_block_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Create a new multi-agent group with the specified configuration.

        Args:
          agent_ids

          base_template_id: The id of the base template.

          deployment_id: The id of the deployment.

          description

          template_id: The id of the template.

          hidden: If set to True, the group will be hidden.

          manager_config

          project_id: The associated project id.

          shared_block_ids

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/_internal_templates/groups",
            body=maybe_transform(
                {
                    "agent_ids": agent_ids,
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "description": description,
                    "template_id": template_id,
                    "hidden": hidden,
                    "manager_config": manager_config,
                    "project_id": project_id,
                    "shared_block_ids": shared_block_ids,
                },
                internal_template_create_group_params.InternalTemplateCreateGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )


class AsyncInternalTemplatesResource(AsyncAPIResource):
    @cached_property
    def deployment(self) -> AsyncDeploymentResource:
        return AsyncDeploymentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInternalTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInternalTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInternalTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncInternalTemplatesResourceWithStreamingResponse(self)

    async def create_agent(
        self,
        *,
        base_template_id: str,
        deployment_id: str,
        entity_id: str,
        template_id: str,
        agent_type: AgentType | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        context_window_limit: Optional[int] | Omit = omit,
        description: Optional[str] | Omit = omit,
        embedding: Optional[str] | Omit = omit,
        embedding_chunk_size: Optional[int] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        enable_reasoner: Optional[bool] | Omit = omit,
        enable_sleeptime: Optional[bool] | Omit = omit,
        from_template: Optional[str] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        identity_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_base_tool_rules: Optional[bool] | Omit = omit,
        include_base_tools: bool | Omit = omit,
        include_default_source: bool | Omit = omit,
        include_multi_agent_tools: bool | Omit = omit,
        initial_message_sequence: Optional[Iterable[MessageCreateParam]] | Omit = omit,
        llm_config: Optional[LlmConfigParam] | Omit = omit,
        max_files_open: Optional[int] | Omit = omit,
        max_reasoning_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        memory_blocks: Optional[Iterable[CreateBlockParam]] | Omit = omit,
        memory_variables: Optional[Dict[str, str]] | Omit = omit,
        message_buffer_autoclear: bool | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        per_file_view_window_char_limit: Optional[int] | Omit = omit,
        project: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        reasoning: Optional[bool] | Omit = omit,
        response_format: Optional[internal_template_create_agent_params.ResponseFormat] | Omit = omit,
        secrets: Optional[Dict[str, str]] | Omit = omit,
        source_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template: bool | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        tool_exec_environment_variables: Optional[Dict[str, str]] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_rules: Optional[Iterable[internal_template_create_agent_params.ToolRule]] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Create a new agent with template-related fields.

        Args:
          base_template_id: The id of the base template.

          deployment_id: The id of the deployment.

          entity_id: The id of the entity within the template.

          template_id: The id of the template.

          agent_type: The type of agent.

          block_ids: The ids of the blocks used by the agent.

          context_window_limit: The context window limit used by the agent.

          description: The description of the agent.

          embedding: The embedding configuration handle used by the agent, specified in the format
              provider/model-name.

          embedding_chunk_size: The embedding chunk size used by the agent.

          embedding_config: Configuration for embedding model connection and processing parameters.

          enable_reasoner: Whether to enable internal extended thinking step for a reasoner model.

          enable_sleeptime: If set to True, memory management will move to a background agent thread.

          from_template: The template id used to configure the agent

          hidden: If set to True, the agent will be hidden.

          identity_ids: The ids of the identities associated with this agent.

          include_base_tool_rules: If true, attaches the Letta base tool rules (e.g. deny all tools not explicitly
              allowed).

          include_base_tools: If true, attaches the Letta core tools (e.g. core_memory related functions).

          include_default_source: If true, automatically creates and attaches a default data source for this
              agent.

          include_multi_agent_tools: If true, attaches the Letta multi-agent tools (e.g. sending a message to another
              agent).

          initial_message_sequence: The initial set of messages to put in the agent's in-context memory.

          llm_config: Configuration for Language Model (LLM) connection and generation parameters.

          max_files_open: Maximum number of files that can be open at once for this agent. Setting this
              too high may exceed the context window, which will break the agent.

          max_reasoning_tokens: The maximum number of tokens to generate for reasoning step. If not set, the
              model will use its default value.

          max_tokens: The maximum number of tokens to generate, including reasoning step. If not set,
              the model will use its default value.

          memory_blocks: The blocks to create in the agent's in-context memory.

          memory_variables: The variables that should be set for the agent.

          message_buffer_autoclear: If set to True, the agent will not remember previous messages (though the agent
              will still retain state via core memory blocks and archival/recall memory). Not
              recommended unless you have an advanced use case.

          metadata: The metadata of the agent.

          model: The LLM configuration handle used by the agent, specified in the format
              provider/model-name, as an alternative to specifying llm_config.

          name: The name of the agent.

          per_file_view_window_char_limit: The per-file view window character limit for this agent. Setting this too high
              may exceed the context window, which will break the agent.

          project: Deprecated: Project should now be passed via the X-Project header instead of in
              the request body. If using the sdk, this can be done via the new x_project field
              below.

          project_id: The id of the project the agent belongs to.

          reasoning: Whether to enable reasoning for this agent.

          response_format: The response format for the agent.

          secrets: The environment variables for tool execution specific to this agent.

          source_ids: The ids of the sources used by the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          template: Whether the agent is a template

          timezone: The timezone of the agent (IANA format).

          tool_exec_environment_variables: Deprecated: use `secrets` field instead.

          tool_ids: The ids of the tools used by the agent.

          tool_rules: The tool rules governing the agent.

          tools: The tools used by the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/_internal_templates/agents",
            body=await async_maybe_transform(
                {
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "entity_id": entity_id,
                    "template_id": template_id,
                    "agent_type": agent_type,
                    "block_ids": block_ids,
                    "context_window_limit": context_window_limit,
                    "description": description,
                    "embedding": embedding,
                    "embedding_chunk_size": embedding_chunk_size,
                    "embedding_config": embedding_config,
                    "enable_reasoner": enable_reasoner,
                    "enable_sleeptime": enable_sleeptime,
                    "from_template": from_template,
                    "hidden": hidden,
                    "identity_ids": identity_ids,
                    "include_base_tool_rules": include_base_tool_rules,
                    "include_base_tools": include_base_tools,
                    "include_default_source": include_default_source,
                    "include_multi_agent_tools": include_multi_agent_tools,
                    "initial_message_sequence": initial_message_sequence,
                    "llm_config": llm_config,
                    "max_files_open": max_files_open,
                    "max_reasoning_tokens": max_reasoning_tokens,
                    "max_tokens": max_tokens,
                    "memory_blocks": memory_blocks,
                    "memory_variables": memory_variables,
                    "message_buffer_autoclear": message_buffer_autoclear,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                    "per_file_view_window_char_limit": per_file_view_window_char_limit,
                    "project": project,
                    "project_id": project_id,
                    "reasoning": reasoning,
                    "response_format": response_format,
                    "secrets": secrets,
                    "source_ids": source_ids,
                    "system": system,
                    "tags": tags,
                    "template": template,
                    "timezone": timezone,
                    "tool_exec_environment_variables": tool_exec_environment_variables,
                    "tool_ids": tool_ids,
                    "tool_rules": tool_rules,
                    "tools": tools,
                },
                internal_template_create_agent_params.InternalTemplateCreateAgentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def create_block(
        self,
        *,
        base_template_id: str,
        deployment_id: str,
        entity_id: str,
        label: str,
        template_id: str,
        value: str,
        description: Optional[str] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        is_template: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preserve_on_migration: Optional[bool] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        read_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Create a new block with template-related fields.

        Args:
          base_template_id: The id of the base template.

          deployment_id: The id of the deployment.

          entity_id: The id of the entity within the template.

          label: Label of the block.

          template_id: The id of the template.

          value: Value of the block.

          description: Description of the block.

          hidden: If set to True, the block will be hidden.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: Name of the block if it is a template.

          preserve_on_migration: Preserve the block on template migration.

          project_id: The associated project id.

          read_only: Whether the agent has read-only access to the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/_internal_templates/blocks",
            body=await async_maybe_transform(
                {
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "entity_id": entity_id,
                    "label": label,
                    "template_id": template_id,
                    "value": value,
                    "description": description,
                    "hidden": hidden,
                    "is_template": is_template,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "preserve_on_migration": preserve_on_migration,
                    "project_id": project_id,
                    "read_only": read_only,
                },
                internal_template_create_block_params.InternalTemplateCreateBlockParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    async def create_group(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        base_template_id: str,
        deployment_id: str,
        description: str,
        template_id: str,
        hidden: Optional[bool] | Omit = omit,
        manager_config: internal_template_create_group_params.ManagerConfig | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        shared_block_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Create a new multi-agent group with the specified configuration.

        Args:
          agent_ids

          base_template_id: The id of the base template.

          deployment_id: The id of the deployment.

          description

          template_id: The id of the template.

          hidden: If set to True, the group will be hidden.

          manager_config

          project_id: The associated project id.

          shared_block_ids

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/_internal_templates/groups",
            body=await async_maybe_transform(
                {
                    "agent_ids": agent_ids,
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "description": description,
                    "template_id": template_id,
                    "hidden": hidden,
                    "manager_config": manager_config,
                    "project_id": project_id,
                    "shared_block_ids": shared_block_ids,
                },
                internal_template_create_group_params.InternalTemplateCreateGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )


class _InternalTemplatesResourceWithRawResponse:
    def __init__(self, _internal_templates: _InternalTemplatesResource) -> None:
        self.__internal_templates = _internal_templates

        self.create_agent = to_raw_response_wrapper(
            _internal_templates.create_agent,
        )
        self.create_block = to_raw_response_wrapper(
            _internal_templates.create_block,
        )
        self.create_group = to_raw_response_wrapper(
            _internal_templates.create_group,
        )

    @cached_property
    def deployment(self) -> DeploymentResourceWithRawResponse:
        return DeploymentResourceWithRawResponse(self.__internal_templates.deployment)


class AsyncInternalTemplatesResourceWithRawResponse:
    def __init__(self, _internal_templates: AsyncInternalTemplatesResource) -> None:
        self.__internal_templates = _internal_templates

        self.create_agent = async_to_raw_response_wrapper(
            _internal_templates.create_agent,
        )
        self.create_block = async_to_raw_response_wrapper(
            _internal_templates.create_block,
        )
        self.create_group = async_to_raw_response_wrapper(
            _internal_templates.create_group,
        )

    @cached_property
    def deployment(self) -> AsyncDeploymentResourceWithRawResponse:
        return AsyncDeploymentResourceWithRawResponse(self.__internal_templates.deployment)


class _InternalTemplatesResourceWithStreamingResponse:
    def __init__(self, _internal_templates: _InternalTemplatesResource) -> None:
        self.__internal_templates = _internal_templates

        self.create_agent = to_streamed_response_wrapper(
            _internal_templates.create_agent,
        )
        self.create_block = to_streamed_response_wrapper(
            _internal_templates.create_block,
        )
        self.create_group = to_streamed_response_wrapper(
            _internal_templates.create_group,
        )

    @cached_property
    def deployment(self) -> DeploymentResourceWithStreamingResponse:
        return DeploymentResourceWithStreamingResponse(self.__internal_templates.deployment)


class AsyncInternalTemplatesResourceWithStreamingResponse:
    def __init__(self, _internal_templates: AsyncInternalTemplatesResource) -> None:
        self.__internal_templates = _internal_templates

        self.create_agent = async_to_streamed_response_wrapper(
            _internal_templates.create_agent,
        )
        self.create_block = async_to_streamed_response_wrapper(
            _internal_templates.create_block,
        )
        self.create_group = async_to_streamed_response_wrapper(
            _internal_templates.create_group,
        )

    @cached_property
    def deployment(self) -> AsyncDeploymentResourceWithStreamingResponse:
        return AsyncDeploymentResourceWithStreamingResponse(self.__internal_templates.deployment)
