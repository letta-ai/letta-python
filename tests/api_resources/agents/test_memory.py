# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from letta.types import Memory
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        memory = client.agents.memory.retrieve(
            "agent_id",
        )
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.agents.memory.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.agents.memory.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(Memory, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.memory.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        memory = client.agents.memory.update(
            agent_id="agent_id",
            body={},
        )
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        memory = client.agents.memory.update(
            agent_id="agent_id",
            body={},
            user_id="user_id",
        )
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.agents.memory.with_raw_response.update(
            agent_id="agent_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.agents.memory.with_streaming_response.update(
            agent_id="agent_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(Memory, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.memory.with_raw_response.update(
                agent_id="",
                body={},
            )


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        memory = await async_client.agents.memory.retrieve(
            "agent_id",
        )
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.memory.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.memory.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(Memory, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.memory.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        memory = await async_client.agents.memory.update(
            agent_id="agent_id",
            body={},
        )
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        memory = await async_client.agents.memory.update(
            agent_id="agent_id",
            body={},
            user_id="user_id",
        )
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.memory.with_raw_response.update(
            agent_id="agent_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(Memory, memory, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.memory.with_streaming_response.update(
            agent_id="agent_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(Memory, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.memory.with_raw_response.update(
                agent_id="",
                body={},
            )
