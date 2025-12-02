# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

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
from ...types.agents import passage_list_params, passage_create_params, passage_search_params
from ...types.agents.passage_list_response import PassageListResponse
from ...types.agents.passage_create_response import PassageCreateResponse
from ...types.agents.passage_search_response import PassageSearchResponse

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

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        agent_id: str,
        *,
        text: str,
        created_at: Union[str, datetime, None] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageCreateResponse:
        """
        Insert a memory into an agent's archival memory store.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          text: Text to write to archival memory.

          created_at: Optional timestamp for the memory (defaults to current UTC time).

          tags: Optional list of tags to attach to the memory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/archival-memory",
            body=maybe_transform(
                {
                    "text": text,
                    "created_at": created_at,
                    "tags": tags,
                },
                passage_create_params.PassageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PassageCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        agent_id: str,
        *,
        after: Optional[str] | Omit = omit,
        ascending: Optional[bool] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageListResponse:
        """
        Retrieve the memories in an agent's archival memory store (paginated query).

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          after: Unique ID of the memory to start the query range at.

          ascending: Whether to sort passages oldest to newest (True, default) or newest to oldest
              (False)

          before: Unique ID of the memory to end the query range at.

          limit: How many results to include in the response.

          search: Search passages by text

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/archival-memory",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "ascending": ascending,
                        "before": before,
                        "limit": limit,
                        "search": search,
                    },
                    passage_list_params.PassageListParams,
                ),
            ),
            cast_to=PassageListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        memory_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a memory from an agent's archival memory store.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return self._delete(
            f"/v1/agents/{agent_id}/archival-memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    def search(
        self,
        agent_id: str,
        *,
        query: str,
        end_datetime: Union[str, datetime, None] | Omit = omit,
        start_datetime: Union[str, datetime, None] | Omit = omit,
        tag_match_mode: Literal["any", "all"] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageSearchResponse:
        """
        Search archival memory using semantic (embedding-based) search with optional
        temporal filtering.

        This endpoint allows manual triggering of archival memory searches, enabling
        users to query an agent's archival memory store directly via the API. The search
        uses the same functionality as the agent's archival_memory_search tool but is
        accessible for external API usage.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          query: String to search for using semantic similarity

          end_datetime: Filter results to passages created before this datetime

          start_datetime: Filter results to passages created after this datetime

          tag_match_mode: How to match tags - 'any' to match passages with any of the tags, 'all' to match
              only passages with all tags

          tags: Optional list of tags to filter search results

          top_k: Maximum number of results to return. Uses system default if not specified

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/archival-memory/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "end_datetime": end_datetime,
                        "start_datetime": start_datetime,
                        "tag_match_mode": tag_match_mode,
                        "tags": tags,
                        "top_k": top_k,
                    },
                    passage_search_params.PassageSearchParams,
                ),
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

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        agent_id: str,
        *,
        text: str,
        created_at: Union[str, datetime, None] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageCreateResponse:
        """
        Insert a memory into an agent's archival memory store.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          text: Text to write to archival memory.

          created_at: Optional timestamp for the memory (defaults to current UTC time).

          tags: Optional list of tags to attach to the memory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/archival-memory",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "created_at": created_at,
                    "tags": tags,
                },
                passage_create_params.PassageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PassageCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def list(
        self,
        agent_id: str,
        *,
        after: Optional[str] | Omit = omit,
        ascending: Optional[bool] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageListResponse:
        """
        Retrieve the memories in an agent's archival memory store (paginated query).

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          after: Unique ID of the memory to start the query range at.

          ascending: Whether to sort passages oldest to newest (True, default) or newest to oldest
              (False)

          before: Unique ID of the memory to end the query range at.

          limit: How many results to include in the response.

          search: Search passages by text

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/archival-memory",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "ascending": ascending,
                        "before": before,
                        "limit": limit,
                        "search": search,
                    },
                    passage_list_params.PassageListParams,
                ),
            ),
            cast_to=PassageListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        memory_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a memory from an agent's archival memory store.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return await self._delete(
            f"/v1/agents/{agent_id}/archival-memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    async def search(
        self,
        agent_id: str,
        *,
        query: str,
        end_datetime: Union[str, datetime, None] | Omit = omit,
        start_datetime: Union[str, datetime, None] | Omit = omit,
        tag_match_mode: Literal["any", "all"] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageSearchResponse:
        """
        Search archival memory using semantic (embedding-based) search with optional
        temporal filtering.

        This endpoint allows manual triggering of archival memory searches, enabling
        users to query an agent's archival memory store directly via the API. The search
        uses the same functionality as the agent's archival_memory_search tool but is
        accessible for external API usage.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          query: String to search for using semantic similarity

          end_datetime: Filter results to passages created before this datetime

          start_datetime: Filter results to passages created after this datetime

          tag_match_mode: How to match tags - 'any' to match passages with any of the tags, 'all' to match
              only passages with all tags

          tags: Optional list of tags to filter search results

          top_k: Maximum number of results to return. Uses system default if not specified

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/archival-memory/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "end_datetime": end_datetime,
                        "start_datetime": start_datetime,
                        "tag_match_mode": tag_match_mode,
                        "tags": tags,
                        "top_k": top_k,
                    },
                    passage_search_params.PassageSearchParams,
                ),
            ),
            cast_to=PassageSearchResponse,
        )


class PassagesResourceWithRawResponse:
    def __init__(self, passages: PassagesResource) -> None:
        self._passages = passages

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                passages.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                passages.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                passages.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                passages.search,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncPassagesResourceWithRawResponse:
    def __init__(self, passages: AsyncPassagesResource) -> None:
        self._passages = passages

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                passages.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                passages.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                passages.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                passages.search,  # pyright: ignore[reportDeprecated],
            )
        )


class PassagesResourceWithStreamingResponse:
    def __init__(self, passages: PassagesResource) -> None:
        self._passages = passages

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                passages.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                passages.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                passages.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                passages.search,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncPassagesResourceWithStreamingResponse:
    def __init__(self, passages: AsyncPassagesResource) -> None:
        self._passages = passages

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                passages.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                passages.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                passages.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                passages.search,  # pyright: ignore[reportDeprecated],
            )
        )
