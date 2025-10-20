# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types._internal_templates import deployment_list_entities_params
from ...types._internal_templates.deployment_delete_response import DeploymentDeleteResponse
from ...types._internal_templates.deployment_list_entities_response import DeploymentListEntitiesResponse

__all__ = ["DeploymentResource", "AsyncDeploymentResource"]


class DeploymentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return DeploymentResourceWithStreamingResponse(self)

    def delete(
        self,
        deployment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentDeleteResponse:
        """
        Delete all entities (blocks, agents, groups) with the specified deployment_id.
        Deletion order: blocks -> agents -> groups to maintain referential integrity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._delete(
            f"/v1/_internal_templates/deployment/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentDeleteResponse,
        )

    def list_entities(
        self,
        deployment_id: str,
        *,
        entity_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentListEntitiesResponse:
        """
        List all entities (blocks, agents, groups) with the specified deployment_id.
        Optionally filter by entity types.

        Args:
          entity_types: Filter by entity types (block, agent, group)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            f"/v1/_internal_templates/deployment/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"entity_types": entity_types}, deployment_list_entities_params.DeploymentListEntitiesParams
                ),
            ),
            cast_to=DeploymentListEntitiesResponse,
        )


class AsyncDeploymentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-sdk-python#with_streaming_response
        """
        return AsyncDeploymentResourceWithStreamingResponse(self)

    async def delete(
        self,
        deployment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentDeleteResponse:
        """
        Delete all entities (blocks, agents, groups) with the specified deployment_id.
        Deletion order: blocks -> agents -> groups to maintain referential integrity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._delete(
            f"/v1/_internal_templates/deployment/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentDeleteResponse,
        )

    async def list_entities(
        self,
        deployment_id: str,
        *,
        entity_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentListEntitiesResponse:
        """
        List all entities (blocks, agents, groups) with the specified deployment_id.
        Optionally filter by entity types.

        Args:
          entity_types: Filter by entity types (block, agent, group)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            f"/v1/_internal_templates/deployment/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"entity_types": entity_types}, deployment_list_entities_params.DeploymentListEntitiesParams
                ),
            ),
            cast_to=DeploymentListEntitiesResponse,
        )


class DeploymentResourceWithRawResponse:
    def __init__(self, deployment: DeploymentResource) -> None:
        self._deployment = deployment

        self.delete = to_raw_response_wrapper(
            deployment.delete,
        )
        self.list_entities = to_raw_response_wrapper(
            deployment.list_entities,
        )


class AsyncDeploymentResourceWithRawResponse:
    def __init__(self, deployment: AsyncDeploymentResource) -> None:
        self._deployment = deployment

        self.delete = async_to_raw_response_wrapper(
            deployment.delete,
        )
        self.list_entities = async_to_raw_response_wrapper(
            deployment.list_entities,
        )


class DeploymentResourceWithStreamingResponse:
    def __init__(self, deployment: DeploymentResource) -> None:
        self._deployment = deployment

        self.delete = to_streamed_response_wrapper(
            deployment.delete,
        )
        self.list_entities = to_streamed_response_wrapper(
            deployment.list_entities,
        )


class AsyncDeploymentResourceWithStreamingResponse:
    def __init__(self, deployment: AsyncDeploymentResource) -> None:
        self._deployment = deployment

        self.delete = async_to_streamed_response_wrapper(
            deployment.delete,
        )
        self.list_entities = async_to_streamed_response_wrapper(
            deployment.list_entities,
        )
