# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...types import (
    AgentType,
    agent_list_params,
    agent_create_params,
    agent_export_params,
    agent_import_params,
    agent_search_params,
    agent_update_params,
    agent_migrate_params,
    agent_retrieve_params,
    agent_summarize_params,
    agent_list_groups_params,
    agent_reset_messages_params,
)
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from .sources import (
    SourcesResource,
    AsyncSourcesResource,
    SourcesResourceWithRawResponse,
    AsyncSourcesResourceWithRawResponse,
    SourcesResourceWithStreamingResponse,
    AsyncSourcesResourceWithStreamingResponse,
)
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import extract_files, maybe_transform, strip_not_given, deepcopy_minimal, async_maybe_transform
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .archival_memory import (
    ArchivalMemoryResource,
    AsyncArchivalMemoryResource,
    ArchivalMemoryResourceWithRawResponse,
    AsyncArchivalMemoryResourceWithRawResponse,
    ArchivalMemoryResourceWithStreamingResponse,
    AsyncArchivalMemoryResourceWithStreamingResponse,
)
from ...types.agent_type import AgentType
from ...types.agent_state import AgentState
from .core_memory.core_memory import (
    CoreMemoryResource,
    AsyncCoreMemoryResource,
    CoreMemoryResourceWithRawResponse,
    AsyncCoreMemoryResourceWithRawResponse,
    CoreMemoryResourceWithStreamingResponse,
    AsyncCoreMemoryResourceWithStreamingResponse,
)
from ...types.llm_config_param import LlmConfigParam
from ...types.create_block_param import CreateBlockParam
from ...types.agent_list_response import AgentListResponse
from ...types.agent_count_response import AgentCountResponse
from ...types.message_create_param import MessageCreateParam
from ...types.agent_import_response import AgentImportResponse
from ...types.agent_search_response import AgentSearchResponse
from ...types.agent_migrate_response import AgentMigrateResponse
from ...types.embedding_config_param import EmbeddingConfigParam
from ...types.agent_list_groups_response import AgentListGroupsResponse
from ...types.agent_retrieve_context_response import AgentRetrieveContextResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def sources(self) -> SourcesResource:
        return SourcesResource(self._client)

    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def core_memory(self) -> CoreMemoryResource:
        return CoreMemoryResource(self._client)

    @cached_property
    def archival_memory(self) -> ArchivalMemoryResource:
        return ArchivalMemoryResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_type: AgentType | Omit = omit,
        base_template_id: Optional[str] | Omit = omit,
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
        response_format: Optional[agent_create_params.ResponseFormat] | Omit = omit,
        secrets: Optional[Dict[str, str]] | Omit = omit,
        source_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template: bool | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        tool_exec_environment_variables: Optional[Dict[str, str]] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_rules: Optional[Iterable[agent_create_params.ToolRule]] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        x_project: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Create an agent.

        Args:
          agent_type: The type of agent.

          base_template_id: The base template id of the agent.

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

          template_id: The id of the template the agent belongs to.

          timezone: The timezone of the agent (IANA format).

          tool_exec_environment_variables: Deprecated: use `secrets` field instead.

          tool_ids: The ids of the tools used by the agent.

          tool_rules: The tool rules governing the agent.

          tools: The tools used by the agent.

          x_project: The project slug to associate with the agent (cloud only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Project": x_project}), **(extra_headers or {})}
        return self._post(
            "/v1/agents/",
            body=maybe_transform(
                {
                    "agent_type": agent_type,
                    "base_template_id": base_template_id,
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
                    "template_id": template_id,
                    "timezone": timezone,
                    "tool_exec_environment_variables": tool_exec_environment_variables,
                    "tool_ids": tool_ids,
                    "tool_rules": tool_rules,
                    "tools": tools,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        include_relationships: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Get the state of the agent.

        Args:
          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_relationships": include_relationships}, agent_retrieve_params.AgentRetrieveParams
                ),
            ),
            cast_to=AgentState,
        )

    def update(
        self,
        agent_id: str,
        *,
        base_template_id: Optional[str] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        embedding: Optional[str] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        enable_sleeptime: Optional[bool] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        identity_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        last_run_completion: Union[str, datetime, None] | Omit = omit,
        last_run_duration_ms: Optional[int] | Omit = omit,
        llm_config: Optional[LlmConfigParam] | Omit = omit,
        max_files_open: Optional[int] | Omit = omit,
        message_buffer_autoclear: Optional[bool] | Omit = omit,
        message_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        per_file_view_window_char_limit: Optional[int] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        reasoning: Optional[bool] | Omit = omit,
        response_format: Optional[agent_update_params.ResponseFormat] | Omit = omit,
        secrets: Optional[Dict[str, str]] | Omit = omit,
        source_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        tool_exec_environment_variables: Optional[Dict[str, str]] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_rules: Optional[Iterable[agent_update_params.ToolRule]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Update an existing agent.

        Args:
          base_template_id: The base template id of the agent.

          block_ids: The ids of the blocks used by the agent.

          description: The description of the agent.

          embedding: The embedding configuration handle used by the agent, specified in the format
              provider/model-name.

          embedding_config: Configuration for embedding model connection and processing parameters.

          enable_sleeptime: If set to True, memory management will move to a background agent thread.

          hidden: If set to True, the agent will be hidden.

          identity_ids: The ids of the identities associated with this agent.

          last_run_completion: The timestamp when the agent last completed a run.

          last_run_duration_ms: The duration in milliseconds of the agent's last run.

          llm_config: Configuration for Language Model (LLM) connection and generation parameters.

          max_files_open: Maximum number of files that can be open at once for this agent. Setting this
              too high may exceed the context window, which will break the agent.

          message_buffer_autoclear: If set to True, the agent will not remember previous messages (though the agent
              will still retain state via core memory blocks and archival/recall memory). Not
              recommended unless you have an advanced use case.

          message_ids: The ids of the messages in the agent's in-context memory.

          metadata: The metadata of the agent.

          model: The LLM configuration handle used by the agent, specified in the format
              provider/model-name, as an alternative to specifying llm_config.

          name: The name of the agent.

          per_file_view_window_char_limit: The per-file view window character limit for this agent. Setting this too high
              may exceed the context window, which will break the agent.

          project_id: The id of the project the agent belongs to.

          reasoning: Whether to enable reasoning for this agent.

          response_format: The response format for the agent.

          secrets: The environment variables for tool execution specific to this agent.

          source_ids: The ids of the sources used by the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          template_id: The id of the template the agent belongs to.

          timezone: The timezone of the agent (IANA format).

          tool_exec_environment_variables: Deprecated: use `secrets` field instead

          tool_ids: The ids of the tools used by the agent.

          tool_rules: The tool rules governing the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}",
            body=maybe_transform(
                {
                    "base_template_id": base_template_id,
                    "block_ids": block_ids,
                    "description": description,
                    "embedding": embedding,
                    "embedding_config": embedding_config,
                    "enable_sleeptime": enable_sleeptime,
                    "hidden": hidden,
                    "identity_ids": identity_ids,
                    "last_run_completion": last_run_completion,
                    "last_run_duration_ms": last_run_duration_ms,
                    "llm_config": llm_config,
                    "max_files_open": max_files_open,
                    "message_buffer_autoclear": message_buffer_autoclear,
                    "message_ids": message_ids,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                    "per_file_view_window_char_limit": per_file_view_window_char_limit,
                    "project_id": project_id,
                    "reasoning": reasoning,
                    "response_format": response_format,
                    "secrets": secrets,
                    "source_ids": source_ids,
                    "system": system,
                    "tags": tags,
                    "template_id": template_id,
                    "timezone": timezone,
                    "tool_exec_environment_variables": tool_exec_environment_variables,
                    "tool_ids": tool_ids,
                    "tool_rules": tool_rules,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        ascending: bool | Omit = omit,
        base_template_id: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        identifier_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        identity_id: Optional[str] | Omit = omit,
        include_relationships: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        match_all_tags: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at", "last_run_completion"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        query_text: Optional[str] | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Get a list of all agents.

        Args:
          after: Cursor for pagination

          ascending: Whether to sort agents oldest to newest (True) or newest to oldest (False,
              default)

          base_template_id: Search agents by base template ID

          before: Cursor for pagination

          identifier_keys: Search agents by identifier keys

          identity_id: Search agents by identity ID

          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.

          limit: Limit for pagination

          match_all_tags: If True, only returns agents that match ALL given tags. Otherwise, return agents
              that have ANY of the passed-in tags.

          name: Name of the agent

          order: Sort order for agents by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          project_id: Search agents by project ID - this will default to your default project on cloud

          query_text: Search agents by name

          sort_by: Field to sort by. Options: 'created_at' (default), 'last_run_completion'

          tags: List of tags to filter agents by

          template_id: Search agents by template ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/agents/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "ascending": ascending,
                        "base_template_id": base_template_id,
                        "before": before,
                        "identifier_keys": identifier_keys,
                        "identity_id": identity_id,
                        "include_relationships": include_relationships,
                        "limit": limit,
                        "match_all_tags": match_all_tags,
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                        "project_id": project_id,
                        "query_text": query_text,
                        "sort_by": sort_by,
                        "tags": tags,
                        "template_id": template_id,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCountResponse:
        """Get the total number of agents."""
        return self._get(
            "/v1/agents/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    def export(
        self,
        agent_id: str,
        *,
        max_steps: int | Omit = omit,
        use_legacy_format: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Export the serialized JSON representation of an agent, formatted with
        indentation.

        Supports two export formats:

        - Legacy format (use_legacy_format=true): Single agent with inline tools/blocks
        - New format (default): Multi-entity format with separate agents, tools, blocks,
          files, etc.

        Args:
          use_legacy_format: If true, exports using the legacy single-agent format (v1). If false, exports
              using the new multi-entity format (v2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "max_steps": max_steps,
                        "use_legacy_format": use_legacy_format,
                    },
                    agent_export_params.AgentExportParams,
                ),
            ),
            cast_to=str,
        )

    def import_(
        self,
        *,
        file: FileTypes,
        append_copy_suffix: bool | Omit = omit,
        env_vars_json: Optional[str] | Omit = omit,
        override_embedding_handle: Optional[str] | Omit = omit,
        override_existing_tools: bool | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        strip_messages: bool | Omit = omit,
        x_override_embedding_model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentImportResponse:
        """Import a serialized agent file and recreate the agent(s) in the system.

        Returns
        the IDs of all imported agents.

        Args:
          append_copy_suffix: If set to True, appends "\\__copy" to the end of the agent name.

          env_vars_json: Environment variables as a JSON string to pass to the agent for tool execution.

          override_embedding_handle: Override import with specific embedding handle.

          override_existing_tools: If set to True, existing tools can get their source code overwritten by the
              uploaded tool definitions. Note that Letta core tools can never be updated
              externally.

          project_id: The project ID to associate the uploaded agent with.

          strip_messages: If set to True, strips all messages from the agent before importing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-override-embedding-model": x_override_embedding_model}),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "file": file,
                "append_copy_suffix": append_copy_suffix,
                "env_vars_json": env_vars_json,
                "override_embedding_handle": override_embedding_handle,
                "override_existing_tools": override_existing_tools,
                "project_id": project_id,
                "strip_messages": strip_messages,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/agents/import",
            body=maybe_transform(body, agent_import_params.AgentImportParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentImportResponse,
        )

    def list_groups(
        self,
        agent_id: str,
        *,
        manager_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListGroupsResponse:
        """
        Lists the groups for an agent

        Args:
          manager_type: Manager type to filter groups by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"manager_type": manager_type}, agent_list_groups_params.AgentListGroupsParams),
            ),
            cast_to=AgentListGroupsResponse,
        )

    def migrate(
        self,
        agent_id: str,
        *,
        preserve_core_memories: bool,
        to_template: str,
        preserve_tool_variables: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentMigrateResponse:
        """Migrate an agent to a new versioned agent template.

        This will only work for
        "classic" and non-multiagent agent templates.

        Args:
          preserve_tool_variables: If true, preserves the existing agent's tool environment variables instead of
              using the template's variables

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/migrate",
            body=maybe_transform(
                {
                    "preserve_core_memories": preserve_core_memories,
                    "to_template": to_template,
                    "preserve_tool_variables": preserve_tool_variables,
                },
                agent_migrate_params.AgentMigrateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentMigrateResponse,
        )

    def reset_messages(
        self,
        agent_id: str,
        *,
        add_default_initial_messages: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Resets the messages for an agent

        Args:
          add_default_initial_messages: If true, adds the default initial messages after resetting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/reset-messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"add_default_initial_messages": add_default_initial_messages},
                    agent_reset_messages_params.AgentResetMessagesParams,
                ),
            ),
            cast_to=AgentState,
        )

    def retrieve_context(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveContextResponse:
        """
        Retrieve the context window of a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/context",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveContextResponse,
        )

    def search(
        self,
        *,
        after: Optional[str] | Omit = omit,
        ascending: bool | Omit = omit,
        combinator: Literal["AND"] | Omit = omit,
        limit: float | Omit = omit,
        project_id: str | Omit = omit,
        search: Iterable[agent_search_params.Search] | Omit = omit,
        sort_by: Literal["created_at", "last_run_completion"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSearchResponse:
        """
        Search deployed agents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents/search",
            body=maybe_transform(
                {
                    "after": after,
                    "ascending": ascending,
                    "combinator": combinator,
                    "limit": limit,
                    "project_id": project_id,
                    "search": search,
                    "sort_by": sort_by,
                },
                agent_search_params.AgentSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSearchResponse,
        )

    def summarize(
        self,
        agent_id: str,
        *,
        max_message_length: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Summarize an agent's conversation history to a target message length.

        This endpoint summarizes the current message history for a given agent,
        truncating and compressing it down to the specified `max_message_length`.

        Args:
          max_message_length: Maximum number of messages to retain after summarization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/agents/{agent_id}/summarize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"max_message_length": max_message_length}, agent_summarize_params.AgentSummarizeParams
                ),
            ),
            cast_to=NoneType,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def sources(self) -> AsyncSourcesResource:
        return AsyncSourcesResource(self._client)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def core_memory(self) -> AsyncCoreMemoryResource:
        return AsyncCoreMemoryResource(self._client)

    @cached_property
    def archival_memory(self) -> AsyncArchivalMemoryResource:
        return AsyncArchivalMemoryResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_type: AgentType | Omit = omit,
        base_template_id: Optional[str] | Omit = omit,
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
        response_format: Optional[agent_create_params.ResponseFormat] | Omit = omit,
        secrets: Optional[Dict[str, str]] | Omit = omit,
        source_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template: bool | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        tool_exec_environment_variables: Optional[Dict[str, str]] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_rules: Optional[Iterable[agent_create_params.ToolRule]] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        x_project: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Create an agent.

        Args:
          agent_type: The type of agent.

          base_template_id: The base template id of the agent.

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

          template_id: The id of the template the agent belongs to.

          timezone: The timezone of the agent (IANA format).

          tool_exec_environment_variables: Deprecated: use `secrets` field instead.

          tool_ids: The ids of the tools used by the agent.

          tool_rules: The tool rules governing the agent.

          tools: The tools used by the agent.

          x_project: The project slug to associate with the agent (cloud only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Project": x_project}), **(extra_headers or {})}
        return await self._post(
            "/v1/agents/",
            body=await async_maybe_transform(
                {
                    "agent_type": agent_type,
                    "base_template_id": base_template_id,
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
                    "template_id": template_id,
                    "timezone": timezone,
                    "tool_exec_environment_variables": tool_exec_environment_variables,
                    "tool_ids": tool_ids,
                    "tool_rules": tool_rules,
                    "tools": tools,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        include_relationships: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Get the state of the agent.

        Args:
          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_relationships": include_relationships}, agent_retrieve_params.AgentRetrieveParams
                ),
            ),
            cast_to=AgentState,
        )

    async def update(
        self,
        agent_id: str,
        *,
        base_template_id: Optional[str] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        embedding: Optional[str] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        enable_sleeptime: Optional[bool] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        identity_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        last_run_completion: Union[str, datetime, None] | Omit = omit,
        last_run_duration_ms: Optional[int] | Omit = omit,
        llm_config: Optional[LlmConfigParam] | Omit = omit,
        max_files_open: Optional[int] | Omit = omit,
        message_buffer_autoclear: Optional[bool] | Omit = omit,
        message_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        per_file_view_window_char_limit: Optional[int] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        reasoning: Optional[bool] | Omit = omit,
        response_format: Optional[agent_update_params.ResponseFormat] | Omit = omit,
        secrets: Optional[Dict[str, str]] | Omit = omit,
        source_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        tool_exec_environment_variables: Optional[Dict[str, str]] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_rules: Optional[Iterable[agent_update_params.ToolRule]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Update an existing agent.

        Args:
          base_template_id: The base template id of the agent.

          block_ids: The ids of the blocks used by the agent.

          description: The description of the agent.

          embedding: The embedding configuration handle used by the agent, specified in the format
              provider/model-name.

          embedding_config: Configuration for embedding model connection and processing parameters.

          enable_sleeptime: If set to True, memory management will move to a background agent thread.

          hidden: If set to True, the agent will be hidden.

          identity_ids: The ids of the identities associated with this agent.

          last_run_completion: The timestamp when the agent last completed a run.

          last_run_duration_ms: The duration in milliseconds of the agent's last run.

          llm_config: Configuration for Language Model (LLM) connection and generation parameters.

          max_files_open: Maximum number of files that can be open at once for this agent. Setting this
              too high may exceed the context window, which will break the agent.

          message_buffer_autoclear: If set to True, the agent will not remember previous messages (though the agent
              will still retain state via core memory blocks and archival/recall memory). Not
              recommended unless you have an advanced use case.

          message_ids: The ids of the messages in the agent's in-context memory.

          metadata: The metadata of the agent.

          model: The LLM configuration handle used by the agent, specified in the format
              provider/model-name, as an alternative to specifying llm_config.

          name: The name of the agent.

          per_file_view_window_char_limit: The per-file view window character limit for this agent. Setting this too high
              may exceed the context window, which will break the agent.

          project_id: The id of the project the agent belongs to.

          reasoning: Whether to enable reasoning for this agent.

          response_format: The response format for the agent.

          secrets: The environment variables for tool execution specific to this agent.

          source_ids: The ids of the sources used by the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          template_id: The id of the template the agent belongs to.

          timezone: The timezone of the agent (IANA format).

          tool_exec_environment_variables: Deprecated: use `secrets` field instead

          tool_ids: The ids of the tools used by the agent.

          tool_rules: The tool rules governing the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "base_template_id": base_template_id,
                    "block_ids": block_ids,
                    "description": description,
                    "embedding": embedding,
                    "embedding_config": embedding_config,
                    "enable_sleeptime": enable_sleeptime,
                    "hidden": hidden,
                    "identity_ids": identity_ids,
                    "last_run_completion": last_run_completion,
                    "last_run_duration_ms": last_run_duration_ms,
                    "llm_config": llm_config,
                    "max_files_open": max_files_open,
                    "message_buffer_autoclear": message_buffer_autoclear,
                    "message_ids": message_ids,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                    "per_file_view_window_char_limit": per_file_view_window_char_limit,
                    "project_id": project_id,
                    "reasoning": reasoning,
                    "response_format": response_format,
                    "secrets": secrets,
                    "source_ids": source_ids,
                    "system": system,
                    "tags": tags,
                    "template_id": template_id,
                    "timezone": timezone,
                    "tool_exec_environment_variables": tool_exec_environment_variables,
                    "tool_ids": tool_ids,
                    "tool_rules": tool_rules,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        ascending: bool | Omit = omit,
        base_template_id: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        identifier_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        identity_id: Optional[str] | Omit = omit,
        include_relationships: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        match_all_tags: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at", "last_run_completion"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        query_text: Optional[str] | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Get a list of all agents.

        Args:
          after: Cursor for pagination

          ascending: Whether to sort agents oldest to newest (True) or newest to oldest (False,
              default)

          base_template_id: Search agents by base template ID

          before: Cursor for pagination

          identifier_keys: Search agents by identifier keys

          identity_id: Search agents by identity ID

          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.

          limit: Limit for pagination

          match_all_tags: If True, only returns agents that match ALL given tags. Otherwise, return agents
              that have ANY of the passed-in tags.

          name: Name of the agent

          order: Sort order for agents by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          project_id: Search agents by project ID - this will default to your default project on cloud

          query_text: Search agents by name

          sort_by: Field to sort by. Options: 'created_at' (default), 'last_run_completion'

          tags: List of tags to filter agents by

          template_id: Search agents by template ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/agents/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "ascending": ascending,
                        "base_template_id": base_template_id,
                        "before": before,
                        "identifier_keys": identifier_keys,
                        "identity_id": identity_id,
                        "include_relationships": include_relationships,
                        "limit": limit,
                        "match_all_tags": match_all_tags,
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                        "project_id": project_id,
                        "query_text": query_text,
                        "sort_by": sort_by,
                        "tags": tags,
                        "template_id": template_id,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCountResponse:
        """Get the total number of agents."""
        return await self._get(
            "/v1/agents/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    async def export(
        self,
        agent_id: str,
        *,
        max_steps: int | Omit = omit,
        use_legacy_format: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Export the serialized JSON representation of an agent, formatted with
        indentation.

        Supports two export formats:

        - Legacy format (use_legacy_format=true): Single agent with inline tools/blocks
        - New format (default): Multi-entity format with separate agents, tools, blocks,
          files, etc.

        Args:
          use_legacy_format: If true, exports using the legacy single-agent format (v1). If false, exports
              using the new multi-entity format (v2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "max_steps": max_steps,
                        "use_legacy_format": use_legacy_format,
                    },
                    agent_export_params.AgentExportParams,
                ),
            ),
            cast_to=str,
        )

    async def import_(
        self,
        *,
        file: FileTypes,
        append_copy_suffix: bool | Omit = omit,
        env_vars_json: Optional[str] | Omit = omit,
        override_embedding_handle: Optional[str] | Omit = omit,
        override_existing_tools: bool | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        strip_messages: bool | Omit = omit,
        x_override_embedding_model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentImportResponse:
        """Import a serialized agent file and recreate the agent(s) in the system.

        Returns
        the IDs of all imported agents.

        Args:
          append_copy_suffix: If set to True, appends "\\__copy" to the end of the agent name.

          env_vars_json: Environment variables as a JSON string to pass to the agent for tool execution.

          override_embedding_handle: Override import with specific embedding handle.

          override_existing_tools: If set to True, existing tools can get their source code overwritten by the
              uploaded tool definitions. Note that Letta core tools can never be updated
              externally.

          project_id: The project ID to associate the uploaded agent with.

          strip_messages: If set to True, strips all messages from the agent before importing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-override-embedding-model": x_override_embedding_model}),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "file": file,
                "append_copy_suffix": append_copy_suffix,
                "env_vars_json": env_vars_json,
                "override_embedding_handle": override_embedding_handle,
                "override_existing_tools": override_existing_tools,
                "project_id": project_id,
                "strip_messages": strip_messages,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/agents/import",
            body=await async_maybe_transform(body, agent_import_params.AgentImportParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentImportResponse,
        )

    async def list_groups(
        self,
        agent_id: str,
        *,
        manager_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListGroupsResponse:
        """
        Lists the groups for an agent

        Args:
          manager_type: Manager type to filter groups by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"manager_type": manager_type}, agent_list_groups_params.AgentListGroupsParams
                ),
            ),
            cast_to=AgentListGroupsResponse,
        )

    async def migrate(
        self,
        agent_id: str,
        *,
        preserve_core_memories: bool,
        to_template: str,
        preserve_tool_variables: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentMigrateResponse:
        """Migrate an agent to a new versioned agent template.

        This will only work for
        "classic" and non-multiagent agent templates.

        Args:
          preserve_tool_variables: If true, preserves the existing agent's tool environment variables instead of
              using the template's variables

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/migrate",
            body=await async_maybe_transform(
                {
                    "preserve_core_memories": preserve_core_memories,
                    "to_template": to_template,
                    "preserve_tool_variables": preserve_tool_variables,
                },
                agent_migrate_params.AgentMigrateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentMigrateResponse,
        )

    async def reset_messages(
        self,
        agent_id: str,
        *,
        add_default_initial_messages: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Resets the messages for an agent

        Args:
          add_default_initial_messages: If true, adds the default initial messages after resetting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/reset-messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"add_default_initial_messages": add_default_initial_messages},
                    agent_reset_messages_params.AgentResetMessagesParams,
                ),
            ),
            cast_to=AgentState,
        )

    async def retrieve_context(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveContextResponse:
        """
        Retrieve the context window of a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/context",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveContextResponse,
        )

    async def search(
        self,
        *,
        after: Optional[str] | Omit = omit,
        ascending: bool | Omit = omit,
        combinator: Literal["AND"] | Omit = omit,
        limit: float | Omit = omit,
        project_id: str | Omit = omit,
        search: Iterable[agent_search_params.Search] | Omit = omit,
        sort_by: Literal["created_at", "last_run_completion"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSearchResponse:
        """
        Search deployed agents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents/search",
            body=await async_maybe_transform(
                {
                    "after": after,
                    "ascending": ascending,
                    "combinator": combinator,
                    "limit": limit,
                    "project_id": project_id,
                    "search": search,
                    "sort_by": sort_by,
                },
                agent_search_params.AgentSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSearchResponse,
        )

    async def summarize(
        self,
        agent_id: str,
        *,
        max_message_length: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Summarize an agent's conversation history to a target message length.

        This endpoint summarizes the current message history for a given agent,
        truncating and compressing it down to the specified `max_message_length`.

        Args:
          max_message_length: Maximum number of messages to retain after summarization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/agents/{agent_id}/summarize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"max_message_length": max_message_length}, agent_summarize_params.AgentSummarizeParams
                ),
            ),
            cast_to=NoneType,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.count = to_raw_response_wrapper(
            agents.count,
        )
        self.export = to_raw_response_wrapper(
            agents.export,
        )
        self.import_ = to_raw_response_wrapper(
            agents.import_,
        )
        self.list_groups = to_raw_response_wrapper(
            agents.list_groups,
        )
        self.migrate = to_raw_response_wrapper(
            agents.migrate,
        )
        self.reset_messages = to_raw_response_wrapper(
            agents.reset_messages,
        )
        self.retrieve_context = to_raw_response_wrapper(
            agents.retrieve_context,
        )
        self.search = to_raw_response_wrapper(
            agents.search,
        )
        self.summarize = to_raw_response_wrapper(
            agents.summarize,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def sources(self) -> SourcesResourceWithRawResponse:
        return SourcesResourceWithRawResponse(self._agents.sources)

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._agents.folders)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._agents.files)

    @cached_property
    def core_memory(self) -> CoreMemoryResourceWithRawResponse:
        return CoreMemoryResourceWithRawResponse(self._agents.core_memory)

    @cached_property
    def archival_memory(self) -> ArchivalMemoryResourceWithRawResponse:
        return ArchivalMemoryResourceWithRawResponse(self._agents.archival_memory)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._agents.messages)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.count = async_to_raw_response_wrapper(
            agents.count,
        )
        self.export = async_to_raw_response_wrapper(
            agents.export,
        )
        self.import_ = async_to_raw_response_wrapper(
            agents.import_,
        )
        self.list_groups = async_to_raw_response_wrapper(
            agents.list_groups,
        )
        self.migrate = async_to_raw_response_wrapper(
            agents.migrate,
        )
        self.reset_messages = async_to_raw_response_wrapper(
            agents.reset_messages,
        )
        self.retrieve_context = async_to_raw_response_wrapper(
            agents.retrieve_context,
        )
        self.search = async_to_raw_response_wrapper(
            agents.search,
        )
        self.summarize = async_to_raw_response_wrapper(
            agents.summarize,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithRawResponse:
        return AsyncSourcesResourceWithRawResponse(self._agents.sources)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._agents.folders)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._agents.files)

    @cached_property
    def core_memory(self) -> AsyncCoreMemoryResourceWithRawResponse:
        return AsyncCoreMemoryResourceWithRawResponse(self._agents.core_memory)

    @cached_property
    def archival_memory(self) -> AsyncArchivalMemoryResourceWithRawResponse:
        return AsyncArchivalMemoryResourceWithRawResponse(self._agents.archival_memory)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._agents.messages)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.count = to_streamed_response_wrapper(
            agents.count,
        )
        self.export = to_streamed_response_wrapper(
            agents.export,
        )
        self.import_ = to_streamed_response_wrapper(
            agents.import_,
        )
        self.list_groups = to_streamed_response_wrapper(
            agents.list_groups,
        )
        self.migrate = to_streamed_response_wrapper(
            agents.migrate,
        )
        self.reset_messages = to_streamed_response_wrapper(
            agents.reset_messages,
        )
        self.retrieve_context = to_streamed_response_wrapper(
            agents.retrieve_context,
        )
        self.search = to_streamed_response_wrapper(
            agents.search,
        )
        self.summarize = to_streamed_response_wrapper(
            agents.summarize,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def sources(self) -> SourcesResourceWithStreamingResponse:
        return SourcesResourceWithStreamingResponse(self._agents.sources)

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._agents.folders)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._agents.files)

    @cached_property
    def core_memory(self) -> CoreMemoryResourceWithStreamingResponse:
        return CoreMemoryResourceWithStreamingResponse(self._agents.core_memory)

    @cached_property
    def archival_memory(self) -> ArchivalMemoryResourceWithStreamingResponse:
        return ArchivalMemoryResourceWithStreamingResponse(self._agents.archival_memory)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._agents.messages)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            agents.count,
        )
        self.export = async_to_streamed_response_wrapper(
            agents.export,
        )
        self.import_ = async_to_streamed_response_wrapper(
            agents.import_,
        )
        self.list_groups = async_to_streamed_response_wrapper(
            agents.list_groups,
        )
        self.migrate = async_to_streamed_response_wrapper(
            agents.migrate,
        )
        self.reset_messages = async_to_streamed_response_wrapper(
            agents.reset_messages,
        )
        self.retrieve_context = async_to_streamed_response_wrapper(
            agents.retrieve_context,
        )
        self.search = async_to_streamed_response_wrapper(
            agents.search,
        )
        self.summarize = async_to_streamed_response_wrapper(
            agents.summarize,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithStreamingResponse:
        return AsyncSourcesResourceWithStreamingResponse(self._agents.sources)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._agents.folders)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._agents.files)

    @cached_property
    def core_memory(self) -> AsyncCoreMemoryResourceWithStreamingResponse:
        return AsyncCoreMemoryResourceWithStreamingResponse(self._agents.core_memory)

    @cached_property
    def archival_memory(self) -> AsyncArchivalMemoryResourceWithStreamingResponse:
        return AsyncArchivalMemoryResourceWithStreamingResponse(self._agents.archival_memory)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._agents.messages)
