# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    TemplateCreateResponse,
    TemplateDeleteResponse,
    TemplateUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Letta) -> None:
        template = client.templates.create(
            agent_id="agent_id",
            type="agent",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Letta) -> None:
        template = client.templates.create(
            agent_id="agent_id",
            type="agent",
            name="name",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Letta) -> None:
        response = client.templates.with_raw_response.create(
            agent_id="agent_id",
            type="agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Letta) -> None:
        with client.templates.with_streaming_response.create(
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
    def test_method_create_overload_2(self, client: Letta) -> None:
        template = client.templates.create(
            agent_file={"foo": "bar"},
            type="agent_file",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Letta) -> None:
        template = client.templates.create(
            agent_file={"foo": "bar"},
            type="agent_file",
            name="name",
            update_existing_tools=True,
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Letta) -> None:
        response = client.templates.with_raw_response.create(
            agent_file={"foo": "bar"},
            type="agent_file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Letta) -> None:
        with client.templates.with_streaming_response.create(
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
    def test_method_update(self, client: Letta) -> None:
        template = client.templates.update(
            template_name="template_name",
            agent_file_json={"foo": "bar"},
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        template = client.templates.update(
            template_name="template_name",
            agent_file_json={"foo": "bar"},
            save_existing_changes=True,
            update_existing_tools=True,
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.templates.with_raw_response.update(
            template_name="template_name",
            agent_file_json={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.templates.with_streaming_response.update(
            template_name="template_name",
            agent_file_json={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateUpdateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            client.templates.with_raw_response.update(
                template_name="",
                agent_file_json={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        template = client.templates.delete(
            "template_name",
        )
        assert_matches_type(TemplateDeleteResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.templates.with_raw_response.delete(
            "template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateDeleteResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.templates.with_streaming_response.delete(
            "template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateDeleteResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            client.templates.with_raw_response.delete(
                "",
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLetta) -> None:
        template = await async_client.templates.create(
            agent_id="agent_id",
            type="agent",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLetta) -> None:
        template = await async_client.templates.create(
            agent_id="agent_id",
            type="agent",
            name="name",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLetta) -> None:
        response = await async_client.templates.with_raw_response.create(
            agent_id="agent_id",
            type="agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLetta) -> None:
        async with async_client.templates.with_streaming_response.create(
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
    async def test_method_create_overload_2(self, async_client: AsyncLetta) -> None:
        template = await async_client.templates.create(
            agent_file={"foo": "bar"},
            type="agent_file",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLetta) -> None:
        template = await async_client.templates.create(
            agent_file={"foo": "bar"},
            type="agent_file",
            name="name",
            update_existing_tools=True,
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLetta) -> None:
        response = await async_client.templates.with_raw_response.create(
            agent_file={"foo": "bar"},
            type="agent_file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLetta) -> None:
        async with async_client.templates.with_streaming_response.create(
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
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        template = await async_client.templates.update(
            template_name="template_name",
            agent_file_json={"foo": "bar"},
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        template = await async_client.templates.update(
            template_name="template_name",
            agent_file_json={"foo": "bar"},
            save_existing_changes=True,
            update_existing_tools=True,
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.templates.with_raw_response.update(
            template_name="template_name",
            agent_file_json={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.templates.with_streaming_response.update(
            template_name="template_name",
            agent_file_json={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateUpdateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            await async_client.templates.with_raw_response.update(
                template_name="",
                agent_file_json={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        template = await async_client.templates.delete(
            "template_name",
        )
        assert_matches_type(TemplateDeleteResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.templates.with_raw_response.delete(
            "template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateDeleteResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.templates.with_streaming_response.delete(
            "template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateDeleteResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            await async_client.templates.with_raw_response.delete(
                "",
            )
