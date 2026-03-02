# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import conversation_list_params, conversation_create_params, conversation_update_params
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
        model: Optional[str] | Omit = omit,
        model_settings: Optional[conversation_create_params.ModelSettings] | Omit = omit,
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

          model:
              The model handle for this conversation (overrides agent's model). Format:
              provider/model-name.

          model_settings: The model settings for this conversation (overrides agent's model settings).

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
                    "model": model,
                    "model_settings": model_settings,
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
          conversation_id: The conversation identifier. Can be a conversation ID ('conv-<uuid4>'), an agent
              ID ('agent-<uuid4>') for agent-direct messaging, or 'default'.

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
        model: Optional[str] | Omit = omit,
        model_settings: Optional[conversation_update_params.ModelSettings] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """Update a conversation.

        Args:
          conversation_id: The conversation identifier.

        Can be a conversation ID ('conv-<uuid4>'), an agent
              ID ('agent-<uuid4>') for agent-direct messaging, or 'default'.

          model:
              The model handle for this conversation (overrides agent's model). Format:
              provider/model-name.

          model_settings: The model settings for this conversation (overrides agent's model settings).

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
            body=maybe_transform(
                {
                    "model": model,
                    "model_settings": model_settings,
                    "summary": summary,
                },
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at", "last_run_completion"] | Omit = omit,
        summary_search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """
        List all conversations for an agent (or all conversations if agent_id not
        provided).

        Args:
          after: Cursor for pagination (conversation ID)

          agent_id: The agent ID to list conversations for (optional - returns all conversations if
              not provided)

          limit: Maximum number of conversations to return

          order: Sort order for conversations. 'asc' for oldest first, 'desc' for newest first

          order_by: Field to sort by

          summary_search: Search for text within conversation summaries

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
                        "after": after,
                        "agent_id": agent_id,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                        "summary_search": summary_search,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    def delete(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a conversation (soft delete).

        This marks the conversation as deleted but does not permanently remove it from
        the database. The conversation will no longer appear in list operations. Any
        isolated blocks associated with the conversation will be permanently deleted.

        Args:
          conversation_id: The conversation identifier. Can be a conversation ID ('conv-<uuid4>'), an agent
              ID ('agent-<uuid4>') for agent-direct messaging, or 'default'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._delete(
            f"/v1/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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

        If conversation_id is an agent ID (starts with "agent-"), cancels runs for the
        agent's default conversation.

        Args:
          conversation_id: The conversation identifier. Can be a conversation ID ('conv-<uuid4>'), an agent
              ID ('agent-<uuid4>') for agent-direct messaging, or 'default'.

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
        model: Optional[str] | Omit = omit,
        model_settings: Optional[conversation_create_params.ModelSettings] | Omit = omit,
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

          model:
              The model handle for this conversation (overrides agent's model). Format:
              provider/model-name.

          model_settings: The model settings for this conversation (overrides agent's model settings).

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
                    "model": model,
                    "model_settings": model_settings,
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
          conversation_id: The conversation identifier. Can be a conversation ID ('conv-<uuid4>'), an agent
              ID ('agent-<uuid4>') for agent-direct messaging, or 'default'.

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
        model: Optional[str] | Omit = omit,
        model_settings: Optional[conversation_update_params.ModelSettings] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """Update a conversation.

        Args:
          conversation_id: The conversation identifier.

        Can be a conversation ID ('conv-<uuid4>'), an agent
              ID ('agent-<uuid4>') for agent-direct messaging, or 'default'.

          model:
              The model handle for this conversation (overrides agent's model). Format:
              provider/model-name.

          model_settings: The model settings for this conversation (overrides agent's model settings).

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
            body=await async_maybe_transform(
                {
                    "model": model,
                    "model_settings": model_settings,
                    "summary": summary,
                },
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created_at", "last_run_completion"] | Omit = omit,
        summary_search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """
        List all conversations for an agent (or all conversations if agent_id not
        provided).

        Args:
          after: Cursor for pagination (conversation ID)

          agent_id: The agent ID to list conversations for (optional - returns all conversations if
              not provided)

          limit: Maximum number of conversations to return

          order: Sort order for conversations. 'asc' for oldest first, 'desc' for newest first

          order_by: Field to sort by

          summary_search: Search for text within conversation summaries

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
                        "after": after,
                        "agent_id": agent_id,
                        "limit": limit,
                        "order": order,
                        "order_by": order_by,
                        "summary_search": summary_search,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    async def delete(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a conversation (soft delete).

        This marks the conversation as deleted but does not permanently remove it from
        the database. The conversation will no longer appear in list operations. Any
        isolated blocks associated with the conversation will be permanently deleted.

        Args:
          conversation_id: The conversation identifier. Can be a conversation ID ('conv-<uuid4>'), an agent
              ID ('agent-<uuid4>') for agent-direct messaging, or 'default'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._delete(
            f"/v1/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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

        If conversation_id is an agent ID (starts with "agent-"), cancels runs for the
        agent's default conversation.

        Args:
          conversation_id: The conversation identifier. Can be a conversation ID ('conv-<uuid4>'), an agent
              ID ('agent-<uuid4>') for agent-direct messaging, or 'default'.

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
        self.delete = to_raw_response_wrapper(
            conversations.delete,
        )
        self.cancel = to_raw_response_wrapper(
            conversations.cancel,
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
        self.delete = async_to_raw_response_wrapper(
            conversations.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            conversations.cancel,
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
        self.delete = to_streamed_response_wrapper(
            conversations.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            conversations.cancel,
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
        self.delete = async_to_streamed_response_wrapper(
            conversations.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            conversations.cancel,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._conversations.messages)
