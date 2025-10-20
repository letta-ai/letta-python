# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    DuplicateFileHandling,
    folder_list_params,
    folder_create_params,
    folder_update_params,
    folder_list_files_params,
    folder_list_agents_params,
    folder_upload_file_params,
    folder_list_passages_params,
    folder_retrieve_metadata_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.folder import Folder
from ..types.file_metadata import FileMetadata
from ..types.folder_list_response import FolderListResponse
from ..types.folder_count_response import FolderCountResponse
from ..types.embedding_config_param import EmbeddingConfigParam
from ..types.duplicate_file_handling import DuplicateFileHandling
from ..types.folder_list_files_response import FolderListFilesResponse
from ..types.organization_sources_stats import OrganizationSourcesStats
from ..types.folder_list_agents_response import FolderListAgentsResponse
from ..types.folder_list_passages_response import FolderListPassagesResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        embedding: Optional[str] | Omit = omit,
        embedding_chunk_size: Optional[int] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Create a new data folder.

        Args:
          name: The name of the source.

          description: The description of the source.

          embedding: The handle for the embedding config used by the source.

          embedding_chunk_size: The chunk size of the embedding.

          embedding_config: Configuration for embedding model connection and processing parameters.

          instructions: Instructions for how to use the source.

          metadata: Metadata associated with the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/folders/",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "embedding": embedding,
                    "embedding_chunk_size": embedding_chunk_size,
                    "embedding_config": embedding_config,
                    "instructions": instructions,
                    "metadata": metadata,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )

    def retrieve(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Get a folder by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            f"/v1/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )

    def update(
        self,
        folder_id: str,
        *,
        description: Optional[str] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Update the name or documentation of an existing data folder.

        Args:
          description: The description of the source.

          embedding_config: Configuration for embedding model connection and processing parameters.

          instructions: Instructions for how to use the source.

          metadata: Metadata associated with the source.

          name: The name of the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._patch(
            f"/v1/folders/{folder_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "embedding_config": embedding_config,
                    "instructions": instructions,
                    "metadata": metadata,
                    "name": name,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """
        List all data folders created by a user.

        Args:
          after: Folder ID cursor for pagination. Returns folders that come after this folder ID
              in the specified sort order

          before: Folder ID cursor for pagination. Returns folders that come before this folder ID
              in the specified sort order

          limit: Maximum number of folders to return

          name: Folder name to filter by

          order: Sort order for folders by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/folders/",
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
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                    },
                    folder_list_params.FolderListParams,
                ),
            ),
            cast_to=FolderListResponse,
        )

    def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a data folder.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._delete(
            f"/v1/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCountResponse:
        """Count all data folders created by a user."""
        return self._get(
            "/v1/folders/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    def delete_file(
        self,
        file_id: str,
        *,
        folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a file from a folder.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/folders/{folder_id}/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def get_by_name(
        self,
        folder_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        **Deprecated**: Please use the list endpoint `GET /v1/folders?name=` instead.

        Get a folder by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_name:
            raise ValueError(f"Expected a non-empty value for `folder_name` but received {folder_name!r}")
        return self._get(
            f"/v1/folders/name/{folder_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def list_agents(
        self,
        folder_id: str,
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
    ) -> FolderListAgentsResponse:
        """
        Get all agent IDs that have the specified folder attached.

        Args:
          after: Agent ID cursor for pagination. Returns agents that come after this agent ID in
              the specified sort order

          before: Agent ID cursor for pagination. Returns agents that come before this agent ID in
              the specified sort order

          limit: Maximum number of agents to return

          order: Sort order for agents by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            f"/v1/folders/{folder_id}/agents",
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
                    folder_list_agents_params.FolderListAgentsParams,
                ),
            ),
            cast_to=FolderListAgentsResponse,
        )

    def list_files(
        self,
        folder_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_content: bool | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListFilesResponse:
        """
        List paginated files associated with a data folder.

        Args:
          after: File ID cursor for pagination. Returns files that come after this file ID in the
              specified sort order

          before: File ID cursor for pagination. Returns files that come before this file ID in
              the specified sort order

          include_content: Whether to include full file content

          limit: Maximum number of files to return

          order: Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            f"/v1/folders/{folder_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include_content": include_content,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    folder_list_files_params.FolderListFilesParams,
                ),
            ),
            cast_to=FolderListFilesResponse,
        )

    def list_passages(
        self,
        folder_id: str,
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
    ) -> FolderListPassagesResponse:
        """
        List all passages associated with a data folder.

        Args:
          after: Passage ID cursor for pagination. Returns passages that come after this passage
              ID in the specified sort order

          before: Passage ID cursor for pagination. Returns passages that come before this passage
              ID in the specified sort order

          limit: Maximum number of passages to return

          order: Sort order for passages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            f"/v1/folders/{folder_id}/passages",
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
                    folder_list_passages_params.FolderListPassagesParams,
                ),
            ),
            cast_to=FolderListPassagesResponse,
        )

    def retrieve_metadata(
        self,
        *,
        include_detailed_per_source_metadata: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationSourcesStats:
        """
        Get aggregated metadata for all folders in an organization.

        Returns structured metadata including:

        - Total number of folders
        - Total number of files across all folders
        - Total size of all files
        - Per-source breakdown with file details (file_name, file_size per file) if
          include_detailed_per_source_metadata is True

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/folders/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_detailed_per_source_metadata": include_detailed_per_source_metadata},
                    folder_retrieve_metadata_params.FolderRetrieveMetadataParams,
                ),
            ),
            cast_to=OrganizationSourcesStats,
        )

    def upload_file(
        self,
        folder_id: str,
        *,
        file: FileTypes,
        duplicate_handling: DuplicateFileHandling | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileMetadata:
        """
        Upload a file to a data folder.

        Args:
          duplicate_handling: How to handle duplicate filenames

          name: Optional custom name to override the uploaded file's name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/v1/folders/{folder_id}/upload",
            body=maybe_transform(body, folder_upload_file_params.FolderUploadFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "duplicate_handling": duplicate_handling,
                        "name": name,
                    },
                    folder_upload_file_params.FolderUploadFileParams,
                ),
            ),
            cast_to=FileMetadata,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        embedding: Optional[str] | Omit = omit,
        embedding_chunk_size: Optional[int] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Create a new data folder.

        Args:
          name: The name of the source.

          description: The description of the source.

          embedding: The handle for the embedding config used by the source.

          embedding_chunk_size: The chunk size of the embedding.

          embedding_config: Configuration for embedding model connection and processing parameters.

          instructions: Instructions for how to use the source.

          metadata: Metadata associated with the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/folders/",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "embedding": embedding,
                    "embedding_chunk_size": embedding_chunk_size,
                    "embedding_config": embedding_config,
                    "instructions": instructions,
                    "metadata": metadata,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )

    async def retrieve(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Get a folder by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            f"/v1/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )

    async def update(
        self,
        folder_id: str,
        *,
        description: Optional[str] | Omit = omit,
        embedding_config: Optional[EmbeddingConfigParam] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Update the name or documentation of an existing data folder.

        Args:
          description: The description of the source.

          embedding_config: Configuration for embedding model connection and processing parameters.

          instructions: Instructions for how to use the source.

          metadata: Metadata associated with the source.

          name: The name of the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._patch(
            f"/v1/folders/{folder_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "embedding_config": embedding_config,
                    "instructions": instructions,
                    "metadata": metadata,
                    "name": name,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """
        List all data folders created by a user.

        Args:
          after: Folder ID cursor for pagination. Returns folders that come after this folder ID
              in the specified sort order

          before: Folder ID cursor for pagination. Returns folders that come before this folder ID
              in the specified sort order

          limit: Maximum number of folders to return

          name: Folder name to filter by

          order: Sort order for folders by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/folders/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                    },
                    folder_list_params.FolderListParams,
                ),
            ),
            cast_to=FolderListResponse,
        )

    async def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a data folder.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._delete(
            f"/v1/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCountResponse:
        """Count all data folders created by a user."""
        return await self._get(
            "/v1/folders/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    async def delete_file(
        self,
        file_id: str,
        *,
        folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a file from a folder.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/folders/{folder_id}/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_by_name(
        self,
        folder_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        **Deprecated**: Please use the list endpoint `GET /v1/folders?name=` instead.

        Get a folder by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_name:
            raise ValueError(f"Expected a non-empty value for `folder_name` but received {folder_name!r}")
        return await self._get(
            f"/v1/folders/name/{folder_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def list_agents(
        self,
        folder_id: str,
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
    ) -> FolderListAgentsResponse:
        """
        Get all agent IDs that have the specified folder attached.

        Args:
          after: Agent ID cursor for pagination. Returns agents that come after this agent ID in
              the specified sort order

          before: Agent ID cursor for pagination. Returns agents that come before this agent ID in
              the specified sort order

          limit: Maximum number of agents to return

          order: Sort order for agents by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            f"/v1/folders/{folder_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    folder_list_agents_params.FolderListAgentsParams,
                ),
            ),
            cast_to=FolderListAgentsResponse,
        )

    async def list_files(
        self,
        folder_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_content: bool | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListFilesResponse:
        """
        List paginated files associated with a data folder.

        Args:
          after: File ID cursor for pagination. Returns files that come after this file ID in the
              specified sort order

          before: File ID cursor for pagination. Returns files that come before this file ID in
              the specified sort order

          include_content: Whether to include full file content

          limit: Maximum number of files to return

          order: Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            f"/v1/folders/{folder_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include_content": include_content,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    folder_list_files_params.FolderListFilesParams,
                ),
            ),
            cast_to=FolderListFilesResponse,
        )

    async def list_passages(
        self,
        folder_id: str,
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
    ) -> FolderListPassagesResponse:
        """
        List all passages associated with a data folder.

        Args:
          after: Passage ID cursor for pagination. Returns passages that come after this passage
              ID in the specified sort order

          before: Passage ID cursor for pagination. Returns passages that come before this passage
              ID in the specified sort order

          limit: Maximum number of passages to return

          order: Sort order for passages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            f"/v1/folders/{folder_id}/passages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    folder_list_passages_params.FolderListPassagesParams,
                ),
            ),
            cast_to=FolderListPassagesResponse,
        )

    async def retrieve_metadata(
        self,
        *,
        include_detailed_per_source_metadata: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationSourcesStats:
        """
        Get aggregated metadata for all folders in an organization.

        Returns structured metadata including:

        - Total number of folders
        - Total number of files across all folders
        - Total size of all files
        - Per-source breakdown with file details (file_name, file_size per file) if
          include_detailed_per_source_metadata is True

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/folders/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_detailed_per_source_metadata": include_detailed_per_source_metadata},
                    folder_retrieve_metadata_params.FolderRetrieveMetadataParams,
                ),
            ),
            cast_to=OrganizationSourcesStats,
        )

    async def upload_file(
        self,
        folder_id: str,
        *,
        file: FileTypes,
        duplicate_handling: DuplicateFileHandling | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileMetadata:
        """
        Upload a file to a data folder.

        Args:
          duplicate_handling: How to handle duplicate filenames

          name: Optional custom name to override the uploaded file's name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/v1/folders/{folder_id}/upload",
            body=await async_maybe_transform(body, folder_upload_file_params.FolderUploadFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "duplicate_handling": duplicate_handling,
                        "name": name,
                    },
                    folder_upload_file_params.FolderUploadFileParams,
                ),
            ),
            cast_to=FileMetadata,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            folders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            folders.update,
        )
        self.list = to_raw_response_wrapper(
            folders.list,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )
        self.count = to_raw_response_wrapper(
            folders.count,
        )
        self.delete_file = to_raw_response_wrapper(
            folders.delete_file,
        )
        self.get_by_name = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                folders.get_by_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_agents = to_raw_response_wrapper(
            folders.list_agents,
        )
        self.list_files = to_raw_response_wrapper(
            folders.list_files,
        )
        self.list_passages = to_raw_response_wrapper(
            folders.list_passages,
        )
        self.retrieve_metadata = to_raw_response_wrapper(
            folders.retrieve_metadata,
        )
        self.upload_file = to_raw_response_wrapper(
            folders.upload_file,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            folders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            folders.update,
        )
        self.list = async_to_raw_response_wrapper(
            folders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )
        self.count = async_to_raw_response_wrapper(
            folders.count,
        )
        self.delete_file = async_to_raw_response_wrapper(
            folders.delete_file,
        )
        self.get_by_name = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                folders.get_by_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_agents = async_to_raw_response_wrapper(
            folders.list_agents,
        )
        self.list_files = async_to_raw_response_wrapper(
            folders.list_files,
        )
        self.list_passages = async_to_raw_response_wrapper(
            folders.list_passages,
        )
        self.retrieve_metadata = async_to_raw_response_wrapper(
            folders.retrieve_metadata,
        )
        self.upload_file = async_to_raw_response_wrapper(
            folders.upload_file,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            folders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            folders.update,
        )
        self.list = to_streamed_response_wrapper(
            folders.list,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )
        self.count = to_streamed_response_wrapper(
            folders.count,
        )
        self.delete_file = to_streamed_response_wrapper(
            folders.delete_file,
        )
        self.get_by_name = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                folders.get_by_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_agents = to_streamed_response_wrapper(
            folders.list_agents,
        )
        self.list_files = to_streamed_response_wrapper(
            folders.list_files,
        )
        self.list_passages = to_streamed_response_wrapper(
            folders.list_passages,
        )
        self.retrieve_metadata = to_streamed_response_wrapper(
            folders.retrieve_metadata,
        )
        self.upload_file = to_streamed_response_wrapper(
            folders.upload_file,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            folders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            folders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            folders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            folders.count,
        )
        self.delete_file = async_to_streamed_response_wrapper(
            folders.delete_file,
        )
        self.get_by_name = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                folders.get_by_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_agents = async_to_streamed_response_wrapper(
            folders.list_agents,
        )
        self.list_files = async_to_streamed_response_wrapper(
            folders.list_files,
        )
        self.list_passages = async_to_streamed_response_wrapper(
            folders.list_passages,
        )
        self.retrieve_metadata = async_to_streamed_response_wrapper(
            folders.retrieve_metadata,
        )
        self.upload_file = async_to_streamed_response_wrapper(
            folders.upload_file,
        )
