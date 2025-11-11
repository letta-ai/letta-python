# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Mapping, Iterable, Optional, cast
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
from .blocks import (
    BlocksResource,
    AsyncBlocksResource,
    BlocksResourceWithRawResponse,
    AsyncBlocksResourceWithRawResponse,
    BlocksResourceWithStreamingResponse,
    AsyncBlocksResourceWithStreamingResponse,
)
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from ...types import (
    AgentType,
    StopReasonType,
    agent_list_params,
    agent_create_params,
    agent_modify_params,
    agent_retrieve_params,
    agent_export_file_params,
    agent_import_file_params,
)
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import extract_files, maybe_transform, strip_not_given, deepcopy_minimal, async_maybe_transform
from .archives import (
    ArchivesResource,
    AsyncArchivesResource,
    ArchivesResourceWithRawResponse,
    AsyncArchivesResourceWithRawResponse,
    ArchivesResourceWithStreamingResponse,
    AsyncArchivesResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .identities import (
    IdentitiesResource,
    AsyncIdentitiesResource,
    IdentitiesResourceWithRawResponse,
    AsyncIdentitiesResourceWithRawResponse,
    IdentitiesResourceWithStreamingResponse,
    AsyncIdentitiesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncArrayPage, AsyncArrayPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.agent_type import AgentType
from ...types.agent_state import AgentState
from ...types.llm_config_param import LlmConfigParam
from ...types.stop_reason_type import StopReasonType
from ...types.create_block_param import CreateBlockParam
from ...types.message_create_param import MessageCreateParam
from ...types.embedding_config_param import EmbeddingConfigParam
from ...types.agent_import_file_response import AgentImportFileResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def blocks(self) -> BlocksResource:
        return BlocksResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def archives(self) -> ArchivesResource:
        return ArchivesResource(self._client)

    @cached_property
    def identities(self) -> IdentitiesResource:
        return IdentitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
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
        embedding: Optional[agent_create_params.Embedding] | Omit = omit,
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
        model: Optional[agent_create_params.Model] | Omit = omit,
        name: str | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
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

          base_template_id: Deprecated: No longer used. The base template id of the agent.

          block_ids: The ids of the blocks used by the agent.

          context_window_limit: The context window limit used by the agent.

          description: The description of the agent.

          embedding: The embedding configuration handle used by the agent, specified in the format
              provider/model-name.

          embedding_chunk_size: Deprecated: No longer used. The embedding chunk size used by the agent.

          embedding_config: Configuration for embedding model connection and processing parameters.

          enable_reasoner: Deprecated: Use `model` field to configure reasoning instead. Whether to enable
              internal extended thinking step for a reasoner model.

          enable_sleeptime: If set to True, memory management will move to a background agent thread.

          from_template: Deprecated: please use the 'create agents from a template' endpoint instead.

          hidden: Deprecated: No longer used. If set to True, the agent will be hidden.

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

          max_reasoning_tokens: Deprecated: Use `model` field to configure reasoning tokens instead. The maximum
              number of tokens to generate for reasoning step.

          max_tokens: Deprecated: Use `model` field to configure max output tokens instead. The
              maximum number of tokens to generate, including reasoning step.

          memory_blocks: The blocks to create in the agent's in-context memory.

          memory_variables: Deprecated: Only relevant for creating agents from a template. Use the 'create
              agents from a template' endpoint instead.

          message_buffer_autoclear: If set to True, the agent will not remember previous messages (though the agent
              will still retain state via core memory blocks and archival/recall memory). Not
              recommended unless you have an advanced use case.

          metadata: The metadata of the agent.

          model: The model handle or model settings for the agent to use, specified either by a
              handle or an object. See the model schema for more information.

          name: The name of the agent.

          parallel_tool_calls: Deprecated: Use `model` field to configure parallel tool calls instead. If set
              to True, enables parallel tool calling.

          per_file_view_window_char_limit: The per-file view window character limit for this agent. Setting this too high
              may exceed the context window, which will break the agent.

          project: Deprecated: Project should now be passed via the X-Project header instead of in
              the request body. If using the SDK, this can be done via the x_project
              parameter.

          project_id: Deprecated: No longer used. The id of the project the agent belongs to.

          reasoning: Deprecated: Use `model` field to configure reasoning instead. Whether to enable
              reasoning for this agent.

          response_format: The response format for the agent.

          secrets: The environment variables for tool execution specific to this agent.

          source_ids: The ids of the sources used by the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          template: Deprecated: No longer used.

          template_id: Deprecated: No longer used. The id of the template the agent belongs to.

          timezone: The timezone of the agent (IANA format).

          tool_exec_environment_variables: Deprecated: Use `secrets` field instead. Environment variables for tool
              execution.

          tool_ids: The ids of the tools used by the agent.

          tool_rules: The tool rules governing the agent.

          tools: The tools used by the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                    "parallel_tool_calls": parallel_tool_calls,
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
        include: List[
            Literal[
                "agent.blocks",
                "agent.identities",
                "agent.managed_group",
                "agent.secrets",
                "agent.sources",
                "agent.tags",
                "agent.tools",
            ]
        ]
        | Omit = omit,
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
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          include: Specify which relational fields to include in the response. No relationships are
              included by default.

          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.This is a legacy
              parameter, and no longer supported after 1.0.0 SDK versions.

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
                    {
                        "include": include,
                        "include_relationships": include_relationships,
                    },
                    agent_retrieve_params.AgentRetrieveParams,
                ),
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
        include: List[
            Literal[
                "agent.blocks",
                "agent.identities",
                "agent.managed_group",
                "agent.secrets",
                "agent.sources",
                "agent.tags",
                "agent.tools",
            ]
        ]
        | Omit = omit,
        include_relationships: Optional[SequenceNotStr[str]] | Omit = omit,
        last_stop_reason: Optional[StopReasonType] | Omit = omit,
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
    ) -> SyncArrayPage[AgentState]:
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

          include: Specify which relational fields to include in the response. No relationships are
              included by default.

          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.This is a legacy
              parameter, and no longer supported after 1.0.0 SDK versions.

          last_stop_reason: Filter agents by their last stop reason.

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
        return self._get_api_list(
            "/v1/agents/",
            page=SyncArrayPage[AgentState],
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
                        "include": include,
                        "include_relationships": include_relationships,
                        "last_stop_reason": last_stop_reason,
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
            model=AgentState,
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
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

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

    def export_file(
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

        Args:
          use_legacy_format: If True, exports using the legacy single-agent 'v1' format with inline
              tools/blocks. If False, exports using the new multi-entity 'v2' format, with
              separate agents, tools, blocks, files, etc.

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
                    agent_export_file_params.AgentExportFileParams,
                ),
            ),
            cast_to=str,
        )

    def import_file(
        self,
        *,
        file: FileTypes,
        append_copy_suffix: bool | Omit = omit,
        env_vars_json: Optional[str] | Omit = omit,
        override_embedding_handle: Optional[str] | Omit = omit,
        override_existing_tools: bool | Omit = omit,
        override_name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        strip_messages: bool | Omit = omit,
        x_override_embedding_model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentImportFileResponse:
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

          override_name: If provided, overrides the agent name with this value.

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
                "override_name": override_name,
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
            body=maybe_transform(body, agent_import_file_params.AgentImportFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentImportFileResponse,
        )

    def modify(
        self,
        agent_id: str,
        *,
        base_template_id: Optional[str] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        context_window_limit: Optional[int] | Omit = omit,
        description: Optional[str] | Omit = omit,
        embedding: Optional[agent_modify_params.Embedding] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        enable_sleeptime: Optional[bool] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        identity_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        last_run_completion: Union[str, datetime, None] | Omit = omit,
        last_run_duration_ms: Optional[int] | Omit = omit,
        last_stop_reason: Optional[StopReasonType] | Omit = omit,
        llm_config: Optional[LlmConfigParam] | Omit = omit,
        max_files_open: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        message_buffer_autoclear: Optional[bool] | Omit = omit,
        message_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[agent_modify_params.Model] | Omit = omit,
        name: Optional[str] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        per_file_view_window_char_limit: Optional[int] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        reasoning: Optional[bool] | Omit = omit,
        response_format: Optional[agent_modify_params.ResponseFormat] | Omit = omit,
        secrets: Optional[Dict[str, str]] | Omit = omit,
        source_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        tool_exec_environment_variables: Optional[Dict[str, str]] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_rules: Optional[Iterable[agent_modify_params.ToolRule]] | Omit = omit,
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
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          base_template_id: The base template id of the agent.

          block_ids: The ids of the blocks used by the agent.

          context_window_limit: The context window limit used by the agent.

          description: The description of the agent.

          embedding: The embedding configuration handle used by the agent, specified in the format
              provider/model-name.

          embedding_config: Configuration for embedding model connection and processing parameters.

          enable_sleeptime: If set to True, memory management will move to a background agent thread.

          hidden: If set to True, the agent will be hidden.

          identity_ids: The ids of the identities associated with this agent.

          last_run_completion: The timestamp when the agent last completed a run.

          last_run_duration_ms: The duration in milliseconds of the agent's last run.

          last_stop_reason: The stop reason from the agent's last run.

          llm_config: Configuration for Language Model (LLM) connection and generation parameters.

          max_files_open: Maximum number of files that can be open at once for this agent. Setting this
              too high may exceed the context window, which will break the agent.

          max_tokens: Deprecated: Use `model` field to configure max output tokens instead. The
              maximum number of tokens to generate, including reasoning step.

          message_buffer_autoclear: If set to True, the agent will not remember previous messages (though the agent
              will still retain state via core memory blocks and archival/recall memory). Not
              recommended unless you have an advanced use case.

          message_ids: The ids of the messages in the agent's in-context memory.

          metadata: The metadata of the agent.

          model: The model used by the agent, specified either by a handle or an object. See the
              model schema for more information.

          name: The name of the agent.

          parallel_tool_calls: Deprecated: Use `model` field to configure parallel tool calls instead. If set
              to True, enables parallel tool calling.

          per_file_view_window_char_limit: The per-file view window character limit for this agent. Setting this too high
              may exceed the context window, which will break the agent.

          project_id: The id of the project the agent belongs to.

          reasoning: Deprecated: Use `model` field to configure reasoning instead. Whether to enable
              reasoning for this agent.

          response_format: Deprecated: Use `model` field to configure response format instead. The response
              format for the agent.

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
                    "context_window_limit": context_window_limit,
                    "description": description,
                    "embedding": embedding,
                    "embedding_config": embedding_config,
                    "enable_sleeptime": enable_sleeptime,
                    "hidden": hidden,
                    "identity_ids": identity_ids,
                    "last_run_completion": last_run_completion,
                    "last_run_duration_ms": last_run_duration_ms,
                    "last_stop_reason": last_stop_reason,
                    "llm_config": llm_config,
                    "max_files_open": max_files_open,
                    "max_tokens": max_tokens,
                    "message_buffer_autoclear": message_buffer_autoclear,
                    "message_ids": message_ids,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                    "parallel_tool_calls": parallel_tool_calls,
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
                agent_modify_params.AgentModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def blocks(self) -> AsyncBlocksResource:
        return AsyncBlocksResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def archives(self) -> AsyncArchivesResource:
        return AsyncArchivesResource(self._client)

    @cached_property
    def identities(self) -> AsyncIdentitiesResource:
        return AsyncIdentitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
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
        embedding: Optional[agent_create_params.Embedding] | Omit = omit,
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
        model: Optional[agent_create_params.Model] | Omit = omit,
        name: str | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
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

          base_template_id: Deprecated: No longer used. The base template id of the agent.

          block_ids: The ids of the blocks used by the agent.

          context_window_limit: The context window limit used by the agent.

          description: The description of the agent.

          embedding: The embedding configuration handle used by the agent, specified in the format
              provider/model-name.

          embedding_chunk_size: Deprecated: No longer used. The embedding chunk size used by the agent.

          embedding_config: Configuration for embedding model connection and processing parameters.

          enable_reasoner: Deprecated: Use `model` field to configure reasoning instead. Whether to enable
              internal extended thinking step for a reasoner model.

          enable_sleeptime: If set to True, memory management will move to a background agent thread.

          from_template: Deprecated: please use the 'create agents from a template' endpoint instead.

          hidden: Deprecated: No longer used. If set to True, the agent will be hidden.

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

          max_reasoning_tokens: Deprecated: Use `model` field to configure reasoning tokens instead. The maximum
              number of tokens to generate for reasoning step.

          max_tokens: Deprecated: Use `model` field to configure max output tokens instead. The
              maximum number of tokens to generate, including reasoning step.

          memory_blocks: The blocks to create in the agent's in-context memory.

          memory_variables: Deprecated: Only relevant for creating agents from a template. Use the 'create
              agents from a template' endpoint instead.

          message_buffer_autoclear: If set to True, the agent will not remember previous messages (though the agent
              will still retain state via core memory blocks and archival/recall memory). Not
              recommended unless you have an advanced use case.

          metadata: The metadata of the agent.

          model: The model handle or model settings for the agent to use, specified either by a
              handle or an object. See the model schema for more information.

          name: The name of the agent.

          parallel_tool_calls: Deprecated: Use `model` field to configure parallel tool calls instead. If set
              to True, enables parallel tool calling.

          per_file_view_window_char_limit: The per-file view window character limit for this agent. Setting this too high
              may exceed the context window, which will break the agent.

          project: Deprecated: Project should now be passed via the X-Project header instead of in
              the request body. If using the SDK, this can be done via the x_project
              parameter.

          project_id: Deprecated: No longer used. The id of the project the agent belongs to.

          reasoning: Deprecated: Use `model` field to configure reasoning instead. Whether to enable
              reasoning for this agent.

          response_format: The response format for the agent.

          secrets: The environment variables for tool execution specific to this agent.

          source_ids: The ids of the sources used by the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          template: Deprecated: No longer used.

          template_id: Deprecated: No longer used. The id of the template the agent belongs to.

          timezone: The timezone of the agent (IANA format).

          tool_exec_environment_variables: Deprecated: Use `secrets` field instead. Environment variables for tool
              execution.

          tool_ids: The ids of the tools used by the agent.

          tool_rules: The tool rules governing the agent.

          tools: The tools used by the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                    "parallel_tool_calls": parallel_tool_calls,
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
        include: List[
            Literal[
                "agent.blocks",
                "agent.identities",
                "agent.managed_group",
                "agent.secrets",
                "agent.sources",
                "agent.tags",
                "agent.tools",
            ]
        ]
        | Omit = omit,
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
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          include: Specify which relational fields to include in the response. No relationships are
              included by default.

          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.This is a legacy
              parameter, and no longer supported after 1.0.0 SDK versions.

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
                    {
                        "include": include,
                        "include_relationships": include_relationships,
                    },
                    agent_retrieve_params.AgentRetrieveParams,
                ),
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
        include: List[
            Literal[
                "agent.blocks",
                "agent.identities",
                "agent.managed_group",
                "agent.secrets",
                "agent.sources",
                "agent.tags",
                "agent.tools",
            ]
        ]
        | Omit = omit,
        include_relationships: Optional[SequenceNotStr[str]] | Omit = omit,
        last_stop_reason: Optional[StopReasonType] | Omit = omit,
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
    ) -> AsyncPaginator[AgentState, AsyncArrayPage[AgentState]]:
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

          include: Specify which relational fields to include in the response. No relationships are
              included by default.

          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.This is a legacy
              parameter, and no longer supported after 1.0.0 SDK versions.

          last_stop_reason: Filter agents by their last stop reason.

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
        return self._get_api_list(
            "/v1/agents/",
            page=AsyncArrayPage[AgentState],
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
                        "include": include,
                        "include_relationships": include_relationships,
                        "last_stop_reason": last_stop_reason,
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
            model=AgentState,
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
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

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

    async def export_file(
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

        Args:
          use_legacy_format: If True, exports using the legacy single-agent 'v1' format with inline
              tools/blocks. If False, exports using the new multi-entity 'v2' format, with
              separate agents, tools, blocks, files, etc.

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
                    agent_export_file_params.AgentExportFileParams,
                ),
            ),
            cast_to=str,
        )

    async def import_file(
        self,
        *,
        file: FileTypes,
        append_copy_suffix: bool | Omit = omit,
        env_vars_json: Optional[str] | Omit = omit,
        override_embedding_handle: Optional[str] | Omit = omit,
        override_existing_tools: bool | Omit = omit,
        override_name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        strip_messages: bool | Omit = omit,
        x_override_embedding_model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentImportFileResponse:
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

          override_name: If provided, overrides the agent name with this value.

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
                "override_name": override_name,
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
            body=await async_maybe_transform(body, agent_import_file_params.AgentImportFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentImportFileResponse,
        )

    async def modify(
        self,
        agent_id: str,
        *,
        base_template_id: Optional[str] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        context_window_limit: Optional[int] | Omit = omit,
        description: Optional[str] | Omit = omit,
        embedding: Optional[agent_modify_params.Embedding] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        enable_sleeptime: Optional[bool] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        identity_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        last_run_completion: Union[str, datetime, None] | Omit = omit,
        last_run_duration_ms: Optional[int] | Omit = omit,
        last_stop_reason: Optional[StopReasonType] | Omit = omit,
        llm_config: Optional[LlmConfigParam] | Omit = omit,
        max_files_open: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        message_buffer_autoclear: Optional[bool] | Omit = omit,
        message_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[agent_modify_params.Model] | Omit = omit,
        name: Optional[str] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        per_file_view_window_char_limit: Optional[int] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        reasoning: Optional[bool] | Omit = omit,
        response_format: Optional[agent_modify_params.ResponseFormat] | Omit = omit,
        secrets: Optional[Dict[str, str]] | Omit = omit,
        source_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        tool_exec_environment_variables: Optional[Dict[str, str]] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_rules: Optional[Iterable[agent_modify_params.ToolRule]] | Omit = omit,
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
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          base_template_id: The base template id of the agent.

          block_ids: The ids of the blocks used by the agent.

          context_window_limit: The context window limit used by the agent.

          description: The description of the agent.

          embedding: The embedding configuration handle used by the agent, specified in the format
              provider/model-name.

          embedding_config: Configuration for embedding model connection and processing parameters.

          enable_sleeptime: If set to True, memory management will move to a background agent thread.

          hidden: If set to True, the agent will be hidden.

          identity_ids: The ids of the identities associated with this agent.

          last_run_completion: The timestamp when the agent last completed a run.

          last_run_duration_ms: The duration in milliseconds of the agent's last run.

          last_stop_reason: The stop reason from the agent's last run.

          llm_config: Configuration for Language Model (LLM) connection and generation parameters.

          max_files_open: Maximum number of files that can be open at once for this agent. Setting this
              too high may exceed the context window, which will break the agent.

          max_tokens: Deprecated: Use `model` field to configure max output tokens instead. The
              maximum number of tokens to generate, including reasoning step.

          message_buffer_autoclear: If set to True, the agent will not remember previous messages (though the agent
              will still retain state via core memory blocks and archival/recall memory). Not
              recommended unless you have an advanced use case.

          message_ids: The ids of the messages in the agent's in-context memory.

          metadata: The metadata of the agent.

          model: The model used by the agent, specified either by a handle or an object. See the
              model schema for more information.

          name: The name of the agent.

          parallel_tool_calls: Deprecated: Use `model` field to configure parallel tool calls instead. If set
              to True, enables parallel tool calling.

          per_file_view_window_char_limit: The per-file view window character limit for this agent. Setting this too high
              may exceed the context window, which will break the agent.

          project_id: The id of the project the agent belongs to.

          reasoning: Deprecated: Use `model` field to configure reasoning instead. Whether to enable
              reasoning for this agent.

          response_format: Deprecated: Use `model` field to configure response format instead. The response
              format for the agent.

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
                    "context_window_limit": context_window_limit,
                    "description": description,
                    "embedding": embedding,
                    "embedding_config": embedding_config,
                    "enable_sleeptime": enable_sleeptime,
                    "hidden": hidden,
                    "identity_ids": identity_ids,
                    "last_run_completion": last_run_completion,
                    "last_run_duration_ms": last_run_duration_ms,
                    "last_stop_reason": last_stop_reason,
                    "llm_config": llm_config,
                    "max_files_open": max_files_open,
                    "max_tokens": max_tokens,
                    "message_buffer_autoclear": message_buffer_autoclear,
                    "message_ids": message_ids,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                    "parallel_tool_calls": parallel_tool_calls,
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
                agent_modify_params.AgentModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
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
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.export_file = to_raw_response_wrapper(
            agents.export_file,
        )
        self.import_file = to_raw_response_wrapper(
            agents.import_file,
        )
        self.modify = to_raw_response_wrapper(
            agents.modify,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._agents.messages)

    @cached_property
    def blocks(self) -> BlocksResourceWithRawResponse:
        return BlocksResourceWithRawResponse(self._agents.blocks)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._agents.folders)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._agents.files)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._agents.groups)

    @cached_property
    def archives(self) -> ArchivesResourceWithRawResponse:
        return ArchivesResourceWithRawResponse(self._agents.archives)

    @cached_property
    def identities(self) -> IdentitiesResourceWithRawResponse:
        return IdentitiesResourceWithRawResponse(self._agents.identities)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.export_file = async_to_raw_response_wrapper(
            agents.export_file,
        )
        self.import_file = async_to_raw_response_wrapper(
            agents.import_file,
        )
        self.modify = async_to_raw_response_wrapper(
            agents.modify,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._agents.messages)

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithRawResponse:
        return AsyncBlocksResourceWithRawResponse(self._agents.blocks)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._agents.folders)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._agents.files)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._agents.groups)

    @cached_property
    def archives(self) -> AsyncArchivesResourceWithRawResponse:
        return AsyncArchivesResourceWithRawResponse(self._agents.archives)

    @cached_property
    def identities(self) -> AsyncIdentitiesResourceWithRawResponse:
        return AsyncIdentitiesResourceWithRawResponse(self._agents.identities)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.export_file = to_streamed_response_wrapper(
            agents.export_file,
        )
        self.import_file = to_streamed_response_wrapper(
            agents.import_file,
        )
        self.modify = to_streamed_response_wrapper(
            agents.modify,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._agents.messages)

    @cached_property
    def blocks(self) -> BlocksResourceWithStreamingResponse:
        return BlocksResourceWithStreamingResponse(self._agents.blocks)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._agents.folders)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._agents.files)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._agents.groups)

    @cached_property
    def archives(self) -> ArchivesResourceWithStreamingResponse:
        return ArchivesResourceWithStreamingResponse(self._agents.archives)

    @cached_property
    def identities(self) -> IdentitiesResourceWithStreamingResponse:
        return IdentitiesResourceWithStreamingResponse(self._agents.identities)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.export_file = async_to_streamed_response_wrapper(
            agents.export_file,
        )
        self.import_file = async_to_streamed_response_wrapper(
            agents.import_file,
        )
        self.modify = async_to_streamed_response_wrapper(
            agents.modify,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._agents.messages)

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithStreamingResponse:
        return AsyncBlocksResourceWithStreamingResponse(self._agents.blocks)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._agents.folders)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._agents.files)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._agents.groups)

    @cached_property
    def archives(self) -> AsyncArchivesResourceWithStreamingResponse:
        return AsyncArchivesResourceWithStreamingResponse(self._agents.archives)

    @cached_property
    def identities(self) -> AsyncIdentitiesResourceWithStreamingResponse:
        return AsyncIdentitiesResourceWithStreamingResponse(self._agents.identities)
