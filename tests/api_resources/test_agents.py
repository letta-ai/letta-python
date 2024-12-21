# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from letta.types import (
    AgentState,
    AgentListResponse,
    AgentMigrateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        agent = client.agents.create(
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        agent = client.agents.create(
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                    "description": "description",
                    "is_template": True,
                    "limit": 0,
                    "metadata": {},
                    "name": "name",
                }
            ],
            agent_type="memgpt_agent",
            block_ids=["string"],
            context_window_limit=0,
            description="description",
            embedding="embedding",
            embedding_chunk_size=0,
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "openai",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
                "handle": "handle",
            },
            include_base_tools=True,
            initial_message_sequence=[
                {
                    "role": "user",
                    "text": "text",
                    "name": "name",
                }
            ],
            llm="llm",
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "handle": "handle",
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "put_inner_thoughts_in_kwargs": True,
            },
            metadata={},
            name="name",
            source_ids=["string"],
            system="system",
            tags=["string"],
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "type": "InitToolRule",
                }
            ],
            tools=["string"],
            user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.agents.with_raw_response.create(
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.agents.with_streaming_response.create(
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        agent = client.agents.retrieve(
            "agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.agents.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.agents.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        agent = client.agents.update(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        agent = client.agents.update(
            agent_id="agent_id",
            block_ids=["string"],
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "openai",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
                "handle": "handle",
            },
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "handle": "handle",
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "put_inner_thoughts_in_kwargs": True,
            },
            message_ids=["string"],
            metadata={},
            name="name",
            source_ids=["string"],
            system="system",
            tags=["string"],
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "type": "InitToolRule",
                }
            ],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        agent = client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        agent = client.agents.list(
            match_all_tags=True,
            name="name",
            tags=["string"],
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        agent = client.agents.delete(
            "agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.agents.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.agents.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_migrate(self, client: Letta) -> None:
        agent = client.agents.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        )
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @parametrize
    def test_method_migrate_with_all_params(self, client: Letta) -> None:
        agent = client.agents.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
            variables={"foo": "string"},
        )
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_migrate(self, client: Letta) -> None:
        response = client.agents.with_raw_response.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_migrate(self, client: Letta) -> None:
        with client.agents.with_streaming_response.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentMigrateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_migrate(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.migrate(
                agent_id="",
                preserve_core_memories=True,
                to_template="to_template",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.create(
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.create(
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                    "description": "description",
                    "is_template": True,
                    "limit": 0,
                    "metadata": {},
                    "name": "name",
                }
            ],
            agent_type="memgpt_agent",
            block_ids=["string"],
            context_window_limit=0,
            description="description",
            embedding="embedding",
            embedding_chunk_size=0,
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "openai",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
                "handle": "handle",
            },
            include_base_tools=True,
            initial_message_sequence=[
                {
                    "role": "user",
                    "text": "text",
                    "name": "name",
                }
            ],
            llm="llm",
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "handle": "handle",
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "put_inner_thoughts_in_kwargs": True,
            },
            metadata={},
            name="name",
            source_ids=["string"],
            system="system",
            tags=["string"],
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "type": "InitToolRule",
                }
            ],
            tools=["string"],
            user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.create(
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.create(
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.retrieve(
            "agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.update(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.update(
            agent_id="agent_id",
            block_ids=["string"],
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "openai",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
                "handle": "handle",
            },
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "handle": "handle",
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "put_inner_thoughts_in_kwargs": True,
            },
            message_ids=["string"],
            metadata={},
            name="name",
            source_ids=["string"],
            system="system",
            tags=["string"],
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "type": "InitToolRule",
                }
            ],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.list(
            match_all_tags=True,
            name="name",
            tags=["string"],
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.delete(
            "agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_migrate(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        )
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @parametrize
    async def test_method_migrate_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
            variables={"foo": "string"},
        )
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_migrate(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_migrate(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentMigrateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_migrate(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.migrate(
                agent_id="",
                preserve_core_memories=True,
                to_template="to_template",
            )
