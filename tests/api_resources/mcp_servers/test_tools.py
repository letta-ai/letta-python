# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import Tool
from letta_client.types.agents import ToolExecutionResult
from letta_client.types.mcp_servers import ToolListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        tool = client.mcp_servers.tools.retrieve(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.mcp_servers.tools.with_raw_response.retrieve(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.mcp_servers.tools.with_streaming_response.retrieve(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.tools.with_raw_response.retrieve(
                tool_id="tool_id",
                mcp_server_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.mcp_servers.tools.with_raw_response.retrieve(
                tool_id="",
                mcp_server_id="mcp_server_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        tool = client.mcp_servers.tools.list(
            "mcp_server_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.mcp_servers.tools.with_raw_response.list(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.mcp_servers.tools.with_streaming_response.list(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.tools.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: Letta) -> None:
        tool = client.mcp_servers.tools.run(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Letta) -> None:
        tool = client.mcp_servers.tools.run(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
            args={"foo": "bar"},
        )
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Letta) -> None:
        response = client.mcp_servers.tools.with_raw_response.run(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Letta) -> None:
        with client.mcp_servers.tools.with_streaming_response.run(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolExecutionResult, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_run(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.tools.with_raw_response.run(
                tool_id="tool_id",
                mcp_server_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.mcp_servers.tools.with_raw_response.run(
                tool_id="",
                mcp_server_id="mcp_server_id",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        tool = await async_client.mcp_servers.tools.retrieve(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.tools.with_raw_response.retrieve(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.tools.with_streaming_response.retrieve(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.tools.with_raw_response.retrieve(
                tool_id="tool_id",
                mcp_server_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.mcp_servers.tools.with_raw_response.retrieve(
                tool_id="",
                mcp_server_id="mcp_server_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        tool = await async_client.mcp_servers.tools.list(
            "mcp_server_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.tools.with_raw_response.list(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.tools.with_streaming_response.list(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.tools.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncLetta) -> None:
        tool = await async_client.mcp_servers.tools.run(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.mcp_servers.tools.run(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
            args={"foo": "bar"},
        )
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.tools.with_raw_response.run(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.tools.with_streaming_response.run(
            tool_id="tool_id",
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolExecutionResult, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.tools.with_raw_response.run(
                tool_id="tool_id",
                mcp_server_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.mcp_servers.tools.with_raw_response.run(
                tool_id="",
                mcp_server_id="mcp_server_id",
            )
