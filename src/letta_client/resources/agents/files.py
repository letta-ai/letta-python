# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ...types.agents import file_list_params
from ...types.agents.file_list_response import FileListResponse
from ...types.agents.file_open_response import FileOpenResponse
from ...types.agents.file_close_all_response import FileCloseAllResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        is_open: Optional[bool] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        Get the files attached to an agent with their open/closed status.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          after: File ID cursor for pagination. Returns files that come after this file ID in the
              specified sort order

          before: File ID cursor for pagination. Returns files that come before this file ID in
              the specified sort order

          cursor: Pagination cursor from previous response (deprecated, use before/after)

          is_open: Filter by open status (true for open files, false for closed files)

          limit: Maximum number of files to return

          order: Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "cursor": cursor,
                        "is_open": is_open,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    def close(
        self,
        file_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Closes a specific file for a given agent.

        This endpoint marks a specific file as closed in the agent's file state. The
        file will be removed from the agent's working memory view.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          file_id: The ID of the file in the format 'file-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/files/{file_id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def close_all(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCloseAllResponse:
        """
        Closes all currently open files for a given agent.

        This endpoint updates the file state for the agent so that no files are marked
        as open. Typically used to reset the working memory view for the agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/files/close-all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCloseAllResponse,
        )

    def open(
        self,
        file_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileOpenResponse:
        """
        Opens a specific file for a given agent.

        This endpoint marks a specific file as open in the agent's file state. The file
        will be included in the agent's working memory view. Returns a list of file
        names that were closed due to LRU eviction.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          file_id: The ID of the file in the format 'file-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            f"/v1/agents/{agent_id}/files/{file_id}/open",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileOpenResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def list(
        self,
        agent_id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        is_open: Optional[bool] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        Get the files attached to an agent with their open/closed status.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          after: File ID cursor for pagination. Returns files that come after this file ID in the
              specified sort order

          before: File ID cursor for pagination. Returns files that come before this file ID in
              the specified sort order

          cursor: Pagination cursor from previous response (deprecated, use before/after)

          is_open: Filter by open status (true for open files, false for closed files)

          limit: Maximum number of files to return

          order: Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest
              first

          order_by: Field to sort by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "cursor": cursor,
                        "is_open": is_open,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    async def close(
        self,
        file_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Closes a specific file for a given agent.

        This endpoint marks a specific file as closed in the agent's file state. The
        file will be removed from the agent's working memory view.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          file_id: The ID of the file in the format 'file-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/files/{file_id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def close_all(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCloseAllResponse:
        """
        Closes all currently open files for a given agent.

        This endpoint updates the file state for the agent so that no files are marked
        as open. Typically used to reset the working memory view for the agent.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/files/close-all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCloseAllResponse,
        )

    async def open(
        self,
        file_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileOpenResponse:
        """
        Opens a specific file for a given agent.

        This endpoint marks a specific file as open in the agent's file state. The file
        will be included in the agent's working memory view. Returns a list of file
        names that were closed due to LRU eviction.

        Args:
          agent_id: The ID of the agent in the format 'agent-<uuid4>'

          file_id: The ID of the file in the format 'file-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            f"/v1/agents/{agent_id}/files/{file_id}/open",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileOpenResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.close = to_raw_response_wrapper(
            files.close,
        )
        self.close_all = to_raw_response_wrapper(
            files.close_all,
        )
        self.open = to_raw_response_wrapper(
            files.open,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.close = async_to_raw_response_wrapper(
            files.close,
        )
        self.close_all = async_to_raw_response_wrapper(
            files.close_all,
        )
        self.open = async_to_raw_response_wrapper(
            files.open,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.close = to_streamed_response_wrapper(
            files.close,
        )
        self.close_all = to_streamed_response_wrapper(
            files.close_all,
        )
        self.open = to_streamed_response_wrapper(
            files.open,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.close = async_to_streamed_response_wrapper(
            files.close,
        )
        self.close_all = async_to_streamed_response_wrapper(
            files.close_all,
        )
        self.open = async_to_streamed_response_wrapper(
            files.open,
        )
