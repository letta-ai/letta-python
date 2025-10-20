# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    IdentityType,
    identity_list_params,
    identity_create_params,
    identity_modify_params,
    identity_upsert_params,
    identity_list_agents_params,
    identity_list_blocks_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.identity import Identity
from ..types.identity_type import IdentityType
from ..types.identity_list_response import IdentityListResponse
from ..types.identity_count_response import IdentityCountResponse
from ..types.identity_property_param import IdentityPropertyParam
from ..types.identity_list_agents_response import IdentityListAgentsResponse
from ..types.identity_list_blocks_response import IdentityListBlocksResponse

__all__ = ["IdentitiesResource", "AsyncIdentitiesResource"]


class IdentitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return IdentitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
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
        x_project: str | Omit = omit,
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

          x_project: The project slug to associate with the identity (cloud only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Project": x_project}), **(extra_headers or {})}
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
    ) -> IdentityListResponse:
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
        return self._get(
            "/v1/identities/",
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
            cast_to=IdentityListResponse,
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

    def list_agents(
        self,
        identity_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityListAgentsResponse:
        """
        Get all agents associated with the specified identity.

        Args:
          after: Agent ID cursor for pagination. Returns agents that come after this agent ID in
              the specified sort order

          before: Agent ID cursor for pagination. Returns agents that come before this agent ID in
              the specified sort order

          limit: Maximum number of agents to return

          order: Sort order for agents by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return self._get(
            f"/v1/identities/{identity_id}/agents",
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
                        "order": order,
                        "order_by": order_by,
                    },
                    identity_list_agents_params.IdentityListAgentsParams,
                ),
            ),
            cast_to=IdentityListAgentsResponse,
        )

    def list_blocks(
        self,
        identity_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityListBlocksResponse:
        """
        Get all blocks associated with the specified identity.

        Args:
          after: Block ID cursor for pagination. Returns blocks that come after this block ID in
              the specified sort order

          before: Block ID cursor for pagination. Returns blocks that come before this block ID in
              the specified sort order

          limit: Maximum number of blocks to return

          order: Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return self._get(
            f"/v1/identities/{identity_id}/blocks",
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
                        "order": order,
                        "order_by": order_by,
                    },
                    identity_list_blocks_params.IdentityListBlocksParams,
                ),
            ),
            cast_to=IdentityListBlocksResponse,
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
        x_project: str | Omit = omit,
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

          x_project: The project slug to associate with the identity (cloud only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Project": x_project}), **(extra_headers or {})}
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

    def upsert_properties(
        self,
        identity_id: str,
        *,
        body: Iterable[IdentityPropertyParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Upsert Identity Properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return self._put(
            f"/v1/identities/{identity_id}/properties",
            body=maybe_transform(body, Iterable[IdentityPropertyParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncIdentitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
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
        x_project: str | Omit = omit,
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

          x_project: The project slug to associate with the identity (cloud only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Project": x_project}), **(extra_headers or {})}
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

    async def list(
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
    ) -> IdentityListResponse:
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
        return await self._get(
            "/v1/identities/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
            cast_to=IdentityListResponse,
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

    async def list_agents(
        self,
        identity_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityListAgentsResponse:
        """
        Get all agents associated with the specified identity.

        Args:
          after: Agent ID cursor for pagination. Returns agents that come after this agent ID in
              the specified sort order

          before: Agent ID cursor for pagination. Returns agents that come before this agent ID in
              the specified sort order

          limit: Maximum number of agents to return

          order: Sort order for agents by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return await self._get(
            f"/v1/identities/{identity_id}/agents",
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
                        "order": order,
                        "order_by": order_by,
                    },
                    identity_list_agents_params.IdentityListAgentsParams,
                ),
            ),
            cast_to=IdentityListAgentsResponse,
        )

    async def list_blocks(
        self,
        identity_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityListBlocksResponse:
        """
        Get all blocks associated with the specified identity.

        Args:
          after: Block ID cursor for pagination. Returns blocks that come after this block ID in
              the specified sort order

          before: Block ID cursor for pagination. Returns blocks that come before this block ID in
              the specified sort order

          limit: Maximum number of blocks to return

          order: Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return await self._get(
            f"/v1/identities/{identity_id}/blocks",
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
                        "order": order,
                        "order_by": order_by,
                    },
                    identity_list_blocks_params.IdentityListBlocksParams,
                ),
            ),
            cast_to=IdentityListBlocksResponse,
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
        x_project: str | Omit = omit,
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

          x_project: The project slug to associate with the identity (cloud only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Project": x_project}), **(extra_headers or {})}
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

    async def upsert_properties(
        self,
        identity_id: str,
        *,
        body: Iterable[IdentityPropertyParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Upsert Identity Properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        return await self._put(
            f"/v1/identities/{identity_id}/properties",
            body=await async_maybe_transform(body, Iterable[IdentityPropertyParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        self.list_agents = to_raw_response_wrapper(
            identities.list_agents,
        )
        self.list_blocks = to_raw_response_wrapper(
            identities.list_blocks,
        )
        self.modify = to_raw_response_wrapper(
            identities.modify,
        )
        self.upsert = to_raw_response_wrapper(
            identities.upsert,
        )
        self.upsert_properties = to_raw_response_wrapper(
            identities.upsert_properties,
        )


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
        self.list_agents = async_to_raw_response_wrapper(
            identities.list_agents,
        )
        self.list_blocks = async_to_raw_response_wrapper(
            identities.list_blocks,
        )
        self.modify = async_to_raw_response_wrapper(
            identities.modify,
        )
        self.upsert = async_to_raw_response_wrapper(
            identities.upsert,
        )
        self.upsert_properties = async_to_raw_response_wrapper(
            identities.upsert_properties,
        )


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
        self.list_agents = to_streamed_response_wrapper(
            identities.list_agents,
        )
        self.list_blocks = to_streamed_response_wrapper(
            identities.list_blocks,
        )
        self.modify = to_streamed_response_wrapper(
            identities.modify,
        )
        self.upsert = to_streamed_response_wrapper(
            identities.upsert,
        )
        self.upsert_properties = to_streamed_response_wrapper(
            identities.upsert_properties,
        )


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
        self.list_agents = async_to_streamed_response_wrapper(
            identities.list_agents,
        )
        self.list_blocks = async_to_streamed_response_wrapper(
            identities.list_blocks,
        )
        self.modify = async_to_streamed_response_wrapper(
            identities.modify,
        )
        self.upsert = async_to_streamed_response_wrapper(
            identities.upsert,
        )
        self.upsert_properties = async_to_streamed_response_wrapper(
            identities.upsert_properties,
        )
