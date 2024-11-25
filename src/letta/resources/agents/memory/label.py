# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
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
from ....types.memory import Memory
from ....types.agents.memory import label_update_params

__all__ = ["LabelResource", "AsyncLabelResource"]


class LabelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return LabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return LabelResourceWithStreamingResponse(self)

    def update(
        self,
        agent_id: str,
        *,
        current_label: str,
        new_label: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """
        Update the label of a block in an agent's memory.

        Args:
          current_label: Current label of the block.

          new_label: New label of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/memory/label",
            body=maybe_transform(
                {
                    "current_label": current_label,
                    "new_label": new_label,
                },
                label_update_params.LabelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )


class AsyncLabelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncLabelResourceWithStreamingResponse(self)

    async def update(
        self,
        agent_id: str,
        *,
        current_label: str,
        new_label: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """
        Update the label of a block in an agent's memory.

        Args:
          current_label: Current label of the block.

          new_label: New label of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/memory/label",
            body=await async_maybe_transform(
                {
                    "current_label": current_label,
                    "new_label": new_label,
                },
                label_update_params.LabelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Memory,
        )


class LabelResourceWithRawResponse:
    def __init__(self, label: LabelResource) -> None:
        self._label = label

        self.update = to_raw_response_wrapper(
            label.update,
        )


class AsyncLabelResourceWithRawResponse:
    def __init__(self, label: AsyncLabelResource) -> None:
        self._label = label

        self.update = async_to_raw_response_wrapper(
            label.update,
        )


class LabelResourceWithStreamingResponse:
    def __init__(self, label: LabelResource) -> None:
        self._label = label

        self.update = to_streamed_response_wrapper(
            label.update,
        )


class AsyncLabelResourceWithStreamingResponse:
    def __init__(self, label: AsyncLabelResource) -> None:
        self._label = label

        self.update = async_to_streamed_response_wrapper(
            label.update,
        )
