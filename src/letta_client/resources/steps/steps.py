# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .trace import (
    TraceResource,
    AsyncTraceResource,
    TraceResourceWithRawResponse,
    AsyncTraceResourceWithRawResponse,
    TraceResourceWithStreamingResponse,
    AsyncTraceResourceWithStreamingResponse,
)
from ...types import step_list_params
from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
from .feedback import (
    FeedbackResource,
    AsyncFeedbackResource,
    FeedbackResourceWithRawResponse,
    AsyncFeedbackResourceWithRawResponse,
    FeedbackResourceWithStreamingResponse,
    AsyncFeedbackResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncArrayPage, AsyncArrayPage
from ...types.step import Step
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["StepsResource", "AsyncStepsResource"]


class StepsResource(SyncAPIResource):
    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def trace(self) -> TraceResource:
        return TraceResource(self._client)

    @cached_property
    def feedback(self) -> FeedbackResource:
        return FeedbackResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

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
          step_id: The ID of the step in the format 'step-<uuid4>'

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncArrayPage[Step]:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/steps/",
            page=SyncArrayPage[Step],
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
            model=Step,
        )


class AsyncStepsResource(AsyncAPIResource):
    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def trace(self) -> AsyncTraceResource:
        return AsyncTraceResource(self._client)

    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        return AsyncFeedbackResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

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
          step_id: The ID of the step in the format 'step-<uuid4>'

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Step, AsyncArrayPage[Step]]:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/steps/",
            page=AsyncArrayPage[Step],
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
            model=Step,
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

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._steps.metrics)

    @cached_property
    def trace(self) -> TraceResourceWithRawResponse:
        return TraceResourceWithRawResponse(self._steps.trace)

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        return FeedbackResourceWithRawResponse(self._steps.feedback)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._steps.messages)


class AsyncStepsResourceWithRawResponse:
    def __init__(self, steps: AsyncStepsResource) -> None:
        self._steps = steps

        self.retrieve = async_to_raw_response_wrapper(
            steps.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            steps.list,
        )

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._steps.metrics)

    @cached_property
    def trace(self) -> AsyncTraceResourceWithRawResponse:
        return AsyncTraceResourceWithRawResponse(self._steps.trace)

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        return AsyncFeedbackResourceWithRawResponse(self._steps.feedback)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._steps.messages)


class StepsResourceWithStreamingResponse:
    def __init__(self, steps: StepsResource) -> None:
        self._steps = steps

        self.retrieve = to_streamed_response_wrapper(
            steps.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            steps.list,
        )

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._steps.metrics)

    @cached_property
    def trace(self) -> TraceResourceWithStreamingResponse:
        return TraceResourceWithStreamingResponse(self._steps.trace)

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        return FeedbackResourceWithStreamingResponse(self._steps.feedback)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._steps.messages)


class AsyncStepsResourceWithStreamingResponse:
    def __init__(self, steps: AsyncStepsResource) -> None:
        self._steps = steps

        self.retrieve = async_to_streamed_response_wrapper(
            steps.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            steps.list,
        )

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._steps.metrics)

    @cached_property
    def trace(self) -> AsyncTraceResourceWithStreamingResponse:
        return AsyncTraceResourceWithStreamingResponse(self._steps.trace)

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        return AsyncFeedbackResourceWithStreamingResponse(self._steps.feedback)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._steps.messages)
