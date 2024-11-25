# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.recall_memory_summary import RecallMemorySummary

__all__ = ["RecallResource", "AsyncRecallResource"]


class RecallResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return RecallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return RecallResourceWithStreamingResponse(self)

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecallMemorySummary:
        """
        Retrieve the summary of the recall memory of a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/memory/recall",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecallMemorySummary,
        )


class AsyncRecallResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncRecallResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecallMemorySummary:
        """
        Retrieve the summary of the recall memory of a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/memory/recall",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecallMemorySummary,
        )


class RecallResourceWithRawResponse:
    def __init__(self, recall: RecallResource) -> None:
        self._recall = recall

        self.retrieve = to_raw_response_wrapper(
            recall.retrieve,
        )


class AsyncRecallResourceWithRawResponse:
    def __init__(self, recall: AsyncRecallResource) -> None:
        self._recall = recall

        self.retrieve = async_to_raw_response_wrapper(
            recall.retrieve,
        )


class RecallResourceWithStreamingResponse:
    def __init__(self, recall: RecallResource) -> None:
        self._recall = recall

        self.retrieve = to_streamed_response_wrapper(
            recall.retrieve,
        )


class AsyncRecallResourceWithStreamingResponse:
    def __init__(self, recall: AsyncRecallResource) -> None:
        self._recall = recall

        self.retrieve = async_to_streamed_response_wrapper(
            recall.retrieve,
        )
