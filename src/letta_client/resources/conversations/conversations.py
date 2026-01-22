# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    conversation_list_params,
    conversation_create_params,
    conversation_update_params,
    conversation_compact_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.conversation import Conversation
from ...types.compaction_response import CompactionResponse
from ...types.conversation_list_response import ConversationListResponse
from ...types.conversation_cancel_response import ConversationCancelResponse

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str,
        isolated_block_labels: Optional[SequenceNotStr[str]] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """
        Create a new conversation for an agent.

        Args:
          agent_id: The agent ID to create a conversation for

          isolated_block_labels: List of block labels that should be isolated (conversation-specific) rather than
              shared across conversations. New blocks will be created as copies of the agent's
              blocks with these labels.

          summary: A summary of the conversation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/conversations/",
            body=maybe_transform(
                {
                    "isolated_block_labels": isolated_block_labels,
                    "summary": summary,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, conversation_create_params.ConversationCreateParams),
            ),
            cast_to=Conversation,
        )

    def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """
        Retrieve a specific conversation.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            f"/v1/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )

    def update(
        self,
        conversation_id: str,
        *,
        summary: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """
        Update a conversation.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          summary: A summary of the conversation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._patch(
            f"/v1/conversations/{conversation_id}",
            body=maybe_transform({"summary": summary}, conversation_update_params.ConversationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )

    def list(
        self,
        *,
        agent_id: str,
        after: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """
        List all conversations for an agent.

        Args:
          agent_id: The agent ID to list conversations for

          after: Cursor for pagination (conversation ID)

          limit: Maximum number of conversations to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/conversations/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "after": after,
                        "limit": limit,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    def cancel(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationCancelResponse:
        """
        Cancel runs associated with a conversation.

        Note: To cancel active runs, Redis is required.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            f"/v1/conversations/{conversation_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationCancelResponse,
        )

    def compact(
        self,
        conversation_id: str,
        *,
        compaction_settings: Optional[conversation_compact_params.CompactionSettings] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompactionResponse:
        """
        Compact (summarize) a conversation's message history.

        This endpoint summarizes the in-context messages for a specific conversation,
        reducing the message count while preserving important context.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          compaction_settings: Configuration for conversation compaction / summarization.

              `model` is the only required user-facing field – it specifies the summarizer
              model handle (e.g. `"openai/gpt-4o-mini"`). Per-model settings (temperature, max
              tokens, etc.) are derived from the default configuration for that handle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            f"/v1/conversations/{conversation_id}/compact",
            body=maybe_transform(
                {"compaction_settings": compaction_settings}, conversation_compact_params.ConversationCompactParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompactionResponse,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str,
        isolated_block_labels: Optional[SequenceNotStr[str]] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """
        Create a new conversation for an agent.

        Args:
          agent_id: The agent ID to create a conversation for

          isolated_block_labels: List of block labels that should be isolated (conversation-specific) rather than
              shared across conversations. New blocks will be created as copies of the agent's
              blocks with these labels.

          summary: A summary of the conversation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/conversations/",
            body=await async_maybe_transform(
                {
                    "isolated_block_labels": isolated_block_labels,
                    "summary": summary,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"agent_id": agent_id}, conversation_create_params.ConversationCreateParams
                ),
            ),
            cast_to=Conversation,
        )

    async def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """
        Retrieve a specific conversation.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            f"/v1/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )

    async def update(
        self,
        conversation_id: str,
        *,
        summary: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """
        Update a conversation.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          summary: A summary of the conversation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._patch(
            f"/v1/conversations/{conversation_id}",
            body=await async_maybe_transform({"summary": summary}, conversation_update_params.ConversationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )

    async def list(
        self,
        *,
        agent_id: str,
        after: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """
        List all conversations for an agent.

        Args:
          agent_id: The agent ID to list conversations for

          after: Cursor for pagination (conversation ID)

          limit: Maximum number of conversations to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/conversations/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "after": after,
                        "limit": limit,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    async def cancel(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationCancelResponse:
        """
        Cancel runs associated with a conversation.

        Note: To cancel active runs, Redis is required.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            f"/v1/conversations/{conversation_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationCancelResponse,
        )

    async def compact(
        self,
        conversation_id: str,
        *,
        compaction_settings: Optional[conversation_compact_params.CompactionSettings] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompactionResponse:
        """
        Compact (summarize) a conversation's message history.

        This endpoint summarizes the in-context messages for a specific conversation,
        reducing the message count while preserving important context.

        Args:
          conversation_id: The ID of the conv in the format 'conv-<uuid4>'

          compaction_settings: Configuration for conversation compaction / summarization.

              `model` is the only required user-facing field – it specifies the summarizer
              model handle (e.g. `"openai/gpt-4o-mini"`). Per-model settings (temperature, max
              tokens, etc.) are derived from the default configuration for that handle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            f"/v1/conversations/{conversation_id}/compact",
            body=await async_maybe_transform(
                {"compaction_settings": compaction_settings}, conversation_compact_params.ConversationCompactParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompactionResponse,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            conversations.update,
        )
        self.list = to_raw_response_wrapper(
            conversations.list,
        )
        self.cancel = to_raw_response_wrapper(
            conversations.cancel,
        )
        self.compact = to_raw_response_wrapper(
            conversations.compact,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._conversations.messages)


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            conversations.update,
        )
        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            conversations.cancel,
        )
        self.compact = async_to_raw_response_wrapper(
            conversations.compact,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._conversations.messages)


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = to_streamed_response_wrapper(
            conversations.list,
        )
        self.cancel = to_streamed_response_wrapper(
            conversations.cancel,
        )
        self.compact = to_streamed_response_wrapper(
            conversations.compact,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._conversations.messages)


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            conversations.cancel,
        )
        self.compact = async_to_streamed_response_wrapper(
            conversations.compact,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._conversations.messages)
