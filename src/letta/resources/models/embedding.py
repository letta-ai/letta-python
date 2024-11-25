# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.models.embedding_retrieve_response import EmbeddingRetrieveResponse

__all__ = ["EmbeddingResource", "AsyncEmbeddingResource"]


class EmbeddingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbeddingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return EmbeddingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbeddingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return EmbeddingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingRetrieveResponse:
        """List Embedding Backends"""
        return self._get(
            "/v1/models/embedding",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingRetrieveResponse,
        )


class AsyncEmbeddingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbeddingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbeddingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbeddingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncEmbeddingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingRetrieveResponse:
        """List Embedding Backends"""
        return await self._get(
            "/v1/models/embedding",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingRetrieveResponse,
        )


class EmbeddingResourceWithRawResponse:
    def __init__(self, embedding: EmbeddingResource) -> None:
        self._embedding = embedding

        self.retrieve = to_raw_response_wrapper(
            embedding.retrieve,
        )


class AsyncEmbeddingResourceWithRawResponse:
    def __init__(self, embedding: AsyncEmbeddingResource) -> None:
        self._embedding = embedding

        self.retrieve = async_to_raw_response_wrapper(
            embedding.retrieve,
        )


class EmbeddingResourceWithStreamingResponse:
    def __init__(self, embedding: EmbeddingResource) -> None:
        self._embedding = embedding

        self.retrieve = to_streamed_response_wrapper(
            embedding.retrieve,
        )


class AsyncEmbeddingResourceWithStreamingResponse:
    def __init__(self, embedding: AsyncEmbeddingResource) -> None:
        self._embedding = embedding

        self.retrieve = async_to_streamed_response_wrapper(
            embedding.retrieve,
        )
