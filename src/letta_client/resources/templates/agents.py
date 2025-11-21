# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.templates import agent_create_params
from ...types.templates.agent_create_response import AgentCreateResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
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
        template_version: str,
        *,
        agent_name: str | Omit = omit,
        identity_ids: SequenceNotStr[str] | Omit = omit,
        initial_message_sequence: Iterable[agent_create_params.InitialMessageSequence] | Omit = omit,
        memory_variables: Dict[str, str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        tool_variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """
        Creates an Agent or multiple Agents from a template

        Args:
          agent_name: The name of the agent, optional otherwise a random one will be assigned

          identity_ids: The identity ids to assign to the agent

          initial_message_sequence: Set an initial sequence of messages, if not provided, the agent will start with
              the default message sequence, if an empty array is provided, the agent will
              start with no messages

          memory_variables: The memory variables to assign to the agent

          tags: The tags to assign to the agent

          tool_variables: The tool variables to assign to the agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_version:
            raise ValueError(f"Expected a non-empty value for `template_version` but received {template_version!r}")
        return self._post(
            f"/v1/templates/{template_version}/agents",
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "identity_ids": identity_ids,
                    "initial_message_sequence": initial_message_sequence,
                    "memory_variables": memory_variables,
                    "tags": tags,
                    "tool_variables": tool_variables,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
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
        template_version: str,
        *,
        agent_name: str | Omit = omit,
        identity_ids: SequenceNotStr[str] | Omit = omit,
        initial_message_sequence: Iterable[agent_create_params.InitialMessageSequence] | Omit = omit,
        memory_variables: Dict[str, str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        tool_variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """
        Creates an Agent or multiple Agents from a template

        Args:
          agent_name: The name of the agent, optional otherwise a random one will be assigned

          identity_ids: The identity ids to assign to the agent

          initial_message_sequence: Set an initial sequence of messages, if not provided, the agent will start with
              the default message sequence, if an empty array is provided, the agent will
              start with no messages

          memory_variables: The memory variables to assign to the agent

          tags: The tags to assign to the agent

          tool_variables: The tool variables to assign to the agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_version:
            raise ValueError(f"Expected a non-empty value for `template_version` but received {template_version!r}")
        return await self._post(
            f"/v1/templates/{template_version}/agents",
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "identity_ids": identity_ids,
                    "initial_message_sequence": initial_message_sequence,
                    "memory_variables": memory_variables,
                    "tags": tags,
                    "tool_variables": tool_variables,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
