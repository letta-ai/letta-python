# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agent_state import AgentState

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def add(
        self,
        tool_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Add tools to an exsiting agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._patch(
            f"/v1/agents/{agent_id}/add-tool/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def remove(
        self,
        tool_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Add tools to an exsiting agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._patch(
            f"/v1/agents/{agent_id}/remove-tool/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def add(
        self,
        tool_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Add tools to an exsiting agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._patch(
            f"/v1/agents/{agent_id}/add-tool/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def remove(
        self,
        tool_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentState:
        """
        Add tools to an exsiting agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._patch(
            f"/v1/agents/{agent_id}/remove-tool/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.add = to_raw_response_wrapper(
            tools.add,
        )
        self.remove = to_raw_response_wrapper(
            tools.remove,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.add = async_to_raw_response_wrapper(
            tools.add,
        )
        self.remove = async_to_raw_response_wrapper(
            tools.remove,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.add = to_streamed_response_wrapper(
            tools.add,
        )
        self.remove = to_streamed_response_wrapper(
            tools.remove,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.add = async_to_streamed_response_wrapper(
            tools.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            tools.remove,
        )
