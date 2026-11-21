# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import goal_list_params, goal_create_params, goal_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.goal import Goal
from .._base_client import make_request_options
from ..types.goal_list_response import GoalListResponse

__all__ = ["GoalsResource", "AsyncGoalsResource"]


class GoalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GoalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return GoalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return GoalsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        agent_id: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        status: Literal["active", "completed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Goal:
        """
        Supply agent_id for agent-wide records or conversation_id for
        conversation-scoped records. With both, the conversation must belong to the
        agent. Use agent_id with conversation_id=default for the virtual default
        conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/goals",
            body=maybe_transform(
                {
                    "description": description,
                    "agent_id": agent_id,
                    "conversation_id": conversation_id,
                    "status": status,
                },
                goal_create_params.GoalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Goal,
        )

    def retrieve(
        self,
        goal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Goal:
        """
        Get a goal

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        return self._get(
            path_template("/v1/goals/{goal_id}", goal_id=goal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Goal,
        )

    def update(
        self,
        goal_id: str,
        *,
        description: str | Omit = omit,
        status: Literal["active", "completed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Goal:
        """
        Update a goal

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        return self._patch(
            path_template("/v1/goals/{goal_id}", goal_id=goal_id),
            body=maybe_transform(
                {
                    "description": description,
                    "status": status,
                },
                goal_update_params.GoalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Goal,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["active", "completed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalListResponse:
        """
        Supply agent_id for agent-wide records or conversation_id for
        conversation-scoped records. With both, the conversation must belong to the
        agent. Use agent_id with conversation_id=default for the virtual default
        conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/goals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "conversation_id": conversation_id,
                        "limit": limit,
                        "status": status,
                    },
                    goal_list_params.GoalListParams,
                ),
            ),
            cast_to=GoalListResponse,
        )

    def delete(
        self,
        goal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a goal

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/goals/{goal_id}", goal_id=goal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGoalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGoalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGoalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncGoalsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        agent_id: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        status: Literal["active", "completed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Goal:
        """
        Supply agent_id for agent-wide records or conversation_id for
        conversation-scoped records. With both, the conversation must belong to the
        agent. Use agent_id with conversation_id=default for the virtual default
        conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/goals",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "agent_id": agent_id,
                    "conversation_id": conversation_id,
                    "status": status,
                },
                goal_create_params.GoalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Goal,
        )

    async def retrieve(
        self,
        goal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Goal:
        """
        Get a goal

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        return await self._get(
            path_template("/v1/goals/{goal_id}", goal_id=goal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Goal,
        )

    async def update(
        self,
        goal_id: str,
        *,
        description: str | Omit = omit,
        status: Literal["active", "completed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Goal:
        """
        Update a goal

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        return await self._patch(
            path_template("/v1/goals/{goal_id}", goal_id=goal_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "status": status,
                },
                goal_update_params.GoalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Goal,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["active", "completed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalListResponse:
        """
        Supply agent_id for agent-wide records or conversation_id for
        conversation-scoped records. With both, the conversation must belong to the
        agent. Use agent_id with conversation_id=default for the virtual default
        conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/goals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "conversation_id": conversation_id,
                        "limit": limit,
                        "status": status,
                    },
                    goal_list_params.GoalListParams,
                ),
            ),
            cast_to=GoalListResponse,
        )

    async def delete(
        self,
        goal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a goal

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/goals/{goal_id}", goal_id=goal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GoalsResourceWithRawResponse:
    def __init__(self, goals: GoalsResource) -> None:
        self._goals = goals

        self.create = to_raw_response_wrapper(
            goals.create,
        )
        self.retrieve = to_raw_response_wrapper(
            goals.retrieve,
        )
        self.update = to_raw_response_wrapper(
            goals.update,
        )
        self.list = to_raw_response_wrapper(
            goals.list,
        )
        self.delete = to_raw_response_wrapper(
            goals.delete,
        )


class AsyncGoalsResourceWithRawResponse:
    def __init__(self, goals: AsyncGoalsResource) -> None:
        self._goals = goals

        self.create = async_to_raw_response_wrapper(
            goals.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            goals.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            goals.update,
        )
        self.list = async_to_raw_response_wrapper(
            goals.list,
        )
        self.delete = async_to_raw_response_wrapper(
            goals.delete,
        )


class GoalsResourceWithStreamingResponse:
    def __init__(self, goals: GoalsResource) -> None:
        self._goals = goals

        self.create = to_streamed_response_wrapper(
            goals.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            goals.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            goals.update,
        )
        self.list = to_streamed_response_wrapper(
            goals.list,
        )
        self.delete = to_streamed_response_wrapper(
            goals.delete,
        )


class AsyncGoalsResourceWithStreamingResponse:
    def __init__(self, goals: AsyncGoalsResource) -> None:
        self._goals = goals

        self.create = async_to_streamed_response_wrapper(
            goals.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            goals.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            goals.update,
        )
        self.list = async_to_streamed_response_wrapper(
            goals.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            goals.delete,
        )
