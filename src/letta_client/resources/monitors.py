# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import monitor_list_params, monitor_create_params, monitor_update_params
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
from .._base_client import make_request_options
from ..types.monitor import Monitor
from ..types.monitor_list_response import MonitorListResponse

__all__ = ["MonitorsResource", "AsyncMonitorsResource"]


class MonitorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MonitorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return MonitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return MonitorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        command: str,
        description: str,
        kind: Literal["command", "websocket", "script", "github_pull_request"],
        agent_id: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        device_id: Optional[str] | Omit = omit,
        exit_code: Optional[int] | Omit = omit,
        output_file: Optional[str] | Omit = omit,
        persistent: bool | Omit = omit,
        started_at: Union[str, datetime, None] | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
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
            "/v1/monitors",
            body=maybe_transform(
                {
                    "command": command,
                    "description": description,
                    "kind": kind,
                    "agent_id": agent_id,
                    "conversation_id": conversation_id,
                    "device_id": device_id,
                    "exit_code": exit_code,
                    "output_file": output_file,
                    "persistent": persistent,
                    "started_at": started_at,
                    "status": status,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def retrieve(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Get a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._get(
            path_template("/v1/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def update(
        self,
        monitor_id: str,
        *,
        command: str | Omit = omit,
        description: str | Omit = omit,
        device_id: Optional[str] | Omit = omit,
        exit_code: Optional[int] | Omit = omit,
        kind: Literal["command", "websocket", "script", "github_pull_request"] | Omit = omit,
        output_file: Optional[str] | Omit = omit,
        persistent: bool | Omit = omit,
        started_at: Union[str, datetime, None] | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Update a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._patch(
            path_template("/v1/monitors/{monitor_id}", monitor_id=monitor_id),
            body=maybe_transform(
                {
                    "command": command,
                    "description": description,
                    "device_id": device_id,
                    "exit_code": exit_code,
                    "kind": kind,
                    "output_file": output_file,
                    "persistent": persistent,
                    "started_at": started_at,
                    "status": status,
                },
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
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
            "/v1/monitors",
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
                    monitor_list_params.MonitorListParams,
                ),
            ),
            cast_to=MonitorListResponse,
        )

    def delete(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMonitorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMonitorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMonitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncMonitorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        command: str,
        description: str,
        kind: Literal["command", "websocket", "script", "github_pull_request"],
        agent_id: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        device_id: Optional[str] | Omit = omit,
        exit_code: Optional[int] | Omit = omit,
        output_file: Optional[str] | Omit = omit,
        persistent: bool | Omit = omit,
        started_at: Union[str, datetime, None] | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
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
            "/v1/monitors",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "description": description,
                    "kind": kind,
                    "agent_id": agent_id,
                    "conversation_id": conversation_id,
                    "device_id": device_id,
                    "exit_code": exit_code,
                    "output_file": output_file,
                    "persistent": persistent,
                    "started_at": started_at,
                    "status": status,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def retrieve(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Get a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._get(
            path_template("/v1/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def update(
        self,
        monitor_id: str,
        *,
        command: str | Omit = omit,
        description: str | Omit = omit,
        device_id: Optional[str] | Omit = omit,
        exit_code: Optional[int] | Omit = omit,
        kind: Literal["command", "websocket", "script", "github_pull_request"] | Omit = omit,
        output_file: Optional[str] | Omit = omit,
        persistent: bool | Omit = omit,
        started_at: Union[str, datetime, None] | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Update a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._patch(
            path_template("/v1/monitors/{monitor_id}", monitor_id=monitor_id),
            body=await async_maybe_transform(
                {
                    "command": command,
                    "description": description,
                    "device_id": device_id,
                    "exit_code": exit_code,
                    "kind": kind,
                    "output_file": output_file,
                    "persistent": persistent,
                    "started_at": started_at,
                    "status": status,
                },
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
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
            "/v1/monitors",
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
                    monitor_list_params.MonitorListParams,
                ),
            ),
            cast_to=MonitorListResponse,
        )

    async def delete(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MonitorsResourceWithRawResponse:
    def __init__(self, monitors: MonitorsResource) -> None:
        self._monitors = monitors

        self.create = to_raw_response_wrapper(
            monitors.create,
        )
        self.retrieve = to_raw_response_wrapper(
            monitors.retrieve,
        )
        self.update = to_raw_response_wrapper(
            monitors.update,
        )
        self.list = to_raw_response_wrapper(
            monitors.list,
        )
        self.delete = to_raw_response_wrapper(
            monitors.delete,
        )


class AsyncMonitorsResourceWithRawResponse:
    def __init__(self, monitors: AsyncMonitorsResource) -> None:
        self._monitors = monitors

        self.create = async_to_raw_response_wrapper(
            monitors.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            monitors.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            monitors.update,
        )
        self.list = async_to_raw_response_wrapper(
            monitors.list,
        )
        self.delete = async_to_raw_response_wrapper(
            monitors.delete,
        )


class MonitorsResourceWithStreamingResponse:
    def __init__(self, monitors: MonitorsResource) -> None:
        self._monitors = monitors

        self.create = to_streamed_response_wrapper(
            monitors.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            monitors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            monitors.update,
        )
        self.list = to_streamed_response_wrapper(
            monitors.list,
        )
        self.delete = to_streamed_response_wrapper(
            monitors.delete,
        )


class AsyncMonitorsResourceWithStreamingResponse:
    def __init__(self, monitors: AsyncMonitorsResource) -> None:
        self._monitors = monitors

        self.create = async_to_streamed_response_wrapper(
            monitors.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            monitors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            monitors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            monitors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            monitors.delete,
        )
