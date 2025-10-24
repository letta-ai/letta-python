# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.agents import block_list_params, block_update_params
from ...types.agent_state import AgentState
from ...types.agents.block import Block
from ...types.agents.block_list_response import BlockListResponse

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

    def retrieve(
        self,
        block_label: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Retrieve a core memory block from an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_label:
            raise ValueError(f"Expected a non-empty value for `block_label` but received {block_label!r}")
        return self._get(
            f"/v1/agents/{agent_id}/core-memory/blocks/{block_label}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    def update(
        self,
        block_label: str,
        *,
        agent_id: str,
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
        Updates a core memory block of an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_label:
            raise ValueError(f"Expected a non-empty value for `block_label` but received {block_label!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/core-memory/blocks/{block_label}",
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
        agent_id: str,
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
    ) -> BlockListResponse:
        """
        Retrieve the core memory blocks of a specific agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/core-memory/blocks",
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
                    block_list_params.BlockListParams,
                ),
            ),
            cast_to=BlockListResponse,
        )

    def attach(
        self,
        block_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Attach a core memory block to an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          block_id: The ID of the block in the format 'block-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/core-memory/blocks/attach/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    def detach(
        self,
        block_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Detach a core memory block from an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          block_id: The ID of the block in the format 'block-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/core-memory/blocks/detach/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
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

    async def retrieve(
        self,
        block_label: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Block:
        """
        Retrieve a core memory block from an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_label:
            raise ValueError(f"Expected a non-empty value for `block_label` but received {block_label!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/core-memory/blocks/{block_label}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Block,
        )

    async def update(
        self,
        block_label: str,
        *,
        agent_id: str,
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
        Updates a core memory block of an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_label:
            raise ValueError(f"Expected a non-empty value for `block_label` but received {block_label!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/core-memory/blocks/{block_label}",
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
        agent_id: str,
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
    ) -> BlockListResponse:
        """
        Retrieve the core memory blocks of a specific agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/core-memory/blocks",
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
                    block_list_params.BlockListParams,
                ),
            ),
            cast_to=BlockListResponse,
        )

    async def attach(
        self,
        block_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Attach a core memory block to an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          block_id: The ID of the block in the format 'block-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/core-memory/blocks/attach/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )

    async def detach(
        self,
        block_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentState:
        """
        Detach a core memory block from an agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          block_id: The ID of the block in the format 'block-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/core-memory/blocks/detach/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentState,
        )


class BlocksResourceWithRawResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.retrieve = to_raw_response_wrapper(
            blocks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            blocks.update,
        )
        self.list = to_raw_response_wrapper(
            blocks.list,
        )
        self.attach = to_raw_response_wrapper(
            blocks.attach,
        )
        self.detach = to_raw_response_wrapper(
            blocks.detach,
        )


class AsyncBlocksResourceWithRawResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.retrieve = async_to_raw_response_wrapper(
            blocks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            blocks.update,
        )
        self.list = async_to_raw_response_wrapper(
            blocks.list,
        )
        self.attach = async_to_raw_response_wrapper(
            blocks.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            blocks.detach,
        )


class BlocksResourceWithStreamingResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.retrieve = to_streamed_response_wrapper(
            blocks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            blocks.update,
        )
        self.list = to_streamed_response_wrapper(
            blocks.list,
        )
        self.attach = to_streamed_response_wrapper(
            blocks.attach,
        )
        self.detach = to_streamed_response_wrapper(
            blocks.detach,
        )


class AsyncBlocksResourceWithStreamingResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.retrieve = async_to_streamed_response_wrapper(
            blocks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            blocks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            blocks.list,
        )
        self.attach = async_to_streamed_response_wrapper(
            blocks.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            blocks.detach,
        )
