# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    ClientSideAccessTokenListResponse,
    ClientSideAccessTokenCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientSideAccessTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LettaSDK) -> None:
        client_side_access_token = client.client_side_access_tokens.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
        )
        assert_matches_type(ClientSideAccessTokenCreateResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LettaSDK) -> None:
        client_side_access_token = client.client_side_access_tokens.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
            expires_at="expires_at",
        )
        assert_matches_type(ClientSideAccessTokenCreateResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LettaSDK) -> None:
        response = client.client_side_access_tokens.with_raw_response.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_side_access_token = response.parse()
        assert_matches_type(ClientSideAccessTokenCreateResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LettaSDK) -> None:
        with client.client_side_access_tokens.with_streaming_response.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_side_access_token = response.parse()
            assert_matches_type(ClientSideAccessTokenCreateResponse, client_side_access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        client_side_access_token = client.client_side_access_tokens.list()
        assert_matches_type(ClientSideAccessTokenListResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        client_side_access_token = client.client_side_access_tokens.list(
            agent_id="agentId",
            limit=0,
            offset=0,
        )
        assert_matches_type(ClientSideAccessTokenListResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.client_side_access_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_side_access_token = response.parse()
        assert_matches_type(ClientSideAccessTokenListResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.client_side_access_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_side_access_token = response.parse()
            assert_matches_type(ClientSideAccessTokenListResponse, client_side_access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        client_side_access_token = client.client_side_access_tokens.delete(
            token="token",
        )
        assert_matches_type(object, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LettaSDK) -> None:
        client_side_access_token = client.client_side_access_tokens.delete(
            token="token",
            body={},
        )
        assert_matches_type(object, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.client_side_access_tokens.with_raw_response.delete(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_side_access_token = response.parse()
        assert_matches_type(object, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.client_side_access_tokens.with_streaming_response.delete(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_side_access_token = response.parse()
            assert_matches_type(object, client_side_access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.client_side_access_tokens.with_raw_response.delete(
                token="",
            )


class TestAsyncClientSideAccessTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLettaSDK) -> None:
        client_side_access_token = await async_client.client_side_access_tokens.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
        )
        assert_matches_type(ClientSideAccessTokenCreateResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        client_side_access_token = await async_client.client_side_access_tokens.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
            expires_at="expires_at",
        )
        assert_matches_type(ClientSideAccessTokenCreateResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.client_side_access_tokens.with_raw_response.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_side_access_token = await response.parse()
        assert_matches_type(ClientSideAccessTokenCreateResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.client_side_access_tokens.with_streaming_response.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_side_access_token = await response.parse()
            assert_matches_type(ClientSideAccessTokenCreateResponse, client_side_access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        client_side_access_token = await async_client.client_side_access_tokens.list()
        assert_matches_type(ClientSideAccessTokenListResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        client_side_access_token = await async_client.client_side_access_tokens.list(
            agent_id="agentId",
            limit=0,
            offset=0,
        )
        assert_matches_type(ClientSideAccessTokenListResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.client_side_access_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_side_access_token = await response.parse()
        assert_matches_type(ClientSideAccessTokenListResponse, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.client_side_access_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_side_access_token = await response.parse()
            assert_matches_type(ClientSideAccessTokenListResponse, client_side_access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        client_side_access_token = await async_client.client_side_access_tokens.delete(
            token="token",
        )
        assert_matches_type(object, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        client_side_access_token = await async_client.client_side_access_tokens.delete(
            token="token",
            body={},
        )
        assert_matches_type(object, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.client_side_access_tokens.with_raw_response.delete(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_side_access_token = await response.parse()
        assert_matches_type(object, client_side_access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.client_side_access_tokens.with_streaming_response.delete(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_side_access_token = await response.parse()
            assert_matches_type(object, client_side_access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.client_side_access_tokens.with_raw_response.delete(
                token="",
            )
