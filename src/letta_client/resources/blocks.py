# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import block_list_params, block_create_params, block_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.block import Block
from .._base_client import make_request_options
from ..types.block_list_response import BlockListResponse

__all__ = ["BlocksResource", "AsyncBlocksResource"]


class BlocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return BlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return BlocksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        label: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        body_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        value: Optional[str] | NotGiven = NOT_GIVEN,
        header_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Block:
        """
        Create Block

        Args:
          label: Label of the block.

          description: Description of the block.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: Name of the block.

          body_user_id: The unique identifier of the user associated with the block.

          value: Value of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": header_user_id}), **(extra_headers or {})}
        return self._post(
            "/v1/blocks/",
            body=maybe_transform(
                {
                    "label": label,
                    "description": description,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "template": template,
                    "body_user_id": body_user_id,
                    "value": value,
                },
                block_create_params.BlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    def retrieve(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Block:
        """
        Get Block

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._get(
            f"/v1/blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    def update(
        self,
        block_id: str,
        *,
        id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        label: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        value: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Block:
        """
        Update Block

        Args:
          id: The unique identifier of the block.

          description: Description of the block.

          label: Label of the block (e.g. 'human', 'persona').

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: Name of the block.

          template: Whether the block is a template (e.g. saved human/persona options).

          user_id: The unique identifier of the user associated with the block.

          value: Value of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._patch(
            f"/v1/blocks/{block_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "label": label,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "template": template,
                    "user_id": user_id,
                    "value": value,
                },
                block_update_params.BlockUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    def list(
        self,
        *,
        label: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        templates_only: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockListResponse:
        """List Blocks

        Args:
          label: Labels to include (e.g.

        human, persona)

          name: Name of the block

          templates_only: Whether to include only templates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._get(
            "/v1/blocks/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "label": label,
                        "name": name,
                        "templates_only": templates_only,
                    },
                    block_list_params.BlockListParams,
                ),
            ),
            cast_to=BlockListResponse,
        )

    def delete(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Block:
        """
        Delete Block

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._delete(
            f"/v1/blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )


class AsyncBlocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncBlocksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        label: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        body_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        value: Optional[str] | NotGiven = NOT_GIVEN,
        header_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Block:
        """
        Create Block

        Args:
          label: Label of the block.

          description: Description of the block.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: Name of the block.

          body_user_id: The unique identifier of the user associated with the block.

          value: Value of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": header_user_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/blocks/",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "description": description,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "template": template,
                    "body_user_id": body_user_id,
                    "value": value,
                },
                block_create_params.BlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    async def retrieve(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Block:
        """
        Get Block

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._get(
            f"/v1/blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    async def update(
        self,
        block_id: str,
        *,
        id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        label: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        value: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Block:
        """
        Update Block

        Args:
          id: The unique identifier of the block.

          description: Description of the block.

          label: Label of the block (e.g. 'human', 'persona').

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: Name of the block.

          template: Whether the block is a template (e.g. saved human/persona options).

          user_id: The unique identifier of the user associated with the block.

          value: Value of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._patch(
            f"/v1/blocks/{block_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "label": label,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "template": template,
                    "user_id": user_id,
                    "value": value,
                },
                block_update_params.BlockUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    async def list(
        self,
        *,
        label: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        templates_only: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockListResponse:
        """List Blocks

        Args:
          label: Labels to include (e.g.

        human, persona)

          name: Name of the block

          templates_only: Whether to include only templates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/blocks/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "label": label,
                        "name": name,
                        "templates_only": templates_only,
                    },
                    block_list_params.BlockListParams,
                ),
            ),
            cast_to=BlockListResponse,
        )

    async def delete(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Block:
        """
        Delete Block

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._delete(
            f"/v1/blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )


class BlocksResourceWithRawResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.create = to_raw_response_wrapper(
            blocks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            blocks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            blocks.update,
        )
        self.list = to_raw_response_wrapper(
            blocks.list,
        )
        self.delete = to_raw_response_wrapper(
            blocks.delete,
        )


class AsyncBlocksResourceWithRawResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.create = async_to_raw_response_wrapper(
            blocks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            blocks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            blocks.update,
        )
        self.list = async_to_raw_response_wrapper(
            blocks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            blocks.delete,
        )


class BlocksResourceWithStreamingResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.create = to_streamed_response_wrapper(
            blocks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            blocks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            blocks.update,
        )
        self.list = to_streamed_response_wrapper(
            blocks.list,
        )
        self.delete = to_streamed_response_wrapper(
            blocks.delete,
        )


class AsyncBlocksResourceWithStreamingResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.create = async_to_streamed_response_wrapper(
            blocks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            blocks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            blocks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            blocks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            blocks.delete,
        )
