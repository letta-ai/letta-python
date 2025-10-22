# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    Group,
    AgentState,
)
from letta_sdk.types.agents.core_memory import Block

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInternalTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_agent(self, client: LettaSDK) -> None:
        internal_template = client._internal_templates.create_agent(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            template_id="template_id",
        )
        assert_matches_type(AgentState, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_agent_with_all_params(self, client: LettaSDK) -> None:
        internal_template = client._internal_templates.create_agent(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            template_id="template_id",
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
                "batch_size": 0,
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
                "handle": "handle",
            },
            enable_reasoner=True,
            enable_sleeptime=True,
            from_template="from_template",
            hidden=True,
            identity_ids=["string"],
            include_base_tool_rules=True,
            include_base_tools=True,
            include_default_source=True,
            include_multi_agent_tools=True,
            initial_message_sequence=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "compatibility_type": "gguf",
                "enable_reasoner": True,
                "frequency_penalty": 0,
                "handle": "handle",
                "max_reasoning_tokens": 0,
                "max_tokens": 0,
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "provider_category": "base",
                "provider_name": "provider_name",
                "put_inner_thoughts_in_kwargs": True,
                "reasoning_effort": "minimal",
                "temperature": 0,
                "tier": "tier",
                "verbosity": "low",
            },
            max_files_open=0,
            max_reasoning_tokens=0,
            max_tokens=0,
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                    "base_template_id": "base_template_id",
                    "deployment_id": "deployment_id",
                    "description": "description",
                    "entity_id": "entity_id",
                    "hidden": True,
                    "is_template": True,
                    "limit": 0,
                    "metadata": {"foo": "bar"},
                    "name": "name",
                    "preserve_on_migration": True,
                    "project_id": "project_id",
                    "read_only": True,
                }
            ],
            memory_variables={"foo": "string"},
            message_buffer_autoclear=True,
            metadata={"foo": "bar"},
            model="model",
            name="name",
            per_file_view_window_char_limit=0,
            project="project",
            project_id="project_id",
            reasoning=True,
            response_format={"type": "text"},
            secrets={"foo": "string"},
            source_ids=["string"],
            system="system",
            tags=["string"],
            template=True,
            timezone="timezone",
            tool_exec_environment_variables={"foo": "string"},
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "prompt_template": "prompt_template",
                    "type": "constrain_child_tools",
                }
            ],
            tools=["string"],
        )
        assert_matches_type(AgentState, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_agent(self, client: LettaSDK) -> None:
        response = client._internal_templates.with_raw_response.create_agent(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            template_id="template_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_template = response.parse()
        assert_matches_type(AgentState, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_agent(self, client: LettaSDK) -> None:
        with client._internal_templates.with_streaming_response.create_agent(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            template_id="template_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_template = response.parse()
            assert_matches_type(AgentState, internal_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_block(self, client: LettaSDK) -> None:
        internal_template = client._internal_templates.create_block(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
            template_id="template_id",
            value="value",
        )
        assert_matches_type(Block, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_block_with_all_params(self, client: LettaSDK) -> None:
        internal_template = client._internal_templates.create_block(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
            template_id="template_id",
            value="value",
            description="description",
            hidden=True,
            is_template=True,
            limit=0,
            metadata={"foo": "bar"},
            name="name",
            preserve_on_migration=True,
            project_id="project_id",
            read_only=True,
        )
        assert_matches_type(Block, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_block(self, client: LettaSDK) -> None:
        response = client._internal_templates.with_raw_response.create_block(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
            template_id="template_id",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_template = response.parse()
        assert_matches_type(Block, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_block(self, client: LettaSDK) -> None:
        with client._internal_templates.with_streaming_response.create_block(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
            template_id="template_id",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_template = response.parse()
            assert_matches_type(Block, internal_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_group(self, client: LettaSDK) -> None:
        internal_template = client._internal_templates.create_group(
            agent_ids=["string"],
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            template_id="template_id",
        )
        assert_matches_type(Group, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_group_with_all_params(self, client: LettaSDK) -> None:
        internal_template = client._internal_templates.create_group(
            agent_ids=["string"],
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            template_id="template_id",
            hidden=True,
            manager_config={
                "manager_type": "round_robin",
                "max_turns": 0,
            },
            project_id="project_id",
            shared_block_ids=["string"],
        )
        assert_matches_type(Group, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_group(self, client: LettaSDK) -> None:
        response = client._internal_templates.with_raw_response.create_group(
            agent_ids=["string"],
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            template_id="template_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_template = response.parse()
        assert_matches_type(Group, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_group(self, client: LettaSDK) -> None:
        with client._internal_templates.with_streaming_response.create_group(
            agent_ids=["string"],
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            template_id="template_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_template = response.parse()
            assert_matches_type(Group, internal_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInternalTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_agent(self, async_client: AsyncLettaSDK) -> None:
        internal_template = await async_client._internal_templates.create_agent(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            template_id="template_id",
        )
        assert_matches_type(AgentState, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_agent_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        internal_template = await async_client._internal_templates.create_agent(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            template_id="template_id",
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
                "batch_size": 0,
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
                "handle": "handle",
            },
            enable_reasoner=True,
            enable_sleeptime=True,
            from_template="from_template",
            hidden=True,
            identity_ids=["string"],
            include_base_tool_rules=True,
            include_base_tools=True,
            include_default_source=True,
            include_multi_agent_tools=True,
            initial_message_sequence=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "compatibility_type": "gguf",
                "enable_reasoner": True,
                "frequency_penalty": 0,
                "handle": "handle",
                "max_reasoning_tokens": 0,
                "max_tokens": 0,
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "provider_category": "base",
                "provider_name": "provider_name",
                "put_inner_thoughts_in_kwargs": True,
                "reasoning_effort": "minimal",
                "temperature": 0,
                "tier": "tier",
                "verbosity": "low",
            },
            max_files_open=0,
            max_reasoning_tokens=0,
            max_tokens=0,
            memory_blocks=[
                {
                    "label": "label",
                    "value": "value",
                    "base_template_id": "base_template_id",
                    "deployment_id": "deployment_id",
                    "description": "description",
                    "entity_id": "entity_id",
                    "hidden": True,
                    "is_template": True,
                    "limit": 0,
                    "metadata": {"foo": "bar"},
                    "name": "name",
                    "preserve_on_migration": True,
                    "project_id": "project_id",
                    "read_only": True,
                }
            ],
            memory_variables={"foo": "string"},
            message_buffer_autoclear=True,
            metadata={"foo": "bar"},
            model="model",
            name="name",
            per_file_view_window_char_limit=0,
            project="project",
            project_id="project_id",
            reasoning=True,
            response_format={"type": "text"},
            secrets={"foo": "string"},
            source_ids=["string"],
            system="system",
            tags=["string"],
            template=True,
            timezone="timezone",
            tool_exec_environment_variables={"foo": "string"},
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "prompt_template": "prompt_template",
                    "type": "constrain_child_tools",
                }
            ],
            tools=["string"],
        )
        assert_matches_type(AgentState, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_agent(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client._internal_templates.with_raw_response.create_agent(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            template_id="template_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_template = await response.parse()
        assert_matches_type(AgentState, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_agent(self, async_client: AsyncLettaSDK) -> None:
        async with async_client._internal_templates.with_streaming_response.create_agent(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            template_id="template_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_template = await response.parse()
            assert_matches_type(AgentState, internal_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_block(self, async_client: AsyncLettaSDK) -> None:
        internal_template = await async_client._internal_templates.create_block(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
            template_id="template_id",
            value="value",
        )
        assert_matches_type(Block, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_block_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        internal_template = await async_client._internal_templates.create_block(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
            template_id="template_id",
            value="value",
            description="description",
            hidden=True,
            is_template=True,
            limit=0,
            metadata={"foo": "bar"},
            name="name",
            preserve_on_migration=True,
            project_id="project_id",
            read_only=True,
        )
        assert_matches_type(Block, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_block(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client._internal_templates.with_raw_response.create_block(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
            template_id="template_id",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_template = await response.parse()
        assert_matches_type(Block, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_block(self, async_client: AsyncLettaSDK) -> None:
        async with async_client._internal_templates.with_streaming_response.create_block(
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
            template_id="template_id",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_template = await response.parse()
            assert_matches_type(Block, internal_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_group(self, async_client: AsyncLettaSDK) -> None:
        internal_template = await async_client._internal_templates.create_group(
            agent_ids=["string"],
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            template_id="template_id",
        )
        assert_matches_type(Group, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_group_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        internal_template = await async_client._internal_templates.create_group(
            agent_ids=["string"],
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            template_id="template_id",
            hidden=True,
            manager_config={
                "manager_type": "round_robin",
                "max_turns": 0,
            },
            project_id="project_id",
            shared_block_ids=["string"],
        )
        assert_matches_type(Group, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_group(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client._internal_templates.with_raw_response.create_group(
            agent_ids=["string"],
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            template_id="template_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_template = await response.parse()
        assert_matches_type(Group, internal_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_group(self, async_client: AsyncLettaSDK) -> None:
        async with async_client._internal_templates.with_streaming_response.create_group(
            agent_ids=["string"],
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            description="description",
            template_id="template_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_template = await response.parse()
            assert_matches_type(Group, internal_template, path=["response"])

        assert cast(Any, response.is_closed) is True
