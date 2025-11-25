# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import passage_search_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.passage_search_response import PassageSearchResponse

__all__ = ["PassagesResource", "AsyncPassagesResource"]


class PassagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PassagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return PassagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PassagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return PassagesResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        query: str,
        agent_id: Optional[str] | Omit = omit,
        archive_id: Optional[str] | Omit = omit,
        end_date: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        tag_match_mode: Literal["any", "all"] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageSearchResponse:
        """
        Search passages across the organization with optional agent and archive
        filtering. Returns passages with relevance scores.

        This endpoint supports semantic search through passages:

        - If neither agent_id nor archive_id is provided, searches ALL passages in the
          organization
        - If agent_id is provided, searches passages across all archives attached to
          that agent
        - If archive_id is provided, searches passages within that specific archive
        - If both are provided, agent_id takes precedence

        Args:
          query: Text query for semantic search

          agent_id: Filter passages by agent ID

          archive_id: Filter passages by archive ID

          end_date: Filter results to passages created before this datetime

          limit: Maximum number of results to return

          start_date: Filter results to passages created after this datetime

          tag_match_mode: How to match tags - 'any' to match passages with any of the tags, 'all' to match
              only passages with all tags

          tags: Optional list of tags to filter search results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/passages/search",
            body=maybe_transform(
                {
                    "query": query,
                    "agent_id": agent_id,
                    "archive_id": archive_id,
                    "end_date": end_date,
                    "limit": limit,
                    "start_date": start_date,
                    "tag_match_mode": tag_match_mode,
                    "tags": tags,
                },
                passage_search_params.PassageSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PassageSearchResponse,
        )


class AsyncPassagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPassagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPassagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPassagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncPassagesResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        query: str,
        agent_id: Optional[str] | Omit = omit,
        archive_id: Optional[str] | Omit = omit,
        end_date: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        tag_match_mode: Literal["any", "all"] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageSearchResponse:
        """
        Search passages across the organization with optional agent and archive
        filtering. Returns passages with relevance scores.

        This endpoint supports semantic search through passages:

        - If neither agent_id nor archive_id is provided, searches ALL passages in the
          organization
        - If agent_id is provided, searches passages across all archives attached to
          that agent
        - If archive_id is provided, searches passages within that specific archive
        - If both are provided, agent_id takes precedence

        Args:
          query: Text query for semantic search

          agent_id: Filter passages by agent ID

          archive_id: Filter passages by archive ID

          end_date: Filter results to passages created before this datetime

          limit: Maximum number of results to return

          start_date: Filter results to passages created after this datetime

          tag_match_mode: How to match tags - 'any' to match passages with any of the tags, 'all' to match
              only passages with all tags

          tags: Optional list of tags to filter search results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/passages/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "agent_id": agent_id,
                    "archive_id": archive_id,
                    "end_date": end_date,
                    "limit": limit,
                    "start_date": start_date,
                    "tag_match_mode": tag_match_mode,
                    "tags": tags,
                },
                passage_search_params.PassageSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PassageSearchResponse,
        )


class PassagesResourceWithRawResponse:
    def __init__(self, passages: PassagesResource) -> None:
        self._passages = passages

        self.search = to_raw_response_wrapper(
            passages.search,
        )


class AsyncPassagesResourceWithRawResponse:
    def __init__(self, passages: AsyncPassagesResource) -> None:
        self._passages = passages

        self.search = async_to_raw_response_wrapper(
            passages.search,
        )


class PassagesResourceWithStreamingResponse:
    def __init__(self, passages: PassagesResource) -> None:
        self._passages = passages

        self.search = to_streamed_response_wrapper(
            passages.search,
        )


class AsyncPassagesResourceWithStreamingResponse:
    def __init__(self, passages: AsyncPassagesResource) -> None:
        self._passages = passages

        self.search = async_to_streamed_response_wrapper(
            passages.search,
        )
