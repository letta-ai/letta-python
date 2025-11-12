# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

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
    MessageModifyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Letta) -> None:
        message = client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Letta) -> None:
        message = client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
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
            stream_tokens=True,
            streaming=False,
            use_assistant_message=True,
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.create(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Letta) -> None:
        message_stream = client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        )
        message_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Letta) -> None:
        message_stream = client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
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
            stream_tokens=True,
            use_assistant_message=True,
        )
        message_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.create(
                agent_id="",
                streaming=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        message = client.agents.messages.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(SyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            before="before",
            group_id="group_id",
            include_err=True,
            limit=0,
            order="asc",
            order_by="created_at",
            use_assistant_message=True,
        )
        assert_matches_type(SyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Letta) -> None:
        message = client.agents.messages.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            run_ids=["string"],
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.cancel(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_async(self, client: Letta) -> None:
        message = client.agents.messages.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_async_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            callback_url="callback_url",
            enable_thinking="enable_thinking",
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
            use_assistant_message=True,
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_async(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_async(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.create_async(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_overload_1(self, client: Letta) -> None:
        message = client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content="content",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_with_all_params_overload_1(self, client: Letta) -> None:
        message = client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content="content",
            message_type="system_message",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_modify_overload_1(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_modify_overload_1(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageModifyResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_modify_overload_1(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.modify(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.modify(
                message_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                content="content",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_overload_2(self, client: Letta) -> None:
        message = client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_with_all_params_overload_2(self, client: Letta) -> None:
        message = client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "signature": "signature",
                    "type": "text",
                }
            ],
            message_type="user_message",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_modify_overload_2(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_modify_overload_2(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageModifyResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_modify_overload_2(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.modify(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
                content=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.modify(
                message_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                content=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_overload_3(self, client: Letta) -> None:
        message = client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            reasoning="reasoning",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_with_all_params_overload_3(self, client: Letta) -> None:
        message = client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            reasoning="reasoning",
            message_type="reasoning_message",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_modify_overload_3(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            reasoning="reasoning",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_modify_overload_3(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            reasoning="reasoning",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageModifyResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_modify_overload_3(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.modify(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
                reasoning="reasoning",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.modify(
                message_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                reasoning="reasoning",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_overload_4(self, client: Letta) -> None:
        message = client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[{"text": "text"}],
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_with_all_params_overload_4(self, client: Letta) -> None:
        message = client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "signature": "signature",
                    "type": "text",
                }
            ],
            message_type="assistant_message",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_modify_overload_4(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[{"text": "text"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_modify_overload_4(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[{"text": "text"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageModifyResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_modify_overload_4(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.modify(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
                content=[{"text": "text"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.modify(
                message_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                content=[{"text": "text"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset(self, client: Letta) -> None:
        message = client.agents.messages.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            add_default_initial_messages=True,
        )
        assert_matches_type(AgentState, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(AgentState, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(AgentState, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.reset(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream(self, client: Letta) -> None:
        message_stream = client.agents.messages.stream(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        message_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_with_all_params(self, client: Letta) -> None:
        message_stream = client.agents.messages.stream(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
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
            stream_tokens=True,
            streaming=True,
            use_assistant_message=True,
        )
        message_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.stream(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.stream(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.stream(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize(self, client: Letta) -> None:
        message = client.agents.messages.summarize(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_summarize(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.summarize(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_summarize(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.summarize(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_summarize(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.summarize(
                "",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
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
            stream_tokens=True,
            streaming=False,
            use_assistant_message=True,
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.create(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLetta) -> None:
        message_stream = await async_client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        )
        await message_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLetta) -> None:
        message_stream = await async_client.agents.messages.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
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
            stream_tokens=True,
            use_assistant_message=True,
        )
        await message_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.create(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            streaming=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.create(
                agent_id="",
                streaming=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AsyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            before="before",
            group_id="group_id",
            include_err=True,
            limit=0,
            order="asc",
            order_by="created_at",
            use_assistant_message=True,
        )
        assert_matches_type(AsyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncArrayPage[Message], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            run_ids=["string"],
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.cancel(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.cancel(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_async(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_async_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            callback_url="callback_url",
            enable_thinking="enable_thinking",
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
            use_assistant_message=True,
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_async(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.create_async(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_async(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.create_async(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_overload_1(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content="content",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_with_all_params_overload_1(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content="content",
            message_type="system_message",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_modify_overload_1(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_modify_overload_1(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageModifyResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_modify_overload_1(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.modify(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.modify(
                message_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                content="content",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_overload_2(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_with_all_params_overload_2(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "signature": "signature",
                    "type": "text",
                }
            ],
            message_type="user_message",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_modify_overload_2(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_modify_overload_2(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageModifyResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_modify_overload_2(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.modify(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
                content=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.modify(
                message_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                content=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_overload_3(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            reasoning="reasoning",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_with_all_params_overload_3(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            reasoning="reasoning",
            message_type="reasoning_message",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_modify_overload_3(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            reasoning="reasoning",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_modify_overload_3(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            reasoning="reasoning",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageModifyResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_modify_overload_3(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.modify(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
                reasoning="reasoning",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.modify(
                message_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                reasoning="reasoning",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_overload_4(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[{"text": "text"}],
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_with_all_params_overload_4(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[
                {
                    "text": "text",
                    "signature": "signature",
                    "type": "text",
                }
            ],
            message_type="assistant_message",
        )
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_modify_overload_4(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[{"text": "text"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageModifyResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_modify_overload_4(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.modify(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            content=[{"text": "text"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageModifyResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_modify_overload_4(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.modify(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
                content=[{"text": "text"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.modify(
                message_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                content=[{"text": "text"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            add_default_initial_messages=True,
        )
        assert_matches_type(AgentState, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AgentState, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.reset(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AgentState, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.reset(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncLetta) -> None:
        message_stream = await async_client.agents.messages.stream(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        await message_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncLetta) -> None:
        message_stream = await async_client.agents.messages.stream(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
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
            stream_tokens=True,
            streaming=True,
            use_assistant_message=True,
        )
        await message_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.stream(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.stream(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.stream(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.summarize(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.summarize(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.summarize(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_summarize(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.summarize(
                "",
            )
