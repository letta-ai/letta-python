# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncArrayPage, AsyncArrayPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.identities import block_list_params
from ...types.identities.block_list_response import BlockListResponse

__all__ = ["BlocksResource", "AsyncBlocksResource"]


class BlocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return BlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return BlocksResourceWithStreamingResponse(self)

    def list(
        self,
        identity_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncArrayPage[BlockListResponse]:
        """
        Get all blocks associated with the specified identity.

        Args:
          identity_id: The ID of the identity in the format 'identity-<uuid4>'

          after: Block ID cursor for pagination. Returns blocks that come after this block ID in
              the specified sort order

          before: Block ID cursor for pagination. Returns blocks that come before this block ID in
              the specified sort order

          limit: Maximum number of blocks to return

          order: Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return self._get_api_list(
            f"/v1/identities/{identity_id}/blocks",
            page=SyncArrayPage[BlockListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    block_list_params.BlockListParams,
                ),
            ),
            model=BlockListResponse,
        )


class AsyncBlocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncBlocksResourceWithStreamingResponse(self)

    def list(
        self,
        identity_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BlockListResponse, AsyncArrayPage[BlockListResponse]]:
        """
        Get all blocks associated with the specified identity.

        Args:
          identity_id: The ID of the identity in the format 'identity-<uuid4>'

          after: Block ID cursor for pagination. Returns blocks that come after this block ID in
              the specified sort order

          before: Block ID cursor for pagination. Returns blocks that come before this block ID in
              the specified sort order

          limit: Maximum number of blocks to return

          order: Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return self._get_api_list(
            f"/v1/identities/{identity_id}/blocks",
            page=AsyncArrayPage[BlockListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    block_list_params.BlockListParams,
                ),
            ),
            model=BlockListResponse,
        )


class BlocksResourceWithRawResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.list = to_raw_response_wrapper(
            blocks.list,
        )


class AsyncBlocksResourceWithRawResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.list = async_to_raw_response_wrapper(
            blocks.list,
        )


class BlocksResourceWithStreamingResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.list = to_streamed_response_wrapper(
            blocks.list,
        )


class AsyncBlocksResourceWithStreamingResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.list = async_to_streamed_response_wrapper(
            blocks.list,
        )
