# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    Tool,
    ToolSearchResponse,
    ToolUpsertBaseToolsResponse,
)
from letta_client.pagination import SyncArrayPage, AsyncArrayPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        tool = client.tools.create(
            source_code="source_code",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        tool = client.tools.create(
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            enable_parallel_execution=True,
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
            return_char_limit=1,
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.tools.with_raw_response.create(
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
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
    def test_method_retrieve(self, client: Letta) -> None:
        tool = client.tools.retrieve(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.tools.with_raw_response.retrieve(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.tools.with_streaming_response.retrieve(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Letta) -> None:
        tool = client.tools.update(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        tool = client.tools.update(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            enable_parallel_execution=True,
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
            return_char_limit=1,
            source_code="source_code",
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.tools.with_raw_response.update(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.tools.with_streaming_response.update(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.update(
                tool_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        tool = client.tools.list()
        assert_matches_type(SyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        tool = client.tools.list(
            after="after",
            before="before",
            exclude_tool_types=["string", "string"],
            limit=0,
            name="name",
            names=["string", "string"],
            order="asc",
            order_by="created_at",
            return_only_letta_tools=True,
            search="search",
            tool_ids=["string", "string"],
            tool_types=["string", "string"],
        )
        assert_matches_type(SyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(SyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(SyncArrayPage[Tool], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        tool = client.tools.delete(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.tools.with_raw_response.delete(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.tools.with_streaming_response.delete(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Letta) -> None:
        tool = client.tools.search()
        assert_matches_type(ToolSearchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Letta) -> None:
        tool = client.tools.search(
            limit=1,
            query="query",
            search_mode="vector",
            tags=["string"],
            tool_types=["string"],
        )
        assert_matches_type(ToolSearchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Letta) -> None:
        response = client.tools.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolSearchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Letta) -> None:
        with client.tools.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolSearchResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Letta) -> None:
        tool = client.tools.upsert(
            source_code="source_code",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Letta) -> None:
        tool = client.tools.upsert(
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            enable_parallel_execution=True,
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
            return_char_limit=1,
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Letta) -> None:
        response = client.tools.with_raw_response.upsert(
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Letta) -> None:
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
    def test_method_upsert_base_tools(self, client: Letta) -> None:
        tool = client.tools.upsert_base_tools()
        assert_matches_type(ToolUpsertBaseToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert_base_tools(self, client: Letta) -> None:
        response = client.tools.with_raw_response.upsert_base_tools()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolUpsertBaseToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert_base_tools(self, client: Letta) -> None:
        with client.tools.with_streaming_response.upsert_base_tools() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolUpsertBaseToolsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.create(
            source_code="source_code",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.create(
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            enable_parallel_execution=True,
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
            return_char_limit=1,
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.create(
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
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
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.retrieve(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.retrieve(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.retrieve(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.update(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.update(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            enable_parallel_execution=True,
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
            return_char_limit=1,
            source_code="source_code",
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.update(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.update(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.update(
                tool_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(AsyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.list(
            after="after",
            before="before",
            exclude_tool_types=["string", "string"],
            limit=0,
            name="name",
            names=["string", "string"],
            order="asc",
            order_by="created_at",
            return_only_letta_tools=True,
            search="search",
            tool_ids=["string", "string"],
            tool_types=["string", "string"],
        )
        assert_matches_type(AsyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AsyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AsyncArrayPage[Tool], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.delete(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.delete(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.delete(
            "tool-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.search()
        assert_matches_type(ToolSearchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.search(
            limit=1,
            query="query",
            search_mode="vector",
            tags=["string"],
            tool_types=["string"],
        )
        assert_matches_type(ToolSearchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolSearchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolSearchResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.upsert(
            source_code="source_code",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.upsert(
            source_code="source_code",
            args_json_schema={"foo": "bar"},
            default_requires_approval=True,
            description="description",
            enable_parallel_execution=True,
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
            return_char_limit=1,
            source_type="source_type",
            tags=["string"],
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.upsert(
            source_code="source_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLetta) -> None:
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
    async def test_method_upsert_base_tools(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.upsert_base_tools()
        assert_matches_type(ToolUpsertBaseToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert_base_tools(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.upsert_base_tools()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolUpsertBaseToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert_base_tools(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.upsert_base_tools() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolUpsertBaseToolsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
