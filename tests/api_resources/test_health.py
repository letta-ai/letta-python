# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import Health

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        health = client.health.retrieve()
        assert_matches_type(Health, health, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.health.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert_matches_type(Health, health, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.health.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert_matches_type(Health, health, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHealth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        health = await async_client.health.retrieve()
        assert_matches_type(Health, health, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.health.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert_matches_type(Health, health, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.health.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert_matches_type(Health, health, path=["response"])

        assert cast(Any, response.is_closed) is True
