# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

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
from ...pagination import SyncArrayPage, AsyncArrayPage
from ...types.tool import Tool
from ..._base_client import AsyncPaginator, make_request_options
from ...types.agents import tool_list_params, tool_update_approval_params
from ...types.agent_state import AgentState

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
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
    ) -> SyncArrayPage[Tool]:
        """
        Get tools from an existing agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          after: Tool ID cursor for pagination. Returns tools that come after this tool ID in the
              specified sort order

          before: Tool ID cursor for pagination. Returns tools that come before this tool ID in
              the specified sort order

          limit: Maximum number of tools to return

          order: Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/v1/agents/{agent_id}/tools",
            page=SyncArrayPage[Tool],
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
                    tool_list_params.ToolListParams,
                ),
            ),
            model=Tool,
        )

    def attach(
        self,
        tool_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AgentState]:
        """
        Attach a tool to an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/tools/attach/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def detach(
        self,
        tool_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AgentState]:
        """
        Detach a tool from an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/tools/detach/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def update_approval(
        self,
        tool_name: str,
        *,
        agent_id: str,
        body_requires_approval: bool,
        query_requires_approval: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AgentState]:
        """
        Modify the approval requirement for a tool attached to an agent.

        Accepts requires_approval via request body (preferred) or query parameter
        (deprecated).

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          body_requires_approval: Whether the tool requires approval before execution

          query_requires_approval: Whether the tool requires approval before execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_name:
            raise ValueError(f"Expected a non-empty value for `tool_name` but received {tool_name!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/tools/approval/{tool_name}",
            body=maybe_transform(
                {"body_requires_approval": body_requires_approval}, tool_update_approval_params.ToolUpdateApprovalParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"query_requires_approval": query_requires_approval},
                    tool_update_approval_params.ToolUpdateApprovalParams,
                ),
            ),
            cast_to=AgentState,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
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
    ) -> AsyncPaginator[Tool, AsyncArrayPage[Tool]]:
        """
        Get tools from an existing agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          after: Tool ID cursor for pagination. Returns tools that come after this tool ID in the
              specified sort order

          before: Tool ID cursor for pagination. Returns tools that come before this tool ID in
              the specified sort order

          limit: Maximum number of tools to return

          order: Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/v1/agents/{agent_id}/tools",
            page=AsyncArrayPage[Tool],
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
                    tool_list_params.ToolListParams,
                ),
            ),
            model=Tool,
        )

    async def attach(
        self,
        tool_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AgentState]:
        """
        Attach a tool to an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/tools/attach/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def detach(
        self,
        tool_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AgentState]:
        """
        Detach a tool from an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/tools/detach/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def update_approval(
        self,
        tool_name: str,
        *,
        agent_id: str,
        body_requires_approval: bool,
        query_requires_approval: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AgentState]:
        """
        Modify the approval requirement for a tool attached to an agent.

        Accepts requires_approval via request body (preferred) or query parameter
        (deprecated).

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          body_requires_approval: Whether the tool requires approval before execution

          query_requires_approval: Whether the tool requires approval before execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not tool_name:
            raise ValueError(f"Expected a non-empty value for `tool_name` but received {tool_name!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/tools/approval/{tool_name}",
            body=await async_maybe_transform(
                {"body_requires_approval": body_requires_approval}, tool_update_approval_params.ToolUpdateApprovalParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_requires_approval": query_requires_approval},
                    tool_update_approval_params.ToolUpdateApprovalParams,
                ),
            ),
            cast_to=AgentState,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.attach = to_raw_response_wrapper(
            tools.attach,
        )
        self.detach = to_raw_response_wrapper(
            tools.detach,
        )
        self.update_approval = to_raw_response_wrapper(
            tools.update_approval,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.attach = async_to_raw_response_wrapper(
            tools.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            tools.detach,
        )
        self.update_approval = async_to_raw_response_wrapper(
            tools.update_approval,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.attach = to_streamed_response_wrapper(
            tools.attach,
        )
        self.detach = to_streamed_response_wrapper(
            tools.detach,
        )
        self.update_approval = to_streamed_response_wrapper(
            tools.update_approval,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.attach = async_to_streamed_response_wrapper(
            tools.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            tools.detach,
        )
        self.update_approval = async_to_streamed_response_wrapper(
            tools.update_approval,
        )
