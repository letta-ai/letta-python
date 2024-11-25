# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import Block, BlockListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        block = client.blocks.create(
            label="label",
            value="value",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        block = client.blocks.create(
            label="label",
            value="value",
            description="description",
            is_template=True,
            limit=0,
            metadata={},
            name="name",
            user_id="user_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.create(
            label="label",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.create(
            label="label",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(Block, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        block = client.blocks.retrieve(
            block_id="block_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Letta) -> None:
        block = client.blocks.retrieve(
            block_id="block_id",
            user_id="user_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.retrieve(
            block_id="block_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.retrieve(
            block_id="block_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(Block, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.blocks.with_raw_response.retrieve(
                block_id="",
            )

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        block = client.blocks.update(
            block_id="block_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        block = client.blocks.update(
            block_id="block_id",
            description="description",
            is_template=True,
            label="label",
            limit=0,
            metadata={},
            name="name",
            value="value",
            user_id="user_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.update(
            block_id="block_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.update(
            block_id="block_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(Block, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.blocks.with_raw_response.update(
                block_id="",
            )

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        block = client.blocks.list()
        assert_matches_type(BlockListResponse, block, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        block = client.blocks.list(
            label="label",
            name="name",
            templates_only=True,
            user_id="user_id",
        )
        assert_matches_type(BlockListResponse, block, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(BlockListResponse, block, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(BlockListResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        block = client.blocks.delete(
            block_id="block_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Letta) -> None:
        block = client.blocks.delete(
            block_id="block_id",
            user_id="user_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.delete(
            block_id="block_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.delete(
            block_id="block_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(Block, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.blocks.with_raw_response.delete(
                block_id="",
            )


class TestAsyncBlocks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.create(
            label="label",
            value="value",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.create(
            label="label",
            value="value",
            description="description",
            is_template=True,
            limit=0,
            metadata={},
            name="name",
            user_id="user_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.create(
            label="label",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.create(
            label="label",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(Block, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.retrieve(
            block_id="block_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.retrieve(
            block_id="block_id",
            user_id="user_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.retrieve(
            block_id="block_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.retrieve(
            block_id="block_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(Block, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.blocks.with_raw_response.retrieve(
                block_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.update(
            block_id="block_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.update(
            block_id="block_id",
            description="description",
            is_template=True,
            label="label",
            limit=0,
            metadata={},
            name="name",
            value="value",
            user_id="user_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.update(
            block_id="block_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.update(
            block_id="block_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(Block, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.blocks.with_raw_response.update(
                block_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.list()
        assert_matches_type(BlockListResponse, block, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.list(
            label="label",
            name="name",
            templates_only=True,
            user_id="user_id",
        )
        assert_matches_type(BlockListResponse, block, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(BlockListResponse, block, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(BlockListResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.delete(
            block_id="block_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.delete(
            block_id="block_id",
            user_id="user_id",
        )
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.delete(
            block_id="block_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(Block, block, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.delete(
            block_id="block_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(Block, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.blocks.with_raw_response.delete(
                block_id="",
            )
