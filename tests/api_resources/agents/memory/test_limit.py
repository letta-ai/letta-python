# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from letta.types import Memory
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLimit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        limit = client.agents.memory.limit.update(
            agent_id="agent_id",
            label="label",
            limit=0,
        )
        assert_matches_type(Memory, limit, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        limit = client.agents.memory.limit.update(
            agent_id="agent_id",
            label="label",
            limit=0,
            user_id="user_id",
        )
        assert_matches_type(Memory, limit, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.agents.memory.limit.with_raw_response.update(
            agent_id="agent_id",
            label="label",
            limit=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(Memory, limit, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.agents.memory.limit.with_streaming_response.update(
            agent_id="agent_id",
            label="label",
            limit=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(Memory, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.memory.limit.with_raw_response.update(
                agent_id="",
                label="label",
                limit=0,
            )


class TestAsyncLimit:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        limit = await async_client.agents.memory.limit.update(
            agent_id="agent_id",
            label="label",
            limit=0,
        )
        assert_matches_type(Memory, limit, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        limit = await async_client.agents.memory.limit.update(
            agent_id="agent_id",
            label="label",
            limit=0,
            user_id="user_id",
        )
        assert_matches_type(Memory, limit, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.memory.limit.with_raw_response.update(
            agent_id="agent_id",
            label="label",
            limit=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(Memory, limit, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.memory.limit.with_streaming_response.update(
            agent_id="agent_id",
            label="label",
            limit=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(Memory, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.memory.limit.with_raw_response.update(
                agent_id="",
                label="label",
                limit=0,
            )
