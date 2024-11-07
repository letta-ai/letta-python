# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from tests.utils import assert_matches_type
from letta.types.admin_users import APIKey, KeyListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        key = client.admin_users.keys.create(
            user_id="user_id",
        )
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        key = client.admin_users.keys.create(
            user_id="user_id",
            name="name",
        )
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.admin_users.keys.with_raw_response.create(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.admin_users.keys.with_streaming_response.create(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(APIKey, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        key = client.admin_users.keys.list(
            user_id="user_id",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.admin_users.keys.with_raw_response.list(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.admin_users.keys.with_streaming_response.list(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        key = client.admin_users.keys.delete(
            api_key="api_key",
        )
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.admin_users.keys.with_raw_response.delete(
            api_key="api_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.admin_users.keys.with_streaming_response.delete(
            api_key="api_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(APIKey, key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        key = await async_client.admin_users.keys.create(
            user_id="user_id",
        )
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        key = await async_client.admin_users.keys.create(
            user_id="user_id",
            name="name",
        )
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.admin_users.keys.with_raw_response.create(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.admin_users.keys.with_streaming_response.create(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(APIKey, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        key = await async_client.admin_users.keys.list(
            user_id="user_id",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.admin_users.keys.with_raw_response.list(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.admin_users.keys.with_streaming_response.list(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        key = await async_client.admin_users.keys.delete(
            api_key="api_key",
        )
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.admin_users.keys.with_raw_response.delete(
            api_key="api_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(APIKey, key, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.admin_users.keys.with_streaming_response.delete(
            api_key="api_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(APIKey, key, path=["response"])

        assert cast(Any, response.is_closed) is True
