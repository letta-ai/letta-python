# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import admin_organization_create_params, admin_organization_delete_params
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
from ..types.organization import Organization

__all__ = ["AdminOrganizationsResource", "AsyncAdminOrganizationsResource"]


class AdminOrganizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdminOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AdminOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AdminOrganizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """
        Create a new org in the database

        Args:
          name: The name of the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/admin/orgs/",
            body=maybe_transform({"name": name}, admin_organization_create_params.AdminOrganizationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    def delete(
        self,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """
        Delete Org

        Args:
          org_id: The org_id key to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/admin/orgs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"org_id": org_id}, admin_organization_delete_params.AdminOrganizationDeleteParams
                ),
            ),
            cast_to=Organization,
        )


class AsyncAdminOrganizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdminOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncAdminOrganizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """
        Create a new org in the database

        Args:
          name: The name of the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/admin/orgs/",
            body=await async_maybe_transform(
                {"name": name}, admin_organization_create_params.AdminOrganizationCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    async def delete(
        self,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """
        Delete Org

        Args:
          org_id: The org_id key to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/admin/orgs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"org_id": org_id}, admin_organization_delete_params.AdminOrganizationDeleteParams
                ),
            ),
            cast_to=Organization,
        )


class AdminOrganizationsResourceWithRawResponse:
    def __init__(self, admin_organizations: AdminOrganizationsResource) -> None:
        self._admin_organizations = admin_organizations

        self.create = to_raw_response_wrapper(
            admin_organizations.create,
        )
        self.delete = to_raw_response_wrapper(
            admin_organizations.delete,
        )


class AsyncAdminOrganizationsResourceWithRawResponse:
    def __init__(self, admin_organizations: AsyncAdminOrganizationsResource) -> None:
        self._admin_organizations = admin_organizations

        self.create = async_to_raw_response_wrapper(
            admin_organizations.create,
        )
        self.delete = async_to_raw_response_wrapper(
            admin_organizations.delete,
        )


class AdminOrganizationsResourceWithStreamingResponse:
    def __init__(self, admin_organizations: AdminOrganizationsResource) -> None:
        self._admin_organizations = admin_organizations

        self.create = to_streamed_response_wrapper(
            admin_organizations.create,
        )
        self.delete = to_streamed_response_wrapper(
            admin_organizations.delete,
        )


class AsyncAdminOrganizationsResourceWithStreamingResponse:
    def __init__(self, admin_organizations: AsyncAdminOrganizationsResource) -> None:
        self._admin_organizations = admin_organizations

        self.create = async_to_streamed_response_wrapper(
            admin_organizations.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            admin_organizations.delete,
        )
