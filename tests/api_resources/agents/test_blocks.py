# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import AgentState, BlockResponse
from letta_client.pagination import SyncArrayPage, AsyncArrayPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        block = client.agents.blocks.retrieve(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.agents.blocks.with_raw_response.retrieve(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.agents.blocks.with_streaming_response.retrieve(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.blocks.with_raw_response.retrieve(
                block_label="block_label",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_label` but received ''"):
            client.agents.blocks.with_raw_response.retrieve(
                block_label="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Letta) -> None:
        block = client.agents.blocks.update(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        block = client.agents.blocks.update(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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
            tags=["string"],
            template_id="template_id",
            template_name="template_name",
            value="value",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.agents.blocks.with_raw_response.update(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.agents.blocks.with_streaming_response.update(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.blocks.with_raw_response.update(
                block_label="block_label",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_label` but received ''"):
            client.agents.blocks.with_raw_response.update(
                block_label="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        block = client.agents.blocks.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(SyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        block = client.agents.blocks.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(SyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.blocks.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(SyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.blocks.with_streaming_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(SyncArrayPage[BlockResponse], block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.blocks.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach(self, client: Letta) -> None:
        block = client.agents.blocks.attach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Letta) -> None:
        response = client.agents.blocks.with_raw_response.attach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(AgentState, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: Letta) -> None:
        with client.agents.blocks.with_streaming_response.attach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(AgentState, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.blocks.with_raw_response.attach(
                block_id="block-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.agents.blocks.with_raw_response.attach(
                block_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach(self, client: Letta) -> None:
        block = client.agents.blocks.detach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Letta) -> None:
        response = client.agents.blocks.with_raw_response.detach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(AgentState, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: Letta) -> None:
        with client.agents.blocks.with_streaming_response.detach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(AgentState, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.blocks.with_raw_response.detach(
                block_id="block-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.agents.blocks.with_raw_response.detach(
                block_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )


class TestAsyncBlocks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.blocks.retrieve(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.blocks.with_raw_response.retrieve(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.blocks.with_streaming_response.retrieve(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.blocks.with_raw_response.retrieve(
                block_label="block_label",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_label` but received ''"):
            await async_client.agents.blocks.with_raw_response.retrieve(
                block_label="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.blocks.update(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.blocks.update(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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
            tags=["string"],
            template_id="template_id",
            template_name="template_name",
            value="value",
        )
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.blocks.with_raw_response.update(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(BlockResponse, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.blocks.with_streaming_response.update(
            block_label="block_label",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(BlockResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.blocks.with_raw_response.update(
                block_label="block_label",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_label` but received ''"):
            await async_client.agents.blocks.with_raw_response.update(
                block_label="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.blocks.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AsyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.blocks.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(AsyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.blocks.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(AsyncArrayPage[BlockResponse], block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.blocks.with_streaming_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(AsyncArrayPage[BlockResponse], block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.blocks.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.blocks.attach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.blocks.with_raw_response.attach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(AgentState, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.blocks.with_streaming_response.attach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(AgentState, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.blocks.with_raw_response.attach(
                block_id="block-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.agents.blocks.with_raw_response.attach(
                block_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncLetta) -> None:
        block = await async_client.agents.blocks.detach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.blocks.with_raw_response.detach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(AgentState, block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.blocks.with_streaming_response.detach(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(AgentState, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.blocks.with_raw_response.detach(
                block_id="block-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.agents.blocks.with_raw_response.detach(
                block_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )
