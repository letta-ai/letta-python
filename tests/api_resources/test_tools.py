# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    Tool,
    ToolListResponse,
    ToolCountResponse,
    ToolReturnMessage,
    ToolUpsertBaseResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LettaSDK) -> None:
        tool = client.tools.create(
            source_code="source_code",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LettaSDK) -> None:
        tool = client.tools.create(
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            json_schema={"foo": "bar"},
            npm_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            pip_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            return_char_limit=0,
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.create(
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.create(
            source_code="source_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        tool = client.tools.retrieve(
            "tool_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.retrieve(
            "tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.retrieve(
            "tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        tool = client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        tool = client.tools.list(
            after="after",
            before="before",
            exclude_tool_types=["string"],
            limit=0,
            name="name",
            names=["string"],
            order="asc",
            order_by="created_at",
            return_only_letta_tools=True,
            search="search",
            tool_ids=["string"],
            tool_types=["string"],
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        tool = client.tools.delete(
            "tool_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.delete(
            "tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.delete(
            "tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_count(self, client: LettaSDK) -> None:
        tool = client.tools.count()
        assert_matches_type(ToolCountResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_count_with_all_params(self, client: LettaSDK) -> None:
        tool = client.tools.count(
            exclude_letta_tools=True,
            exclude_tool_types=["string"],
            name="name",
            names=["string"],
            return_only_letta_tools=True,
            search="search",
            tool_ids=["string"],
            tool_types=["string"],
        )
        assert_matches_type(ToolCountResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCountResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCountResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify(self, client: LettaSDK) -> None:
        tool = client.tools.modify(
            tool_id="tool_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_with_all_params(self, client: LettaSDK) -> None:
        tool = client.tools.modify(
            tool_id="tool_id",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            json_schema={"foo": "bar"},
            metadata={"foo": "bar"},
            npm_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            pip_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            return_char_limit=0,
            source_code="source_code",
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_modify(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.modify(
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_modify(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.modify(
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_modify(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.modify(
                tool_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: LettaSDK) -> None:
        tool = client.tools.run(
            args={"foo": "bar"},
            source_code="source_code",
        )
        assert_matches_type(ToolReturnMessage, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: LettaSDK) -> None:
        tool = client.tools.run(
            args={"foo": "bar"},
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            env_vars={"foo": "string"},
            json_schema={"foo": "bar"},
            name="name",
            npm_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            pip_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            source_type="source_type",
        )
        assert_matches_type(ToolReturnMessage, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.run(
            args={"foo": "bar"},
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolReturnMessage, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.run(
            args={"foo": "bar"},
            source_code="source_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolReturnMessage, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: LettaSDK) -> None:
        tool = client.tools.upsert(
            source_code="source_code",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: LettaSDK) -> None:
        tool = client.tools.upsert(
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            json_schema={"foo": "bar"},
            npm_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            pip_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            return_char_limit=0,
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.upsert(
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.upsert(
            source_code="source_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_base(self, client: LettaSDK) -> None:
        tool = client.tools.upsert_base()
        assert_matches_type(ToolUpsertBaseResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert_base(self, client: LettaSDK) -> None:
        response = client.tools.with_raw_response.upsert_base()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolUpsertBaseResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert_base(self, client: LettaSDK) -> None:
        with client.tools.with_streaming_response.upsert_base() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolUpsertBaseResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.create(
            source_code="source_code",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.create(
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            json_schema={"foo": "bar"},
            npm_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            pip_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            return_char_limit=0,
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.create(
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.create(
            source_code="source_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.retrieve(
            "tool_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.retrieve(
            "tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.retrieve(
            "tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.list(
            after="after",
            before="before",
            exclude_tool_types=["string"],
            limit=0,
            name="name",
            names=["string"],
            order="asc",
            order_by="created_at",
            return_only_letta_tools=True,
            search="search",
            tool_ids=["string"],
            tool_types=["string"],
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.delete(
            "tool_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.delete(
            "tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.delete(
            "tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.count()
        assert_matches_type(ToolCountResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.count(
            exclude_letta_tools=True,
            exclude_tool_types=["string"],
            name="name",
            names=["string"],
            return_only_letta_tools=True,
            search="search",
            tool_ids=["string"],
            tool_types=["string"],
        )
        assert_matches_type(ToolCountResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCountResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCountResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.modify(
            tool_id="tool_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.modify(
            tool_id="tool_id",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            json_schema={"foo": "bar"},
            metadata={"foo": "bar"},
            npm_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            pip_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            return_char_limit=0,
            source_code="source_code",
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_modify(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.modify(
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_modify(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.modify(
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_modify(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.modify(
                tool_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.run(
            args={"foo": "bar"},
            source_code="source_code",
        )
        assert_matches_type(ToolReturnMessage, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.run(
            args={"foo": "bar"},
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            env_vars={"foo": "string"},
            json_schema={"foo": "bar"},
            name="name",
            npm_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            pip_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            source_type="source_type",
        )
        assert_matches_type(ToolReturnMessage, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.run(
            args={"foo": "bar"},
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolReturnMessage, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.run(
            args={"foo": "bar"},
            source_code="source_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolReturnMessage, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.upsert(
            source_code="source_code",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.upsert(
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            json_schema={"foo": "bar"},
            npm_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            pip_requirements=[
                {
                    "name": "x",
                    "version": "version",
                }
            ],
            return_char_limit=0,
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.upsert(
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.upsert(
            source_code="source_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_base(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.upsert_base()
        assert_matches_type(ToolUpsertBaseResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert_base(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.with_raw_response.upsert_base()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolUpsertBaseResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert_base(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.with_streaming_response.upsert_base() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolUpsertBaseResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
