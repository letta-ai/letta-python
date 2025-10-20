# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import block_list_params, block_create_params, block_update_params, block_list_agents_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.block_list_response import BlockListResponse
from ..types.block_count_response import BlockCountResponse
from ..types.agents.core_memory.block import Block
from ..types.block_list_agents_response import BlockListAgentsResponse

__all__ = ["BlocksResource", "AsyncBlocksResource"]


class BlocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return BlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return BlocksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        label: str,
        value: str,
        base_template_id: Optional[str] | Omit = omit,
        deployment_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        entity_id: Optional[str] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        is_template: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preserve_on_migration: Optional[bool] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        read_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Create Block

        Args:
          label: Label of the block.

          value: Value of the block.

          base_template_id: The base template id of the block.

          deployment_id: The id of the deployment.

          description: Description of the block.

          entity_id: The id of the entity within the template.

          hidden: If set to True, the block will be hidden.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: The id of the template.

          preserve_on_migration: Preserve the block on template migration.

          project_id: The associated project id.

          read_only: Whether the agent has read-only access to the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/blocks/",
            body=maybe_transform(
                {
                    "label": label,
                    "value": value,
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "description": description,
                    "entity_id": entity_id,
                    "hidden": hidden,
                    "is_template": is_template,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "preserve_on_migration": preserve_on_migration,
                    "project_id": project_id,
                    "read_only": read_only,
                },
                block_create_params.BlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    def retrieve(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Retrieve Block

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._get(
            f"/v1/blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    def update(
        self,
        block_id: str,
        *,
        base_template_id: Optional[str] | Omit = omit,
        deployment_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        entity_id: Optional[str] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        is_template: bool | Omit = omit,
        label: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preserve_on_migration: Optional[bool] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        read_only: bool | Omit = omit,
        value: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Modify Block

        Args:
          base_template_id: The base template id of the block.

          deployment_id: The id of the deployment.

          description: Description of the block.

          entity_id: The id of the entity within the template.

          hidden: If set to True, the block will be hidden.

          is_template: Whether the block is a template (e.g. saved human/persona options).

          label: Label of the block (e.g. 'human', 'persona') in the context window.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: The id of the template.

          preserve_on_migration: Preserve the block on template migration.

          project_id: The associated project id.

          read_only: Whether the agent has read-only access to the block.

          value: Value of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._patch(
            f"/v1/blocks/{block_id}",
            body=maybe_transform(
                {
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "description": description,
                    "entity_id": entity_id,
                    "hidden": hidden,
                    "is_template": is_template,
                    "label": label,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "preserve_on_migration": preserve_on_migration,
                    "project_id": project_id,
                    "read_only": read_only,
                    "value": value,
                },
                block_update_params.BlockUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        connected_to_agents_count_eq: Optional[Iterable[int]] | Omit = omit,
        connected_to_agents_count_gt: Optional[int] | Omit = omit,
        connected_to_agents_count_lt: Optional[int] | Omit = omit,
        description_search: Optional[str] | Omit = omit,
        identifier_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        identity_id: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        label_search: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        templates_only: bool | Omit = omit,
        value_search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockListResponse:
        """List Blocks

        Args:
          after: Block ID cursor for pagination.

        Returns blocks that come after this block ID in
              the specified sort order

          before: Block ID cursor for pagination. Returns blocks that come before this block ID in
              the specified sort order

          connected_to_agents_count_eq: Filter blocks by the exact number of connected agents. If provided, returns
              blocks that have exactly this number of connected agents.

          connected_to_agents_count_gt: Filter blocks by the number of connected agents. If provided, returns blocks
              that have more than this number of connected agents.

          connected_to_agents_count_lt: Filter blocks by the number of connected agents. If provided, returns blocks
              that have less than this number of connected agents.

          description_search: Search blocks by description. If provided, returns blocks that match this
              description. This is a full-text search on block descriptions.

          identifier_keys: Search agents by identifier keys

          identity_id: Search agents by identifier id

          label: Labels to include (e.g. human, persona)

          label_search: Search blocks by label. If provided, returns blocks that match this label. This
              is a full-text search on labels.

          limit: Number of blocks to return

          name: Name of the block

          order: Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          project_id: Search blocks by project id

          templates_only: Whether to include only templates

          value_search: Search blocks by value. If provided, returns blocks that match this value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/blocks/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "connected_to_agents_count_eq": connected_to_agents_count_eq,
                        "connected_to_agents_count_gt": connected_to_agents_count_gt,
                        "connected_to_agents_count_lt": connected_to_agents_count_lt,
                        "description_search": description_search,
                        "identifier_keys": identifier_keys,
                        "identity_id": identity_id,
                        "label": label,
                        "label_search": label_search,
                        "limit": limit,
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                        "project_id": project_id,
                        "templates_only": templates_only,
                        "value_search": value_search,
                    },
                    block_list_params.BlockListParams,
                ),
            ),
            cast_to=BlockListResponse,
        )

    def delete(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete Block

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._delete(
            f"/v1/blocks/{block_id}",
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
    ) -> BlockCountResponse:
        """Count all blocks created by a user."""
        return self._get(
            "/v1/blocks/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    def list_agents(
        self,
        block_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_relationships: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockListAgentsResponse:
        """Retrieves all agents associated with the specified block.

        Raises a 404 if the
        block does not exist.

        Args:
          after: Agent ID cursor for pagination. Returns agents that come after this agent ID in
              the specified sort order

          before: Agent ID cursor for pagination. Returns agents that come before this agent ID in
              the specified sort order

          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.

          limit: Maximum number of agents to return

          order: Sort order for agents by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._get(
            f"/v1/blocks/{block_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include_relationships": include_relationships,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    block_list_agents_params.BlockListAgentsParams,
                ),
            ),
            cast_to=BlockListAgentsResponse,
        )


class AsyncBlocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncBlocksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        label: str,
        value: str,
        base_template_id: Optional[str] | Omit = omit,
        deployment_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        entity_id: Optional[str] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        is_template: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preserve_on_migration: Optional[bool] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        read_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Create Block

        Args:
          label: Label of the block.

          value: Value of the block.

          base_template_id: The base template id of the block.

          deployment_id: The id of the deployment.

          description: Description of the block.

          entity_id: The id of the entity within the template.

          hidden: If set to True, the block will be hidden.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: The id of the template.

          preserve_on_migration: Preserve the block on template migration.

          project_id: The associated project id.

          read_only: Whether the agent has read-only access to the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/blocks/",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "value": value,
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "description": description,
                    "entity_id": entity_id,
                    "hidden": hidden,
                    "is_template": is_template,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "preserve_on_migration": preserve_on_migration,
                    "project_id": project_id,
                    "read_only": read_only,
                },
                block_create_params.BlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    async def retrieve(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Retrieve Block

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._get(
            f"/v1/blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    async def update(
        self,
        block_id: str,
        *,
        base_template_id: Optional[str] | Omit = omit,
        deployment_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        entity_id: Optional[str] | Omit = omit,
        hidden: Optional[bool] | Omit = omit,
        is_template: bool | Omit = omit,
        label: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preserve_on_migration: Optional[bool] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        read_only: bool | Omit = omit,
        value: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Modify Block

        Args:
          base_template_id: The base template id of the block.

          deployment_id: The id of the deployment.

          description: Description of the block.

          entity_id: The id of the entity within the template.

          hidden: If set to True, the block will be hidden.

          is_template: Whether the block is a template (e.g. saved human/persona options).

          label: Label of the block (e.g. 'human', 'persona') in the context window.

          limit: Character limit of the block.

          metadata: Metadata of the block.

          name: The id of the template.

          preserve_on_migration: Preserve the block on template migration.

          project_id: The associated project id.

          read_only: Whether the agent has read-only access to the block.

          value: Value of the block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._patch(
            f"/v1/blocks/{block_id}",
            body=await async_maybe_transform(
                {
                    "base_template_id": base_template_id,
                    "deployment_id": deployment_id,
                    "description": description,
                    "entity_id": entity_id,
                    "hidden": hidden,
                    "is_template": is_template,
                    "label": label,
                    "limit": limit,
                    "metadata": metadata,
                    "name": name,
                    "preserve_on_migration": preserve_on_migration,
                    "project_id": project_id,
                    "read_only": read_only,
                    "value": value,
                },
                block_update_params.BlockUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        connected_to_agents_count_eq: Optional[Iterable[int]] | Omit = omit,
        connected_to_agents_count_gt: Optional[int] | Omit = omit,
        connected_to_agents_count_lt: Optional[int] | Omit = omit,
        description_search: Optional[str] | Omit = omit,
        identifier_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        identity_id: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        label_search: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        templates_only: bool | Omit = omit,
        value_search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockListResponse:
        """List Blocks

        Args:
          after: Block ID cursor for pagination.

        Returns blocks that come after this block ID in
              the specified sort order

          before: Block ID cursor for pagination. Returns blocks that come before this block ID in
              the specified sort order

          connected_to_agents_count_eq: Filter blocks by the exact number of connected agents. If provided, returns
              blocks that have exactly this number of connected agents.

          connected_to_agents_count_gt: Filter blocks by the number of connected agents. If provided, returns blocks
              that have more than this number of connected agents.

          connected_to_agents_count_lt: Filter blocks by the number of connected agents. If provided, returns blocks
              that have less than this number of connected agents.

          description_search: Search blocks by description. If provided, returns blocks that match this
              description. This is a full-text search on block descriptions.

          identifier_keys: Search agents by identifier keys

          identity_id: Search agents by identifier id

          label: Labels to include (e.g. human, persona)

          label_search: Search blocks by label. If provided, returns blocks that match this label. This
              is a full-text search on labels.

          limit: Number of blocks to return

          name: Name of the block

          order: Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          project_id: Search blocks by project id

          templates_only: Whether to include only templates

          value_search: Search blocks by value. If provided, returns blocks that match this value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/blocks/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "connected_to_agents_count_eq": connected_to_agents_count_eq,
                        "connected_to_agents_count_gt": connected_to_agents_count_gt,
                        "connected_to_agents_count_lt": connected_to_agents_count_lt,
                        "description_search": description_search,
                        "identifier_keys": identifier_keys,
                        "identity_id": identity_id,
                        "label": label,
                        "label_search": label_search,
                        "limit": limit,
                        "name": name,
                        "order": order,
                        "order_by": order_by,
                        "project_id": project_id,
                        "templates_only": templates_only,
                        "value_search": value_search,
                    },
                    block_list_params.BlockListParams,
                ),
            ),
            cast_to=BlockListResponse,
        )

    async def delete(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete Block

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._delete(
            f"/v1/blocks/{block_id}",
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
    ) -> BlockCountResponse:
        """Count all blocks created by a user."""
        return await self._get(
            "/v1/blocks/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    async def list_agents(
        self,
        block_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_relationships: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockListAgentsResponse:
        """Retrieves all agents associated with the specified block.

        Raises a 404 if the
        block does not exist.

        Args:
          after: Agent ID cursor for pagination. Returns agents that come after this agent ID in
              the specified sort order

          before: Agent ID cursor for pagination. Returns agents that come before this agent ID in
              the specified sort order

          include_relationships: Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include
              in the response. If not provided, all relationships are loaded by default. Using
              this can optimize performance by reducing unnecessary joins.

          limit: Maximum number of agents to return

          order: Sort order for agents by creation time. 'asc' for oldest first, 'desc' for
              newest first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._get(
            f"/v1/blocks/{block_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include_relationships": include_relationships,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    block_list_agents_params.BlockListAgentsParams,
                ),
            ),
            cast_to=BlockListAgentsResponse,
        )


class BlocksResourceWithRawResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.create = to_raw_response_wrapper(
            blocks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            blocks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            blocks.update,
        )
        self.list = to_raw_response_wrapper(
            blocks.list,
        )
        self.delete = to_raw_response_wrapper(
            blocks.delete,
        )
        self.count = to_raw_response_wrapper(
            blocks.count,
        )
        self.list_agents = to_raw_response_wrapper(
            blocks.list_agents,
        )


class AsyncBlocksResourceWithRawResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.create = async_to_raw_response_wrapper(
            blocks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            blocks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            blocks.update,
        )
        self.list = async_to_raw_response_wrapper(
            blocks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            blocks.delete,
        )
        self.count = async_to_raw_response_wrapper(
            blocks.count,
        )
        self.list_agents = async_to_raw_response_wrapper(
            blocks.list_agents,
        )


class BlocksResourceWithStreamingResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.create = to_streamed_response_wrapper(
            blocks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            blocks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            blocks.update,
        )
        self.list = to_streamed_response_wrapper(
            blocks.list,
        )
        self.delete = to_streamed_response_wrapper(
            blocks.delete,
        )
        self.count = to_streamed_response_wrapper(
            blocks.count,
        )
        self.list_agents = to_streamed_response_wrapper(
            blocks.list_agents,
        )


class AsyncBlocksResourceWithStreamingResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.create = async_to_streamed_response_wrapper(
            blocks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            blocks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            blocks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            blocks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            blocks.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            blocks.count,
        )
        self.list_agents = async_to_streamed_response_wrapper(
            blocks.list_agents,
        )
