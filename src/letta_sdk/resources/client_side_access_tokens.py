# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    client_side_access_token_list_params,
    client_side_access_token_create_params,
    client_side_access_token_delete_params,
)
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
from .._base_client import make_request_options
from ..types.client_side_access_token_list_response import ClientSideAccessTokenListResponse
from ..types.client_side_access_token_create_response import ClientSideAccessTokenCreateResponse

__all__ = ["ClientSideAccessTokensResource", "AsyncClientSideAccessTokensResource"]


class ClientSideAccessTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientSideAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ClientSideAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientSideAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return ClientSideAccessTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        hostname: str,
        policy: Iterable[client_side_access_token_create_params.Policy],
        expires_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientSideAccessTokenCreateResponse:
        """
        Create a new client side access token with the specified configuration.

        Args:
          hostname: The hostname of the client side application. Please specify the full URL
              including the protocol (http or https).

          expires_at: The expiration date of the token. If not provided, the token will expire in 5
              minutes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/client-side-access-tokens",
            body=maybe_transform(
                {
                    "hostname": hostname,
                    "policy": policy,
                    "expires_at": expires_at,
                },
                client_side_access_token_create_params.ClientSideAccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientSideAccessTokenCreateResponse,
        )

    def list(
        self,
        *,
        agent_id: str | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientSideAccessTokenListResponse:
        """List all client side access tokens for the current account.

        This is only
        available for cloud users.

        Args:
          agent_id: The agent ID to filter tokens by. If provided, only tokens for this agent will
              be returned.

          limit: The number of tokens to return per page. Defaults to 10.

          offset: The offset for pagination. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/client-side-access-tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    client_side_access_token_list_params.ClientSideAccessTokenListParams,
                ),
            ),
            cast_to=ClientSideAccessTokenListResponse,
        )

    def delete(
        self,
        token: str,
        *,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a client side access token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._delete(
            f"/v1/client-side-access-tokens/{token}",
            body=maybe_transform(body, client_side_access_token_delete_params.ClientSideAccessTokenDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncClientSideAccessTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientSideAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientSideAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientSideAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AsyncClientSideAccessTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        hostname: str,
        policy: Iterable[client_side_access_token_create_params.Policy],
        expires_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientSideAccessTokenCreateResponse:
        """
        Create a new client side access token with the specified configuration.

        Args:
          hostname: The hostname of the client side application. Please specify the full URL
              including the protocol (http or https).

          expires_at: The expiration date of the token. If not provided, the token will expire in 5
              minutes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/client-side-access-tokens",
            body=await async_maybe_transform(
                {
                    "hostname": hostname,
                    "policy": policy,
                    "expires_at": expires_at,
                },
                client_side_access_token_create_params.ClientSideAccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientSideAccessTokenCreateResponse,
        )

    async def list(
        self,
        *,
        agent_id: str | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientSideAccessTokenListResponse:
        """List all client side access tokens for the current account.

        This is only
        available for cloud users.

        Args:
          agent_id: The agent ID to filter tokens by. If provided, only tokens for this agent will
              be returned.

          limit: The number of tokens to return per page. Defaults to 10.

          offset: The offset for pagination. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/client-side-access-tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    client_side_access_token_list_params.ClientSideAccessTokenListParams,
                ),
            ),
            cast_to=ClientSideAccessTokenListResponse,
        )

    async def delete(
        self,
        token: str,
        *,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a client side access token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._delete(
            f"/v1/client-side-access-tokens/{token}",
            body=await async_maybe_transform(
                body, client_side_access_token_delete_params.ClientSideAccessTokenDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ClientSideAccessTokensResourceWithRawResponse:
    def __init__(self, client_side_access_tokens: ClientSideAccessTokensResource) -> None:
        self._client_side_access_tokens = client_side_access_tokens

        self.create = to_raw_response_wrapper(
            client_side_access_tokens.create,
        )
        self.list = to_raw_response_wrapper(
            client_side_access_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            client_side_access_tokens.delete,
        )


class AsyncClientSideAccessTokensResourceWithRawResponse:
    def __init__(self, client_side_access_tokens: AsyncClientSideAccessTokensResource) -> None:
        self._client_side_access_tokens = client_side_access_tokens

        self.create = async_to_raw_response_wrapper(
            client_side_access_tokens.create,
        )
        self.list = async_to_raw_response_wrapper(
            client_side_access_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            client_side_access_tokens.delete,
        )


class ClientSideAccessTokensResourceWithStreamingResponse:
    def __init__(self, client_side_access_tokens: ClientSideAccessTokensResource) -> None:
        self._client_side_access_tokens = client_side_access_tokens

        self.create = to_streamed_response_wrapper(
            client_side_access_tokens.create,
        )
        self.list = to_streamed_response_wrapper(
            client_side_access_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            client_side_access_tokens.delete,
        )


class AsyncClientSideAccessTokensResourceWithStreamingResponse:
    def __init__(self, client_side_access_tokens: AsyncClientSideAccessTokensResource) -> None:
        self._client_side_access_tokens = client_side_access_tokens

        self.create = async_to_streamed_response_wrapper(
            client_side_access_tokens.create,
        )
        self.list = async_to_streamed_response_wrapper(
            client_side_access_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            client_side_access_tokens.delete,
        )
