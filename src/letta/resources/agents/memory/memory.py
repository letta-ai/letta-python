# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .block import (
    BlockResource,
    AsyncBlockResource,
    BlockResourceWithRawResponse,
    AsyncBlockResourceWithRawResponse,
    BlockResourceWithStreamingResponse,
    AsyncBlockResourceWithStreamingResponse,
)
from .label import (
    LabelResource,
    AsyncLabelResource,
    LabelResourceWithRawResponse,
    AsyncLabelResourceWithRawResponse,
    LabelResourceWithStreamingResponse,
    AsyncLabelResourceWithStreamingResponse,
)
from .limit import (
    LimitResource,
    AsyncLimitResource,
    LimitResourceWithRawResponse,
    AsyncLimitResourceWithRawResponse,
    LimitResourceWithStreamingResponse,
    AsyncLimitResourceWithStreamingResponse,
)
from .recall import (
    RecallResource,
    AsyncRecallResource,
    RecallResourceWithRawResponse,
    AsyncRecallResourceWithRawResponse,
    RecallResourceWithStreamingResponse,
    AsyncRecallResourceWithStreamingResponse,
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
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents import memory_update_params
from ....types.memory import Memory

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def label(self) -> LabelResource:
        return LabelResource(self._client)

    @cached_property
    def block(self) -> BlockResource:
        return BlockResource(self._client)

    @cached_property
    def limit(self) -> LimitResource:
        return LimitResource(self._client)

    @cached_property
    def recall(self) -> RecallResource:
        return RecallResource(self._client)

    @cached_property
    def archival(self) -> ArchivalResource:
        return ArchivalResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v1/agents/{agent_id}/memory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )

    def update(
        self,
        agent_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """Update the core memory of a specific agent.

        This endpoint accepts new memory
        contents (labels as keys, and values as values) and updates the core memory of
        the agent identified by the user ID and agent ID. This endpoint accepts new
        memory contents to update the core memory of the agent. This endpoint only
        supports modifying existing blocks; it does not support deleting/unlinking or
        creating/linking blocks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/memory",
            body=maybe_transform(body, memory_update_params.MemoryUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )


class AsyncMemoryResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def label(self) -> AsyncLabelResource:
        return AsyncLabelResource(self._client)

    @cached_property
    def block(self) -> AsyncBlockResource:
        return AsyncBlockResource(self._client)

    @cached_property
    def limit(self) -> AsyncLimitResource:
        return AsyncLimitResource(self._client)

    @cached_property
    def recall(self) -> AsyncRecallResource:
        return AsyncRecallResource(self._client)

    @cached_property
    def archival(self) -> AsyncArchivalResource:
        return AsyncArchivalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v1/agents/{agent_id}/memory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )

    async def update(
        self,
        agent_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """Update the core memory of a specific agent.

        This endpoint accepts new memory
        contents (labels as keys, and values as values) and updates the core memory of
        the agent identified by the user ID and agent ID. This endpoint accepts new
        memory contents to update the core memory of the agent. This endpoint only
        supports modifying existing blocks; it does not support deleting/unlinking or
        creating/linking blocks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/memory",
            body=await async_maybe_transform(body, memory_update_params.MemoryUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.retrieve = to_raw_response_wrapper(
            memory.retrieve,
        )
        self.update = to_raw_response_wrapper(
            memory.update,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._memory.messages)

    @cached_property
    def label(self) -> LabelResourceWithRawResponse:
        return LabelResourceWithRawResponse(self._memory.label)

    @cached_property
    def block(self) -> BlockResourceWithRawResponse:
        return BlockResourceWithRawResponse(self._memory.block)

    @cached_property
    def limit(self) -> LimitResourceWithRawResponse:
        return LimitResourceWithRawResponse(self._memory.limit)

    @cached_property
    def recall(self) -> RecallResourceWithRawResponse:
        return RecallResourceWithRawResponse(self._memory.recall)

    @cached_property
    def archival(self) -> ArchivalResourceWithRawResponse:
        return ArchivalResourceWithRawResponse(self._memory.archival)


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.retrieve = async_to_raw_response_wrapper(
            memory.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            memory.update,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._memory.messages)

    @cached_property
    def label(self) -> AsyncLabelResourceWithRawResponse:
        return AsyncLabelResourceWithRawResponse(self._memory.label)

    @cached_property
    def block(self) -> AsyncBlockResourceWithRawResponse:
        return AsyncBlockResourceWithRawResponse(self._memory.block)

    @cached_property
    def limit(self) -> AsyncLimitResourceWithRawResponse:
        return AsyncLimitResourceWithRawResponse(self._memory.limit)

    @cached_property
    def recall(self) -> AsyncRecallResourceWithRawResponse:
        return AsyncRecallResourceWithRawResponse(self._memory.recall)

    @cached_property
    def archival(self) -> AsyncArchivalResourceWithRawResponse:
        return AsyncArchivalResourceWithRawResponse(self._memory.archival)


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.retrieve = to_streamed_response_wrapper(
            memory.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            memory.update,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._memory.messages)

    @cached_property
    def label(self) -> LabelResourceWithStreamingResponse:
        return LabelResourceWithStreamingResponse(self._memory.label)

    @cached_property
    def block(self) -> BlockResourceWithStreamingResponse:
        return BlockResourceWithStreamingResponse(self._memory.block)

    @cached_property
    def limit(self) -> LimitResourceWithStreamingResponse:
        return LimitResourceWithStreamingResponse(self._memory.limit)

    @cached_property
    def recall(self) -> RecallResourceWithStreamingResponse:
        return RecallResourceWithStreamingResponse(self._memory.recall)

    @cached_property
    def archival(self) -> ArchivalResourceWithStreamingResponse:
        return ArchivalResourceWithStreamingResponse(self._memory.archival)


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.retrieve = async_to_streamed_response_wrapper(
            memory.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            memory.update,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._memory.messages)

    @cached_property
    def label(self) -> AsyncLabelResourceWithStreamingResponse:
        return AsyncLabelResourceWithStreamingResponse(self._memory.label)

    @cached_property
    def block(self) -> AsyncBlockResourceWithStreamingResponse:
        return AsyncBlockResourceWithStreamingResponse(self._memory.block)

    @cached_property
    def limit(self) -> AsyncLimitResourceWithStreamingResponse:
        return AsyncLimitResourceWithStreamingResponse(self._memory.limit)

    @cached_property
    def recall(self) -> AsyncRecallResourceWithStreamingResponse:
        return AsyncRecallResourceWithStreamingResponse(self._memory.recall)

    @cached_property
    def archival(self) -> AsyncArchivalResourceWithStreamingResponse:
        return AsyncArchivalResourceWithStreamingResponse(self._memory.archival)
