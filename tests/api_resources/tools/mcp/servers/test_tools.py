# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types.tools.mcp.servers import ToolListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        tool = client.tools.mcp.servers.tools.list(
            "mcp_server_name",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.tools.with_raw_response.list(
            "mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.tools.with_streaming_response.list(
            "mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            client.tools.mcp.servers.tools.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute(self, client: LettaSDK) -> None:
        tool = client.tools.mcp.servers.tools.execute(
            tool_name="tool_name",
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: LettaSDK) -> None:
        tool = client.tools.mcp.servers.tools.execute(
            tool_name="tool_name",
            mcp_server_name="mcp_server_name",
            args={"foo": "bar"},
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.tools.with_raw_response.execute(
            tool_name="tool_name",
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.tools.with_streaming_response.execute(
            tool_name="tool_name",
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            client.tools.mcp.servers.tools.with_raw_response.execute(
                tool_name="tool_name",
                mcp_server_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_name` but received ''"):
            client.tools.mcp.servers.tools.with_raw_response.execute(
                tool_name="",
                mcp_server_name="mcp_server_name",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.mcp.servers.tools.list(
            "mcp_server_name",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.tools.with_raw_response.list(
            "mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.tools.with_streaming_response.list(
            "mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            await async_client.tools.mcp.servers.tools.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.mcp.servers.tools.execute(
            tool_name="tool_name",
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        tool = await async_client.tools.mcp.servers.tools.execute(
            tool_name="tool_name",
            mcp_server_name="mcp_server_name",
            args={"foo": "bar"},
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.tools.with_raw_response.execute(
            tool_name="tool_name",
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.tools.with_streaming_response.execute(
            tool_name="tool_name",
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            await async_client.tools.mcp.servers.tools.with_raw_response.execute(
                tool_name="tool_name",
                mcp_server_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_name` but received ''"):
            await async_client.tools.mcp.servers.tools.with_raw_response.execute(
                tool_name="",
                mcp_server_name="mcp_server_name",
            )
