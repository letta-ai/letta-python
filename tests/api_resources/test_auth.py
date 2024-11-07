# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from letta.types import AuthResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_authenticate(self, client: Letta) -> None:
        auth = client.auth.authenticate()
        assert_matches_type(AuthResponse, auth, path=["response"])

    @parametrize
    def test_method_authenticate_with_all_params(self, client: Letta) -> None:
        auth = client.auth.authenticate(
            password="password",
        )
        assert_matches_type(AuthResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_authenticate(self, client: Letta) -> None:
        response = client.auth.with_raw_response.authenticate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_authenticate(self, client: Letta) -> None:
        with client.auth.with_streaming_response.authenticate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_authenticate(self, async_client: AsyncLetta) -> None:
        auth = await async_client.auth.authenticate()
        assert_matches_type(AuthResponse, auth, path=["response"])

    @parametrize
    async def test_method_authenticate_with_all_params(self, async_client: AsyncLetta) -> None:
        auth = await async_client.auth.authenticate(
            password="password",
        )
        assert_matches_type(AuthResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_authenticate(self, async_client: AsyncLetta) -> None:
        response = await async_client.auth.with_raw_response.authenticate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_authenticate(self, async_client: AsyncLetta) -> None:
        async with async_client.auth.with_streaming_response.authenticate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
