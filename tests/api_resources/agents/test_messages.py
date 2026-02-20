# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import AgentState
from letta_client.pagination import SyncArrayPage, AsyncArrayPage
from letta_client.types.agents import (
    Run,
    Message,
    LettaResponse,
    MessageCancelResponse,
)
from letta_client.types.conversations import CompactionResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Letta) -> None:
        message = client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Letta) -> None:
        message = client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            client_tools=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            enable_thinking="enable_thinking",
            include_compaction_messages=True,
            include_pings=True,
            include_return_message_types=["system_message"],
            input="string",
            max_steps=0,
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "signature": "signature",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            override_model="override_model",
            return_logprobs=True,
            return_token_ids=True,
            stream_tokens=True,
            streaming=False,
            top_logprobs=0,
            use_assistant_message=True,
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(LettaResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.create(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Letta) -> None:
        message_stream = client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        )
        message_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Letta) -> None:
        message_stream = client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            client_tools=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            enable_thinking="enable_thinking",
            include_compaction_messages=True,
            include_pings=True,
            include_return_message_types=["system_message"],
            input="string",
            max_steps=0,
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "signature": "signature",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            override_model="override_model",
            return_logprobs=True,
            return_token_ids=True,
            stream_tokens=True,
            top_logprobs=0,
            use_assistant_message=True,
        )
        message_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.create(
                agent_id="",
                streaming=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        message = client.agents.messages.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(SyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            before="before",
            conversation_id="conversation_id",
            group_id="group_id",
            include_err=True,
            limit=0,
            order="asc",
            order_by="created_at",
            use_assistant_message=True,
        )
        assert_matches_type(SyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncArrayPage[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Letta) -> None:
        message = client.agents.messages.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            run_ids=["string"],
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCancelResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.cancel(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compact(self, client: Letta) -> None:
        message = client.agents.messages.compact(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(CompactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compact_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.compact(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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
        assert_matches_type(CompactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_compact(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.compact(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(CompactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_compact(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.compact(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(CompactionResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_compact(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.compact(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_async(self, client: Letta) -> None:
        message = client.agents.messages.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_async_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            callback_url="callback_url",
            client_tools=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            enable_thinking="enable_thinking",
            include_compaction_messages=True,
            include_return_message_types=["system_message"],
            input="string",
            max_steps=0,
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "signature": "signature",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            override_model="override_model",
            return_logprobs=True,
            return_token_ids=True,
            top_logprobs=0,
            use_assistant_message=True,
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_async(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_async(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Run, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_async(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.create_async(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset(self, client: Letta) -> None:
        message = client.agents.messages.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            add_default_initial_messages=True,
        )
        assert_matches_type(Optional[AgentState], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Optional[AgentState], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Optional[AgentState], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reset(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.reset(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            message_stream = client.agents.messages.stream(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        message_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_with_all_params(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            message_stream = client.agents.messages.stream(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                assistant_message_tool_kwarg="assistant_message_tool_kwarg",
                assistant_message_tool_name="assistant_message_tool_name",
                background=True,
                client_tools=[
                    {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    }
                ],
                enable_thinking="enable_thinking",
                include_compaction_messages=True,
                include_pings=True,
                include_return_message_types=["system_message"],
                input="string",
                max_steps=0,
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "signature": "signature",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                        "batch_item_id": "batch_item_id",
                        "group_id": "group_id",
                        "name": "name",
                        "otid": "otid",
                        "sender_id": "sender_id",
                        "type": "message",
                    }
                ],
                override_model="override_model",
                return_logprobs=True,
                return_token_ids=True,
                stream_tokens=True,
                streaming=True,
                top_logprobs=0,
                use_assistant_message=True,
            )

        message_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.agents.messages.with_raw_response.stream(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with client.agents.messages.with_streaming_response.stream(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                stream = response.parse()
                stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.agents.messages.with_raw_response.stream(
                    agent_id="",
                )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            client_tools=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            enable_thinking="enable_thinking",
            include_compaction_messages=True,
            include_pings=True,
            include_return_message_types=["system_message"],
            input="string",
            max_steps=0,
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "signature": "signature",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            override_model="override_model",
            return_logprobs=True,
            return_token_ids=True,
            stream_tokens=True,
            streaming=False,
            top_logprobs=0,
            use_assistant_message=True,
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(LettaResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.create(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLetta) -> None:
        message_stream = await async_client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        )
        await message_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLetta) -> None:
        message_stream = await async_client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            client_tools=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            enable_thinking="enable_thinking",
            include_compaction_messages=True,
            include_pings=True,
            include_return_message_types=["system_message"],
            input="string",
            max_steps=0,
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "signature": "signature",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            override_model="override_model",
            return_logprobs=True,
            return_token_ids=True,
            stream_tokens=True,
            top_logprobs=0,
            use_assistant_message=True,
        )
        await message_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.create(
                agent_id="",
                streaming=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AsyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            before="before",
            conversation_id="conversation_id",
            group_id="group_id",
            include_err=True,
            limit=0,
            order="asc",
            order_by="created_at",
            use_assistant_message=True,
        )
        assert_matches_type(AsyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncArrayPage[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            run_ids=["string"],
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCancelResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.cancel(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compact(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.compact(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(CompactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compact_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.compact(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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
        assert_matches_type(CompactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_compact(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.compact(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(CompactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_compact(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.compact(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(CompactionResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_compact(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.compact(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_async(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_async_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            callback_url="callback_url",
            client_tools=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            enable_thinking="enable_thinking",
            include_compaction_messages=True,
            include_return_message_types=["system_message"],
            input="string",
            max_steps=0,
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "signature": "signature",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            override_model="override_model",
            return_logprobs=True,
            return_token_ids=True,
            top_logprobs=0,
            use_assistant_message=True,
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_async(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_async(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Run, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_async(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.create_async(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            add_default_initial_messages=True,
        )
        assert_matches_type(Optional[AgentState], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Optional[AgentState], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Optional[AgentState], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reset(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.reset(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            message_stream = await async_client.agents.messages.stream(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        await message_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            message_stream = await async_client.agents.messages.stream(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                assistant_message_tool_kwarg="assistant_message_tool_kwarg",
                assistant_message_tool_name="assistant_message_tool_name",
                background=True,
                client_tools=[
                    {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    }
                ],
                enable_thinking="enable_thinking",
                include_compaction_messages=True,
                include_pings=True,
                include_return_message_types=["system_message"],
                input="string",
                max_steps=0,
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "signature": "signature",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                        "batch_item_id": "batch_item_id",
                        "group_id": "group_id",
                        "name": "name",
                        "otid": "otid",
                        "sender_id": "sender_id",
                        "type": "message",
                    }
                ],
                override_model="override_model",
                return_logprobs=True,
                return_token_ids=True,
                stream_tokens=True,
                streaming=True,
                top_logprobs=0,
                use_assistant_message=True,
            )

        await message_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.agents.messages.with_raw_response.stream(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.agents.messages.with_streaming_response.stream(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                stream = await response.parse()
                await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.agents.messages.with_raw_response.stream(
                    agent_id="",
                )
