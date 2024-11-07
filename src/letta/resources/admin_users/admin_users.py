# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ...types import (
    admin_user_list_params,
    admin_user_create_params,
    admin_user_delete_params,
    admin_user_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
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
from ...types.user import User
from ..._base_client import make_request_options
from ...types.admin_user_list_response import AdminUserListResponse

__all__ = ["AdminUsersResource", "AsyncAdminUsersResource"]


class AdminUsersResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AdminUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AdminUsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Create a new user in the database

        Args:
          name: The name of the user.

          organization_id: The organization id of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/admin/users/",
            body=maybe_transform(
                {
                    "name": name,
                    "organization_id": organization_id,
                },
                admin_user_create_params.AdminUserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def update(
        self,
        *,
        id: str,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        organization_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Update a user in the database

        Args:
          id: The id of the user to update.

          name: The new name of the user.

          organization_id: The new organization id of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/admin/users/",
            body=maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "organization_id": organization_id,
                },
                admin_user_update_params.AdminUserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

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
    ) -> AdminUserListResponse:
        """
        Get a list of all users in the database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/admin/users/",
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
                    admin_user_list_params.AdminUserListParams,
                ),
            ),
            cast_to=AdminUserListResponse,
        )

    def delete(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Delete User

        Args:
          user_id: The user_id key to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/admin/users/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"user_id": user_id}, admin_user_delete_params.AdminUserDeleteParams),
            ),
            cast_to=User,
        )


class AsyncAdminUsersResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncAdminUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Create a new user in the database

        Args:
          name: The name of the user.

          organization_id: The organization id of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/admin/users/",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "organization_id": organization_id,
                },
                admin_user_create_params.AdminUserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def update(
        self,
        *,
        id: str,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        organization_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Update a user in the database

        Args:
          id: The id of the user to update.

          name: The new name of the user.

          organization_id: The new organization id of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/admin/users/",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "organization_id": organization_id,
                },
                admin_user_update_params.AdminUserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

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
    ) -> AdminUserListResponse:
        """
        Get a list of all users in the database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/admin/users/",
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
                    admin_user_list_params.AdminUserListParams,
                ),
            ),
            cast_to=AdminUserListResponse,
        )

    async def delete(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Delete User

        Args:
          user_id: The user_id key to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/admin/users/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"user_id": user_id}, admin_user_delete_params.AdminUserDeleteParams),
            ),
            cast_to=User,
        )


class AdminUsersResourceWithRawResponse:
    def __init__(self, admin_users: AdminUsersResource) -> None:
        self._admin_users = admin_users

        self.create = to_raw_response_wrapper(
            admin_users.create,
        )
        self.update = to_raw_response_wrapper(
            admin_users.update,
        )
        self.list = to_raw_response_wrapper(
            admin_users.list,
        )
        self.delete = to_raw_response_wrapper(
            admin_users.delete,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._admin_users.keys)


class AsyncAdminUsersResourceWithRawResponse:
    def __init__(self, admin_users: AsyncAdminUsersResource) -> None:
        self._admin_users = admin_users

        self.create = async_to_raw_response_wrapper(
            admin_users.create,
        )
        self.update = async_to_raw_response_wrapper(
            admin_users.update,
        )
        self.list = async_to_raw_response_wrapper(
            admin_users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            admin_users.delete,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._admin_users.keys)


class AdminUsersResourceWithStreamingResponse:
    def __init__(self, admin_users: AdminUsersResource) -> None:
        self._admin_users = admin_users

        self.create = to_streamed_response_wrapper(
            admin_users.create,
        )
        self.update = to_streamed_response_wrapper(
            admin_users.update,
        )
        self.list = to_streamed_response_wrapper(
            admin_users.list,
        )
        self.delete = to_streamed_response_wrapper(
            admin_users.delete,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._admin_users.keys)


class AsyncAdminUsersResourceWithStreamingResponse:
    def __init__(self, admin_users: AsyncAdminUsersResource) -> None:
        self._admin_users = admin_users

        self.create = async_to_streamed_response_wrapper(
            admin_users.create,
        )
        self.update = async_to_streamed_response_wrapper(
            admin_users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            admin_users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            admin_users.delete,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._admin_users.keys)
