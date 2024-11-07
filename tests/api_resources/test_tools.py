# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from letta.types import (
    ToolListResponse,
    ToolAddBaseToolsResponse,
)
from tests.utils import assert_matches_type
from letta.types.shared import Tool

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        tool = client.tools.create(
            source_code="source_code",
            source_type="source_type",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        tool = client.tools.create(
            source_code="source_code",
            source_type="source_type",
            description="description",
            json_schema={},
            module="module",
            name="name",
            tags=["string", "string", "string"],
            user_id="user_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.tools.with_raw_response.create(
            source_code="source_code",
            source_type="source_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.tools.with_streaming_response.create(
            source_code="source_code",
            source_type="source_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        tool = client.tools.retrieve(
            tool_id="tool_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Letta) -> None:
        tool = client.tools.retrieve(
            tool_id="tool_id",
            user_id="user_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.tools.with_raw_response.retrieve(
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.tools.with_streaming_response.retrieve(
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.retrieve(
                tool_id="",
            )

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        tool = client.tools.update(
            tool_id="tool_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        tool = client.tools.update(
            tool_id="tool_id",
            description="description",
            json_schema={},
            module="module",
            name="name",
            source_code="source_code",
            source_type="source_type",
            tags=["string", "string", "string"],
            user_id="user_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.tools.with_raw_response.update(
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.tools.with_streaming_response.update(
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.update(
                tool_id="",
            )

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        tool = client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        tool = client.tools.list(
            cursor="cursor",
            limit=0,
            user_id="user_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        tool = client.tools.delete(
            tool_id="tool_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Letta) -> None:
        tool = client.tools.delete(
            tool_id="tool_id",
            user_id="user_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.tools.with_raw_response.delete(
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(object, tool, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.tools.with_streaming_response.delete(
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.with_raw_response.delete(
                tool_id="",
            )

    @parametrize
    def test_method_add_base_tools(self, client: Letta) -> None:
        tool = client.tools.add_base_tools()
        assert_matches_type(ToolAddBaseToolsResponse, tool, path=["response"])

    @parametrize
    def test_method_add_base_tools_with_all_params(self, client: Letta) -> None:
        tool = client.tools.add_base_tools(
            user_id="user_id",
        )
        assert_matches_type(ToolAddBaseToolsResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_add_base_tools(self, client: Letta) -> None:
        response = client.tools.with_raw_response.add_base_tools()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolAddBaseToolsResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_add_base_tools(self, client: Letta) -> None:
        with client.tools.with_streaming_response.add_base_tools() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolAddBaseToolsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_by_name(self, client: Letta) -> None:
        tool = client.tools.retrieve_by_name(
            tool_name="tool_name",
        )
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    def test_method_retrieve_by_name_with_all_params(self, client: Letta) -> None:
        tool = client.tools.retrieve_by_name(
            tool_name="tool_name",
            user_id="user_id",
        )
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve_by_name(self, client: Letta) -> None:
        response = client.tools.with_raw_response.retrieve_by_name(
            tool_name="tool_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_by_name(self, client: Letta) -> None:
        with client.tools.with_streaming_response.retrieve_by_name(
            tool_name="tool_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(str, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_by_name(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_name` but received ''"):
            client.tools.with_raw_response.retrieve_by_name(
                tool_name="",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.create(
            source_code="source_code",
            source_type="source_type",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.create(
            source_code="source_code",
            source_type="source_type",
            description="description",
            json_schema={},
            module="module",
            name="name",
            tags=["string", "string", "string"],
            user_id="user_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.create(
            source_code="source_code",
            source_type="source_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.create(
            source_code="source_code",
            source_type="source_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.retrieve(
            tool_id="tool_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.retrieve(
            tool_id="tool_id",
            user_id="user_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.retrieve(
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.retrieve(
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.retrieve(
                tool_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.update(
            tool_id="tool_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.update(
            tool_id="tool_id",
            description="description",
            json_schema={},
            module="module",
            name="name",
            source_code="source_code",
            source_type="source_type",
            tags=["string", "string", "string"],
            user_id="user_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.update(
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.update(
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.update(
                tool_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.list(
            cursor="cursor",
            limit=0,
            user_id="user_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.delete(
            tool_id="tool_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.delete(
            tool_id="tool_id",
            user_id="user_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.delete(
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(object, tool, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.delete(
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.with_raw_response.delete(
                tool_id="",
            )

    @parametrize
    async def test_method_add_base_tools(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.add_base_tools()
        assert_matches_type(ToolAddBaseToolsResponse, tool, path=["response"])

    @parametrize
    async def test_method_add_base_tools_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.add_base_tools(
            user_id="user_id",
        )
        assert_matches_type(ToolAddBaseToolsResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_add_base_tools(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.add_base_tools()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolAddBaseToolsResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_add_base_tools(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.add_base_tools() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolAddBaseToolsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_by_name(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.retrieve_by_name(
            tool_name="tool_name",
        )
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    async def test_method_retrieve_by_name_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.tools.retrieve_by_name(
            tool_name="tool_name",
            user_id="user_id",
        )
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_by_name(self, async_client: AsyncLetta) -> None:
        response = await async_client.tools.with_raw_response.retrieve_by_name(
            tool_name="tool_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(str, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_by_name(self, async_client: AsyncLetta) -> None:
        async with async_client.tools.with_streaming_response.retrieve_by_name(
            tool_name="tool_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(str, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_by_name(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_name` but received ''"):
            await async_client.tools.with_raw_response.retrieve_by_name(
                tool_name="",
            )
