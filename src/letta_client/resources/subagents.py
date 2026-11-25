# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import subagent_list_params, subagent_create_params, subagent_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.subagent import Subagent
from ..types.subagent_list_response import SubagentListResponse

__all__ = ["SubagentsResource", "AsyncSubagentsResource"]


class SubagentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubagentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return SubagentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubagentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return SubagentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        harness: str,
        parent_conversation_id: str,
        agent_id: Optional[str] | Omit = omit,
        archived: bool | Omit = omit,
        computer: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        fork_context: bool | Omit = omit,
        mcp_config: Optional[Dict[str, object]] | Omit = omit,
        model_config: Optional[Dict[str, object]] | Omit = omit,
        parent_agent_id: str | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        repositories: Optional[SequenceNotStr[str]] | Omit = omit,
        sandbox_size: Optional[str] | Omit = omit,
        status: Literal["running", "idle", "completed", "failed", "stopped"] | Omit = omit,
        subagent_type: Optional[str] | Omit = omit,
        worker_session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subagent:
        """
        Create a subagent record

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/subagents",
            body=maybe_transform(
                {
                    "description": description,
                    "harness": harness,
                    "parent_conversation_id": parent_conversation_id,
                    "agent_id": agent_id,
                    "archived": archived,
                    "computer": computer,
                    "conversation_id": conversation_id,
                    "fork_context": fork_context,
                    "mcp_config": mcp_config,
                    "model_config": model_config,
                    "parent_agent_id": parent_agent_id,
                    "prompt": prompt,
                    "repositories": repositories,
                    "sandbox_size": sandbox_size,
                    "status": status,
                    "subagent_type": subagent_type,
                    "worker_session_id": worker_session_id,
                },
                subagent_create_params.SubagentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subagent,
        )

    def update(
        self,
        subagent_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        archived: bool | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        status: Literal["running", "idle", "completed", "failed", "stopped"] | Omit = omit,
        worker_session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subagent:
        """
        Update a subagent record

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subagent_id:
            raise ValueError(f"Expected a non-empty value for `subagent_id` but received {subagent_id!r}")
        return self._patch(
            path_template("/v1/subagents/{subagent_id}", subagent_id=subagent_id),
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "archived": archived,
                    "conversation_id": conversation_id,
                    "status": status,
                    "worker_session_id": worker_session_id,
                },
                subagent_update_params.SubagentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subagent,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        parent_agent_id: str | Omit = omit,
        parent_conversation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubagentListResponse:
        """
        List subagents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/subagents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "limit": limit,
                        "parent_agent_id": parent_agent_id,
                        "parent_conversation_id": parent_conversation_id,
                    },
                    subagent_list_params.SubagentListParams,
                ),
            ),
            cast_to=SubagentListResponse,
        )


class AsyncSubagentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubagentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubagentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubagentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncSubagentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        harness: str,
        parent_conversation_id: str,
        agent_id: Optional[str] | Omit = omit,
        archived: bool | Omit = omit,
        computer: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        fork_context: bool | Omit = omit,
        mcp_config: Optional[Dict[str, object]] | Omit = omit,
        model_config: Optional[Dict[str, object]] | Omit = omit,
        parent_agent_id: str | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        repositories: Optional[SequenceNotStr[str]] | Omit = omit,
        sandbox_size: Optional[str] | Omit = omit,
        status: Literal["running", "idle", "completed", "failed", "stopped"] | Omit = omit,
        subagent_type: Optional[str] | Omit = omit,
        worker_session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subagent:
        """
        Create a subagent record

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/subagents",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "harness": harness,
                    "parent_conversation_id": parent_conversation_id,
                    "agent_id": agent_id,
                    "archived": archived,
                    "computer": computer,
                    "conversation_id": conversation_id,
                    "fork_context": fork_context,
                    "mcp_config": mcp_config,
                    "model_config": model_config,
                    "parent_agent_id": parent_agent_id,
                    "prompt": prompt,
                    "repositories": repositories,
                    "sandbox_size": sandbox_size,
                    "status": status,
                    "subagent_type": subagent_type,
                    "worker_session_id": worker_session_id,
                },
                subagent_create_params.SubagentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subagent,
        )

    async def update(
        self,
        subagent_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        archived: bool | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        status: Literal["running", "idle", "completed", "failed", "stopped"] | Omit = omit,
        worker_session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subagent:
        """
        Update a subagent record

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subagent_id:
            raise ValueError(f"Expected a non-empty value for `subagent_id` but received {subagent_id!r}")
        return await self._patch(
            path_template("/v1/subagents/{subagent_id}", subagent_id=subagent_id),
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "archived": archived,
                    "conversation_id": conversation_id,
                    "status": status,
                    "worker_session_id": worker_session_id,
                },
                subagent_update_params.SubagentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subagent,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        archived: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        parent_agent_id: str | Omit = omit,
        parent_conversation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubagentListResponse:
        """
        List subagents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/subagents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "limit": limit,
                        "parent_agent_id": parent_agent_id,
                        "parent_conversation_id": parent_conversation_id,
                    },
                    subagent_list_params.SubagentListParams,
                ),
            ),
            cast_to=SubagentListResponse,
        )


class SubagentsResourceWithRawResponse:
    def __init__(self, subagents: SubagentsResource) -> None:
        self._subagents = subagents

        self.create = to_raw_response_wrapper(
            subagents.create,
        )
        self.update = to_raw_response_wrapper(
            subagents.update,
        )
        self.list = to_raw_response_wrapper(
            subagents.list,
        )


class AsyncSubagentsResourceWithRawResponse:
    def __init__(self, subagents: AsyncSubagentsResource) -> None:
        self._subagents = subagents

        self.create = async_to_raw_response_wrapper(
            subagents.create,
        )
        self.update = async_to_raw_response_wrapper(
            subagents.update,
        )
        self.list = async_to_raw_response_wrapper(
            subagents.list,
        )


class SubagentsResourceWithStreamingResponse:
    def __init__(self, subagents: SubagentsResource) -> None:
        self._subagents = subagents

        self.create = to_streamed_response_wrapper(
            subagents.create,
        )
        self.update = to_streamed_response_wrapper(
            subagents.update,
        )
        self.list = to_streamed_response_wrapper(
            subagents.list,
        )


class AsyncSubagentsResourceWithStreamingResponse:
    def __init__(self, subagents: AsyncSubagentsResource) -> None:
        self._subagents = subagents

        self.create = async_to_streamed_response_wrapper(
            subagents.create,
        )
        self.update = async_to_streamed_response_wrapper(
            subagents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subagents.list,
        )
