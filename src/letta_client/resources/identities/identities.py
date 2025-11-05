# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from .agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)
from .blocks import (
    BlocksResource,
    AsyncBlocksResource,
    BlocksResourceWithRawResponse,
    AsyncBlocksResourceWithRawResponse,
    BlocksResourceWithStreamingResponse,
    AsyncBlocksResourceWithStreamingResponse,
)
from ...types import (
    IdentityType,
    identity_list_params,
    identity_create_params,
    identity_modify_params,
    identity_upsert_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .properties import (
    PropertiesResource,
    AsyncPropertiesResource,
    PropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
    AsyncPropertiesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncArrayPage, AsyncArrayPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.identity import Identity
from ...types.identity_type import IdentityType
from ...types.identity_count_response import IdentityCountResponse
from ...types.identity_property_param import IdentityPropertyParam

__all__ = ["IdentitiesResource", "AsyncIdentitiesResource"]


class IdentitiesResource(SyncAPIResource):
    @cached_property
    def properties(self) -> PropertiesResource:
        return PropertiesResource(self._client)

    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

    @cached_property
    def blocks(self) -> BlocksResource:
        return BlocksResource(self._client)

    @cached_property
    def with_raw_response(self) -> IdentitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return IdentitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return IdentitiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        identifier_key: str,
        identity_type: IdentityType,
        name: str,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        properties: Optional[Iterable[IdentityPropertyParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identity:
        """
        Create Identity

        Args:
          identifier_key: External, user-generated identifier key of the identity.

          identity_type: The type of the identity.

          name: The name of the identity.

          agent_ids: The agent ids that are associated with the identity.

          block_ids: The IDs of the blocks associated with the identity.

          project_id: The project id of the identity, if applicable.

          properties: List of properties associated with the identity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/identities/",
            body=maybe_transform(
                {
                    "identifier_key": identifier_key,
                    "identity_type": identity_type,
                    "name": name,
                    "agent_ids": agent_ids,
                    "block_ids": block_ids,
                    "project_id": project_id,
                    "properties": properties,
                },
                identity_create_params.IdentityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identity,
        )

    def retrieve(
        self,
        identity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identity:
        """
        Retrieve Identity

        Args:
          identity_id: The ID of the identity in the format 'identity-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return self._get(
            f"/v1/identities/{identity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identity,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        identifier_key: Optional[str] | Omit = omit,
        identity_type: Optional[IdentityType] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncArrayPage[Identity]:
        """
        Get a list of all identities in the database

        Args:
          after: Identity ID cursor for pagination. Returns identities that come after this
              identity ID in the specified sort order

          before: Identity ID cursor for pagination. Returns identities that come before this
              identity ID in the specified sort order

          identity_type: Enum to represent the type of the identity.

          limit: Maximum number of identities to return

          order: Sort order for identities by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/identities/",
            page=SyncArrayPage[Identity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "identifier_key": identifier_key,
                        "identity_type": identity_type,
                        "limit": limit,
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                        "project_id": project_id,
                    },
                    identity_list_params.IdentityListParams,
                ),
            ),
            model=Identity,
        )

    def delete(
        self,
        identity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete an identity by its identifier key

        Args:
          identity_id: The ID of the identity in the format 'identity-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return self._delete(
            f"/v1/identities/{identity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityCountResponse:
        """Get count of all identities for a user"""
        return self._get(
            "/v1/identities/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    def modify(
        self,
        identity_id: str,
        *,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        identifier_key: Optional[str] | Omit = omit,
        identity_type: Optional[IdentityType] | Omit = omit,
        name: Optional[str] | Omit = omit,
        properties: Optional[Iterable[IdentityPropertyParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identity:
        """
        Modify Identity

        Args:
          identity_id: The ID of the identity in the format 'identity-<uuid4>'

          agent_ids: The agent ids that are associated with the identity.

          block_ids: The IDs of the blocks associated with the identity.

          identifier_key: External, user-generated identifier key of the identity.

          identity_type: Enum to represent the type of the identity.

          name: The name of the identity.

          properties: List of properties associated with the identity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return self._patch(
            f"/v1/identities/{identity_id}",
            body=maybe_transform(
                {
                    "agent_ids": agent_ids,
                    "block_ids": block_ids,
                    "identifier_key": identifier_key,
                    "identity_type": identity_type,
                    "name": name,
                    "properties": properties,
                },
                identity_modify_params.IdentityModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identity,
        )

    def upsert(
        self,
        *,
        identifier_key: str,
        identity_type: IdentityType,
        name: str,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        properties: Optional[Iterable[IdentityPropertyParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identity:
        """
        Upsert Identity

        Args:
          identifier_key: External, user-generated identifier key of the identity.

          identity_type: The type of the identity.

          name: The name of the identity.

          agent_ids: The agent ids that are associated with the identity.

          block_ids: The IDs of the blocks associated with the identity.

          project_id: The project id of the identity, if applicable.

          properties: List of properties associated with the identity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/identities/",
            body=maybe_transform(
                {
                    "identifier_key": identifier_key,
                    "identity_type": identity_type,
                    "name": name,
                    "agent_ids": agent_ids,
                    "block_ids": block_ids,
                    "project_id": project_id,
                    "properties": properties,
                },
                identity_upsert_params.IdentityUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identity,
        )


class AsyncIdentitiesResource(AsyncAPIResource):
    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        return AsyncPropertiesResource(self._client)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

    @cached_property
    def blocks(self) -> AsyncBlocksResource:
        return AsyncBlocksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIdentitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncIdentitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        identifier_key: str,
        identity_type: IdentityType,
        name: str,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        properties: Optional[Iterable[IdentityPropertyParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identity:
        """
        Create Identity

        Args:
          identifier_key: External, user-generated identifier key of the identity.

          identity_type: The type of the identity.

          name: The name of the identity.

          agent_ids: The agent ids that are associated with the identity.

          block_ids: The IDs of the blocks associated with the identity.

          project_id: The project id of the identity, if applicable.

          properties: List of properties associated with the identity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/identities/",
            body=await async_maybe_transform(
                {
                    "identifier_key": identifier_key,
                    "identity_type": identity_type,
                    "name": name,
                    "agent_ids": agent_ids,
                    "block_ids": block_ids,
                    "project_id": project_id,
                    "properties": properties,
                },
                identity_create_params.IdentityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identity,
        )

    async def retrieve(
        self,
        identity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identity:
        """
        Retrieve Identity

        Args:
          identity_id: The ID of the identity in the format 'identity-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return await self._get(
            f"/v1/identities/{identity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identity,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        identifier_key: Optional[str] | Omit = omit,
        identity_type: Optional[IdentityType] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Identity, AsyncArrayPage[Identity]]:
        """
        Get a list of all identities in the database

        Args:
          after: Identity ID cursor for pagination. Returns identities that come after this
              identity ID in the specified sort order

          before: Identity ID cursor for pagination. Returns identities that come before this
              identity ID in the specified sort order

          identity_type: Enum to represent the type of the identity.

          limit: Maximum number of identities to return

          order: Sort order for identities by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/identities/",
            page=AsyncArrayPage[Identity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "identifier_key": identifier_key,
                        "identity_type": identity_type,
                        "limit": limit,
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                        "project_id": project_id,
                    },
                    identity_list_params.IdentityListParams,
                ),
            ),
            model=Identity,
        )

    async def delete(
        self,
        identity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete an identity by its identifier key

        Args:
          identity_id: The ID of the identity in the format 'identity-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return await self._delete(
            f"/v1/identities/{identity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityCountResponse:
        """Get count of all identities for a user"""
        return await self._get(
            "/v1/identities/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    async def modify(
        self,
        identity_id: str,
        *,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        identifier_key: Optional[str] | Omit = omit,
        identity_type: Optional[IdentityType] | Omit = omit,
        name: Optional[str] | Omit = omit,
        properties: Optional[Iterable[IdentityPropertyParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identity:
        """
        Modify Identity

        Args:
          identity_id: The ID of the identity in the format 'identity-<uuid4>'

          agent_ids: The agent ids that are associated with the identity.

          block_ids: The IDs of the blocks associated with the identity.

          identifier_key: External, user-generated identifier key of the identity.

          identity_type: Enum to represent the type of the identity.

          name: The name of the identity.

          properties: List of properties associated with the identity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return await self._patch(
            f"/v1/identities/{identity_id}",
            body=await async_maybe_transform(
                {
                    "agent_ids": agent_ids,
                    "block_ids": block_ids,
                    "identifier_key": identifier_key,
                    "identity_type": identity_type,
                    "name": name,
                    "properties": properties,
                },
                identity_modify_params.IdentityModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identity,
        )

    async def upsert(
        self,
        *,
        identifier_key: str,
        identity_type: IdentityType,
        name: str,
        agent_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        block_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        properties: Optional[Iterable[IdentityPropertyParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identity:
        """
        Upsert Identity

        Args:
          identifier_key: External, user-generated identifier key of the identity.

          identity_type: The type of the identity.

          name: The name of the identity.

          agent_ids: The agent ids that are associated with the identity.

          block_ids: The IDs of the blocks associated with the identity.

          project_id: The project id of the identity, if applicable.

          properties: List of properties associated with the identity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/identities/",
            body=await async_maybe_transform(
                {
                    "identifier_key": identifier_key,
                    "identity_type": identity_type,
                    "name": name,
                    "agent_ids": agent_ids,
                    "block_ids": block_ids,
                    "project_id": project_id,
                    "properties": properties,
                },
                identity_upsert_params.IdentityUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identity,
        )


class IdentitiesResourceWithRawResponse:
    def __init__(self, identities: IdentitiesResource) -> None:
        self._identities = identities

        self.create = to_raw_response_wrapper(
            identities.create,
        )
        self.retrieve = to_raw_response_wrapper(
            identities.retrieve,
        )
        self.list = to_raw_response_wrapper(
            identities.list,
        )
        self.delete = to_raw_response_wrapper(
            identities.delete,
        )
        self.count = to_raw_response_wrapper(
            identities.count,
        )
        self.modify = to_raw_response_wrapper(
            identities.modify,
        )
        self.upsert = to_raw_response_wrapper(
            identities.upsert,
        )

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        return PropertiesResourceWithRawResponse(self._identities.properties)

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._identities.agents)

    @cached_property
    def blocks(self) -> BlocksResourceWithRawResponse:
        return BlocksResourceWithRawResponse(self._identities.blocks)


class AsyncIdentitiesResourceWithRawResponse:
    def __init__(self, identities: AsyncIdentitiesResource) -> None:
        self._identities = identities

        self.create = async_to_raw_response_wrapper(
            identities.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            identities.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            identities.list,
        )
        self.delete = async_to_raw_response_wrapper(
            identities.delete,
        )
        self.count = async_to_raw_response_wrapper(
            identities.count,
        )
        self.modify = async_to_raw_response_wrapper(
            identities.modify,
        )
        self.upsert = async_to_raw_response_wrapper(
            identities.upsert,
        )

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        return AsyncPropertiesResourceWithRawResponse(self._identities.properties)

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._identities.agents)

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithRawResponse:
        return AsyncBlocksResourceWithRawResponse(self._identities.blocks)


class IdentitiesResourceWithStreamingResponse:
    def __init__(self, identities: IdentitiesResource) -> None:
        self._identities = identities

        self.create = to_streamed_response_wrapper(
            identities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            identities.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            identities.list,
        )
        self.delete = to_streamed_response_wrapper(
            identities.delete,
        )
        self.count = to_streamed_response_wrapper(
            identities.count,
        )
        self.modify = to_streamed_response_wrapper(
            identities.modify,
        )
        self.upsert = to_streamed_response_wrapper(
            identities.upsert,
        )

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        return PropertiesResourceWithStreamingResponse(self._identities.properties)

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._identities.agents)

    @cached_property
    def blocks(self) -> BlocksResourceWithStreamingResponse:
        return BlocksResourceWithStreamingResponse(self._identities.blocks)


class AsyncIdentitiesResourceWithStreamingResponse:
    def __init__(self, identities: AsyncIdentitiesResource) -> None:
        self._identities = identities

        self.create = async_to_streamed_response_wrapper(
            identities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            identities.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            identities.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            identities.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            identities.count,
        )
        self.modify = async_to_streamed_response_wrapper(
            identities.modify,
        )
        self.upsert = async_to_streamed_response_wrapper(
            identities.upsert,
        )

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        return AsyncPropertiesResourceWithStreamingResponse(self._identities.properties)

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._identities.agents)

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithStreamingResponse:
        return AsyncBlocksResourceWithStreamingResponse(self._identities.blocks)
