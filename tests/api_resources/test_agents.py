# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    AgentState,
    AgentListResponse,
    AgentCountResponse,
    AgentImportResponse,
    AgentSearchResponse,
    AgentMigrateResponse,
    AgentListGroupsResponse,
    AgentRetrieveContextResponse,
)
from letta_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LettaSDK) -> None:
        agent = client.agents.create()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.create(
            agent_type="memgpt_agent",
            base_template_id="base_template_id",
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
            template_id="template_id",
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
            x_project="X-Project",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        agent = client.agents.retrieve(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.retrieve(
            agent_id="agent_id",
            include_relationships=["string"],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.retrieve(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.retrieve(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LettaSDK) -> None:
        agent = client.agents.update(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.update(
            agent_id="agent_id",
            base_template_id="base_template_id",
            block_ids=["string"],
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
            hidden=True,
            identity_ids=["string"],
            last_run_completion=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_run_duration_ms=0,
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
            message_buffer_autoclear=True,
            message_ids=["string"],
            metadata={"foo": "bar"},
            model="model",
            name="name",
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
                    "prompt_template": "prompt_template",
                    "type": "constrain_child_tools",
                }
            ],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        agent = client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.list(
            after="after",
            ascending=True,
            base_template_id="base_template_id",
            before="before",
            identifier_keys=["string"],
            identity_id="identity_id",
            include_relationships=["string"],
            limit=0,
            match_all_tags=True,
            name="name",
            order="asc",
            order_by="created_at",
            project_id="project_id",
            query_text="query_text",
            sort_by="sort_by",
            tags=["string"],
            template_id="template_id",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        agent = client.agents.delete(
            "agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_count(self, client: LettaSDK) -> None:
        agent = client.agents.count()
        assert_matches_type(AgentCountResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCountResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCountResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export(self, client: LettaSDK) -> None:
        agent = client.agents.export(
            agent_id="agent_id",
        )
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.export(
            agent_id="agent_id",
            max_steps=0,
            use_legacy_format=True,
        )
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.export(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.export(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(str, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_export(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.export(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import(self, client: LettaSDK) -> None:
        agent = client.agents.import_(
            file=b"raw file contents",
        )
        assert_matches_type(AgentImportResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.import_(
            file=b"raw file contents",
            append_copy_suffix=True,
            env_vars_json="env_vars_json",
            override_embedding_handle="override_embedding_handle",
            override_existing_tools=True,
            project_id="project_id",
            strip_messages=True,
            x_override_embedding_model="x-override-embedding-model",
        )
        assert_matches_type(AgentImportResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.import_(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentImportResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.import_(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentImportResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_groups(self, client: LettaSDK) -> None:
        agent = client.agents.list_groups(
            agent_id="agent_id",
        )
        assert_matches_type(AgentListGroupsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_groups_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.list_groups(
            agent_id="agent_id",
            manager_type="manager_type",
        )
        assert_matches_type(AgentListGroupsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_groups(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.list_groups(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListGroupsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_groups(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.list_groups(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListGroupsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_groups(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.list_groups(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_migrate(self, client: LettaSDK) -> None:
        agent = client.agents.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        )
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_migrate_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
            preserve_tool_variables=True,
        )
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_migrate(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_migrate(self, client: LettaSDK) -> None:
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_migrate(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.migrate(
                agent_id="",
                preserve_core_memories=True,
                to_template="to_template",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_messages(self, client: LettaSDK) -> None:
        agent = client.agents.reset_messages(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_messages_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.reset_messages(
            agent_id="agent_id",
            add_default_initial_messages=True,
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_messages(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.reset_messages(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset_messages(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.reset_messages(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset_messages(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.reset_messages(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_context(self, client: LettaSDK) -> None:
        agent = client.agents.retrieve_context(
            "agent_id",
        )
        assert_matches_type(AgentRetrieveContextResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_context(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.retrieve_context(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveContextResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_context(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.retrieve_context(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveContextResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_context(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve_context(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: LettaSDK) -> None:
        agent = client.agents.search()
        assert_matches_type(AgentSearchResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: LettaSDK) -> None:
        agent = client.agents.search(
            after="after",
            ascending=True,
            combinator="AND",
            limit=0,
            project_id="project_id",
            search=[
                {
                    "field": "version",
                    "value": "value",
                }
            ],
            sort_by="created_at",
        )
        assert_matches_type(AgentSearchResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentSearchResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentSearchResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize(self, client: LettaSDK) -> None:
        agent = client.agents.summarize(
            agent_id="agent_id",
            max_message_length=0,
        )
        assert agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_summarize(self, client: LettaSDK) -> None:
        response = client.agents.with_raw_response.summarize(
            agent_id="agent_id",
            max_message_length=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_summarize(self, client: LettaSDK) -> None:
        with client.agents.with_streaming_response.summarize(
            agent_id="agent_id",
            max_message_length=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_summarize(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.summarize(
                agent_id="",
                max_message_length=0,
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.create()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.create(
            agent_type="memgpt_agent",
            base_template_id="base_template_id",
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
            template_id="template_id",
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
            x_project="X-Project",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.retrieve(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.retrieve(
            agent_id="agent_id",
            include_relationships=["string"],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.update(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.update(
            agent_id="agent_id",
            base_template_id="base_template_id",
            block_ids=["string"],
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
            hidden=True,
            identity_ids=["string"],
            last_run_completion=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_run_duration_ms=0,
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
            message_buffer_autoclear=True,
            message_ids=["string"],
            metadata={"foo": "bar"},
            model="model",
            name="name",
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
                    "prompt_template": "prompt_template",
                    "type": "constrain_child_tools",
                }
            ],
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.list(
            after="after",
            ascending=True,
            base_template_id="base_template_id",
            before="before",
            identifier_keys=["string"],
            identity_id="identity_id",
            include_relationships=["string"],
            limit=0,
            match_all_tags=True,
            name="name",
            order="asc",
            order_by="created_at",
            project_id="project_id",
            query_text="query_text",
            sort_by="sort_by",
            tags=["string"],
            template_id="template_id",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.delete(
            "agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.count()
        assert_matches_type(AgentCountResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCountResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCountResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.export(
            agent_id="agent_id",
        )
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.export(
            agent_id="agent_id",
            max_steps=0,
            use_legacy_format=True,
        )
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.export(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(str, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.export(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(str, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_export(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.export(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.import_(
            file=b"raw file contents",
        )
        assert_matches_type(AgentImportResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.import_(
            file=b"raw file contents",
            append_copy_suffix=True,
            env_vars_json="env_vars_json",
            override_embedding_handle="override_embedding_handle",
            override_existing_tools=True,
            project_id="project_id",
            strip_messages=True,
            x_override_embedding_model="x-override-embedding-model",
        )
        assert_matches_type(AgentImportResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.import_(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentImportResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.import_(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentImportResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_groups(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.list_groups(
            agent_id="agent_id",
        )
        assert_matches_type(AgentListGroupsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_groups_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.list_groups(
            agent_id="agent_id",
            manager_type="manager_type",
        )
        assert_matches_type(AgentListGroupsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_groups(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.list_groups(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListGroupsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_groups(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.list_groups(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListGroupsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_groups(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.list_groups(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_migrate(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        )
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_migrate_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
            preserve_tool_variables=True,
        )
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_migrate(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.migrate(
            agent_id="agent_id",
            preserve_core_memories=True,
            to_template="to_template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentMigrateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_migrate(self, async_client: AsyncLettaSDK) -> None:
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_migrate(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.migrate(
                agent_id="",
                preserve_core_memories=True,
                to_template="to_template",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_messages(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.reset_messages(
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_messages_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.reset_messages(
            agent_id="agent_id",
            add_default_initial_messages=True,
        )
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_messages(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.reset_messages(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentState, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset_messages(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.reset_messages(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentState, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset_messages(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.reset_messages(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_context(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.retrieve_context(
            "agent_id",
        )
        assert_matches_type(AgentRetrieveContextResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_context(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.retrieve_context(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveContextResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_context(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.retrieve_context(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveContextResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_context(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve_context(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.search()
        assert_matches_type(AgentSearchResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.search(
            after="after",
            ascending=True,
            combinator="AND",
            limit=0,
            project_id="project_id",
            search=[
                {
                    "field": "version",
                    "value": "value",
                }
            ],
            sort_by="created_at",
        )
        assert_matches_type(AgentSearchResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentSearchResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentSearchResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize(self, async_client: AsyncLettaSDK) -> None:
        agent = await async_client.agents.summarize(
            agent_id="agent_id",
            max_message_length=0,
        )
        assert agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.with_raw_response.summarize(
            agent_id="agent_id",
            max_message_length=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.with_streaming_response.summarize(
            agent_id="agent_id",
            max_message_length=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_summarize(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.summarize(
                agent_id="",
                max_message_length=0,
            )
