# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.memory import limit_update_params
from ....types.agents.memory.memory import Memory

__all__ = ["LimitResource", "AsyncLimitResource"]


class LimitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LimitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return LimitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LimitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return LimitResourceWithStreamingResponse(self)

    def update(
        self,
        agent_id: str,
        *,
        label: str,
        limit: int,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """
        Update the limit of a block in an agent's memory.

        Args:
          label: Label of the block.

          limit: New limit of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._patch(
            f"/v1/agents/{agent_id}/memory/limit",
            body=maybe_transform(
                {
                    "label": label,
                    "limit": limit,
                },
                limit_update_params.LimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )


class AsyncLimitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLimitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLimitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLimitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncLimitResourceWithStreamingResponse(self)

    async def update(
        self,
        agent_id: str,
        *,
        label: str,
        limit: int,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """
        Update the limit of a block in an agent's memory.

        Args:
          label: Label of the block.

          limit: New limit of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._patch(
            f"/v1/agents/{agent_id}/memory/limit",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "limit": limit,
                },
                limit_update_params.LimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )


class LimitResourceWithRawResponse:
    def __init__(self, limit: LimitResource) -> None:
        self._limit = limit

        self.update = to_raw_response_wrapper(
            limit.update,
        )


class AsyncLimitResourceWithRawResponse:
    def __init__(self, limit: AsyncLimitResource) -> None:
        self._limit = limit

        self.update = async_to_raw_response_wrapper(
            limit.update,
        )


class LimitResourceWithStreamingResponse:
    def __init__(self, limit: LimitResource) -> None:
        self._limit = limit

        self.update = to_streamed_response_wrapper(
            limit.update,
        )


class AsyncLimitResourceWithStreamingResponse:
    def __init__(self, limit: AsyncLimitResource) -> None:
        self._limit = limit

        self.update = async_to_streamed_response_wrapper(
            limit.update,
        )
