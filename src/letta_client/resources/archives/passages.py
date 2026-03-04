# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.passage import Passage
from ...types.archives import passage_create_params, passage_create_many_params
from ...types.archives.passage_create_many_response import PassageCreateManyResponse

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

    def create(
        self,
        archive_id: str,
        *,
        text: str,
        created_at: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Passage:
        """
        Create a new passage in an archive.

        This adds a passage to the archive and creates embeddings for vector storage.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          text: The text content of the passage

          created_at: Optional creation datetime for the passage (ISO 8601 format)

          metadata: Optional metadata for the passage

          tags: Optional tags for categorizing the passage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return self._post(
            f"/v1/archives/{archive_id}/passages",
            body=maybe_transform(
                {
                    "text": text,
                    "created_at": created_at,
                    "metadata": metadata,
                    "tags": tags,
                },
                passage_create_params.PassageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Passage,
        )

    def delete(
        self,
        passage_id: str,
        *,
        archive_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a passage from an archive.

        This permanently removes the passage from both the database and vector storage
        (if applicable).

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          passage_id: The ID of the passage in the format 'passage-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        if not passage_id:
            raise ValueError(f"Expected a non-empty value for `passage_id` but received {passage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/archives/{archive_id}/passages/{passage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_many(
        self,
        archive_id: str,
        *,
        passages: Iterable[passage_create_many_params.Passage],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageCreateManyResponse:
        """
        Create multiple passages in an archive.

        This adds passages to the archive and creates embeddings for vector storage.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          passages: Passages to create in the archive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return self._post(
            f"/v1/archives/{archive_id}/passages/batch",
            body=maybe_transform({"passages": passages}, passage_create_many_params.PassageCreateManyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PassageCreateManyResponse,
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

    async def create(
        self,
        archive_id: str,
        *,
        text: str,
        created_at: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Passage:
        """
        Create a new passage in an archive.

        This adds a passage to the archive and creates embeddings for vector storage.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          text: The text content of the passage

          created_at: Optional creation datetime for the passage (ISO 8601 format)

          metadata: Optional metadata for the passage

          tags: Optional tags for categorizing the passage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return await self._post(
            f"/v1/archives/{archive_id}/passages",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "created_at": created_at,
                    "metadata": metadata,
                    "tags": tags,
                },
                passage_create_params.PassageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Passage,
        )

    async def delete(
        self,
        passage_id: str,
        *,
        archive_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a passage from an archive.

        This permanently removes the passage from both the database and vector storage
        (if applicable).

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          passage_id: The ID of the passage in the format 'passage-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        if not passage_id:
            raise ValueError(f"Expected a non-empty value for `passage_id` but received {passage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/archives/{archive_id}/passages/{passage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_many(
        self,
        archive_id: str,
        *,
        passages: Iterable[passage_create_many_params.Passage],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PassageCreateManyResponse:
        """
        Create multiple passages in an archive.

        This adds passages to the archive and creates embeddings for vector storage.

        Args:
          archive_id: The ID of the archive in the format 'archive-<uuid4>'

          passages: Passages to create in the archive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return await self._post(
            f"/v1/archives/{archive_id}/passages/batch",
            body=await async_maybe_transform(
                {"passages": passages}, passage_create_many_params.PassageCreateManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PassageCreateManyResponse,
        )


class PassagesResourceWithRawResponse:
    def __init__(self, passages: PassagesResource) -> None:
        self._passages = passages

        self.create = to_raw_response_wrapper(
            passages.create,
        )
        self.delete = to_raw_response_wrapper(
            passages.delete,
        )
        self.create_many = to_raw_response_wrapper(
            passages.create_many,
        )


class AsyncPassagesResourceWithRawResponse:
    def __init__(self, passages: AsyncPassagesResource) -> None:
        self._passages = passages

        self.create = async_to_raw_response_wrapper(
            passages.create,
        )
        self.delete = async_to_raw_response_wrapper(
            passages.delete,
        )
        self.create_many = async_to_raw_response_wrapper(
            passages.create_many,
        )


class PassagesResourceWithStreamingResponse:
    def __init__(self, passages: PassagesResource) -> None:
        self._passages = passages

        self.create = to_streamed_response_wrapper(
            passages.create,
        )
        self.delete = to_streamed_response_wrapper(
            passages.delete,
        )
        self.create_many = to_streamed_response_wrapper(
            passages.create_many,
        )


class AsyncPassagesResourceWithStreamingResponse:
    def __init__(self, passages: AsyncPassagesResource) -> None:
        self._passages = passages

        self.create = async_to_streamed_response_wrapper(
            passages.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            passages.delete,
        )
        self.create_many = async_to_streamed_response_wrapper(
            passages.create_many,
        )
