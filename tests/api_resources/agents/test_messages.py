# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from tests.utils import assert_matches_type
from letta.types.agents import (
    MessageListResponse,
    MessageCreateResponse,
    MessageUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        message = client.agents.messages.create(
            agent_id="agent_id",
            messages=[
                {
                    "role": "user",
                    "text": "text",
                }
            ],
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.create(
            agent_id="agent_id",
            messages=[
                {
                    "role": "user",
                    "text": "text",
                    "name": "name",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            user_id="user_id",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "role": "user",
                    "text": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "role": "user",
                    "text": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.create(
                agent_id="",
                messages=[
                    {
                        "role": "user",
                        "text": "text",
                    }
                ],
            )

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            name="name",
            role="assistant",
            text="text",
            tool_call_id="tool_call_id",
            tool_calls=[
                {
                    "id": "id",
                    "function": {
                        "arguments": "arguments",
                        "name": "name",
                    },
                    "type": "type",
                }
            ],
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        message = client.agents.messages.list(
            agent_id="agent_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        message = client.agents.messages.list(
            agent_id="agent_id",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            before="before",
            limit=0,
            msg_object=True,
            user_id="user_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.messages.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.messages.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.list(
                agent_id="",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create(
            agent_id="agent_id",
            messages=[
                {
                    "role": "user",
                    "text": "text",
                }
            ],
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.create(
            agent_id="agent_id",
            messages=[
                {
                    "role": "user",
                    "text": "text",
                    "name": "name",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            user_id="user_id",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "role": "user",
                    "text": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "role": "user",
                    "text": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.create(
                agent_id="",
                messages=[
                    {
                        "role": "user",
                        "text": "text",
                    }
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            name="name",
            role="assistant",
            text="text",
            tool_call_id="tool_call_id",
            tool_calls=[
                {
                    "id": "id",
                    "function": {
                        "arguments": "arguments",
                        "name": "name",
                    },
                    "type": "type",
                }
            ],
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.list(
            agent_id="agent_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        message = await async_client.agents.messages.list(
            agent_id="agent_id",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            before="before",
            limit=0,
            msg_object=True,
            user_id="user_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.messages.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.messages.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.list(
                agent_id="",
            )
