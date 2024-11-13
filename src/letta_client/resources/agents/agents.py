# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from .memory import (
    MemoryResource,
    AsyncMemoryResource,
    MemoryResourceWithRawResponse,
    AsyncMemoryResourceWithRawResponse,
    MemoryResourceWithStreamingResponse,
    AsyncMemoryResourceWithStreamingResponse,
)
from ...types import (
    agent_list_params,
    agent_create_params,
    agent_update_params,
)
from .context import (
    ContextResource,
    AsyncContextResource,
    ContextResourceWithRawResponse,
    AsyncContextResourceWithRawResponse,
    ContextResourceWithStreamingResponse,
    AsyncContextResourceWithStreamingResponse,
)
from .sources import (
    SourcesResource,
    AsyncSourcesResource,
    SourcesResourceWithRawResponse,
    AsyncSourcesResourceWithRawResponse,
    SourcesResourceWithStreamingResponse,
    AsyncSourcesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .archival import (
    ArchivalResource,
    AsyncArchivalResource,
    ArchivalResourceWithRawResponse,
    AsyncArchivalResourceWithRawResponse,
    ArchivalResourceWithStreamingResponse,
    AsyncArchivalResourceWithStreamingResponse,
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
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .memory.memory import MemoryResource, AsyncMemoryResource
from ..._base_client import make_request_options
from ...types.agent_state import AgentState
from ...types.memory_param import MemoryParam
from ...types.llm_config_param import LlmConfigParam
from ...types.agent_list_response import AgentListResponse
from ...types.embedding_config_param import EmbeddingConfigParam

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def context(self) -> ContextResource:
        return ContextResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def sources(self) -> SourcesResource:
        return SourcesResource(self._client)

    @cached_property
    def memory(self) -> MemoryResource:
        return MemoryResource(self._client)

    @cached_property
    def archival(self) -> ArchivalResource:
        return ArchivalResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_type: Optional[Literal["memgpt_agent", "split_thread_agent", "o1_agent"]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        embedding_config: Optional[EmbeddingConfigParam] | NotGiven = NOT_GIVEN,
        initial_message_sequence: Optional[Iterable[agent_create_params.InitialMessageSequence]] | NotGiven = NOT_GIVEN,
        llm_config: Optional[LlmConfigParam] | NotGiven = NOT_GIVEN,
        memory: Optional[MemoryParam] | NotGiven = NOT_GIVEN,
        message_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        system: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tool_rules: Optional[Iterable[agent_create_params.ToolRule]] | NotGiven = NOT_GIVEN,
        tools: Optional[List[str]] | NotGiven = NOT_GIVEN,
        body_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        header_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Create a new agent with the specified configuration.

        Args:
          agent_type: Enum to represent the type of agent.

          description: The description of the agent.

          embedding_config: Embedding model configuration. This object specifies all the information
              necessary to access an embedding model to usage with Letta, except for secret
              keys.

              Attributes: embedding_endpoint_type (str): The endpoint type for the model.
              embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
              model for the embedding. embedding_dim (int): The dimension of the embedding.
              embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
              (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
              azure_version (str): The Azure version for the model (Azure only).
              azure_deployment (str): The Azure deployment for the model (Azure only).

          initial_message_sequence: The initial set of messages to put in the agent's in-context memory.

          llm_config: Configuration for a Language Model (LLM) model. This object specifies all the
              information necessary to access an LLM model to usage with Letta, except for
              secret keys.

              Attributes: model (str): The name of the LLM model. model_endpoint_type (str):
              The endpoint type for the model. model_endpoint (str): The endpoint for the
              model. model_wrapper (str): The wrapper for the model. This is used to wrap
              additional text around the input/output of the model. This is useful for
              text-to-text completions, such as the Completions API in OpenAI. context_window
              (int): The context window size for the model. put_inner_thoughts_in_kwargs
              (bool): Puts `inner_thoughts` as a kwarg in the function call if this is set to
              True. This helps with function calling performance and also the generation of
              inner thoughts.

          memory: Represents the in-context memory of the agent. This includes both the `Block`
              objects (labelled by sections), as well as tools to edit the blocks.

              Attributes: memory (Dict[str, Block]): Mapping from memory block section to
              memory block.

          message_ids: The ids of the messages in the agent's in-context memory.

          metadata: The metadata of the agent.

          name: The name of the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          tool_rules: The tool rules governing the agent.

          tools: The tools used by the agent.

          body_user_id: The user id of the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": header_user_id}), **(extra_headers or {})}
        return self._post(
            "/v1/agents/",
            body=maybe_transform(
                {
                    "agent_type": agent_type,
                    "description": description,
                    "embedding_config": embedding_config,
                    "initial_message_sequence": initial_message_sequence,
                    "llm_config": llm_config,
                    "memory": memory,
                    "message_ids": message_ids,
                    "metadata": metadata,
                    "name": name,
                    "system": system,
                    "tags": tags,
                    "tool_rules": tool_rules,
                    "tools": tools,
                    "body_user_id": body_user_id,
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
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Get the state of the agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._get(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def update(
        self,
        agent_id: str,
        *,
        id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        embedding_config: Optional[EmbeddingConfigParam] | NotGiven = NOT_GIVEN,
        llm_config: Optional[LlmConfigParam] | NotGiven = NOT_GIVEN,
        memory: Optional[MemoryParam] | NotGiven = NOT_GIVEN,
        message_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        system: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tools: Optional[List[str]] | NotGiven = NOT_GIVEN,
        body_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        header_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Update an exsiting agent

        Args:
          id: The id of the agent.

          description: The description of the agent.

          embedding_config: Embedding model configuration. This object specifies all the information
              necessary to access an embedding model to usage with Letta, except for secret
              keys.

              Attributes: embedding_endpoint_type (str): The endpoint type for the model.
              embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
              model for the embedding. embedding_dim (int): The dimension of the embedding.
              embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
              (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
              azure_version (str): The Azure version for the model (Azure only).
              azure_deployment (str): The Azure deployment for the model (Azure only).

          llm_config: Configuration for a Language Model (LLM) model. This object specifies all the
              information necessary to access an LLM model to usage with Letta, except for
              secret keys.

              Attributes: model (str): The name of the LLM model. model_endpoint_type (str):
              The endpoint type for the model. model_endpoint (str): The endpoint for the
              model. model_wrapper (str): The wrapper for the model. This is used to wrap
              additional text around the input/output of the model. This is useful for
              text-to-text completions, such as the Completions API in OpenAI. context_window
              (int): The context window size for the model. put_inner_thoughts_in_kwargs
              (bool): Puts `inner_thoughts` as a kwarg in the function call if this is set to
              True. This helps with function calling performance and also the generation of
              inner thoughts.

          memory: Represents the in-context memory of the agent. This includes both the `Block`
              objects (labelled by sections), as well as tools to edit the blocks.

              Attributes: memory (Dict[str, Block]): Mapping from memory block section to
              memory block.

          message_ids: The ids of the messages in the agent's in-context memory.

          metadata: The metadata of the agent.

          name: The name of the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          tools: The tools used by the agent.

          body_user_id: The user id of the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": header_user_id}), **(extra_headers or {})}
        return self._patch(
            f"/v1/agents/{agent_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "embedding_config": embedding_config,
                    "llm_config": llm_config,
                    "memory": memory,
                    "message_ids": message_ids,
                    "metadata": metadata,
                    "name": name,
                    "system": system,
                    "tags": tags,
                    "tools": tools,
                    "body_user_id": body_user_id,
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
        name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """List all agents associated with a given user.

        This endpoint retrieves a list of
        all agents and their configurations associated with the specified user ID.

        Args:
          name: Name of the agent

          tags: List of tags to filter agents by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._get(
            "/v1/agents/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "tags": tags,
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
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._delete(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def context(self) -> AsyncContextResource:
        return AsyncContextResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def sources(self) -> AsyncSourcesResource:
        return AsyncSourcesResource(self._client)

    @cached_property
    def memory(self) -> AsyncMemoryResource:
        return AsyncMemoryResource(self._client)

    @cached_property
    def archival(self) -> AsyncArchivalResource:
        return AsyncArchivalResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_type: Optional[Literal["memgpt_agent", "split_thread_agent", "o1_agent"]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        embedding_config: Optional[EmbeddingConfigParam] | NotGiven = NOT_GIVEN,
        initial_message_sequence: Optional[Iterable[agent_create_params.InitialMessageSequence]] | NotGiven = NOT_GIVEN,
        llm_config: Optional[LlmConfigParam] | NotGiven = NOT_GIVEN,
        memory: Optional[MemoryParam] | NotGiven = NOT_GIVEN,
        message_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        system: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tool_rules: Optional[Iterable[agent_create_params.ToolRule]] | NotGiven = NOT_GIVEN,
        tools: Optional[List[str]] | NotGiven = NOT_GIVEN,
        body_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        header_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Create a new agent with the specified configuration.

        Args:
          agent_type: Enum to represent the type of agent.

          description: The description of the agent.

          embedding_config: Embedding model configuration. This object specifies all the information
              necessary to access an embedding model to usage with Letta, except for secret
              keys.

              Attributes: embedding_endpoint_type (str): The endpoint type for the model.
              embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
              model for the embedding. embedding_dim (int): The dimension of the embedding.
              embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
              (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
              azure_version (str): The Azure version for the model (Azure only).
              azure_deployment (str): The Azure deployment for the model (Azure only).

          initial_message_sequence: The initial set of messages to put in the agent's in-context memory.

          llm_config: Configuration for a Language Model (LLM) model. This object specifies all the
              information necessary to access an LLM model to usage with Letta, except for
              secret keys.

              Attributes: model (str): The name of the LLM model. model_endpoint_type (str):
              The endpoint type for the model. model_endpoint (str): The endpoint for the
              model. model_wrapper (str): The wrapper for the model. This is used to wrap
              additional text around the input/output of the model. This is useful for
              text-to-text completions, such as the Completions API in OpenAI. context_window
              (int): The context window size for the model. put_inner_thoughts_in_kwargs
              (bool): Puts `inner_thoughts` as a kwarg in the function call if this is set to
              True. This helps with function calling performance and also the generation of
              inner thoughts.

          memory: Represents the in-context memory of the agent. This includes both the `Block`
              objects (labelled by sections), as well as tools to edit the blocks.

              Attributes: memory (Dict[str, Block]): Mapping from memory block section to
              memory block.

          message_ids: The ids of the messages in the agent's in-context memory.

          metadata: The metadata of the agent.

          name: The name of the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          tool_rules: The tool rules governing the agent.

          tools: The tools used by the agent.

          body_user_id: The user id of the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": header_user_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/agents/",
            body=await async_maybe_transform(
                {
                    "agent_type": agent_type,
                    "description": description,
                    "embedding_config": embedding_config,
                    "initial_message_sequence": initial_message_sequence,
                    "llm_config": llm_config,
                    "memory": memory,
                    "message_ids": message_ids,
                    "metadata": metadata,
                    "name": name,
                    "system": system,
                    "tags": tags,
                    "tool_rules": tool_rules,
                    "tools": tools,
                    "body_user_id": body_user_id,
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
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Get the state of the agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._get(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def update(
        self,
        agent_id: str,
        *,
        id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        embedding_config: Optional[EmbeddingConfigParam] | NotGiven = NOT_GIVEN,
        llm_config: Optional[LlmConfigParam] | NotGiven = NOT_GIVEN,
        memory: Optional[MemoryParam] | NotGiven = NOT_GIVEN,
        message_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        system: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tools: Optional[List[str]] | NotGiven = NOT_GIVEN,
        body_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        header_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Update an exsiting agent

        Args:
          id: The id of the agent.

          description: The description of the agent.

          embedding_config: Embedding model configuration. This object specifies all the information
              necessary to access an embedding model to usage with Letta, except for secret
              keys.

              Attributes: embedding_endpoint_type (str): The endpoint type for the model.
              embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
              model for the embedding. embedding_dim (int): The dimension of the embedding.
              embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
              (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
              azure_version (str): The Azure version for the model (Azure only).
              azure_deployment (str): The Azure deployment for the model (Azure only).

          llm_config: Configuration for a Language Model (LLM) model. This object specifies all the
              information necessary to access an LLM model to usage with Letta, except for
              secret keys.

              Attributes: model (str): The name of the LLM model. model_endpoint_type (str):
              The endpoint type for the model. model_endpoint (str): The endpoint for the
              model. model_wrapper (str): The wrapper for the model. This is used to wrap
              additional text around the input/output of the model. This is useful for
              text-to-text completions, such as the Completions API in OpenAI. context_window
              (int): The context window size for the model. put_inner_thoughts_in_kwargs
              (bool): Puts `inner_thoughts` as a kwarg in the function call if this is set to
              True. This helps with function calling performance and also the generation of
              inner thoughts.

          memory: Represents the in-context memory of the agent. This includes both the `Block`
              objects (labelled by sections), as well as tools to edit the blocks.

              Attributes: memory (Dict[str, Block]): Mapping from memory block section to
              memory block.

          message_ids: The ids of the messages in the agent's in-context memory.

          metadata: The metadata of the agent.

          name: The name of the agent.

          system: The system prompt used by the agent.

          tags: The tags associated with the agent.

          tools: The tools used by the agent.

          body_user_id: The user id of the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": header_user_id}), **(extra_headers or {})}
        return await self._patch(
            f"/v1/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "embedding_config": embedding_config,
                    "llm_config": llm_config,
                    "memory": memory,
                    "message_ids": message_ids,
                    "metadata": metadata,
                    "name": name,
                    "system": system,
                    "tags": tags,
                    "tools": tools,
                    "body_user_id": body_user_id,
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
        name: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """List all agents associated with a given user.

        This endpoint retrieves a list of
        all agents and their configurations associated with the specified user ID.

        Args:
          name: Name of the agent

          tags: List of tags to filter agents by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/agents/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "tags": tags,
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
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._delete(
            f"/v1/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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

    @cached_property
    def context(self) -> ContextResourceWithRawResponse:
        return ContextResourceWithRawResponse(self._agents.context)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def sources(self) -> SourcesResourceWithRawResponse:
        return SourcesResourceWithRawResponse(self._agents.sources)

    @cached_property
    def memory(self) -> MemoryResourceWithRawResponse:
        return MemoryResourceWithRawResponse(self._agents.memory)

    @cached_property
    def archival(self) -> ArchivalResourceWithRawResponse:
        return ArchivalResourceWithRawResponse(self._agents.archival)

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

    @cached_property
    def context(self) -> AsyncContextResourceWithRawResponse:
        return AsyncContextResourceWithRawResponse(self._agents.context)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithRawResponse:
        return AsyncSourcesResourceWithRawResponse(self._agents.sources)

    @cached_property
    def memory(self) -> AsyncMemoryResourceWithRawResponse:
        return AsyncMemoryResourceWithRawResponse(self._agents.memory)

    @cached_property
    def archival(self) -> AsyncArchivalResourceWithRawResponse:
        return AsyncArchivalResourceWithRawResponse(self._agents.archival)

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

    @cached_property
    def context(self) -> ContextResourceWithStreamingResponse:
        return ContextResourceWithStreamingResponse(self._agents.context)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def sources(self) -> SourcesResourceWithStreamingResponse:
        return SourcesResourceWithStreamingResponse(self._agents.sources)

    @cached_property
    def memory(self) -> MemoryResourceWithStreamingResponse:
        return MemoryResourceWithStreamingResponse(self._agents.memory)

    @cached_property
    def archival(self) -> ArchivalResourceWithStreamingResponse:
        return ArchivalResourceWithStreamingResponse(self._agents.archival)

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

    @cached_property
    def context(self) -> AsyncContextResourceWithStreamingResponse:
        return AsyncContextResourceWithStreamingResponse(self._agents.context)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithStreamingResponse:
        return AsyncSourcesResourceWithStreamingResponse(self._agents.sources)

    @cached_property
    def memory(self) -> AsyncMemoryResourceWithStreamingResponse:
        return AsyncMemoryResourceWithStreamingResponse(self._agents.memory)

    @cached_property
    def archival(self) -> AsyncArchivalResourceWithStreamingResponse:
        return AsyncArchivalResourceWithStreamingResponse(self._agents.archival)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._agents.messages)
