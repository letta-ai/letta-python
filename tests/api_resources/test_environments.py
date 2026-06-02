# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    EnvironmentListResponse,
    EnvironmentRetrieveResponse,
    EnvironmentSendMessageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        environment = client.environments.retrieve(
            "deviceId",
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.environments.with_raw_response.retrieve(
            "deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.environments.with_streaming_response.retrieve(
            "deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.environments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        environment = client.environments.list()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        environment = client.environments.list(
            after="after",
            limit="limit",
            online_only="onlineOnly",
            source="local",
            user_id="userId",
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.environments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.environments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message(self, client: Letta) -> None:
        environment = client.environments.send_message(
            connection_id="connectionId",
            messages=[
                {
                    "client_message_id": "client_message_id",
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(EnvironmentSendMessageResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message_with_all_params(self, client: Letta) -> None:
        environment = client.environments.send_message(
            connection_id="connectionId",
            messages=[
                {
                    "client_message_id": "client_message_id",
                    "content": "string",
                    "role": "user",
                    "otid": "otid",
                }
            ],
            agent_id="agentId",
            conversation_id="conversationId",
        )
        assert_matches_type(EnvironmentSendMessageResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: Letta) -> None:
        response = client.environments.with_raw_response.send_message(
            connection_id="connectionId",
            messages=[
                {
                    "client_message_id": "client_message_id",
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentSendMessageResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: Letta) -> None:
        with client.environments.with_streaming_response.send_message(
            connection_id="connectionId",
            messages=[
                {
                    "client_message_id": "client_message_id",
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentSendMessageResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send_message(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.environments.with_raw_response.send_message(
                connection_id="",
                messages=[
                    {
                        "client_message_id": "client_message_id",
                        "content": "string",
                        "role": "user",
                    }
                ],
            )


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        environment = await async_client.environments.retrieve(
            "deviceId",
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.environments.with_raw_response.retrieve(
            "deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.environments.with_streaming_response.retrieve(
            "deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.environments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        environment = await async_client.environments.list()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        environment = await async_client.environments.list(
            after="after",
            limit="limit",
            online_only="onlineOnly",
            source="local",
            user_id="userId",
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.environments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.environments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncLetta) -> None:
        environment = await async_client.environments.send_message(
            connection_id="connectionId",
            messages=[
                {
                    "client_message_id": "client_message_id",
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(EnvironmentSendMessageResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncLetta) -> None:
        environment = await async_client.environments.send_message(
            connection_id="connectionId",
            messages=[
                {
                    "client_message_id": "client_message_id",
                    "content": "string",
                    "role": "user",
                    "otid": "otid",
                }
            ],
            agent_id="agentId",
            conversation_id="conversationId",
        )
        assert_matches_type(EnvironmentSendMessageResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncLetta) -> None:
        response = await async_client.environments.with_raw_response.send_message(
            connection_id="connectionId",
            messages=[
                {
                    "client_message_id": "client_message_id",
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentSendMessageResponse, environment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncLetta) -> None:
        async with async_client.environments.with_streaming_response.send_message(
            connection_id="connectionId",
            messages=[
                {
                    "client_message_id": "client_message_id",
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentSendMessageResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send_message(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.environments.with_raw_response.send_message(
                connection_id="",
                messages=[
                    {
                        "client_message_id": "client_message_id",
                        "content": "string",
                        "role": "user",
                    }
                ],
            )
