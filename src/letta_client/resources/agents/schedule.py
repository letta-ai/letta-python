# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import schedule_list_params, schedule_create_params
from ...types.agents.schedule_list_response import ScheduleListResponse
from ...types.agents.schedule_create_response import ScheduleCreateResponse
from ...types.agents.schedule_delete_response import ScheduleDeleteResponse
from ...types.agents.schedule_retrieve_response import ScheduleRetrieveResponse

__all__ = ["ScheduleResource", "AsyncScheduleResource"]


class ScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ScheduleResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        messages: Iterable[schedule_create_params.Message],
        schedule: schedule_create_params.Schedule,
        callback_url: str | Omit = omit,
        context_window_limit: Optional[int] | Omit = omit,
        conversation_id: str | Omit = omit,
        description: str | Omit = omit,
        include_return_message_types: List[
            Literal[
                "system_message",
                "user_message",
                "assistant_message",
                "reasoning_message",
                "hidden_reasoning_message",
                "tool_call_message",
                "tool_return_message",
                "approval_request_message",
                "approval_response_message",
            ]
        ]
        | Omit = omit,
        max_steps: float | Omit = omit,
        model: Optional[str] | Omit = omit,
        model_settings: object | Omit = omit,
        name: str | Omit = omit,
        target_device_id: str | Omit = omit,
        use_sandbox: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCreateResponse:
        """
        Schedule a message to be sent by the agent at a specified time or on a recurring
        basis.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v1/agents/{agent_id}/schedule", agent_id=agent_id),
            body=maybe_transform(
                {
                    "messages": messages,
                    "schedule": schedule,
                    "callback_url": callback_url,
                    "context_window_limit": context_window_limit,
                    "conversation_id": conversation_id,
                    "description": description,
                    "include_return_message_types": include_return_message_types,
                    "max_steps": max_steps,
                    "model": model,
                    "model_settings": model_settings,
                    "name": name,
                    "target_device_id": target_device_id,
                    "use_sandbox": use_sandbox,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
        )

    def retrieve(
        self,
        scheduled_message_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleRetrieveResponse:
        """
        Retrieve a scheduled message by its ID for a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not scheduled_message_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_message_id` but received {scheduled_message_id!r}"
            )
        return self._get(
            path_template(
                "/v1/agents/{agent_id}/schedule/{scheduled_message_id}",
                agent_id=agent_id,
                scheduled_message_id=scheduled_message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleRetrieveResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        after: str | Omit = omit,
        include_completed: Literal["true", "false"] | Omit = omit,
        limit: str | Omit = omit,
        schedule_type: Literal["one-time", "recurring"] | Omit = omit,
        status: Literal["active", "paused", "completed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """
        List all scheduled messages for a specific agent.

        Args:
          include_completed: When 'true', include schedules that already completed (one-time schedules that
              already fired). Defaults to active and paused schedules.

          schedule_type: Filter by schedule kind. one-time schedules have a fixed scheduled_at; recurring
              schedules have a cron_expression.

          status: Return only schedules with this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/agents/{agent_id}/schedule", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "include_completed": include_completed,
                        "limit": limit,
                        "schedule_type": schedule_type,
                        "status": status,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    def delete(
        self,
        scheduled_message_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleDeleteResponse:
        """
        Delete a scheduled message by its ID for a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not scheduled_message_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_message_id` but received {scheduled_message_id!r}"
            )
        return self._delete(
            path_template(
                "/v1/agents/{agent_id}/schedule/{scheduled_message_id}",
                agent_id=agent_id,
                scheduled_message_id=scheduled_message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleDeleteResponse,
        )


class AsyncScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncScheduleResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        messages: Iterable[schedule_create_params.Message],
        schedule: schedule_create_params.Schedule,
        callback_url: str | Omit = omit,
        context_window_limit: Optional[int] | Omit = omit,
        conversation_id: str | Omit = omit,
        description: str | Omit = omit,
        include_return_message_types: List[
            Literal[
                "system_message",
                "user_message",
                "assistant_message",
                "reasoning_message",
                "hidden_reasoning_message",
                "tool_call_message",
                "tool_return_message",
                "approval_request_message",
                "approval_response_message",
            ]
        ]
        | Omit = omit,
        max_steps: float | Omit = omit,
        model: Optional[str] | Omit = omit,
        model_settings: object | Omit = omit,
        name: str | Omit = omit,
        target_device_id: str | Omit = omit,
        use_sandbox: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCreateResponse:
        """
        Schedule a message to be sent by the agent at a specified time or on a recurring
        basis.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v1/agents/{agent_id}/schedule", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "schedule": schedule,
                    "callback_url": callback_url,
                    "context_window_limit": context_window_limit,
                    "conversation_id": conversation_id,
                    "description": description,
                    "include_return_message_types": include_return_message_types,
                    "max_steps": max_steps,
                    "model": model,
                    "model_settings": model_settings,
                    "name": name,
                    "target_device_id": target_device_id,
                    "use_sandbox": use_sandbox,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
        )

    async def retrieve(
        self,
        scheduled_message_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleRetrieveResponse:
        """
        Retrieve a scheduled message by its ID for a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not scheduled_message_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_message_id` but received {scheduled_message_id!r}"
            )
        return await self._get(
            path_template(
                "/v1/agents/{agent_id}/schedule/{scheduled_message_id}",
                agent_id=agent_id,
                scheduled_message_id=scheduled_message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleRetrieveResponse,
        )

    async def list(
        self,
        agent_id: str,
        *,
        after: str | Omit = omit,
        include_completed: Literal["true", "false"] | Omit = omit,
        limit: str | Omit = omit,
        schedule_type: Literal["one-time", "recurring"] | Omit = omit,
        status: Literal["active", "paused", "completed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """
        List all scheduled messages for a specific agent.

        Args:
          include_completed: When 'true', include schedules that already completed (one-time schedules that
              already fired). Defaults to active and paused schedules.

          schedule_type: Filter by schedule kind. one-time schedules have a fixed scheduled_at; recurring
              schedules have a cron_expression.

          status: Return only schedules with this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/agents/{agent_id}/schedule", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "include_completed": include_completed,
                        "limit": limit,
                        "schedule_type": schedule_type,
                        "status": status,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    async def delete(
        self,
        scheduled_message_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleDeleteResponse:
        """
        Delete a scheduled message by its ID for a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not scheduled_message_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_message_id` but received {scheduled_message_id!r}"
            )
        return await self._delete(
            path_template(
                "/v1/agents/{agent_id}/schedule/{scheduled_message_id}",
                agent_id=agent_id,
                scheduled_message_id=scheduled_message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleDeleteResponse,
        )


class ScheduleResourceWithRawResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_raw_response_wrapper(
            schedule.create,
        )
        self.retrieve = to_raw_response_wrapper(
            schedule.retrieve,
        )
        self.list = to_raw_response_wrapper(
            schedule.list,
        )
        self.delete = to_raw_response_wrapper(
            schedule.delete,
        )


class AsyncScheduleResourceWithRawResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_raw_response_wrapper(
            schedule.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            schedule.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            schedule.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schedule.delete,
        )


class ScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_streamed_response_wrapper(
            schedule.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            schedule.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            schedule.list,
        )
        self.delete = to_streamed_response_wrapper(
            schedule.delete,
        )


class AsyncScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_streamed_response_wrapper(
            schedule.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            schedule.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            schedule.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schedule.delete,
        )
