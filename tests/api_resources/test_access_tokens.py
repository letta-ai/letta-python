# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    AccessTokenListResponse,
    AccessTokenCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        access_token = client.access_tokens.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        access_token = client.access_tokens.create(
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
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.access_tokens.with_raw_response.create(
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
        access_token = response.parse()
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.access_tokens.with_streaming_response.create(
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

            access_token = response.parse()
            assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        access_token = client.access_tokens.list()
        assert_matches_type(AccessTokenListResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        access_token = client.access_tokens.list(
            agent_id="agentId",
            limit=0,
            offset=0,
        )
        assert_matches_type(AccessTokenListResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.access_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(AccessTokenListResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.access_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = response.parse()
            assert_matches_type(AccessTokenListResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        access_token = client.access_tokens.delete(
            token="token",
        )
        assert_matches_type(object, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Letta) -> None:
        access_token = client.access_tokens.delete(
            token="token",
            body={},
        )
        assert_matches_type(object, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.access_tokens.with_raw_response.delete(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(object, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.access_tokens.with_streaming_response.delete(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = response.parse()
            assert_matches_type(object, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.access_tokens.with_raw_response.delete(
                token="",
            )


class TestAsyncAccessTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        access_token = await async_client.access_tokens.create(
            hostname="https://example.com",
            policy=[
                {
                    "id": "id",
                    "access": ["read_messages"],
                    "type": "agent",
                }
            ],
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        access_token = await async_client.access_tokens.create(
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
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.access_tokens.with_raw_response.create(
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
        access_token = await response.parse()
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.access_tokens.with_streaming_response.create(
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

            access_token = await response.parse()
            assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        access_token = await async_client.access_tokens.list()
        assert_matches_type(AccessTokenListResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        access_token = await async_client.access_tokens.list(
            agent_id="agentId",
            limit=0,
            offset=0,
        )
        assert_matches_type(AccessTokenListResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.access_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = await response.parse()
        assert_matches_type(AccessTokenListResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.access_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = await response.parse()
            assert_matches_type(AccessTokenListResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        access_token = await async_client.access_tokens.delete(
            token="token",
        )
        assert_matches_type(object, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLetta) -> None:
        access_token = await async_client.access_tokens.delete(
            token="token",
            body={},
        )
        assert_matches_type(object, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.access_tokens.with_raw_response.delete(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = await response.parse()
        assert_matches_type(object, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.access_tokens.with_streaming_response.delete(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = await response.parse()
            assert_matches_type(object, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.access_tokens.with_raw_response.delete(
                token="",
            )
