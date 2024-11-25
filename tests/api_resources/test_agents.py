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
    Contextwindowoverview,
    AgentVersionTemplateResponse,
)
from tests.utils import assert_matches_type
from letta._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        agent = client.agents.create()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        agent = client.agents.create(
            agent_type="memgpt_agent",
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "embedding_endpoint_type",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
            },
            initial_message_sequence=[
                {
                    "role": "assistant",
                    "id": "id",
                    "agent_id": "agent_id",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "model": "model",
                    "name": "name",
                    "text": "text",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "type",
                        }
                    ],
                    "user_id": "user_id",
                }
            ],
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "put_inner_thoughts_in_kwargs": True,
            },
            memory={
                "memory": {
                    "foo": {
                        "value": "value",
                        "id": "id",
                        "created_by_id": "created_by_id",
                        "description": "description",
                        "is_template": True,
                        "label": "label",
                        "last_updated_by_id": "last_updated_by_id",
                        "limit": 0,
                        "metadata": {},
                        "name": "name",
                        "organization_id": "organization_id",
                    }
                },
                "prompt_template": "prompt_template",
            },
            message_ids=["string"],
            metadata={},
            name="name",
            system="system",
            tags=["string"],
            tool_rules=[{"tool_name": "tool_name"}],
            tools=["string"],
            body_user_id="user_id",
            header_user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.agents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.agents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        agent = client.agents.retrieve(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Letta) -> None:
        agent = client.agents.retrieve(
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.agents.with_raw_response.retrieve(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.agents.with_streaming_response.retrieve(
            agent_id="agent_id",
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
                agent_id="",
            )

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        agent = client.agents.update(
            agent_id="agent_id",
            id="id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        agent = client.agents.update(
            agent_id="agent_id",
            id="id",
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "embedding_endpoint_type",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
            },
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "put_inner_thoughts_in_kwargs": True,
            },
            memory={
                "memory": {
                    "foo": {
                        "value": "value",
                        "id": "id",
                        "created_by_id": "created_by_id",
                        "description": "description",
                        "is_template": True,
                        "label": "label",
                        "last_updated_by_id": "last_updated_by_id",
                        "limit": 0,
                        "metadata": {},
                        "name": "name",
                        "organization_id": "organization_id",
                    }
                },
                "prompt_template": "prompt_template",
            },
            message_ids=["string"],
            metadata={},
            name="name",
            system="system",
            tags=["string"],
            tools=["string"],
            body_user_id="user_id",
            header_user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="agent_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="agent_id",
            id="id",
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
                id="id",
            )

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        agent = client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        agent = client.agents.list(
            name="name",
            tags=["string"],
            user_id="user_id",
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
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Letta) -> None:
        agent = client.agents.delete(
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.agents.with_raw_response.delete(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.agents.with_streaming_response.delete(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                agent_id="",
            )

    @parametrize
    def test_method_add_tool(self, client: Letta) -> None:
        agent = client.agents.add_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_method_add_tool_with_all_params(self, client: Letta) -> None:
        agent = client.agents.add_tool(
            tool_id="tool_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_add_tool(self, client: Letta) -> None:
        response = client.agents.with_raw_response.add_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_add_tool(self, client: Letta) -> None:
        with client.agents.with_streaming_response.add_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_tool(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.add_tool(
                tool_id="tool_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.with_raw_response.add_tool(
                tool_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_context(self, client: Letta) -> None:
        agent = client.agents.context(
            agent_id="agent_id",
        )
        assert_matches_type(Contextwindowoverview, agent, path=["response"])

    @parametrize
    def test_method_context_with_all_params(self, client: Letta) -> None:
        agent = client.agents.context(
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(Contextwindowoverview, agent, path=["response"])

    @parametrize
    def test_raw_response_context(self, client: Letta) -> None:
        response = client.agents.with_raw_response.context(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Contextwindowoverview, agent, path=["response"])

    @parametrize
    def test_streaming_response_context(self, client: Letta) -> None:
        with client.agents.with_streaming_response.context(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Contextwindowoverview, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_context(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.context(
                agent_id="",
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

    @parametrize
    def test_method_remove_tool(self, client: Letta) -> None:
        agent = client.agents.remove_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_method_remove_tool_with_all_params(self, client: Letta) -> None:
        agent = client.agents.remove_tool(
            tool_id="tool_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_raw_response_remove_tool(self, client: Letta) -> None:
        response = client.agents.with_raw_response.remove_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    def test_streaming_response_remove_tool(self, client: Letta) -> None:
        with client.agents.with_streaming_response.remove_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_tool(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.remove_tool(
                tool_id="tool_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.with_raw_response.remove_tool(
                tool_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_version_template(self, client: Letta) -> None:
        agent = client.agents.version_template(
            agent_id="agent_id",
        )
        assert_matches_type(AgentVersionTemplateResponse, agent, path=["response"])

    @parametrize
    def test_method_version_template_with_all_params(self, client: Letta) -> None:
        agent = client.agents.version_template(
            agent_id="agent_id",
            return_agent_id=True,
            migrate_deployed_agents=True,
        )
        assert_matches_type(AgentVersionTemplateResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_version_template(self, client: Letta) -> None:
        response = client.agents.with_raw_response.version_template(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentVersionTemplateResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_version_template(self, client: Letta) -> None:
        with client.agents.with_streaming_response.version_template(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentVersionTemplateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_version_template(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.version_template(
                agent_id="",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.create()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.create(
            agent_type="memgpt_agent",
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "embedding_endpoint_type",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
            },
            initial_message_sequence=[
                {
                    "role": "assistant",
                    "id": "id",
                    "agent_id": "agent_id",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "model": "model",
                    "name": "name",
                    "text": "text",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "type",
                        }
                    ],
                    "user_id": "user_id",
                }
            ],
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "put_inner_thoughts_in_kwargs": True,
            },
            memory={
                "memory": {
                    "foo": {
                        "value": "value",
                        "id": "id",
                        "created_by_id": "created_by_id",
                        "description": "description",
                        "is_template": True,
                        "label": "label",
                        "last_updated_by_id": "last_updated_by_id",
                        "limit": 0,
                        "metadata": {},
                        "name": "name",
                        "organization_id": "organization_id",
                    }
                },
                "prompt_template": "prompt_template",
            },
            message_ids=["string"],
            metadata={},
            name="name",
            system="system",
            tags=["string"],
            tool_rules=[{"tool_name": "tool_name"}],
            tools=["string"],
            body_user_id="user_id",
            header_user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.retrieve(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.retrieve(
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            agent_id="agent_id",
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
                agent_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.update(
            agent_id="agent_id",
            id="id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.update(
            agent_id="agent_id",
            id="id",
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "embedding_endpoint_type",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
            },
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "put_inner_thoughts_in_kwargs": True,
            },
            memory={
                "memory": {
                    "foo": {
                        "value": "value",
                        "id": "id",
                        "created_by_id": "created_by_id",
                        "description": "description",
                        "is_template": True,
                        "label": "label",
                        "last_updated_by_id": "last_updated_by_id",
                        "limit": 0,
                        "metadata": {},
                        "name": "name",
                        "organization_id": "organization_id",
                    }
                },
                "prompt_template": "prompt_template",
            },
            message_ids=["string"],
            metadata={},
            name="name",
            system="system",
            tags=["string"],
            tools=["string"],
            body_user_id="user_id",
            header_user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="agent_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="agent_id",
            id="id",
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
                id="id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.list(
            name="name",
            tags=["string"],
            user_id="user_id",
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
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.delete(
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.delete(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.delete(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                agent_id="",
            )

    @parametrize
    async def test_method_add_tool(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.add_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_method_add_tool_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.add_tool(
            tool_id="tool_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_add_tool(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.add_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_add_tool(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.add_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_tool(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.add_tool(
                tool_id="tool_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.with_raw_response.add_tool(
                tool_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_context(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.context(
            agent_id="agent_id",
        )
        assert_matches_type(Contextwindowoverview, agent, path=["response"])

    @parametrize
    async def test_method_context_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.context(
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(Contextwindowoverview, agent, path=["response"])

    @parametrize
    async def test_raw_response_context(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.context(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Contextwindowoverview, agent, path=["response"])

    @parametrize
    async def test_streaming_response_context(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.context(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Contextwindowoverview, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_context(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.context(
                agent_id="",
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

    @parametrize
    async def test_method_remove_tool(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.remove_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_method_remove_tool_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.remove_tool(
            tool_id="tool_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_raw_response_remove_tool(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.remove_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @parametrize
    async def test_streaming_response_remove_tool(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.remove_tool(
            tool_id="tool_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_tool(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.remove_tool(
                tool_id="tool_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.with_raw_response.remove_tool(
                tool_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_version_template(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.version_template(
            agent_id="agent_id",
        )
        assert_matches_type(AgentVersionTemplateResponse, agent, path=["response"])

    @parametrize
    async def test_method_version_template_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.version_template(
            agent_id="agent_id",
            return_agent_id=True,
            migrate_deployed_agents=True,
        )
        assert_matches_type(AgentVersionTemplateResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_version_template(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.version_template(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentVersionTemplateResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_version_template(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.version_template(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentVersionTemplateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_version_template(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.version_template(
                agent_id="",
            )
