# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    TemplateForkResponse,
    TemplateListResponse,
    TemplateCreateResponse,
    TemplateDeleteResponse,
    TemplateRenameResponse,
    TemplateGetSnapshotResponse,
    TemplateSaveVersionResponse,
    TemplateCreateAgentsResponse,
    TemplateListVersionsResponse,
    TemplateUpdateDescriptionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: LettaSDK) -> None:
        template = client.templates.create(
            project="project",
            agent_id="agent_id",
            type="agent",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: LettaSDK) -> None:
        template = client.templates.create(
            project="project",
            agent_id="agent_id",
            type="agent",
            name="name",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.create(
            project="project",
            agent_id="agent_id",
            type="agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.create(
            project="project",
            agent_id="agent_id",
            type="agent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.create(
                project="",
                agent_id="agent_id",
                type="agent",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: LettaSDK) -> None:
        template = client.templates.create(
            project="project",
            agent_file={"foo": "bar"},
            type="agent_file",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: LettaSDK) -> None:
        template = client.templates.create(
            project="project",
            agent_file={"foo": "bar"},
            type="agent_file",
            name="name",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.create(
            project="project",
            agent_file={"foo": "bar"},
            type="agent_file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.create(
            project="project",
            agent_file={"foo": "bar"},
            type="agent_file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.create(
                project="",
                agent_file={"foo": "bar"},
                type="agent_file",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        template = client.templates.list()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        template = client.templates.list(
            exact="exact",
            limit="limit",
            name="name",
            offset="string",
            project_id="project_id",
            project_slug="project_slug",
            search="search",
            sort_by="updated_at",
            template_id="template_id",
            version="version",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        template = client.templates.delete(
            template_name="template_name",
            project="project",
        )
        assert_matches_type(TemplateDeleteResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.delete(
            template_name="template_name",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateDeleteResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.delete(
            template_name="template_name",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateDeleteResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.delete(
                template_name="template_name",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            client.templates.with_raw_response.delete(
                template_name="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_agents(self, client: LettaSDK) -> None:
        template = client.templates.create_agents(
            template_version="template_version",
            project="project",
        )
        assert_matches_type(TemplateCreateAgentsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_agents_with_all_params(self, client: LettaSDK) -> None:
        template = client.templates.create_agents(
            template_version="template_version",
            project="project",
            agent_name="agent_name",
            identity_ids=["string"],
            initial_message_sequence=[
                {
                    "content": "content",
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                }
            ],
            memory_variables={"foo": "string"},
            tags=["-_"],
            tool_variables={"foo": "string"},
        )
        assert_matches_type(TemplateCreateAgentsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_agents(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.create_agents(
            template_version="template_version",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateAgentsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_agents(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.create_agents(
            template_version="template_version",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateCreateAgentsResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_agents(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.create_agents(
                template_version="template_version",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_version` but received ''"):
            client.templates.with_raw_response.create_agents(
                template_version="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fork(self, client: LettaSDK) -> None:
        template = client.templates.fork(
            template_version="template_version",
            project="project",
        )
        assert_matches_type(TemplateForkResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fork_with_all_params(self, client: LettaSDK) -> None:
        template = client.templates.fork(
            template_version="template_version",
            project="project",
            name="name",
        )
        assert_matches_type(TemplateForkResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_fork(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.fork(
            template_version="template_version",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateForkResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_fork(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.fork(
            template_version="template_version",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateForkResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_fork(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.fork(
                template_version="template_version",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_version` but received ''"):
            client.templates.with_raw_response.fork(
                template_version="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_snapshot(self, client: LettaSDK) -> None:
        template = client.templates.get_snapshot(
            template_version="template_version",
            project="project",
        )
        assert_matches_type(TemplateGetSnapshotResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_snapshot(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.get_snapshot(
            template_version="template_version",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateGetSnapshotResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_snapshot(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.get_snapshot(
            template_version="template_version",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateGetSnapshotResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_snapshot(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.get_snapshot(
                template_version="template_version",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_version` but received ''"):
            client.templates.with_raw_response.get_snapshot(
                template_version="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_versions(self, client: LettaSDK) -> None:
        template = client.templates.list_versions(
            name="name",
            project_slug="project_slug",
        )
        assert_matches_type(TemplateListVersionsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_versions_with_all_params(self, client: LettaSDK) -> None:
        template = client.templates.list_versions(
            name="name",
            project_slug="project_slug",
            limit="limit",
            offset="string",
        )
        assert_matches_type(TemplateListVersionsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_versions(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.list_versions(
            name="name",
            project_slug="project_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListVersionsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_versions(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.list_versions(
            name="name",
            project_slug="project_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListVersionsResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_versions(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_slug` but received ''"):
            client.templates.with_raw_response.list_versions(
                name="name",
                project_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.templates.with_raw_response.list_versions(
                name="",
                project_slug="project_slug",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rename(self, client: LettaSDK) -> None:
        template = client.templates.rename(
            template_name="template_name",
            project="project",
            new_name="new_name",
        )
        assert_matches_type(TemplateRenameResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rename(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.rename(
            template_name="template_name",
            project="project",
            new_name="new_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateRenameResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rename(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.rename(
            template_name="template_name",
            project="project",
            new_name="new_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateRenameResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_rename(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.rename(
                template_name="template_name",
                project="",
                new_name="new_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            client.templates.with_raw_response.rename(
                template_name="",
                project="project",
                new_name="new_name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_save_version(self, client: LettaSDK) -> None:
        template = client.templates.save_version(
            template_name="template_name",
            project="project",
        )
        assert_matches_type(TemplateSaveVersionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_save_version_with_all_params(self, client: LettaSDK) -> None:
        template = client.templates.save_version(
            template_name="template_name",
            project="project",
            message="message",
            migrate_agents=True,
            preserve_core_memories_on_migration=True,
            preserve_environment_variables_on_migration=True,
        )
        assert_matches_type(TemplateSaveVersionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_save_version(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.save_version(
            template_name="template_name",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateSaveVersionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_save_version(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.save_version(
            template_name="template_name",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateSaveVersionResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_save_version(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.save_version(
                template_name="template_name",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            client.templates.with_raw_response.save_version(
                template_name="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_description(self, client: LettaSDK) -> None:
        template = client.templates.update_description(
            template_name="template_name",
            project="project",
        )
        assert_matches_type(TemplateUpdateDescriptionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_description_with_all_params(self, client: LettaSDK) -> None:
        template = client.templates.update_description(
            template_name="template_name",
            project="project",
            description="description",
        )
        assert_matches_type(TemplateUpdateDescriptionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_description(self, client: LettaSDK) -> None:
        response = client.templates.with_raw_response.update_description(
            template_name="template_name",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateUpdateDescriptionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_description(self, client: LettaSDK) -> None:
        with client.templates.with_streaming_response.update_description(
            template_name="template_name",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateUpdateDescriptionResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_description(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.templates.with_raw_response.update_description(
                template_name="template_name",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            client.templates.with_raw_response.update_description(
                template_name="",
                project="project",
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.create(
            project="project",
            agent_id="agent_id",
            type="agent",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.create(
            project="project",
            agent_id="agent_id",
            type="agent",
            name="name",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.create(
            project="project",
            agent_id="agent_id",
            type="agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.create(
            project="project",
            agent_id="agent_id",
            type="agent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.create(
                project="",
                agent_id="agent_id",
                type="agent",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.create(
            project="project",
            agent_file={"foo": "bar"},
            type="agent_file",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.create(
            project="project",
            agent_file={"foo": "bar"},
            type="agent_file",
            name="name",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.create(
            project="project",
            agent_file={"foo": "bar"},
            type="agent_file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.create(
            project="project",
            agent_file={"foo": "bar"},
            type="agent_file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.create(
                project="",
                agent_file={"foo": "bar"},
                type="agent_file",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.list()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.list(
            exact="exact",
            limit="limit",
            name="name",
            offset="string",
            project_id="project_id",
            project_slug="project_slug",
            search="search",
            sort_by="updated_at",
            template_id="template_id",
            version="version",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.delete(
            template_name="template_name",
            project="project",
        )
        assert_matches_type(TemplateDeleteResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.delete(
            template_name="template_name",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateDeleteResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.delete(
            template_name="template_name",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateDeleteResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.delete(
                template_name="template_name",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            await async_client.templates.with_raw_response.delete(
                template_name="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_agents(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.create_agents(
            template_version="template_version",
            project="project",
        )
        assert_matches_type(TemplateCreateAgentsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_agents_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.create_agents(
            template_version="template_version",
            project="project",
            agent_name="agent_name",
            identity_ids=["string"],
            initial_message_sequence=[
                {
                    "content": "content",
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                }
            ],
            memory_variables={"foo": "string"},
            tags=["-_"],
            tool_variables={"foo": "string"},
        )
        assert_matches_type(TemplateCreateAgentsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_agents(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.create_agents(
            template_version="template_version",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateAgentsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_agents(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.create_agents(
            template_version="template_version",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateCreateAgentsResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_agents(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.create_agents(
                template_version="template_version",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_version` but received ''"):
            await async_client.templates.with_raw_response.create_agents(
                template_version="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fork(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.fork(
            template_version="template_version",
            project="project",
        )
        assert_matches_type(TemplateForkResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fork_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.fork(
            template_version="template_version",
            project="project",
            name="name",
        )
        assert_matches_type(TemplateForkResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_fork(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.fork(
            template_version="template_version",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateForkResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_fork(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.fork(
            template_version="template_version",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateForkResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_fork(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.fork(
                template_version="template_version",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_version` but received ''"):
            await async_client.templates.with_raw_response.fork(
                template_version="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_snapshot(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.get_snapshot(
            template_version="template_version",
            project="project",
        )
        assert_matches_type(TemplateGetSnapshotResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_snapshot(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.get_snapshot(
            template_version="template_version",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateGetSnapshotResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_snapshot(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.get_snapshot(
            template_version="template_version",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateGetSnapshotResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_snapshot(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.get_snapshot(
                template_version="template_version",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_version` but received ''"):
            await async_client.templates.with_raw_response.get_snapshot(
                template_version="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_versions(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.list_versions(
            name="name",
            project_slug="project_slug",
        )
        assert_matches_type(TemplateListVersionsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_versions_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.list_versions(
            name="name",
            project_slug="project_slug",
            limit="limit",
            offset="string",
        )
        assert_matches_type(TemplateListVersionsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_versions(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.list_versions(
            name="name",
            project_slug="project_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListVersionsResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_versions(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.list_versions(
            name="name",
            project_slug="project_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListVersionsResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_versions(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_slug` but received ''"):
            await async_client.templates.with_raw_response.list_versions(
                name="name",
                project_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.templates.with_raw_response.list_versions(
                name="",
                project_slug="project_slug",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rename(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.rename(
            template_name="template_name",
            project="project",
            new_name="new_name",
        )
        assert_matches_type(TemplateRenameResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rename(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.rename(
            template_name="template_name",
            project="project",
            new_name="new_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateRenameResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rename(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.rename(
            template_name="template_name",
            project="project",
            new_name="new_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateRenameResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_rename(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.rename(
                template_name="template_name",
                project="",
                new_name="new_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            await async_client.templates.with_raw_response.rename(
                template_name="",
                project="project",
                new_name="new_name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_save_version(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.save_version(
            template_name="template_name",
            project="project",
        )
        assert_matches_type(TemplateSaveVersionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_save_version_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.save_version(
            template_name="template_name",
            project="project",
            message="message",
            migrate_agents=True,
            preserve_core_memories_on_migration=True,
            preserve_environment_variables_on_migration=True,
        )
        assert_matches_type(TemplateSaveVersionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_save_version(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.save_version(
            template_name="template_name",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateSaveVersionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_save_version(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.save_version(
            template_name="template_name",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateSaveVersionResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_save_version(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.save_version(
                template_name="template_name",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            await async_client.templates.with_raw_response.save_version(
                template_name="",
                project="project",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_description(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.update_description(
            template_name="template_name",
            project="project",
        )
        assert_matches_type(TemplateUpdateDescriptionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_description_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        template = await async_client.templates.update_description(
            template_name="template_name",
            project="project",
            description="description",
        )
        assert_matches_type(TemplateUpdateDescriptionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_description(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.templates.with_raw_response.update_description(
            template_name="template_name",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateUpdateDescriptionResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_description(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.templates.with_streaming_response.update_description(
            template_name="template_name",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateUpdateDescriptionResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_description(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.templates.with_raw_response.update_description(
                template_name="template_name",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            await async_client.templates.with_raw_response.update_description(
                template_name="",
                project="project",
            )
