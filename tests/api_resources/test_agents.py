# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    AgentState,
    AgentImportFileResponse,
)
from letta_client._utils import parse_datetime
from letta_client.pagination import SyncArrayPage, AsyncArrayPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        agent = client.agents.create()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        agent = client.agents.create(
            agent_type="memgpt_agent",
            base_template_id="base_template_id",
            block_ids=["string"],
            compaction_settings={
                "model": "model",
                "clip_chars": 0,
                "mode": "all",
                "model_settings": {
                    "max_output_tokens": 0,
                    "parallel_tool_calls": True,
                    "provider_type": "openai",
                    "reasoning": {"reasoning_effort": "none"},
                    "response_format": {"type": "text"},
                    "strict": True,
                    "temperature": 0,
                },
                "prompt": "prompt",
                "prompt_acknowledgement": True,
                "sliding_window_percentage": 0,
            },
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
            folder_ids=["string"],
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
                            "signature": "signature",
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
                "display_name": "display_name",
                "effort": "low",
                "enable_reasoner": True,
                "frequency_penalty": 0,
                "handle": "handle",
                "max_reasoning_tokens": 0,
                "max_tokens": 0,
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "parallel_tool_calls": True,
                "provider_category": "base",
                "provider_name": "provider_name",
                "put_inner_thoughts_in_kwargs": True,
                "reasoning_effort": "none",
                "response_format": {"type": "text"},
                "strict": True,
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
                    "preserve_on_migration": True,
                    "project_id": "project_id",
                    "read_only": True,
                    "tags": ["string"],
                    "template_id": "template_id",
                    "template_name": "template_name",
                }
            ],
            memory_variables={"foo": "string"},
            message_buffer_autoclear=True,
            metadata={"foo": "bar"},
            model="model",
            model_settings={
                "max_output_tokens": 0,
                "parallel_tool_calls": True,
                "provider_type": "openai",
                "reasoning": {"reasoning_effort": "none"},
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
            },
            name="name",
            parallel_tool_calls=True,
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
            template_id="template_id",
            timezone="timezone",
            tool_exec_environment_variables={"foo": "string"},
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "child_arg_nodes": [
                        {
                            "name": "name",
                            "args": {"foo": "bar"},
                        }
                    ],
                    "prompt_template": "prompt_template",
                    "type": "constrain_child_tools",
                }
            ],
            tools=["string"],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.agents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.agents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        agent = client.agents.retrieve(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Letta) -> None:
        agent = client.agents.retrieve(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            include=["agent.blocks"],
            include_relationships=["string", "string"],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.agents.with_raw_response.retrieve(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.agents.with_streaming_response.retrieve(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Letta) -> None:
        agent = client.agents.update(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        agent = client.agents.update(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            base_template_id="base_template_id",
            block_ids=["string"],
            compaction_settings={
                "model": "model",
                "clip_chars": 0,
                "mode": "all",
                "model_settings": {
                    "max_output_tokens": 0,
                    "parallel_tool_calls": True,
                    "provider_type": "openai",
                    "reasoning": {"reasoning_effort": "none"},
                    "response_format": {"type": "text"},
                    "strict": True,
                    "temperature": 0,
                },
                "prompt": "prompt",
                "prompt_acknowledgement": True,
                "sliding_window_percentage": 0,
            },
            context_window_limit=0,
            description="description",
            embedding="embedding",
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
            enable_sleeptime=True,
            folder_ids=["string"],
            hidden=True,
            identity_ids=["string"],
            last_run_completion=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_run_duration_ms=0,
            last_stop_reason="end_turn",
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "compatibility_type": "gguf",
                "display_name": "display_name",
                "effort": "low",
                "enable_reasoner": True,
                "frequency_penalty": 0,
                "handle": "handle",
                "max_reasoning_tokens": 0,
                "max_tokens": 0,
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "parallel_tool_calls": True,
                "provider_category": "base",
                "provider_name": "provider_name",
                "put_inner_thoughts_in_kwargs": True,
                "reasoning_effort": "none",
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
                "tier": "tier",
                "verbosity": "low",
            },
            max_files_open=0,
            max_tokens=0,
            message_buffer_autoclear=True,
            message_ids=["string"],
            metadata={"foo": "bar"},
            model="model",
            model_settings={
                "max_output_tokens": 0,
                "parallel_tool_calls": True,
                "provider_type": "openai",
                "reasoning": {"reasoning_effort": "none"},
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
            },
            name="name",
            parallel_tool_calls=True,
            per_file_view_window_char_limit=0,
            project_id="project_id",
            reasoning=True,
            response_format={"type": "text"},
            secrets={"foo": "string"},
            source_ids=["string"],
            system="system",
            tags=["string"],
            template_id="template_id",
            timezone="timezone",
            tool_exec_environment_variables={"foo": "string"},
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "child_arg_nodes": [
                        {
                            "name": "name",
                            "args": {"foo": "bar"},
                        }
                    ],
                    "prompt_template": "prompt_template",
                    "type": "constrain_child_tools",
                }
            ],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        agent = client.agents.list()
        assert_matches_type(SyncArrayPage[AgentState], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        agent = client.agents.list(
            after="after",
            ascending=True,
            base_template_id="base_template_id",
            before="before",
            identifier_keys=["string", "string"],
            identity_id="identity_id",
            include=["agent.blocks"],
            include_relationships=["string", "string"],
            last_stop_reason="end_turn",
            limit=0,
            match_all_tags=True,
            name="name",
            order="asc",
            order_by="created_at",
            project_id="project_id",
            query_text="query_text",
            sort_by="sort_by",
            tags=["string", "string"],
            template_id="template_id",
        )
        assert_matches_type(SyncArrayPage[AgentState], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(SyncArrayPage[AgentState], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(SyncArrayPage[AgentState], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        agent = client.agents.delete(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.agents.with_raw_response.delete(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.agents.with_streaming_response.delete(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_file(self, client: Letta) -> None:
        agent = client.agents.export_file(
            agent_id="agent_id",
        )
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_file_with_all_params(self, client: Letta) -> None:
        agent = client.agents.export_file(
            agent_id="agent_id",
            max_steps=0,
            use_legacy_format=True,
        )
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export_file(self, client: Letta) -> None:
        response = client.agents.with_raw_response.export_file(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export_file(self, client: Letta) -> None:
        with client.agents.with_streaming_response.export_file(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(str, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_export_file(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.export_file(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_file(self, client: Letta) -> None:
        agent = client.agents.import_file(
            file=b"raw file contents",
        )
        assert_matches_type(AgentImportFileResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_file_with_all_params(self, client: Letta) -> None:
        agent = client.agents.import_file(
            file=b"raw file contents",
            append_copy_suffix=True,
            embedding="embedding",
            env_vars_json="env_vars_json",
            name="name",
            override_embedding_handle="override_embedding_handle",
            override_existing_tools=True,
            override_name="override_name",
            project_id="project_id",
            secrets="secrets",
            strip_messages=True,
            x_override_embedding_model="x-override-embedding-model",
        )
        assert_matches_type(AgentImportFileResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import_file(self, client: Letta) -> None:
        response = client.agents.with_raw_response.import_file(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentImportFileResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import_file(self, client: Letta) -> None:
        with client.agents.with_streaming_response.import_file(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentImportFileResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.create()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.create(
            agent_type="memgpt_agent",
            base_template_id="base_template_id",
            block_ids=["string"],
            compaction_settings={
                "model": "model",
                "clip_chars": 0,
                "mode": "all",
                "model_settings": {
                    "max_output_tokens": 0,
                    "parallel_tool_calls": True,
                    "provider_type": "openai",
                    "reasoning": {"reasoning_effort": "none"},
                    "response_format": {"type": "text"},
                    "strict": True,
                    "temperature": 0,
                },
                "prompt": "prompt",
                "prompt_acknowledgement": True,
                "sliding_window_percentage": 0,
            },
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
            folder_ids=["string"],
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
                            "signature": "signature",
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
                "display_name": "display_name",
                "effort": "low",
                "enable_reasoner": True,
                "frequency_penalty": 0,
                "handle": "handle",
                "max_reasoning_tokens": 0,
                "max_tokens": 0,
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "parallel_tool_calls": True,
                "provider_category": "base",
                "provider_name": "provider_name",
                "put_inner_thoughts_in_kwargs": True,
                "reasoning_effort": "none",
                "response_format": {"type": "text"},
                "strict": True,
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
                    "preserve_on_migration": True,
                    "project_id": "project_id",
                    "read_only": True,
                    "tags": ["string"],
                    "template_id": "template_id",
                    "template_name": "template_name",
                }
            ],
            memory_variables={"foo": "string"},
            message_buffer_autoclear=True,
            metadata={"foo": "bar"},
            model="model",
            model_settings={
                "max_output_tokens": 0,
                "parallel_tool_calls": True,
                "provider_type": "openai",
                "reasoning": {"reasoning_effort": "none"},
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
            },
            name="name",
            parallel_tool_calls=True,
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
            template_id="template_id",
            timezone="timezone",
            tool_exec_environment_variables={"foo": "string"},
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "child_arg_nodes": [
                        {
                            "name": "name",
                            "args": {"foo": "bar"},
                        }
                    ],
                    "prompt_template": "prompt_template",
                    "type": "constrain_child_tools",
                }
            ],
            tools=["string"],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.retrieve(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.retrieve(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            include=["agent.blocks"],
            include_relationships=["string", "string"],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.update(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.update(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            base_template_id="base_template_id",
            block_ids=["string"],
            compaction_settings={
                "model": "model",
                "clip_chars": 0,
                "mode": "all",
                "model_settings": {
                    "max_output_tokens": 0,
                    "parallel_tool_calls": True,
                    "provider_type": "openai",
                    "reasoning": {"reasoning_effort": "none"},
                    "response_format": {"type": "text"},
                    "strict": True,
                    "temperature": 0,
                },
                "prompt": "prompt",
                "prompt_acknowledgement": True,
                "sliding_window_percentage": 0,
            },
            context_window_limit=0,
            description="description",
            embedding="embedding",
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
            enable_sleeptime=True,
            folder_ids=["string"],
            hidden=True,
            identity_ids=["string"],
            last_run_completion=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_run_duration_ms=0,
            last_stop_reason="end_turn",
            llm_config={
                "context_window": 0,
                "model": "model",
                "model_endpoint_type": "openai",
                "compatibility_type": "gguf",
                "display_name": "display_name",
                "effort": "low",
                "enable_reasoner": True,
                "frequency_penalty": 0,
                "handle": "handle",
                "max_reasoning_tokens": 0,
                "max_tokens": 0,
                "model_endpoint": "model_endpoint",
                "model_wrapper": "model_wrapper",
                "parallel_tool_calls": True,
                "provider_category": "base",
                "provider_name": "provider_name",
                "put_inner_thoughts_in_kwargs": True,
                "reasoning_effort": "none",
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
                "tier": "tier",
                "verbosity": "low",
            },
            max_files_open=0,
            max_tokens=0,
            message_buffer_autoclear=True,
            message_ids=["string"],
            metadata={"foo": "bar"},
            model="model",
            model_settings={
                "max_output_tokens": 0,
                "parallel_tool_calls": True,
                "provider_type": "openai",
                "reasoning": {"reasoning_effort": "none"},
                "response_format": {"type": "text"},
                "strict": True,
                "temperature": 0,
            },
            name="name",
            parallel_tool_calls=True,
            per_file_view_window_char_limit=0,
            project_id="project_id",
            reasoning=True,
            response_format={"type": "text"},
            secrets={"foo": "string"},
            source_ids=["string"],
            system="system",
            tags=["string"],
            template_id="template_id",
            timezone="timezone",
            tool_exec_environment_variables={"foo": "string"},
            tool_ids=["string"],
            tool_rules=[
                {
                    "children": ["string"],
                    "tool_name": "tool_name",
                    "child_arg_nodes": [
                        {
                            "name": "name",
                            "args": {"foo": "bar"},
                        }
                    ],
                    "prompt_template": "prompt_template",
                    "type": "constrain_child_tools",
                }
            ],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AsyncArrayPage[AgentState], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.list(
            after="after",
            ascending=True,
            base_template_id="base_template_id",
            before="before",
            identifier_keys=["string", "string"],
            identity_id="identity_id",
            include=["agent.blocks"],
            include_relationships=["string", "string"],
            last_stop_reason="end_turn",
            limit=0,
            match_all_tags=True,
            name="name",
            order="asc",
            order_by="created_at",
            project_id="project_id",
            query_text="query_text",
            sort_by="sort_by",
            tags=["string", "string"],
            template_id="template_id",
        )
        assert_matches_type(AsyncArrayPage[AgentState], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AsyncArrayPage[AgentState], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AsyncArrayPage[AgentState], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.delete(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_file(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.export_file(
            agent_id="agent_id",
        )
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_file_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.export_file(
            agent_id="agent_id",
            max_steps=0,
            use_legacy_format=True,
        )
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export_file(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.export_file(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export_file(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.export_file(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(str, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_export_file(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.export_file(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_file(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.import_file(
            file=b"raw file contents",
        )
        assert_matches_type(AgentImportFileResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_file_with_all_params(self, async_client: AsyncLetta) -> None:
        agent = await async_client.agents.import_file(
            file=b"raw file contents",
            append_copy_suffix=True,
            embedding="embedding",
            env_vars_json="env_vars_json",
            name="name",
            override_embedding_handle="override_embedding_handle",
            override_existing_tools=True,
            override_name="override_name",
            project_id="project_id",
            secrets="secrets",
            strip_messages=True,
            x_override_embedding_model="x-override-embedding-model",
        )
        assert_matches_type(AgentImportFileResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import_file(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.with_raw_response.import_file(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentImportFileResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import_file(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.with_streaming_response.import_file(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentImportFileResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
