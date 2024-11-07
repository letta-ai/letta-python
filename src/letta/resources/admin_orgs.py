# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import admin_org_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.admin_org_list_response import AdminOrgListResponse

__all__ = ["AdminOrgsResource", "AsyncAdminOrgsResource"]


class AdminOrgsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdminOrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AdminOrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminOrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AdminOrgsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminOrgListResponse:
        """
        Get a list of all orgs in the database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/admin/orgs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    admin_org_list_params.AdminOrgListParams,
                ),
            ),
            cast_to=AdminOrgListResponse,
        )


class AsyncAdminOrgsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdminOrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminOrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminOrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncAdminOrgsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminOrgListResponse:
        """
        Get a list of all orgs in the database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/admin/orgs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    admin_org_list_params.AdminOrgListParams,
                ),
            ),
            cast_to=AdminOrgListResponse,
        )


class AdminOrgsResourceWithRawResponse:
    def __init__(self, admin_orgs: AdminOrgsResource) -> None:
        self._admin_orgs = admin_orgs

        self.list = to_raw_response_wrapper(
            admin_orgs.list,
        )


class AsyncAdminOrgsResourceWithRawResponse:
    def __init__(self, admin_orgs: AsyncAdminOrgsResource) -> None:
        self._admin_orgs = admin_orgs

        self.list = async_to_raw_response_wrapper(
            admin_orgs.list,
        )


class AdminOrgsResourceWithStreamingResponse:
    def __init__(self, admin_orgs: AdminOrgsResource) -> None:
        self._admin_orgs = admin_orgs

        self.list = to_streamed_response_wrapper(
            admin_orgs.list,
        )


class AsyncAdminOrgsResourceWithStreamingResponse:
    def __init__(self, admin_orgs: AsyncAdminOrgsResource) -> None:
        self._admin_orgs = admin_orgs

        self.list = async_to_streamed_response_wrapper(
            admin_orgs.list,
        )
