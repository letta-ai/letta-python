# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._resource import SyncAPIResource, AsyncAPIResource

from .._compat import cached_property

from ..types.tag_list_response import TagListResponse

from .._base_client import make_request_options

from .._utils import maybe_transform, async_maybe_transform

from typing import Optional

from .._types import Omit, omit, NotGiven

from typing_extensions import Literal

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from .._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ..types import tag_list_params

__all__ = ["TagsResource", "AsyncTagsResource"]

class TagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return TagsResourceWithStreamingResponse(self)

    def list(self,
    *,
    after: Optional[str] | Omit = omit,
    before: Optional[str] | Omit = omit,
    limit: Optional[int] | Omit = omit,
    name: Optional[str] | Omit = omit,
    order: Literal["asc", "desc"] | Omit = omit,
    order_by: Literal["name"] | Omit = omit,
    query_text: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TagListResponse:
        """
        Get the list of all tags (from agents and blocks) that have been created.

        Args:
          after: Tag cursor for pagination. Returns tags that come after this tag in the
              specified sort order

          before: Tag cursor for pagination. Returns tags that come before this tag in the
              specified sort order

          limit: Maximum number of tags to return

          name: Filter tags by name

          order: Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse
              alphabetical order

          order_by: Field to sort by

          query_text: Filter tags by text search. Deprecated, please use name field instead

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/tags/",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "after": after,
                "before": before,
                "limit": limit,
                "name": name,
                "order": order,
                "order_by": order_by,
                "query_text": query_text,
            }, tag_list_params.TagListParams)),
            cast_to=TagListResponse,
        )

class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncTagsResourceWithStreamingResponse(self)

    async def list(self,
    *,
    after: Optional[str] | Omit = omit,
    before: Optional[str] | Omit = omit,
    limit: Optional[int] | Omit = omit,
    name: Optional[str] | Omit = omit,
    order: Literal["asc", "desc"] | Omit = omit,
    order_by: Literal["name"] | Omit = omit,
    query_text: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TagListResponse:
        """
        Get the list of all tags (from agents and blocks) that have been created.

        Args:
          after: Tag cursor for pagination. Returns tags that come after this tag in the
              specified sort order

          before: Tag cursor for pagination. Returns tags that come before this tag in the
              specified sort order

          limit: Maximum number of tags to return

          name: Filter tags by name

          order: Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse
              alphabetical order

          order_by: Field to sort by

          query_text: Filter tags by text search. Deprecated, please use name field instead

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/tags/",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "after": after,
                "before": before,
                "limit": limit,
                "name": name,
                "order": order,
                "order_by": order_by,
                "query_text": query_text,
            }, tag_list_params.TagListParams)),
            cast_to=TagListResponse,
        )

class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.list = to_raw_response_wrapper(
            tags.list,
        )

class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.list = async_to_raw_response_wrapper(
            tags.list,
        )

class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.list = to_streamed_response_wrapper(
            tags.list,
        )

class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.list = async_to_streamed_response_wrapper(
            tags.list,
        )