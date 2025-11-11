# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["ArchivesResource", "AsyncArchivesResource"]


class ArchivesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArchivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ArchivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArchivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ArchivesResourceWithStreamingResponse(self)

    def attach(
        self,
        archive_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Attach an archive to an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/archives/attach/{archive_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def detach(
        self,
        archive_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Detach an archive from an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/archives/detach/{archive_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncArchivesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArchivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArchivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArchivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncArchivesResourceWithStreamingResponse(self)

    async def attach(
        self,
        archive_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Attach an archive to an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/archives/attach/{archive_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def detach(
        self,
        archive_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Detach an archive from an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not archive_id:
            raise ValueError(f"Expected a non-empty value for `archive_id` but received {archive_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/archives/detach/{archive_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ArchivesResourceWithRawResponse:
    def __init__(self, archives: ArchivesResource) -> None:
        self._archives = archives

        self.attach = to_raw_response_wrapper(
            archives.attach,
        )
        self.detach = to_raw_response_wrapper(
            archives.detach,
        )


class AsyncArchivesResourceWithRawResponse:
    def __init__(self, archives: AsyncArchivesResource) -> None:
        self._archives = archives

        self.attach = async_to_raw_response_wrapper(
            archives.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            archives.detach,
        )


class ArchivesResourceWithStreamingResponse:
    def __init__(self, archives: ArchivesResource) -> None:
        self._archives = archives

        self.attach = to_streamed_response_wrapper(
            archives.attach,
        )
        self.detach = to_streamed_response_wrapper(
            archives.detach,
        )


class AsyncArchivesResourceWithStreamingResponse:
    def __init__(self, archives: AsyncArchivesResource) -> None:
        self._archives = archives

        self.attach = async_to_streamed_response_wrapper(
            archives.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            archives.detach,
        )
