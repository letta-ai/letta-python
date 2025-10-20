# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, Mapping, Optional, cast

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...types import (
    DuplicateFileHandling,
    source_create_params,
    source_update_params,
    source_upload_file_params,
    source_get_metadata_params,
    source_list_passages_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.source import Source
from ...types.file_metadata import FileMetadata
from ...types.source_list_response import SourceListResponse
from ...types.source_count_response import SourceCountResponse
from ...types.embedding_config_param import EmbeddingConfigParam
from ...types.duplicate_file_handling import DuplicateFileHandling
from ...types.organization_sources_stats import OrganizationSourcesStats
from ...types.source_get_agents_response import SourceGetAgentsResponse
from ...types.source_list_passages_response import SourceListPassagesResponse

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return SourcesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
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
    ) -> Source:
        """
        Create a new data source.

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
            "/v1/sources/",
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
                source_create_params.SourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    @typing_extensions.deprecated("deprecated")
    def retrieve(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Source:
        """
        Get all sources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            f"/v1/sources/{source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    @typing_extensions.deprecated("deprecated")
    def update(
        self,
        source_id: str,
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
    ) -> Source:
        """
        Update the name or documentation of an existing data source.

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
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._patch(
            f"/v1/sources/{source_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "embedding_config": embedding_config,
                    "instructions": instructions,
                    "metadata": metadata,
                    "name": name,
                },
                source_update_params.SourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListResponse:
        """List all data sources created by a user."""
        return self._get(
            "/v1/sources/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a data source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._delete(
            f"/v1/sources/{source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceCountResponse:
        """Count all data sources created by a user."""
        return self._get(
            "/v1/sources/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    @typing_extensions.deprecated("deprecated")
    def delete_file(
        self,
        file_id: str,
        *,
        source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a data source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/sources/{source_id}/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def get_agents(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetAgentsResponse:
        """
        Get all agent IDs that have the specified source attached.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            f"/v1/sources/{source_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGetAgentsResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def get_by_name(
        self,
        source_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get a source by name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_name:
            raise ValueError(f"Expected a non-empty value for `source_name` but received {source_name!r}")
        return self._get(
            f"/v1/sources/name/{source_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    @typing_extensions.deprecated("deprecated")
    def get_metadata(
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
        Get aggregated metadata for all sources in an organization.

        Returns structured metadata including:

        - Total number of sources
        - Total number of files across all sources
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
            "/v1/sources/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_detailed_per_source_metadata": include_detailed_per_source_metadata},
                    source_get_metadata_params.SourceGetMetadataParams,
                ),
            ),
            cast_to=OrganizationSourcesStats,
        )

    @typing_extensions.deprecated("deprecated")
    def list_passages(
        self,
        source_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListPassagesResponse:
        """
        List all passages associated with a data source.

        Args:
          after: Message after which to retrieve the returned messages.

          before: Message before which to retrieve the returned messages.

          limit: Maximum number of messages to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            f"/v1/sources/{source_id}/passages",
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
                    },
                    source_list_passages_params.SourceListPassagesParams,
                ),
            ),
            cast_to=SourceListPassagesResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def upload_file(
        self,
        source_id: str,
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
        Upload a file to a data source.

        Args:
          duplicate_handling: How to handle duplicate filenames

          name: Optional custom name to override the uploaded file's name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/v1/sources/{source_id}/upload",
            body=maybe_transform(body, source_upload_file_params.SourceUploadFileParams),
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
                    source_upload_file_params.SourceUploadFileParams,
                ),
            ),
            cast_to=FileMetadata,
        )


class AsyncSourcesResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncSourcesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
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
    ) -> Source:
        """
        Create a new data source.

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
            "/v1/sources/",
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
                source_create_params.SourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    @typing_extensions.deprecated("deprecated")
    async def retrieve(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Source:
        """
        Get all sources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            f"/v1/sources/{source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    @typing_extensions.deprecated("deprecated")
    async def update(
        self,
        source_id: str,
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
    ) -> Source:
        """
        Update the name or documentation of an existing data source.

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
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._patch(
            f"/v1/sources/{source_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "embedding_config": embedding_config,
                    "instructions": instructions,
                    "metadata": metadata,
                    "name": name,
                },
                source_update_params.SourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    @typing_extensions.deprecated("deprecated")
    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListResponse:
        """List all data sources created by a user."""
        return await self._get(
            "/v1/sources/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a data source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._delete(
            f"/v1/sources/{source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    async def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceCountResponse:
        """Count all data sources created by a user."""
        return await self._get(
            "/v1/sources/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete_file(
        self,
        file_id: str,
        *,
        source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a data source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/sources/{source_id}/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_agents(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetAgentsResponse:
        """
        Get all agent IDs that have the specified source attached.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            f"/v1/sources/{source_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGetAgentsResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_by_name(
        self,
        source_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get a source by name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_name:
            raise ValueError(f"Expected a non-empty value for `source_name` but received {source_name!r}")
        return await self._get(
            f"/v1/sources/name/{source_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_metadata(
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
        Get aggregated metadata for all sources in an organization.

        Returns structured metadata including:

        - Total number of sources
        - Total number of files across all sources
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
            "/v1/sources/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_detailed_per_source_metadata": include_detailed_per_source_metadata},
                    source_get_metadata_params.SourceGetMetadataParams,
                ),
            ),
            cast_to=OrganizationSourcesStats,
        )

    @typing_extensions.deprecated("deprecated")
    async def list_passages(
        self,
        source_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListPassagesResponse:
        """
        List all passages associated with a data source.

        Args:
          after: Message after which to retrieve the returned messages.

          before: Message before which to retrieve the returned messages.

          limit: Maximum number of messages to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            f"/v1/sources/{source_id}/passages",
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
                    },
                    source_list_passages_params.SourceListPassagesParams,
                ),
            ),
            cast_to=SourceListPassagesResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def upload_file(
        self,
        source_id: str,
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
        Upload a file to a data source.

        Args:
          duplicate_handling: How to handle duplicate filenames

          name: Optional custom name to override the uploaded file's name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/v1/sources/{source_id}/upload",
            body=await async_maybe_transform(body, source_upload_file_params.SourceUploadFileParams),
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
                    source_upload_file_params.SourceUploadFileParams,
                ),
            ),
            cast_to=FileMetadata,
        )


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.count = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.count,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete_file = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.delete_file,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_agents = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.get_agents,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_by_name = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.get_by_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_metadata = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.get_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_passages = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.list_passages,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_file = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sources.upload_file,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._sources.files)


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.count = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.count,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete_file = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.delete_file,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_agents = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.get_agents,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_by_name = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.get_by_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_metadata = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.get_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_passages = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.list_passages,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_file = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sources.upload_file,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._sources.files)


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.count = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.count,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete_file = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.delete_file,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_agents = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.get_agents,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_by_name = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.get_by_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_metadata = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.get_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_passages = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.list_passages,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_file = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sources.upload_file,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._sources.files)


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.count = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.count,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete_file = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.delete_file,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_agents = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.get_agents,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_by_name = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.get_by_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_metadata = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.get_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_passages = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.list_passages,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_file = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sources.upload_file,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._sources.files)
