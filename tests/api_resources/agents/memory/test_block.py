# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from letta.types import Memory
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlock:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        block = client.agents.memory.block.create(
            agent_id="agent_id",
            label="label",
            value="value",
        )
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        block = client.agents.memory.block.create(
            agent_id="agent_id",
            label="label",
            value="value",
            description="description",
            is_template=True,
            limit=0,
            metadata={},
            name="name",
        )
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.agents.memory.block.with_raw_response.create(
            agent_id="agent_id",
            label="label",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.agents.memory.block.with_streaming_response.create(
            agent_id="agent_id",
            label="label",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(Memory, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.memory.block.with_raw_response.create(
                agent_id="",
                label="label",
                value="value",
            )

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        block = client.agents.memory.block.delete(
            block_label="block_label",
            agent_id="agent_id",
        )
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.agents.memory.block.with_raw_response.delete(
            block_label="block_label",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.agents.memory.block.with_streaming_response.delete(
            block_label="block_label",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(Memory, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.memory.block.with_raw_response.delete(
                block_label="block_label",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_label` but received ''"):
            client.agents.memory.block.with_raw_response.delete(
                block_label="",
                agent_id="agent_id",
            )


class TestAsyncBlock:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.memory.block.create(
            agent_id="agent_id",
            label="label",
            value="value",
        )
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.memory.block.create(
            agent_id="agent_id",
            label="label",
            value="value",
            description="description",
            is_template=True,
            limit=0,
            metadata={},
            name="name",
        )
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.memory.block.with_raw_response.create(
            agent_id="agent_id",
            label="label",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.memory.block.with_streaming_response.create(
            agent_id="agent_id",
            label="label",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(Memory, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.memory.block.with_raw_response.create(
                agent_id="",
                label="label",
                value="value",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.memory.block.delete(
            block_label="block_label",
            agent_id="agent_id",
        )
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.memory.block.with_raw_response.delete(
            block_label="block_label",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(Memory, block, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.memory.block.with_streaming_response.delete(
            block_label="block_label",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(Memory, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.memory.block.with_raw_response.delete(
                block_label="block_label",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_label` but received ''"):
            await async_client.agents.memory.block.with_raw_response.delete(
                block_label="",
                agent_id="agent_id",
            )
