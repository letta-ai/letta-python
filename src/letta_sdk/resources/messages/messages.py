# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .batches import (
    BatchesResource,
    AsyncBatchesResource,
    BatchesResourceWithRawResponse,
    AsyncBatchesResourceWithRawResponse,
    BatchesResourceWithStreamingResponse,
    AsyncBatchesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def batches(self) -> BatchesResource:
        return BatchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def batches(self) -> AsyncBatchesResource:
        return AsyncBatchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

    @cached_property
    def batches(self) -> BatchesResourceWithRawResponse:
        return BatchesResourceWithRawResponse(self._messages.batches)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

    @cached_property
    def batches(self) -> AsyncBatchesResourceWithRawResponse:
        return AsyncBatchesResourceWithRawResponse(self._messages.batches)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

    @cached_property
    def batches(self) -> BatchesResourceWithStreamingResponse:
        return BatchesResourceWithStreamingResponse(self._messages.batches)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

    @cached_property
    def batches(self) -> AsyncBatchesResourceWithStreamingResponse:
        return AsyncBatchesResourceWithStreamingResponse(self._messages.batches)
