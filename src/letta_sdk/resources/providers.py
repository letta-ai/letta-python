# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    ProviderType,
    provider_list_params,
    provider_check_params,
    provider_create_params,
    provider_update_params,
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
from ..types.provider import Provider
from ..types.provider_type import ProviderType
from ..types.provider_list_response import ProviderListResponse

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        api_key: str,
        name: str,
        provider_type: ProviderType,
        access_key: Optional[str] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Create a new custom provider.

        Args:
          api_key: API key or secret key used for requests to the provider.

          name: The name of the provider.

          provider_type: The type of the provider.

          access_key: Access key used for requests to the provider.

          api_version: API version used for requests to the provider.

          base_url: Base URL used for requests to the provider.

          region: Region used for requests to the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/providers/",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "name": name,
                    "provider_type": provider_type,
                    "access_key": access_key,
                    "api_version": api_version,
                    "base_url": base_url,
                    "region": region,
                },
                provider_create_params.ProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    def retrieve(
        self,
        provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Get a provider by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._get(
            f"/v1/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    def update(
        self,
        provider_id: str,
        *,
        api_key: str,
        access_key: Optional[str] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Update an existing custom provider.

        Args:
          api_key: API key or secret key used for requests to the provider.

          access_key: Access key used for requests to the provider.

          api_version: API version used for requests to the provider.

          base_url: Base URL used for requests to the provider.

          region: Region used for requests to the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._patch(
            f"/v1/providers/{provider_id}",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "access_key": access_key,
                    "api_version": api_version,
                    "base_url": base_url,
                    "region": region,
                },
                provider_update_params.ProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        provider_type: Optional[ProviderType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """
        Get a list of all custom providers.

        Args:
          after: Provider ID cursor for pagination. Returns providers that come after this
              provider ID in the specified sort order

          before: Provider ID cursor for pagination. Returns providers that come before this
              provider ID in the specified sort order

          limit: Maximum number of providers to return

          name: Filter providers by name

          order: Sort order for providers by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          provider_type: Filter providers by type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/providers/",
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
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                        "provider_type": provider_type,
                    },
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )

    def delete(
        self,
        provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete an existing custom provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._delete(
            f"/v1/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def check(
        self,
        *,
        api_key: str,
        provider_type: ProviderType,
        access_key: Optional[str] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Verify the API key and additional parameters for a provider.

        Args:
          api_key: API key or secret key used for requests to the provider.

          provider_type: The type of the provider.

          access_key: Access key used for requests to the provider.

          api_version: API version used for requests to the provider.

          base_url: Base URL used for requests to the provider.

          region: Region used for requests to the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/providers/check",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "provider_type": provider_type,
                    "access_key": access_key,
                    "api_version": api_version,
                    "base_url": base_url,
                    "region": region,
                },
                provider_check_params.ProviderCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        api_key: str,
        name: str,
        provider_type: ProviderType,
        access_key: Optional[str] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Create a new custom provider.

        Args:
          api_key: API key or secret key used for requests to the provider.

          name: The name of the provider.

          provider_type: The type of the provider.

          access_key: Access key used for requests to the provider.

          api_version: API version used for requests to the provider.

          base_url: Base URL used for requests to the provider.

          region: Region used for requests to the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/providers/",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "name": name,
                    "provider_type": provider_type,
                    "access_key": access_key,
                    "api_version": api_version,
                    "base_url": base_url,
                    "region": region,
                },
                provider_create_params.ProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    async def retrieve(
        self,
        provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Get a provider by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._get(
            f"/v1/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    async def update(
        self,
        provider_id: str,
        *,
        api_key: str,
        access_key: Optional[str] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Provider:
        """
        Update an existing custom provider.

        Args:
          api_key: API key or secret key used for requests to the provider.

          access_key: Access key used for requests to the provider.

          api_version: API version used for requests to the provider.

          base_url: Base URL used for requests to the provider.

          region: Region used for requests to the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._patch(
            f"/v1/providers/{provider_id}",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "access_key": access_key,
                    "api_version": api_version,
                    "base_url": base_url,
                    "region": region,
                },
                provider_update_params.ProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        provider_type: Optional[ProviderType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """
        Get a list of all custom providers.

        Args:
          after: Provider ID cursor for pagination. Returns providers that come after this
              provider ID in the specified sort order

          before: Provider ID cursor for pagination. Returns providers that come before this
              provider ID in the specified sort order

          limit: Maximum number of providers to return

          name: Filter providers by name

          order: Sort order for providers by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          provider_type: Filter providers by type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/providers/",
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
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                        "provider_type": provider_type,
                    },
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )

    async def delete(
        self,
        provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete an existing custom provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._delete(
            f"/v1/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def check(
        self,
        *,
        api_key: str,
        provider_type: ProviderType,
        access_key: Optional[str] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Verify the API key and additional parameters for a provider.

        Args:
          api_key: API key or secret key used for requests to the provider.

          provider_type: The type of the provider.

          access_key: Access key used for requests to the provider.

          api_version: API version used for requests to the provider.

          base_url: Base URL used for requests to the provider.

          region: Region used for requests to the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/providers/check",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "provider_type": provider_type,
                    "access_key": access_key,
                    "api_version": api_version,
                    "base_url": base_url,
                    "region": region,
                },
                provider_check_params.ProviderCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.create = to_raw_response_wrapper(
            providers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            providers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            providers.update,
        )
        self.list = to_raw_response_wrapper(
            providers.list,
        )
        self.delete = to_raw_response_wrapper(
            providers.delete,
        )
        self.check = to_raw_response_wrapper(
            providers.check,
        )


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.create = async_to_raw_response_wrapper(
            providers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            providers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            providers.update,
        )
        self.list = async_to_raw_response_wrapper(
            providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            providers.delete,
        )
        self.check = async_to_raw_response_wrapper(
            providers.check,
        )


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.create = to_streamed_response_wrapper(
            providers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            providers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            providers.update,
        )
        self.list = to_streamed_response_wrapper(
            providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            providers.delete,
        )
        self.check = to_streamed_response_wrapper(
            providers.check,
        )


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.create = async_to_streamed_response_wrapper(
            providers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            providers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            providers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            providers.delete,
        )
        self.check = async_to_streamed_response_wrapper(
            providers.check,
        )
