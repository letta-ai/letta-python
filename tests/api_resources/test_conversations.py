# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    Conversation,
    ConversationListResponse,
    ConversationCancelResponse,
)
from letta_client._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        conversation = client.conversations.create(
            agent_id="agent_id",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        conversation = client.conversations.create(
            agent_id="agent_id",
            context_window_limit=0,
            isolated_block_labels=["string"],
            model="model",
            model_settings={
                "max_output_tokens": 0,
                "parallel_tool_calls": True,
                "provider_type": "openai",
                "reasoning": {"reasoning_effort": "none"},
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
            },
            summary="summary",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.conversations.with_raw_response.create(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.conversations.with_streaming_response.create(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        conversation = client.conversations.retrieve(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.conversations.with_raw_response.retrieve(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.conversations.with_streaming_response.retrieve(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Letta) -> None:
        conversation = client.conversations.update(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        conversation = client.conversations.update(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            archived=True,
            context_window_limit=0,
            last_message_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            model="model",
            model_settings={
                "max_output_tokens": 0,
                "parallel_tool_calls": True,
                "provider_type": "openai",
                "reasoning": {"reasoning_effort": "none"},
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
            },
            summary="summary",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.conversations.with_raw_response.update(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.conversations.with_streaming_response.update(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.with_raw_response.update(
                conversation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        conversation = client.conversations.list()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        conversation = client.conversations.list(
            after="after",
            agent_id="agent_id",
            archive_status="unarchived",
            limit=0,
            order="asc",
            order_by="created_at",
            summary_search="summary_search",
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.conversations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.conversations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        conversation = client.conversations.delete(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.conversations.with_raw_response.delete(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(object, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.conversations.with_streaming_response.delete(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(object, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Letta) -> None:
        conversation = client.conversations.cancel(
            conversation_id="default",
        )
        assert_matches_type(ConversationCancelResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Letta) -> None:
        conversation = client.conversations.cancel(
            conversation_id="default",
            agent_id="agent_id",
        )
        assert_matches_type(ConversationCancelResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Letta) -> None:
        response = client.conversations.with_raw_response.cancel(
            conversation_id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationCancelResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Letta) -> None:
        with client.conversations.with_streaming_response.cancel(
            conversation_id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationCancelResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.with_raw_response.cancel(
                conversation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fork(self, client: Letta) -> None:
        conversation = client.conversations.fork(
            conversation_id="default",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fork_with_all_params(self, client: Letta) -> None:
        conversation = client.conversations.fork(
            conversation_id="default",
            agent_id="agent_id",
            hidden=True,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fork(self, client: Letta) -> None:
        response = client.conversations.with_raw_response.fork(
            conversation_id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fork(self, client: Letta) -> None:
        with client.conversations.with_streaming_response.fork(
            conversation_id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_fork(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.with_raw_response.fork(
                conversation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_recompile(self, client: Letta) -> None:
        conversation = client.conversations.recompile(
            conversation_id="default",
        )
        assert_matches_type(str, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_recompile_with_all_params(self, client: Letta) -> None:
        conversation = client.conversations.recompile(
            conversation_id="default",
            dry_run=True,
            agent_id="agent_id",
            compaction_settings={
                "clip_chars": 0,
                "mode": "all",
                "model": "model",
                "model_settings": {
                    "max_output_tokens": 0,
                    "parallel_tool_calls": True,
                    "provider_type": "openai",
                    "reasoning": {"reasoning_effort": "none"},
                    "response_format": {"type": "text"},
                    "strict": True,
                    "temperature": 0,
                },
                "prompt": "prompt",
                "prompt_acknowledgement": True,
                "sliding_window_percentage": 0,
            },
        )
        assert_matches_type(str, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_recompile(self, client: Letta) -> None:
        response = client.conversations.with_raw_response.recompile(
            conversation_id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(str, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_recompile(self, client: Letta) -> None:
        with client.conversations.with_streaming_response.recompile(
            conversation_id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(str, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_recompile(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.with_raw_response.recompile(
                conversation_id="",
            )


class TestAsyncConversations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.create(
            agent_id="agent_id",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.create(
            agent_id="agent_id",
            context_window_limit=0,
            isolated_block_labels=["string"],
            model="model",
            model_settings={
                "max_output_tokens": 0,
                "parallel_tool_calls": True,
                "provider_type": "openai",
                "reasoning": {"reasoning_effort": "none"},
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
            },
            summary="summary",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.conversations.with_raw_response.create(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.conversations.with_streaming_response.create(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.retrieve(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.conversations.with_raw_response.retrieve(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.conversations.with_streaming_response.retrieve(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.update(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.update(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            archived=True,
            context_window_limit=0,
            last_message_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            model="model",
            model_settings={
                "max_output_tokens": 0,
                "parallel_tool_calls": True,
                "provider_type": "openai",
                "reasoning": {"reasoning_effort": "none"},
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
            },
            summary="summary",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.conversations.with_raw_response.update(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.conversations.with_streaming_response.update(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.with_raw_response.update(
                conversation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.list()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.list(
            after="after",
            agent_id="agent_id",
            archive_status="unarchived",
            limit=0,
            order="asc",
            order_by="created_at",
            summary_search="summary_search",
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.conversations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.conversations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.delete(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.conversations.with_raw_response.delete(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(object, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.conversations.with_streaming_response.delete(
            "conv-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(object, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.cancel(
            conversation_id="default",
        )
        assert_matches_type(ConversationCancelResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.cancel(
            conversation_id="default",
            agent_id="agent_id",
        )
        assert_matches_type(ConversationCancelResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLetta) -> None:
        response = await async_client.conversations.with_raw_response.cancel(
            conversation_id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationCancelResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLetta) -> None:
        async with async_client.conversations.with_streaming_response.cancel(
            conversation_id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationCancelResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.with_raw_response.cancel(
                conversation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fork(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.fork(
            conversation_id="default",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fork_with_all_params(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.fork(
            conversation_id="default",
            agent_id="agent_id",
            hidden=True,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fork(self, async_client: AsyncLetta) -> None:
        response = await async_client.conversations.with_raw_response.fork(
            conversation_id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fork(self, async_client: AsyncLetta) -> None:
        async with async_client.conversations.with_streaming_response.fork(
            conversation_id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_fork(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.with_raw_response.fork(
                conversation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_recompile(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.recompile(
            conversation_id="default",
        )
        assert_matches_type(str, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_recompile_with_all_params(self, async_client: AsyncLetta) -> None:
        conversation = await async_client.conversations.recompile(
            conversation_id="default",
            dry_run=True,
            agent_id="agent_id",
            compaction_settings={
                "clip_chars": 0,
                "mode": "all",
                "model": "model",
                "model_settings": {
                    "max_output_tokens": 0,
                    "parallel_tool_calls": True,
                    "provider_type": "openai",
                    "reasoning": {"reasoning_effort": "none"},
                    "response_format": {"type": "text"},
                    "strict": True,
                    "temperature": 0,
                },
                "prompt": "prompt",
                "prompt_acknowledgement": True,
                "sliding_window_percentage": 0,
            },
        )
        assert_matches_type(str, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_recompile(self, async_client: AsyncLetta) -> None:
        response = await async_client.conversations.with_raw_response.recompile(
            conversation_id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(str, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_recompile(self, async_client: AsyncLetta) -> None:
        async with async_client.conversations.with_streaming_response.recompile(
            conversation_id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(str, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_recompile(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.with_raw_response.recompile(
                conversation_id="",
            )
