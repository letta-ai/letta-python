# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

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
from ....types.memory import Memory
from ....types.agents.memory import block_create_params

__all__ = ["BlockResource", "AsyncBlockResource"]


class BlockResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return BlockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return BlockResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        label: str,
        value: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        is_template: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """
        Creates a memory block and links it to the agent.

        Args:
          label: Label of the block.

          value: Value of the block.

          description: Description of the block.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: Name of the block if it is a template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/memory/block",
            body=maybe_transform(
                {
                    "label": label,
                    "value": value,
                    "description": description,
                    "is_template": is_template,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                },
                block_create_params.BlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )

    def delete(
        self,
        block_label: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """Removes a memory block from an agent by unlnking it.

        If the block is not linked
        to any other agent, it is deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_label:
            raise ValueError(f"Expected a non-empty value for `block_label` but received {block_label!r}")
        return self._delete(
            f"/v1/agents/{agent_id}/memory/block/{block_label}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )


class AsyncBlockResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncBlockResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        label: str,
        value: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        is_template: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """
        Creates a memory block and links it to the agent.

        Args:
          label: Label of the block.

          value: Value of the block.

          description: Description of the block.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: Name of the block if it is a template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/memory/block",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "value": value,
                    "description": description,
                    "is_template": is_template,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                },
                block_create_params.BlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )

    async def delete(
        self,
        block_label: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """Removes a memory block from an agent by unlnking it.

        If the block is not linked
        to any other agent, it is deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_label:
            raise ValueError(f"Expected a non-empty value for `block_label` but received {block_label!r}")
        return await self._delete(
            f"/v1/agents/{agent_id}/memory/block/{block_label}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )


class BlockResourceWithRawResponse:
    def __init__(self, block: BlockResource) -> None:
        self._block = block

        self.create = to_raw_response_wrapper(
            block.create,
        )
        self.delete = to_raw_response_wrapper(
            block.delete,
        )


class AsyncBlockResourceWithRawResponse:
    def __init__(self, block: AsyncBlockResource) -> None:
        self._block = block

        self.create = async_to_raw_response_wrapper(
            block.create,
        )
        self.delete = async_to_raw_response_wrapper(
            block.delete,
        )


class BlockResourceWithStreamingResponse:
    def __init__(self, block: BlockResource) -> None:
        self._block = block

        self.create = to_streamed_response_wrapper(
            block.create,
        )
        self.delete = to_streamed_response_wrapper(
            block.delete,
        )


class AsyncBlockResourceWithStreamingResponse:
    def __init__(self, block: AsyncBlockResource) -> None:
        self._block = block

        self.create = async_to_streamed_response_wrapper(
            block.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            block.delete,
        )
