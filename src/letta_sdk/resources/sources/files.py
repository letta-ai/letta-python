# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.sources import file_list_params, file_retrieve_params
from ...types.file_metadata import FileMetadata
from ...types.sources.file_list_response import FileListResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def retrieve(
        self,
        file_id: str,
        *,
        source_id: str,
        include_content: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileMetadata:
        """
        Retrieve metadata for a specific file by its ID.

        Args:
          include_content: Whether to include full file content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/v1/sources/{source_id}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_content": include_content}, file_retrieve_params.FileRetrieveParams),
            ),
            cast_to=FileMetadata,
        )

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        source_id: str,
        *,
        after: Optional[str] | Omit = omit,
        check_status_updates: bool | Omit = omit,
        include_content: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List paginated files associated with a data source.

        Args:
          after: Pagination cursor to fetch the next set of results

          check_status_updates: Whether to check and update file processing status (from the vector db service).
              If False, will not fetch and update the status, which may lead to performance
              gains.

          include_content: Whether to include full file content

          limit: Number of files to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            f"/v1/sources/{source_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "check_status_updates": check_status_updates,
                        "include_content": include_content,
                        "limit": limit,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def retrieve(
        self,
        file_id: str,
        *,
        source_id: str,
        include_content: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileMetadata:
        """
        Retrieve metadata for a specific file by its ID.

        Args:
          include_content: Whether to include full file content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/v1/sources/{source_id}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_content": include_content}, file_retrieve_params.FileRetrieveParams
                ),
            ),
            cast_to=FileMetadata,
        )

    @typing_extensions.deprecated("deprecated")
    async def list(
        self,
        source_id: str,
        *,
        after: Optional[str] | Omit = omit,
        check_status_updates: bool | Omit = omit,
        include_content: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List paginated files associated with a data source.

        Args:
          after: Pagination cursor to fetch the next set of results

          check_status_updates: Whether to check and update file processing status (from the vector db service).
              If False, will not fetch and update the status, which may lead to performance
              gains.

          include_content: Whether to include full file content

          limit: Number of files to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            f"/v1/sources/{source_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "check_status_updates": check_status_updates,
                        "include_content": include_content,
                        "limit": limit,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                files.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                files.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                files.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                files.list,  # pyright: ignore[reportDeprecated],
            )
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                files.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                files.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                files.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                files.list,  # pyright: ignore[reportDeprecated],
            )
        )
