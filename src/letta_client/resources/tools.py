# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing
import inspect
from typing import Dict, Iterable, Optional
from textwrap import dedent
from typing_extensions import Literal

import httpx
from pydantic import BaseModel

from ..types import tool_list_params, tool_create_params, tool_search_params, tool_update_params, tool_upsert_params
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
from ..pagination import SyncArrayPage, AsyncArrayPage
from ..types.tool import Tool, BaseTool
from .._base_client import AsyncPaginator, make_request_options
from ..types.tool_search_response import ToolSearchResponse
from ..types.npm_requirement_param import NpmRequirementParam
from ..types.pip_requirement_param import PipRequirementParam

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

    def update(
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
                tool_update_params.ToolUpdateParams,
            ),
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
    ) -> SyncArrayPage[Tool]:
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
        return self._get_api_list(
            "/v1/tools/",
            page=SyncArrayPage[Tool],
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
            model=Tool,
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

    def search(
        self,
        *,
        limit: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        search_mode: Literal["vector", "fts", "hybrid"] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSearchResponse:
        """
        Search tools using semantic search.

        Requires tool embedding to be enabled (embed_tools=True). Uses vector search,
        full-text search, or hybrid mode to find tools matching the query.

        Returns tools ranked by relevance with their search scores.

        Args:
          limit: Maximum number of results to return.

          query: Text query for semantic search.

          search_mode: Search mode: vector, fts, or hybrid.

          tags: Filter by tags (match any).

          tool_types: Filter by tool types (e.g., 'custom', 'letta_core').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/search",
            body=maybe_transform(
                {
                    "limit": limit,
                    "query": query,
                    "search_mode": search_mode,
                    "tags": tags,
                    "tool_types": tool_types,
                },
                tool_search_params.ToolSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSearchResponse,
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

    def create_from_function(
        self,
        *,
        func: typing.Callable[..., typing.Any],
        args_schema: typing.Optional[typing.Type[BaseModel]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        source_type: str | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        return_char_limit: int | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Create a new tool from a callable

        Args:
          func: The callable to create the tool from.

          args_schema: The arguments schema of the function, as a Pydantic model.

          description: The description of the tool.

          tags: Metadata tags.

          source_type: The source type of the function.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          return_char_limit: The maximum number of characters in the response.

          pip_requirements: Optional list of pip packages required by this tool.

          npm_requirements: Optional list of npm packages required by this tool.

          default_requires_approval: Whether or not to require approval before executing this tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

        Examples:
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        
        def add_two_numbers(a: int, b: int) -> int:
            return a + b
        
        client.tools.create_from_function(
            func=add_two_numbers,
        )

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int

        def manage_inventory(data: InventoryEntry, quantity_change: int) -> bool:
            pass
        
        client.tools.create_from_function(
            func=manage_inventory,
            args_schema=InventoryEntryData,
        )
        """
        source_code = dedent(inspect.getsource(func))
        args_json_schema: Optional[Dict[str, object]] | Omit = omit
        if not isinstance(args_schema, Omit) and args_schema is not None:
            args_json_schema = args_schema.model_json_schema()

        return self.create(
            source_code=source_code,
            args_json_schema=args_json_schema,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            default_requires_approval=default_requires_approval,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def upsert_from_function(
        self,
        *,
        func: typing.Callable[..., typing.Any],
        args_schema: typing.Optional[typing.Type[BaseModel]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        source_type: str | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        return_char_limit: int | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Create or update a tool from a callable

        Args:
          func: The callable to create or update the tool from.

          args_schema: The arguments schema of the function, as a Pydantic model.

          description: The description of the tool.

          tags: Metadata tags.

          source_type: The source type of the function.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          return_char_limit: The maximum number of characters in the response.

          pip_requirements: Optional list of pip packages required by this tool.

          npm_requirements: Optional list of npm packages required by this tool.

          default_requires_approval: Whether or not to require approval before executing this tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

        Examples:
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )

        def add_two_numbers(a: int, b: int) -> int:
            return a + b
        
        client.tools.upsert_from_function(
            func=add_two_numbers,
        )

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int

        def manage_inventory(data: InventoryEntry, quantity_change: int) -> bool:
            pass
        
        client.tools.upsert_from_function(
            func=manage_inventory,
            args_schema=InventoryEntryData,
        )
        """
        source_code = dedent(inspect.getsource(func))
        args_json_schema: Optional[Dict[str, object]] | Omit = omit
        if not isinstance(args_schema, Omit) and args_schema is not None:
            args_json_schema = args_schema.model_json_schema()

        return self.upsert(
            source_code=source_code,
            args_json_schema=args_json_schema,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            default_requires_approval=default_requires_approval,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def add(
        self,
        *,
        tool: BaseTool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Add a tool to Letta from a custom Tool class

        Args:
          tool: The tool object to be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

        Examples:
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )

        class InventoryItem(BaseModel):
            sku: str  # Unique product identifier
            name: str  # Product name
            price: float  # Current price
            category: str  # Product category (e.g., "Electronics", "Clothing")

        class InventoryEntry(BaseModel):
            timestamp: int  # Unix timestamp of the transaction
            item: InventoryItem  # The product being updated
            transaction_id: str  # Unique identifier for this inventory update

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int  # Change in quantity (positive for additions, negative for removals)

        class ManageInventoryTool(BaseTool):
            name: str = "manage_inventory"
            args_schema: Type[BaseModel] = InventoryEntryData
            description: str = "Update inventory catalogue with a new data entry"
            tags: List[str] = ["inventory", "shop"]

            def run(self, data: InventoryEntry, quantity_change: int) -> bool:
                '''
                Implementation of the manage_inventory tool
                '''
                print(f"Updated inventory for {data.item.name} with a quantity change of {quantity_change}")
                return True
                
        client.tools.add(
            tool=ManageInventoryTool()
        )
        """
        source_code = tool.get_source_code()
        args_json_schema = tool.args_schema.model_json_schema() if tool.args_schema else None

        # Convert PipRequirement/NpmRequirement models to Param dicts
        pip_requirements_param = (
            [typing.cast(PipRequirementParam, req.model_dump()) for req in tool.pip_requirements]
            if tool.pip_requirements
            else omit
        )
        npm_requirements_param = (
            [typing.cast(NpmRequirementParam, req.model_dump()) for req in tool.npm_requirements]
            if tool.npm_requirements
            else omit
        )

        return self.upsert(
            source_code=source_code,
            args_json_schema=args_json_schema or omit,
            description=tool.description or omit,
            tags=tool.tags or omit,
            source_type=tool.source_type or omit,
            json_schema=tool.json_schema or omit,
            return_char_limit=tool.return_char_limit or omit,
            pip_requirements=pip_requirements_param,
            npm_requirements=npm_requirements_param,
            default_requires_approval=tool.default_requires_approval or omit,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
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

    async def update(
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
                tool_update_params.ToolUpdateParams,
            ),
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
    ) -> AsyncPaginator[Tool, AsyncArrayPage[Tool]]:
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
        return self._get_api_list(
            "/v1/tools/",
            page=AsyncArrayPage[Tool],
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
            model=Tool,
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

    async def search(
        self,
        *,
        limit: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        search_mode: Literal["vector", "fts", "hybrid"] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_types: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSearchResponse:
        """
        Search tools using semantic search.

        Requires tool embedding to be enabled (embed_tools=True). Uses vector search,
        full-text search, or hybrid mode to find tools matching the query.

        Returns tools ranked by relevance with their search scores.

        Args:
          limit: Maximum number of results to return.

          query: Text query for semantic search.

          search_mode: Search mode: vector, fts, or hybrid.

          tags: Filter by tags (match any).

          tool_types: Filter by tool types (e.g., 'custom', 'letta_core').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/search",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "query": query,
                    "search_mode": search_mode,
                    "tags": tags,
                    "tool_types": tool_types,
                },
                tool_search_params.ToolSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSearchResponse,
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

    async def create_from_function(
        self,
        *,
        func: typing.Callable[..., typing.Any],
        args_schema: typing.Optional[typing.Type[BaseModel]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        source_type: str | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        return_char_limit: int | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Create a new tool from a callable

        Args:
          func: The callable to create the tool from.

          args_schema: The arguments schema of the function, as a Pydantic model.

          description: The description of the tool.

          tags: Metadata tags.

          source_type: The source type of the function.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          return_char_limit: The maximum number of characters in the response.

          pip_requirements: Optional list of pip packages required by this tool.

          npm_requirements: Optional list of npm packages required by this tool.

          default_requires_approval: Whether or not to require approval before executing this tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

        Examples:
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        
        def add_two_numbers(a: int, b: int) -> int:
            return a + b
        
        await client.tools.create_from_function(
            func=add_two_numbers,
        )

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int

        def manage_inventory(data: InventoryEntry, quantity_change: int) -> bool:
            pass
        
        await client.tools.create_from_function(
            func=manage_inventory,
            args_schema=InventoryEntryData,
        )
        """
        source_code = dedent(inspect.getsource(func))
        args_json_schema: Optional[Dict[str, object]] | Omit = omit
        if not isinstance(args_schema, Omit) and args_schema is not None:
            args_json_schema = args_schema.model_json_schema()

        return await self.create(
            source_code=source_code,
            args_json_schema=args_json_schema,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            default_requires_approval=default_requires_approval,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def upsert_from_function(
        self,
        *,
        func: typing.Callable[..., typing.Any],
        args_schema: typing.Optional[typing.Type[BaseModel]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        source_type: str | Omit = omit,
        json_schema: Optional[Dict[str, object]] | Omit = omit,
        return_char_limit: int | Omit = omit,
        pip_requirements: Optional[Iterable[PipRequirementParam]] | Omit = omit,
        npm_requirements: Optional[Iterable[NpmRequirementParam]] | Omit = omit,
        default_requires_approval: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Create or update a tool from a callable

        Args:
          func: The callable to create or update the tool from.

          args_schema: The arguments schema of the function, as a Pydantic model.

          description: The description of the tool.

          tags: Metadata tags.

          source_type: The source type of the function.

          json_schema: The JSON schema of the function (auto-generated from source_code if not
              provided)

          return_char_limit: The maximum number of characters in the response.

          pip_requirements: Optional list of pip packages required by this tool.

          npm_requirements: Optional list of npm packages required by this tool.

          default_requires_approval: Whether or not to require approval before executing this tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

        Examples:
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )

        def add_two_numbers(a: int, b: int) -> int:
            return a + b
        
        await client.tools.upsert_from_function(
            func=add_two_numbers,
        )

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int

        def manage_inventory(data: InventoryEntry, quantity_change: int) -> bool:
            pass
        
        await client.tools.upsert_from_function(
            func=manage_inventory,
            args_schema=InventoryEntryData,
        )
        """
        source_code = dedent(inspect.getsource(func))
        args_json_schema: Optional[Dict[str, object]] | Omit = omit
        if not isinstance(args_schema, Omit) and args_schema is not None:
            args_json_schema = args_schema.model_json_schema()

        return await self.upsert(
            source_code=source_code,
            args_json_schema=args_json_schema,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            default_requires_approval=default_requires_approval,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def add(
        self,
        *,
        tool: BaseTool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tool:
        """
        Add a tool to Letta from a custom Tool class

        Args:
          tool: The tool object to be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

        Examples:
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )

        class InventoryItem(BaseModel):
            sku: str  # Unique product identifier
            name: str  # Product name
            price: float  # Current price
            category: str  # Product category (e.g., "Electronics", "Clothing")

        class InventoryEntry(BaseModel):
            timestamp: int  # Unix timestamp of the transaction
            item: InventoryItem  # The product being updated
            transaction_id: str  # Unique identifier for this inventory update

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int  # Change in quantity (positive for additions, negative for removals)

        class ManageInventoryTool(BaseTool):
            name: str = "manage_inventory"
            args_schema: Type[BaseModel] = InventoryEntryData
            description: str = "Update inventory catalogue with a new data entry"
            tags: List[str] = ["inventory", "shop"]

            def run(self, data: InventoryEntry, quantity_change: int) -> bool:
                '''
                Implementation of the manage_inventory tool
                '''
                print(f"Updated inventory for {data.item.name} with a quantity change of {quantity_change}")
                return True
                
        await client.tools.add(
            tool=ManageInventoryTool()
        )
        """
        source_code = tool.get_source_code()
        args_json_schema = tool.args_schema.model_json_schema() if tool.args_schema else None

        # Convert PipRequirement/NpmRequirement models to Param dicts
        pip_requirements_param = (
            [typing.cast(PipRequirementParam, req.model_dump()) for req in tool.pip_requirements]
            if tool.pip_requirements
            else omit
        )
        npm_requirements_param = (
            [typing.cast(NpmRequirementParam, req.model_dump()) for req in tool.npm_requirements]
            if tool.npm_requirements
            else omit
        )

        return await self.upsert(
            source_code=source_code,
            args_json_schema=args_json_schema or omit,
            description=tool.description or omit,
            tags=tool.tags or omit,
            source_type=tool.source_type or omit,
            json_schema=tool.json_schema or omit,
            return_char_limit=tool.return_char_limit or omit,
            pip_requirements=pip_requirements_param,
            npm_requirements=npm_requirements_param,
            default_requires_approval=tool.default_requires_approval or omit,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
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
        self.update = to_raw_response_wrapper(
            tools.update,
        )
        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.delete = to_raw_response_wrapper(
            tools.delete,
        )
        self.search = to_raw_response_wrapper(
            tools.search,
        )
        self.upsert = to_raw_response_wrapper(
            tools.upsert,
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
        self.update = async_to_raw_response_wrapper(
            tools.update,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tools.delete,
        )
        self.search = async_to_raw_response_wrapper(
            tools.search,
        )
        self.upsert = async_to_raw_response_wrapper(
            tools.upsert,
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
        self.update = to_streamed_response_wrapper(
            tools.update,
        )
        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = to_streamed_response_wrapper(
            tools.delete,
        )
        self.search = to_streamed_response_wrapper(
            tools.search,
        )
        self.upsert = to_streamed_response_wrapper(
            tools.upsert,
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
        self.update = async_to_streamed_response_wrapper(
            tools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tools.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            tools.search,
        )
        self.upsert = async_to_streamed_response_wrapper(
            tools.upsert,
        )
