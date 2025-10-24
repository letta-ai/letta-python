# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import archive_list_params, archive_create_params, archive_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.archive import Archive
from ..types.archive_list_response import ArchiveListResponse
from ..types.embedding_config_param import EmbeddingConfigParam

__all__ = ["ArchivesResource", "AsyncArchivesResource"]


class ArchivesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArchivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ArchivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArchivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ArchivesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        embedding_config: EmbeddingConfigParam,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Archive:
        """
        Create a new archive.

        Args:
          embedding_config: Embedding configuration for the archive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/archives/",
            body=maybe_transform(
                {
                    "embedding_config": embedding_config,
                    "name": name,
                    "description": description,
                },
                archive_create_params.ArchiveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Archive,
        )

    def retrieve(
        self,
        archive_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Archive:
        """
        Get a single archive by its ID.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return self._get(
            f"/v1/archives/{archive_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Archive,
        )

    def update(
        self,
        archive_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Archive:
        """
        Update an existing archive's name and/or description.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return self._patch(
            f"/v1/archives/{archive_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                archive_update_params.ArchiveUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Archive,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArchiveListResponse:
        """
        Get a list of all archives for the current organization with optional filters
        and pagination.

        Args:
          after: Archive ID cursor for pagination. Returns archives that come after this archive
              ID in the specified sort order

          agent_id: Only archives attached to this agent ID

          before: Archive ID cursor for pagination. Returns archives that come before this archive
              ID in the specified sort order

          limit: Maximum number of archives to return

          name: Filter by archive name (exact match)

          order: Sort order for archives by creation time. 'asc' for oldest first, 'desc' for
              newest first

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/archives/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "before": before,
                        "limit": limit,
                        "name": name,
                        "order": order,
                    },
                    archive_list_params.ArchiveListParams,
                ),
            ),
            cast_to=ArchiveListResponse,
        )

    def delete(
        self,
        archive_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Archive:
        """
        Delete an archive by its ID.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return self._delete(
            f"/v1/archives/{archive_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Archive,
        )


class AsyncArchivesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArchivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArchivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArchivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncArchivesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        embedding_config: EmbeddingConfigParam,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Archive:
        """
        Create a new archive.

        Args:
          embedding_config: Embedding configuration for the archive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/archives/",
            body=await async_maybe_transform(
                {
                    "embedding_config": embedding_config,
                    "name": name,
                    "description": description,
                },
                archive_create_params.ArchiveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Archive,
        )

    async def retrieve(
        self,
        archive_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Archive:
        """
        Get a single archive by its ID.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return await self._get(
            f"/v1/archives/{archive_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Archive,
        )

    async def update(
        self,
        archive_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Archive:
        """
        Update an existing archive's name and/or description.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return await self._patch(
            f"/v1/archives/{archive_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                archive_update_params.ArchiveUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Archive,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArchiveListResponse:
        """
        Get a list of all archives for the current organization with optional filters
        and pagination.

        Args:
          after: Archive ID cursor for pagination. Returns archives that come after this archive
              ID in the specified sort order

          agent_id: Only archives attached to this agent ID

          before: Archive ID cursor for pagination. Returns archives that come before this archive
              ID in the specified sort order

          limit: Maximum number of archives to return

          name: Filter by archive name (exact match)

          order: Sort order for archives by creation time. 'asc' for oldest first, 'desc' for
              newest first

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/archives/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "before": before,
                        "limit": limit,
                        "name": name,
                        "order": order,
                    },
                    archive_list_params.ArchiveListParams,
                ),
            ),
            cast_to=ArchiveListResponse,
        )

    async def delete(
        self,
        archive_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Archive:
        """
        Delete an archive by its ID.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return await self._delete(
            f"/v1/archives/{archive_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Archive,
        )


class ArchivesResourceWithRawResponse:
    def __init__(self, archives: ArchivesResource) -> None:
        self._archives = archives

        self.create = to_raw_response_wrapper(
            archives.create,
        )
        self.retrieve = to_raw_response_wrapper(
            archives.retrieve,
        )
        self.update = to_raw_response_wrapper(
            archives.update,
        )
        self.list = to_raw_response_wrapper(
            archives.list,
        )
        self.delete = to_raw_response_wrapper(
            archives.delete,
        )


class AsyncArchivesResourceWithRawResponse:
    def __init__(self, archives: AsyncArchivesResource) -> None:
        self._archives = archives

        self.create = async_to_raw_response_wrapper(
            archives.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            archives.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            archives.update,
        )
        self.list = async_to_raw_response_wrapper(
            archives.list,
        )
        self.delete = async_to_raw_response_wrapper(
            archives.delete,
        )


class ArchivesResourceWithStreamingResponse:
    def __init__(self, archives: ArchivesResource) -> None:
        self._archives = archives

        self.create = to_streamed_response_wrapper(
            archives.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            archives.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            archives.update,
        )
        self.list = to_streamed_response_wrapper(
            archives.list,
        )
        self.delete = to_streamed_response_wrapper(
            archives.delete,
        )


class AsyncArchivesResourceWithStreamingResponse:
    def __init__(self, archives: AsyncArchivesResource) -> None:
        self._archives = archives

        self.create = async_to_streamed_response_wrapper(
            archives.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            archives.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            archives.update,
        )
        self.list = async_to_streamed_response_wrapper(
            archives.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            archives.delete,
        )
