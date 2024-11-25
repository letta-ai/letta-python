# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import archival_create_params, archival_retrieve_params
from ...types.agents.archival_create_response import ArchivalCreateResponse
from ...types.agents.archival_retrieve_response import ArchivalRetrieveResponse

__all__ = ["ArchivalResource", "AsyncArchivalResource"]


class ArchivalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArchivalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return ArchivalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArchivalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return ArchivalResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        text: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArchivalCreateResponse:
        """
        Insert a memory into an agent's archival memory store.

        Args:
          text: Text to write to archival memory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._post(
            f"/v1/agents/{agent_id}/archival",
            body=maybe_transform({"text": text}, archival_create_params.ArchivalCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArchivalCreateResponse,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        after: Optional[int] | NotGiven = NOT_GIVEN,
        before: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArchivalRetrieveResponse:
        """
        Retrieve the memories in an agent's archival memory store (paginated query).

        Args:
          after: Unique ID of the memory to start the query range at.

          before: Unique ID of the memory to end the query range at.

          limit: How many results to include in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._get(
            f"/v1/agents/{agent_id}/archival",
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
                    },
                    archival_retrieve_params.ArchivalRetrieveParams,
                ),
            ),
            cast_to=ArchivalRetrieveResponse,
        )

    def delete(
        self,
        memory_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a memory from an agent's archival memory store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return self._delete(
            f"/v1/agents/{agent_id}/archival/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncArchivalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArchivalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArchivalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArchivalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncArchivalResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        text: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArchivalCreateResponse:
        """
        Insert a memory into an agent's archival memory store.

        Args:
          text: Text to write to archival memory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._post(
            f"/v1/agents/{agent_id}/archival",
            body=await async_maybe_transform({"text": text}, archival_create_params.ArchivalCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArchivalCreateResponse,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        after: Optional[int] | NotGiven = NOT_GIVEN,
        before: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArchivalRetrieveResponse:
        """
        Retrieve the memories in an agent's archival memory store (paginated query).

        Args:
          after: Unique ID of the memory to start the query range at.

          before: Unique ID of the memory to end the query range at.

          limit: How many results to include in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._get(
            f"/v1/agents/{agent_id}/archival",
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
                    },
                    archival_retrieve_params.ArchivalRetrieveParams,
                ),
            ),
            cast_to=ArchivalRetrieveResponse,
        )

    async def delete(
        self,
        memory_id: str,
        *,
        agent_id: str,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a memory from an agent's archival memory store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        extra_headers = {**strip_not_given({"user_id": user_id}), **(extra_headers or {})}
        return await self._delete(
            f"/v1/agents/{agent_id}/archival/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ArchivalResourceWithRawResponse:
    def __init__(self, archival: ArchivalResource) -> None:
        self._archival = archival

        self.create = to_raw_response_wrapper(
            archival.create,
        )
        self.retrieve = to_raw_response_wrapper(
            archival.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            archival.delete,
        )


class AsyncArchivalResourceWithRawResponse:
    def __init__(self, archival: AsyncArchivalResource) -> None:
        self._archival = archival

        self.create = async_to_raw_response_wrapper(
            archival.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            archival.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            archival.delete,
        )


class ArchivalResourceWithStreamingResponse:
    def __init__(self, archival: ArchivalResource) -> None:
        self._archival = archival

        self.create = to_streamed_response_wrapper(
            archival.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            archival.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            archival.delete,
        )


class AsyncArchivalResourceWithStreamingResponse:
    def __init__(self, archival: AsyncArchivalResource) -> None:
        self._archival = archival

        self.create = async_to_streamed_response_wrapper(
            archival.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            archival.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            archival.delete,
        )
