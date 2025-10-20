# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Optional

import httpx

from ..types import job_list_params, job_list_active_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.job import Job
from .._base_client import make_request_options
from ..types.job_list_response import JobListResponse
from ..types.job_list_active_response import JobListActiveResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Get the status of a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    def list(
        self,
        *,
        active: bool | Omit = omit,
        after: Optional[str] | Omit = omit,
        ascending: bool | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """
        List all jobs.

        Args:
          active: Filter for active jobs.

          after: Cursor for pagination

          ascending: Whether to sort jobs oldest to newest (True, default) or newest to oldest
              (False)

          before: Cursor for pagination

          limit: Limit for pagination

          source_id: Only list jobs associated with the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/jobs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "after": after,
                        "ascending": ascending,
                        "before": before,
                        "limit": limit,
                        "source_id": source_id,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    def delete(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Delete a job by its job_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/v1/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    def cancel(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Cancel a job by its job_id.

        This endpoint marks a job as cancelled, which will cause any associated agent
        execution to terminate as soon as possible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._patch(
            f"/v1/jobs/{job_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    @typing_extensions.deprecated("deprecated")
    def list_active(
        self,
        *,
        after: Optional[str] | Omit = omit,
        ascending: bool | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListActiveResponse:
        """
        List all active jobs.

        Args:
          after: Cursor for pagination

          ascending: Whether to sort jobs oldest to newest (True, default) or newest to oldest
              (False)

          before: Cursor for pagination

          limit: Limit for pagination

          source_id: Only list jobs associated with the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/jobs/active",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "ascending": ascending,
                        "before": before,
                        "limit": limit,
                        "source_id": source_id,
                    },
                    job_list_active_params.JobListActiveParams,
                ),
            ),
            cast_to=JobListActiveResponse,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Get the status of a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    async def list(
        self,
        *,
        active: bool | Omit = omit,
        after: Optional[str] | Omit = omit,
        ascending: bool | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """
        List all jobs.

        Args:
          active: Filter for active jobs.

          after: Cursor for pagination

          ascending: Whether to sort jobs oldest to newest (True, default) or newest to oldest
              (False)

          before: Cursor for pagination

          limit: Limit for pagination

          source_id: Only list jobs associated with the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/jobs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "after": after,
                        "ascending": ascending,
                        "before": before,
                        "limit": limit,
                        "source_id": source_id,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    async def delete(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Delete a job by its job_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/v1/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    async def cancel(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Job:
        """
        Cancel a job by its job_id.

        This endpoint marks a job as cancelled, which will cause any associated agent
        execution to terminate as soon as possible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._patch(
            f"/v1/jobs/{job_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )

    @typing_extensions.deprecated("deprecated")
    async def list_active(
        self,
        *,
        after: Optional[str] | Omit = omit,
        ascending: bool | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListActiveResponse:
        """
        List all active jobs.

        Args:
          after: Cursor for pagination

          ascending: Whether to sort jobs oldest to newest (True, default) or newest to oldest
              (False)

          before: Cursor for pagination

          limit: Limit for pagination

          source_id: Only list jobs associated with the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/jobs/active",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "ascending": ascending,
                        "before": before,
                        "limit": limit,
                        "source_id": source_id,
                    },
                    job_list_active_params.JobListActiveParams,
                ),
            ),
            cast_to=JobListActiveResponse,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.delete = to_raw_response_wrapper(
            jobs.delete,
        )
        self.cancel = to_raw_response_wrapper(
            jobs.cancel,
        )
        self.list_active = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                jobs.list_active,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            jobs.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            jobs.cancel,
        )
        self.list_active = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                jobs.list_active,  # pyright: ignore[reportDeprecated],
            )
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete = to_streamed_response_wrapper(
            jobs.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            jobs.cancel,
        )
        self.list_active = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                jobs.list_active,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            jobs.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            jobs.cancel,
        )
        self.list_active = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                jobs.list_active,  # pyright: ignore[reportDeprecated],
            )
        )
