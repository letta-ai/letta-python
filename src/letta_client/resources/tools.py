# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import tool_list_params, tool_count_params, tool_create_params, tool_modify_params, tool_upsert_params
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
from ..types.tool import Tool
from .._base_client import make_request_options
from ..types.tool_list_response import ToolListResponse
from ..types.tool_count_response import ToolCountResponse
from ..types.npm_requirement_param import NpmRequirementParam
from ..types.pip_requirement_param import PipRequirementParam
from ..types.tool_upsert_base_tools_response import ToolUpsertBaseToolsResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        source_code: str,
        args_json_schema: Optional[Dict[str, object]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enable_parallel_execution: Optional[bool] | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        return_char_limit: int | Omit = omit,
        source_type: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Create a new tool

        Args:
          source_code: The source code of the function.

          args_json_schema: The args JSON schema of the function.

          default_requires_approval: Whether or not to require approval before executing this tool.

          description: The description of the tool.

          enable_parallel_execution: If set to True, then this tool will potentially be executed concurrently with
              other tools. Default False.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          npm_requirements: Optional list of npm packages required by this tool.

          pip_requirements: Optional list of pip packages required by this tool.

          return_char_limit: The maximum number of characters in the response.

          source_type: The source type of the function.

          tags: Metadata tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/",
            body=maybe_transform(
                {
                    "source_code": source_code,
                    "args_json_schema": args_json_schema,
                    "default_requires_approval": default_requires_approval,
                    "description": description,
                    "enable_parallel_execution": enable_parallel_execution,
                    "json_schema": json_schema,
                    "npm_requirements": npm_requirements,
                    "pip_requirements": pip_requirements,
                    "return_char_limit": return_char_limit,
                    "source_type": source_type,
                    "tags": tags,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    def retrieve(
        self,
        tool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Get a tool by ID

        Args:
          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._get(
            f"/v1/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        exclude_tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        names: Optional[SequenceNotStr[str]] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        return_only_letta_tools: Optional[bool] | Omit = omit,
        search: Optional[str] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        Get a list of all tools available to agents.

        Args:
          after: Tool ID cursor for pagination. Returns tools that come after this tool ID in the
              specified sort order

          before: Tool ID cursor for pagination. Returns tools that come before this tool ID in
              the specified sort order

          exclude_tool_types: Tool type(s) to exclude - accepts repeated params or comma-separated values

          limit: Maximum number of tools to return

          name: Filter by single tool name

          names: Filter by specific tool names

          order: Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          return_only_letta_tools: Return only tools with tool*type starting with 'letta*'

          search: Search tool names (case-insensitive partial match)

          tool_ids: Filter by specific tool IDs - accepts repeated params or comma-separated values

          tool_types: Filter by tool type(s) - accepts repeated params or comma-separated values

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/tools/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "exclude_tool_types": exclude_tool_types,
                        "limit": limit,
                        "name": name,
                        "names": names,
                        "order": order,
                        "order_by": order_by,
                        "return_only_letta_tools": return_only_letta_tools,
                        "search": search,
                        "tool_ids": tool_ids,
                        "tool_types": tool_types,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    def delete(
        self,
        tool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a tool by name

        Args:
          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._delete(
            f"/v1/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def count(
        self,
        *,
        exclude_letta_tools: Optional[bool] | Omit = omit,
        exclude_tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        names: Optional[SequenceNotStr[str]] | Omit = omit,
        return_only_letta_tools: Optional[bool] | Omit = omit,
        search: Optional[str] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCountResponse:
        """
        Get a count of all tools available to agents belonging to the org of the user.

        Args:
          exclude_letta_tools: Exclude built-in Letta tools from the count

          exclude_tool_types: Tool type(s) to exclude - accepts repeated params or comma-separated values

          names: Filter by specific tool names

          return_only_letta_tools: Count only tools with tool*type starting with 'letta*'

          search: Search tool names (case-insensitive partial match)

          tool_ids: Filter by specific tool IDs - accepts repeated params or comma-separated values

          tool_types: Filter by tool type(s) - accepts repeated params or comma-separated values

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/tools/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_letta_tools": exclude_letta_tools,
                        "exclude_tool_types": exclude_tool_types,
                        "name": name,
                        "names": names,
                        "return_only_letta_tools": return_only_letta_tools,
                        "search": search,
                        "tool_ids": tool_ids,
                        "tool_types": tool_types,
                    },
                    tool_count_params.ToolCountParams,
                ),
            ),
            cast_to=int,
        )

    def modify(
        self,
        tool_id: str,
        *,
        args_json_schema: Optional[Dict[str, object]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enable_parallel_execution: Optional[bool] | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        return_char_limit: Optional[int] | Omit = omit,
        source_code: Optional[str] | Omit = omit,
        source_type: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Update an existing tool

        Args:
          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          args_json_schema: The args JSON schema of the function.

          default_requires_approval: Whether or not to require approval before executing this tool.

          description: The description of the tool.

          enable_parallel_execution: If set to True, then this tool will potentially be executed concurrently with
              other tools. Default False.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          metadata: A dictionary of additional metadata for the tool.

          npm_requirements: Optional list of npm packages required by this tool.

          pip_requirements: Optional list of pip packages required by this tool.

          return_char_limit: The maximum number of characters in the response.

          source_code: The source code of the function.

          source_type: The type of the source code.

          tags: Metadata tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._patch(
            f"/v1/tools/{tool_id}",
            body=maybe_transform(
                {
                    "args_json_schema": args_json_schema,
                    "default_requires_approval": default_requires_approval,
                    "description": description,
                    "enable_parallel_execution": enable_parallel_execution,
                    "json_schema": json_schema,
                    "metadata": metadata,
                    "npm_requirements": npm_requirements,
                    "pip_requirements": pip_requirements,
                    "return_char_limit": return_char_limit,
                    "source_code": source_code,
                    "source_type": source_type,
                    "tags": tags,
                },
                tool_modify_params.ToolModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    def upsert(
        self,
        *,
        source_code: str,
        args_json_schema: Optional[Dict[str, object]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enable_parallel_execution: Optional[bool] | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        return_char_limit: int | Omit = omit,
        source_type: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Create or update a tool

        Args:
          source_code: The source code of the function.

          args_json_schema: The args JSON schema of the function.

          default_requires_approval: Whether or not to require approval before executing this tool.

          description: The description of the tool.

          enable_parallel_execution: If set to True, then this tool will potentially be executed concurrently with
              other tools. Default False.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          npm_requirements: Optional list of npm packages required by this tool.

          pip_requirements: Optional list of pip packages required by this tool.

          return_char_limit: The maximum number of characters in the response.

          source_type: The source type of the function.

          tags: Metadata tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/tools/",
            body=maybe_transform(
                {
                    "source_code": source_code,
                    "args_json_schema": args_json_schema,
                    "default_requires_approval": default_requires_approval,
                    "description": description,
                    "enable_parallel_execution": enable_parallel_execution,
                    "json_schema": json_schema,
                    "npm_requirements": npm_requirements,
                    "pip_requirements": pip_requirements,
                    "return_char_limit": return_char_limit,
                    "source_type": source_type,
                    "tags": tags,
                },
                tool_upsert_params.ToolUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    def upsert_base_tools(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolUpsertBaseToolsResponse:
        """Upsert base tools"""
        return self._post(
            "/v1/tools/add-base-tools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolUpsertBaseToolsResponse,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        source_code: str,
        args_json_schema: Optional[Dict[str, object]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enable_parallel_execution: Optional[bool] | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        return_char_limit: int | Omit = omit,
        source_type: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Create a new tool

        Args:
          source_code: The source code of the function.

          args_json_schema: The args JSON schema of the function.

          default_requires_approval: Whether or not to require approval before executing this tool.

          description: The description of the tool.

          enable_parallel_execution: If set to True, then this tool will potentially be executed concurrently with
              other tools. Default False.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          npm_requirements: Optional list of npm packages required by this tool.

          pip_requirements: Optional list of pip packages required by this tool.

          return_char_limit: The maximum number of characters in the response.

          source_type: The source type of the function.

          tags: Metadata tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/",
            body=await async_maybe_transform(
                {
                    "source_code": source_code,
                    "args_json_schema": args_json_schema,
                    "default_requires_approval": default_requires_approval,
                    "description": description,
                    "enable_parallel_execution": enable_parallel_execution,
                    "json_schema": json_schema,
                    "npm_requirements": npm_requirements,
                    "pip_requirements": pip_requirements,
                    "return_char_limit": return_char_limit,
                    "source_type": source_type,
                    "tags": tags,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    async def retrieve(
        self,
        tool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Get a tool by ID

        Args:
          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._get(
            f"/v1/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        exclude_tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        names: Optional[SequenceNotStr[str]] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        return_only_letta_tools: Optional[bool] | Omit = omit,
        search: Optional[str] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        Get a list of all tools available to agents.

        Args:
          after: Tool ID cursor for pagination. Returns tools that come after this tool ID in the
              specified sort order

          before: Tool ID cursor for pagination. Returns tools that come before this tool ID in
              the specified sort order

          exclude_tool_types: Tool type(s) to exclude - accepts repeated params or comma-separated values

          limit: Maximum number of tools to return

          name: Filter by single tool name

          names: Filter by specific tool names

          order: Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          return_only_letta_tools: Return only tools with tool*type starting with 'letta*'

          search: Search tool names (case-insensitive partial match)

          tool_ids: Filter by specific tool IDs - accepts repeated params or comma-separated values

          tool_types: Filter by tool type(s) - accepts repeated params or comma-separated values

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/tools/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "exclude_tool_types": exclude_tool_types,
                        "limit": limit,
                        "name": name,
                        "names": names,
                        "order": order,
                        "order_by": order_by,
                        "return_only_letta_tools": return_only_letta_tools,
                        "search": search,
                        "tool_ids": tool_ids,
                        "tool_types": tool_types,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    async def delete(
        self,
        tool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a tool by name

        Args:
          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._delete(
            f"/v1/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def count(
        self,
        *,
        exclude_letta_tools: Optional[bool] | Omit = omit,
        exclude_tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        names: Optional[SequenceNotStr[str]] | Omit = omit,
        return_only_letta_tools: Optional[bool] | Omit = omit,
        search: Optional[str] | Omit = omit,
        tool_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCountResponse:
        """
        Get a count of all tools available to agents belonging to the org of the user.

        Args:
          exclude_letta_tools: Exclude built-in Letta tools from the count

          exclude_tool_types: Tool type(s) to exclude - accepts repeated params or comma-separated values

          names: Filter by specific tool names

          return_only_letta_tools: Count only tools with tool*type starting with 'letta*'

          search: Search tool names (case-insensitive partial match)

          tool_ids: Filter by specific tool IDs - accepts repeated params or comma-separated values

          tool_types: Filter by tool type(s) - accepts repeated params or comma-separated values

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/tools/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude_letta_tools": exclude_letta_tools,
                        "exclude_tool_types": exclude_tool_types,
                        "name": name,
                        "names": names,
                        "return_only_letta_tools": return_only_letta_tools,
                        "search": search,
                        "tool_ids": tool_ids,
                        "tool_types": tool_types,
                    },
                    tool_count_params.ToolCountParams,
                ),
            ),
            cast_to=int,
        )

    async def modify(
        self,
        tool_id: str,
        *,
        args_json_schema: Optional[Dict[str, object]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enable_parallel_execution: Optional[bool] | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        return_char_limit: Optional[int] | Omit = omit,
        source_code: Optional[str] | Omit = omit,
        source_type: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Update an existing tool

        Args:
          tool_id: The ID of the tool in the format 'tool-<uuid4>'

          args_json_schema: The args JSON schema of the function.

          default_requires_approval: Whether or not to require approval before executing this tool.

          description: The description of the tool.

          enable_parallel_execution: If set to True, then this tool will potentially be executed concurrently with
              other tools. Default False.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          metadata: A dictionary of additional metadata for the tool.

          npm_requirements: Optional list of npm packages required by this tool.

          pip_requirements: Optional list of pip packages required by this tool.

          return_char_limit: The maximum number of characters in the response.

          source_code: The source code of the function.

          source_type: The type of the source code.

          tags: Metadata tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._patch(
            f"/v1/tools/{tool_id}",
            body=await async_maybe_transform(
                {
                    "args_json_schema": args_json_schema,
                    "default_requires_approval": default_requires_approval,
                    "description": description,
                    "enable_parallel_execution": enable_parallel_execution,
                    "json_schema": json_schema,
                    "metadata": metadata,
                    "npm_requirements": npm_requirements,
                    "pip_requirements": pip_requirements,
                    "return_char_limit": return_char_limit,
                    "source_code": source_code,
                    "source_type": source_type,
                    "tags": tags,
                },
                tool_modify_params.ToolModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    async def upsert(
        self,
        *,
        source_code: str,
        args_json_schema: Optional[Dict[str, object]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enable_parallel_execution: Optional[bool] | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        return_char_limit: int | Omit = omit,
        source_type: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Create or update a tool

        Args:
          source_code: The source code of the function.

          args_json_schema: The args JSON schema of the function.

          default_requires_approval: Whether or not to require approval before executing this tool.

          description: The description of the tool.

          enable_parallel_execution: If set to True, then this tool will potentially be executed concurrently with
              other tools. Default False.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          npm_requirements: Optional list of npm packages required by this tool.

          pip_requirements: Optional list of pip packages required by this tool.

          return_char_limit: The maximum number of characters in the response.

          source_type: The source type of the function.

          tags: Metadata tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/tools/",
            body=await async_maybe_transform(
                {
                    "source_code": source_code,
                    "args_json_schema": args_json_schema,
                    "default_requires_approval": default_requires_approval,
                    "description": description,
                    "enable_parallel_execution": enable_parallel_execution,
                    "json_schema": json_schema,
                    "npm_requirements": npm_requirements,
                    "pip_requirements": pip_requirements,
                    "return_char_limit": return_char_limit,
                    "source_type": source_type,
                    "tags": tags,
                },
                tool_upsert_params.ToolUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    async def upsert_base_tools(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolUpsertBaseToolsResponse:
        """Upsert base tools"""
        return await self._post(
            "/v1/tools/add-base-tools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolUpsertBaseToolsResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_raw_response_wrapper(
            tools.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tools.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.delete = to_raw_response_wrapper(
            tools.delete,
        )
        self.count = to_raw_response_wrapper(
            tools.count,
        )
        self.modify = to_raw_response_wrapper(
            tools.modify,
        )
        self.upsert = to_raw_response_wrapper(
            tools.upsert,
        )
        self.upsert_base_tools = to_raw_response_wrapper(
            tools.upsert_base_tools,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_raw_response_wrapper(
            tools.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tools.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tools.delete,
        )
        self.count = async_to_raw_response_wrapper(
            tools.count,
        )
        self.modify = async_to_raw_response_wrapper(
            tools.modify,
        )
        self.upsert = async_to_raw_response_wrapper(
            tools.upsert,
        )
        self.upsert_base_tools = async_to_raw_response_wrapper(
            tools.upsert_base_tools,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_streamed_response_wrapper(
            tools.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = to_streamed_response_wrapper(
            tools.delete,
        )
        self.count = to_streamed_response_wrapper(
            tools.count,
        )
        self.modify = to_streamed_response_wrapper(
            tools.modify,
        )
        self.upsert = to_streamed_response_wrapper(
            tools.upsert,
        )
        self.upsert_base_tools = to_streamed_response_wrapper(
            tools.upsert_base_tools,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_streamed_response_wrapper(
            tools.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tools.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            tools.count,
        )
        self.modify = async_to_streamed_response_wrapper(
            tools.modify,
        )
        self.upsert = async_to_streamed_response_wrapper(
            tools.upsert,
        )
        self.upsert_base_tools = async_to_streamed_response_wrapper(
            tools.upsert_base_tools,
        )
