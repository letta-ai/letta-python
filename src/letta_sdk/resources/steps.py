# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import step_list_params, step_list_messages_params, step_update_feedback_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.step import Step
from .._base_client import make_request_options
from ..types.provider_trace import ProviderTrace
from ..types.step_list_response import StepListResponse
from ..types.step_list_messages_response import StepListMessagesResponse
from ..types.step_retrieve_metrics_response import StepRetrieveMetricsResponse

__all__ = ["StepsResource", "AsyncStepsResource"]


class StepsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StepsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return StepsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StepsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return StepsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Step:
        """
        Get a step by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._get(
            f"/v1/steps/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Step,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        end_date: Optional[str] | Omit = omit,
        feedback: Optional[Literal["positive", "negative"]] | Omit = omit,
        has_feedback: Optional[bool] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        model: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        trace_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        x_project: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StepListResponse:
        """
        List steps with optional pagination and date filters.

        Args:
          after: Return steps after this step ID

          agent_id: Filter by the ID of the agent that performed the step

          before: Return steps before this step ID

          end_date: Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

          feedback: Filter by feedback

          has_feedback: Filter by whether steps have feedback (true) or not (false)

          limit: Maximum number of steps to return

          model: Filter by the name of the model used for the step

          order: Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          project_id: Filter by the project ID that is associated with the step (cloud only).

          start_date: Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

          tags: Filter by tags

          trace_ids: Filter by trace ids returned by the server

          x_project: Filter by project slug to associate with the group (cloud only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Project": x_project}), **(extra_headers or {})}
        return self._get(
            "/v1/steps/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "before": before,
                        "end_date": end_date,
                        "feedback": feedback,
                        "has_feedback": has_feedback,
                        "limit": limit,
                        "model": model,
                        "order": order,
                        "order_by": order_by,
                        "project_id": project_id,
                        "start_date": start_date,
                        "tags": tags,
                        "trace_ids": trace_ids,
                    },
                    step_list_params.StepListParams,
                ),
            ),
            cast_to=StepListResponse,
        )

    def list_messages(
        self,
        step_id: str,
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
    ) -> StepListMessagesResponse:
        """List messages for a given step.

        Args:
          after: Message ID cursor for pagination.

        Returns messages that come after this message
              ID in the specified sort order

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          limit: Maximum number of messages to return

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Sort by field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._get(
            f"/v1/steps/{step_id}/messages",
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
                    step_list_messages_params.StepListMessagesParams,
                ),
            ),
            cast_to=StepListMessagesResponse,
        )

    def retrieve_metrics(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StepRetrieveMetricsResponse:
        """
        Get step metrics by step ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._get(
            f"/v1/steps/{step_id}/metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StepRetrieveMetricsResponse,
        )

    def retrieve_trace(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ProviderTrace]:
        """
        Retrieve Trace For Step

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._get(
            f"/v1/steps/{step_id}/trace",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderTrace,
        )

    def update_feedback(
        self,
        step_id: str,
        *,
        feedback: Optional[Literal["positive", "negative"]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Step:
        """
        Modify feedback for a given step.

        Args:
          feedback: Whether this feedback is positive or negative

          tags: Feedback tags to add to the step

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._patch(
            f"/v1/steps/{step_id}/feedback",
            body=maybe_transform(
                {
                    "feedback": feedback,
                    "tags": tags,
                },
                step_update_feedback_params.StepUpdateFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Step,
        )


class AsyncStepsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStepsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStepsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStepsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncStepsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Step:
        """
        Get a step by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._get(
            f"/v1/steps/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Step,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        end_date: Optional[str] | Omit = omit,
        feedback: Optional[Literal["positive", "negative"]] | Omit = omit,
        has_feedback: Optional[bool] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        model: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        trace_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        x_project: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StepListResponse:
        """
        List steps with optional pagination and date filters.

        Args:
          after: Return steps after this step ID

          agent_id: Filter by the ID of the agent that performed the step

          before: Return steps before this step ID

          end_date: Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

          feedback: Filter by feedback

          has_feedback: Filter by whether steps have feedback (true) or not (false)

          limit: Maximum number of steps to return

          model: Filter by the name of the model used for the step

          order: Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          project_id: Filter by the project ID that is associated with the step (cloud only).

          start_date: Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

          tags: Filter by tags

          trace_ids: Filter by trace ids returned by the server

          x_project: Filter by project slug to associate with the group (cloud only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Project": x_project}), **(extra_headers or {})}
        return await self._get(
            "/v1/steps/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "agent_id": agent_id,
                        "before": before,
                        "end_date": end_date,
                        "feedback": feedback,
                        "has_feedback": has_feedback,
                        "limit": limit,
                        "model": model,
                        "order": order,
                        "order_by": order_by,
                        "project_id": project_id,
                        "start_date": start_date,
                        "tags": tags,
                        "trace_ids": trace_ids,
                    },
                    step_list_params.StepListParams,
                ),
            ),
            cast_to=StepListResponse,
        )

    async def list_messages(
        self,
        step_id: str,
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
    ) -> StepListMessagesResponse:
        """List messages for a given step.

        Args:
          after: Message ID cursor for pagination.

        Returns messages that come after this message
              ID in the specified sort order

          before: Message ID cursor for pagination. Returns messages that come before this message
              ID in the specified sort order

          limit: Maximum number of messages to return

          order: Sort order for messages by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Sort by field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._get(
            f"/v1/steps/{step_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    step_list_messages_params.StepListMessagesParams,
                ),
            ),
            cast_to=StepListMessagesResponse,
        )

    async def retrieve_metrics(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StepRetrieveMetricsResponse:
        """
        Get step metrics by step ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._get(
            f"/v1/steps/{step_id}/metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StepRetrieveMetricsResponse,
        )

    async def retrieve_trace(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ProviderTrace]:
        """
        Retrieve Trace For Step

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._get(
            f"/v1/steps/{step_id}/trace",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderTrace,
        )

    async def update_feedback(
        self,
        step_id: str,
        *,
        feedback: Optional[Literal["positive", "negative"]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Step:
        """
        Modify feedback for a given step.

        Args:
          feedback: Whether this feedback is positive or negative

          tags: Feedback tags to add to the step

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._patch(
            f"/v1/steps/{step_id}/feedback",
            body=await async_maybe_transform(
                {
                    "feedback": feedback,
                    "tags": tags,
                },
                step_update_feedback_params.StepUpdateFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Step,
        )


class StepsResourceWithRawResponse:
    def __init__(self, steps: StepsResource) -> None:
        self._steps = steps

        self.retrieve = to_raw_response_wrapper(
            steps.retrieve,
        )
        self.list = to_raw_response_wrapper(
            steps.list,
        )
        self.list_messages = to_raw_response_wrapper(
            steps.list_messages,
        )
        self.retrieve_metrics = to_raw_response_wrapper(
            steps.retrieve_metrics,
        )
        self.retrieve_trace = to_raw_response_wrapper(
            steps.retrieve_trace,
        )
        self.update_feedback = to_raw_response_wrapper(
            steps.update_feedback,
        )


class AsyncStepsResourceWithRawResponse:
    def __init__(self, steps: AsyncStepsResource) -> None:
        self._steps = steps

        self.retrieve = async_to_raw_response_wrapper(
            steps.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            steps.list,
        )
        self.list_messages = async_to_raw_response_wrapper(
            steps.list_messages,
        )
        self.retrieve_metrics = async_to_raw_response_wrapper(
            steps.retrieve_metrics,
        )
        self.retrieve_trace = async_to_raw_response_wrapper(
            steps.retrieve_trace,
        )
        self.update_feedback = async_to_raw_response_wrapper(
            steps.update_feedback,
        )


class StepsResourceWithStreamingResponse:
    def __init__(self, steps: StepsResource) -> None:
        self._steps = steps

        self.retrieve = to_streamed_response_wrapper(
            steps.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            steps.list,
        )
        self.list_messages = to_streamed_response_wrapper(
            steps.list_messages,
        )
        self.retrieve_metrics = to_streamed_response_wrapper(
            steps.retrieve_metrics,
        )
        self.retrieve_trace = to_streamed_response_wrapper(
            steps.retrieve_trace,
        )
        self.update_feedback = to_streamed_response_wrapper(
            steps.update_feedback,
        )


class AsyncStepsResourceWithStreamingResponse:
    def __init__(self, steps: AsyncStepsResource) -> None:
        self._steps = steps

        self.retrieve = async_to_streamed_response_wrapper(
            steps.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            steps.list,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            steps.list_messages,
        )
        self.retrieve_metrics = async_to_streamed_response_wrapper(
            steps.retrieve_metrics,
        )
        self.retrieve_trace = async_to_streamed_response_wrapper(
            steps.retrieve_trace,
        )
        self.update_feedback = async_to_streamed_response_wrapper(
            steps.update_feedback,
        )
