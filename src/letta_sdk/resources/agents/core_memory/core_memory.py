# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .blocks import (
    BlocksResource,
    AsyncBlocksResource,
    BlocksResourceWithRawResponse,
    AsyncBlocksResourceWithRawResponse,
    BlocksResourceWithStreamingResponse,
    AsyncBlocksResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.memory import Memory
from ....types.agents.core_memory_retrieve_variables_response import CoreMemoryRetrieveVariablesResponse

__all__ = ["CoreMemoryResource", "AsyncCoreMemoryResource"]


class CoreMemoryResource(SyncAPIResource):
    @cached_property
    def blocks(self) -> BlocksResource:
        return BlocksResource(self._client)

    @cached_property
    def with_raw_response(self) -> CoreMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CoreMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoreMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return CoreMemoryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Memory:
        """Retrieve the memory state of a specific agent.

        This endpoint fetches the current
        memory state of the agent identified by the user ID and agent ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/core-memory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )

    def retrieve_variables(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CoreMemoryRetrieveVariablesResponse:
        """
        Get the variables associated with an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/core-memory/variables",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoreMemoryRetrieveVariablesResponse,
        )


class AsyncCoreMemoryResource(AsyncAPIResource):
    @cached_property
    def blocks(self) -> AsyncBlocksResource:
        return AsyncBlocksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCoreMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoreMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoreMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AsyncCoreMemoryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Memory:
        """Retrieve the memory state of a specific agent.

        This endpoint fetches the current
        memory state of the agent identified by the user ID and agent ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/core-memory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )

    async def retrieve_variables(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CoreMemoryRetrieveVariablesResponse:
        """
        Get the variables associated with an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/core-memory/variables",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoreMemoryRetrieveVariablesResponse,
        )


class CoreMemoryResourceWithRawResponse:
    def __init__(self, core_memory: CoreMemoryResource) -> None:
        self._core_memory = core_memory

        self.retrieve = to_raw_response_wrapper(
            core_memory.retrieve,
        )
        self.retrieve_variables = to_raw_response_wrapper(
            core_memory.retrieve_variables,
        )

    @cached_property
    def blocks(self) -> BlocksResourceWithRawResponse:
        return BlocksResourceWithRawResponse(self._core_memory.blocks)


class AsyncCoreMemoryResourceWithRawResponse:
    def __init__(self, core_memory: AsyncCoreMemoryResource) -> None:
        self._core_memory = core_memory

        self.retrieve = async_to_raw_response_wrapper(
            core_memory.retrieve,
        )
        self.retrieve_variables = async_to_raw_response_wrapper(
            core_memory.retrieve_variables,
        )

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithRawResponse:
        return AsyncBlocksResourceWithRawResponse(self._core_memory.blocks)


class CoreMemoryResourceWithStreamingResponse:
    def __init__(self, core_memory: CoreMemoryResource) -> None:
        self._core_memory = core_memory

        self.retrieve = to_streamed_response_wrapper(
            core_memory.retrieve,
        )
        self.retrieve_variables = to_streamed_response_wrapper(
            core_memory.retrieve_variables,
        )

    @cached_property
    def blocks(self) -> BlocksResourceWithStreamingResponse:
        return BlocksResourceWithStreamingResponse(self._core_memory.blocks)


class AsyncCoreMemoryResourceWithStreamingResponse:
    def __init__(self, core_memory: AsyncCoreMemoryResource) -> None:
        self._core_memory = core_memory

        self.retrieve = async_to_streamed_response_wrapper(
            core_memory.retrieve,
        )
        self.retrieve_variables = async_to_streamed_response_wrapper(
            core_memory.retrieve_variables,
        )

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithStreamingResponse:
        return AsyncBlocksResourceWithStreamingResponse(self._core_memory.blocks)
