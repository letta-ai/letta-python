# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import BlockResponse
from letta_client.pagination import SyncArrayPage, AsyncArrayPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        block = client.blocks.create(
            label="label",
            value="value",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        block = client.blocks.create(
            label="label",
            value="value",
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            entity_id="entity_id",
            hidden=True,
            is_template=True,
            limit=0,
            metadata={"foo": "bar"},
            preserve_on_migration=True,
            project_id="project_id",
            read_only=True,
            template_id="template_id",
            template_name="template_name",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.create(
            label="label",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.create(
            label="label",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        block = client.blocks.retrieve(
            "block-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.retrieve(
            "block-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.retrieve(
            "block-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.blocks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Letta) -> None:
        block = client.blocks.update(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        block = client.blocks.update(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            entity_id="entity_id",
            hidden=True,
            is_template=True,
            label="label",
            limit=0,
            metadata={"foo": "bar"},
            preserve_on_migration=True,
            project_id="project_id",
            read_only=True,
            template_id="template_id",
            template_name="template_name",
            value="value",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.update(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.update(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.blocks.with_raw_response.update(
                block_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        block = client.blocks.list()
        assert_matches_type(SyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        block = client.blocks.list(
            after="after",
            before="before",
            connected_to_agents_count_eq=[0, 0],
            connected_to_agents_count_gt=0,
            connected_to_agents_count_lt=0,
            description_search="description_search",
            identifier_keys=["string", "string"],
            identity_id="identity_id",
            label="label",
            label_search="label_search",
            limit=0,
            name="name",
            order="asc",
            order_by="created_at",
            project_id="project_id",
            templates_only=True,
            value_search="value_search",
        )
        assert_matches_type(SyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(SyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(SyncArrayPage[BlockResponse], block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        block = client.blocks.delete(
            "block-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.blocks.with_raw_response.delete(
            "block-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(object, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.blocks.with_streaming_response.delete(
            "block-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(object, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.blocks.with_raw_response.delete(
                "",
            )


class TestAsyncBlocks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.create(
            label="label",
            value="value",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.create(
            label="label",
            value="value",
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            entity_id="entity_id",
            hidden=True,
            is_template=True,
            limit=0,
            metadata={"foo": "bar"},
            preserve_on_migration=True,
            project_id="project_id",
            read_only=True,
            template_id="template_id",
            template_name="template_name",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.create(
            label="label",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.create(
            label="label",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.retrieve(
            "block-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.retrieve(
            "block-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.retrieve(
            "block-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.blocks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.update(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.update(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            entity_id="entity_id",
            hidden=True,
            is_template=True,
            label="label",
            limit=0,
            metadata={"foo": "bar"},
            preserve_on_migration=True,
            project_id="project_id",
            read_only=True,
            template_id="template_id",
            template_name="template_name",
            value="value",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.update(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.update(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.blocks.with_raw_response.update(
                block_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.list()
        assert_matches_type(AsyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.list(
            after="after",
            before="before",
            connected_to_agents_count_eq=[0, 0],
            connected_to_agents_count_gt=0,
            connected_to_agents_count_lt=0,
            description_search="description_search",
            identifier_keys=["string", "string"],
            identity_id="identity_id",
            label="label",
            label_search="label_search",
            limit=0,
            name="name",
            order="asc",
            order_by="created_at",
            project_id="project_id",
            templates_only=True,
            value_search="value_search",
        )
        assert_matches_type(AsyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(AsyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(AsyncArrayPage[BlockResponse], block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        block = await async_client.blocks.delete(
            "block-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.blocks.with_raw_response.delete(
            "block-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(object, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.blocks.with_streaming_response.delete(
            "block-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(object, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.blocks.with_raw_response.delete(
                "",
            )
