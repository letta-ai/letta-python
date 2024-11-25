# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

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
    source_attach_params,
    source_create_params,
    source_detach_params,
    source_update_params,
    source_upload_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    strip_not_given,
    deepcopy_minimal,
    async_maybe_transform,
)
from .passages import (
    PassagesResource,
    AsyncPassagesResource,
    PassagesResourceWithRawResponse,
    AsyncPassagesResourceWithRawResponse,
    PassagesResourceWithStreamingResponse,
    AsyncPassagesResourceWithStreamingResponse,
)
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
from ...types.shared.job import Job
from ...types.source_list_response import SourceListResponse
from ...types.embedding_config_param import EmbeddingConfigParam

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    @cached_property
    def passages(self) -> PassagesResource:
        return PassagesResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return SourcesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        embedding_config: Optional[EmbeddingConfigParam] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Create a new data source.

        Args:
          name: The name of the source.

          description: The description of the source.

          embedding_config: Embedding model configuration. This object specifies all the information
              necessary to access an embedding model to usage with Letta, except for secret
              keys.

              Attributes: embedding_endpoint_type (str): The endpoint type for the model.
              embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
              model for the embedding. embedding_dim (int): The dimension of the embedding.
              embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
              (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
              azure_version (str): The Azure version for the model (Azure only).
              azure_deployment (str): The Azure deployment for the model (Azure only).

          metadata: Metadata associated with the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._post(
            "/v1/sources/",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "embedding_config": embedding_config,
                    "metadata": metadata,
                },
                source_create_params.SourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    def retrieve(
        self,
        source_name: str,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._get(
            f"/v1/sources/name/{source_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def update(
        self,
        source_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        embedding_config: Optional[EmbeddingConfigParam] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Update the name or documentation of an existing data source.

        Args:
          description: The description of the source.

          embedding_config: Embedding model configuration. This object specifies all the information
              necessary to access an embedding model to usage with Letta, except for secret
              keys.

              Attributes: embedding_endpoint_type (str): The endpoint type for the model.
              embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
              model for the embedding. embedding_dim (int): The dimension of the embedding.
              embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
              (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
              azure_version (str): The Azure version for the model (Azure only).
              azure_deployment (str): The Azure deployment for the model (Azure only).

          metadata: Metadata associated with the source.

          name: The name of the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._patch(
            f"/v1/sources/{source_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "embedding_config": embedding_config,
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

    def list(
        self,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SourceListResponse:
        """
        List all data sources created by a user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._get(
            "/v1/sources/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceListResponse,
        )

    def delete(
        self,
        source_id: str,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._delete(
            f"/v1/sources/{source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def attach(
        self,
        source_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Attach a data source to an existing agent.

        Args:
          agent_id: The unique identifier of the agent to attach the source to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._post(
            f"/v1/sources/{source_id}/attach",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, source_attach_params.SourceAttachParams),
            ),
            cast_to=Source,
        )

    def detach(
        self,
        source_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Detach a data source from an existing agent.

        Args:
          agent_id: The unique identifier of the agent to detach the source from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._post(
            f"/v1/sources/{source_id}/detach",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, source_detach_params.SourceDetachParams),
            ),
            cast_to=Source,
        )

    def upload(
        self,
        source_id: str,
        *,
        file: FileTypes,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Job:
        """
        Upload a file to a data source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/v1/sources/{source_id}/upload",
            body=maybe_transform(body, source_upload_params.SourceUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class AsyncSourcesResource(AsyncAPIResource):
    @cached_property
    def passages(self) -> AsyncPassagesResource:
        return AsyncPassagesResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncSourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        embedding_config: Optional[EmbeddingConfigParam] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Create a new data source.

        Args:
          name: The name of the source.

          description: The description of the source.

          embedding_config: Embedding model configuration. This object specifies all the information
              necessary to access an embedding model to usage with Letta, except for secret
              keys.

              Attributes: embedding_endpoint_type (str): The endpoint type for the model.
              embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
              model for the embedding. embedding_dim (int): The dimension of the embedding.
              embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
              (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
              azure_version (str): The Azure version for the model (Azure only).
              azure_deployment (str): The Azure deployment for the model (Azure only).

          metadata: Metadata associated with the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/sources/",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "embedding_config": embedding_config,
                    "metadata": metadata,
                },
                source_create_params.SourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    async def retrieve(
        self,
        source_name: str,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._get(
            f"/v1/sources/name/{source_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def update(
        self,
        source_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        embedding_config: Optional[EmbeddingConfigParam] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Update the name or documentation of an existing data source.

        Args:
          description: The description of the source.

          embedding_config: Embedding model configuration. This object specifies all the information
              necessary to access an embedding model to usage with Letta, except for secret
              keys.

              Attributes: embedding_endpoint_type (str): The endpoint type for the model.
              embedding_endpoint (str): The endpoint for the model. embedding_model (str): The
              model for the embedding. embedding_dim (int): The dimension of the embedding.
              embedding_chunk_size (int): The chunk size of the embedding. azure_endpoint
              (:obj:`str`, optional): The Azure endpoint for the model (Azure only).
              azure_version (str): The Azure version for the model (Azure only).
              azure_deployment (str): The Azure deployment for the model (Azure only).

          metadata: Metadata associated with the source.

          name: The name of the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._patch(
            f"/v1/sources/{source_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "embedding_config": embedding_config,
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

    async def list(
        self,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SourceListResponse:
        """
        List all data sources created by a user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/sources/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceListResponse,
        )

    async def delete(
        self,
        source_id: str,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._delete(
            f"/v1/sources/{source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def attach(
        self,
        source_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Attach a data source to an existing agent.

        Args:
          agent_id: The unique identifier of the agent to attach the source to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._post(
            f"/v1/sources/{source_id}/attach",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"agent_id": agent_id}, source_attach_params.SourceAttachParams),
            ),
            cast_to=Source,
        )

    async def detach(
        self,
        source_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Detach a data source from an existing agent.

        Args:
          agent_id: The unique identifier of the agent to detach the source from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._post(
            f"/v1/sources/{source_id}/detach",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"agent_id": agent_id}, source_detach_params.SourceDetachParams),
            ),
            cast_to=Source,
        )

    async def upload(
        self,
        source_id: str,
        *,
        file: FileTypes,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Job:
        """
        Upload a file to a data source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/v1/sources/{source_id}/upload",
            body=await async_maybe_transform(body, source_upload_params.SourceUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.create = to_raw_response_wrapper(
            sources.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sources.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sources.update,
        )
        self.list = to_raw_response_wrapper(
            sources.list,
        )
        self.delete = to_raw_response_wrapper(
            sources.delete,
        )
        self.attach = to_raw_response_wrapper(
            sources.attach,
        )
        self.detach = to_raw_response_wrapper(
            sources.detach,
        )
        self.upload = to_raw_response_wrapper(
            sources.upload,
        )

    @cached_property
    def passages(self) -> PassagesResourceWithRawResponse:
        return PassagesResourceWithRawResponse(self._sources.passages)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._sources.files)


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.create = async_to_raw_response_wrapper(
            sources.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sources.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sources.update,
        )
        self.list = async_to_raw_response_wrapper(
            sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sources.delete,
        )
        self.attach = async_to_raw_response_wrapper(
            sources.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            sources.detach,
        )
        self.upload = async_to_raw_response_wrapper(
            sources.upload,
        )

    @cached_property
    def passages(self) -> AsyncPassagesResourceWithRawResponse:
        return AsyncPassagesResourceWithRawResponse(self._sources.passages)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._sources.files)


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.create = to_streamed_response_wrapper(
            sources.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sources.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sources.update,
        )
        self.list = to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            sources.delete,
        )
        self.attach = to_streamed_response_wrapper(
            sources.attach,
        )
        self.detach = to_streamed_response_wrapper(
            sources.detach,
        )
        self.upload = to_streamed_response_wrapper(
            sources.upload,
        )

    @cached_property
    def passages(self) -> PassagesResourceWithStreamingResponse:
        return PassagesResourceWithStreamingResponse(self._sources.passages)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._sources.files)


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.create = async_to_streamed_response_wrapper(
            sources.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sources.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sources.delete,
        )
        self.attach = async_to_streamed_response_wrapper(
            sources.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            sources.detach,
        )
        self.upload = async_to_streamed_response_wrapper(
            sources.upload,
        )

    @cached_property
    def passages(self) -> AsyncPassagesResourceWithStreamingResponse:
        return AsyncPassagesResourceWithStreamingResponse(self._sources.passages)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._sources.files)
