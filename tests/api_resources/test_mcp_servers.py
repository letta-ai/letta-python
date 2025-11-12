# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    McpServerListResponse,
    McpServerCreateResponse,
    McpServerUpdateResponse,
    McpServerRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcpServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.create(
            args=["string"],
            command="command",
            server_name="server_name",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.create(
            args=["string"],
            command="command",
            server_name="server_name",
            env={"foo": "string"},
            type="sse",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.create(
            args=["string"],
            command="command",
            server_name="server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.create(
            args=["string"],
            command="command",
            server_name="server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.create(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.create(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.create(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.create(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.create(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.create(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.create(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.create(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.retrieve(
            "mcp_server_id",
        )
        assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.retrieve(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.retrieve(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            args=["string"],
            command="command",
            env={"foo": "string"},
            server_name="server_name",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.update(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.update(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.with_raw_response.update(
                mcp_server_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            token="token",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.update(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.update(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.with_raw_response.update(
                mcp_server_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            token="token",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.update(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.update(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_3(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.with_raw_response.update(
                mcp_server_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.list()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.delete(
            "mcp_server_id",
        )
        assert mcp_server is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.delete(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert mcp_server is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.delete(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert mcp_server is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.connect(
            "mcp_server_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.connect(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.connect(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_connect(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.with_raw_response.connect(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refresh(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.refresh(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refresh_with_all_params(self, client: Letta) -> None:
        mcp_server = client.mcp_servers.refresh(
            mcp_server_id="mcp_server_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_refresh(self, client: Letta) -> None:
        response = client.mcp_servers.with_raw_response.refresh(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_refresh(self, client: Letta) -> None:
        with client.mcp_servers.with_streaming_response.refresh(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_refresh(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.with_raw_response.refresh(
                mcp_server_id="",
            )


class TestAsyncMcpServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.create(
            args=["string"],
            command="command",
            server_name="server_name",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.create(
            args=["string"],
            command="command",
            server_name="server_name",
            env={"foo": "string"},
            type="sse",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.create(
            args=["string"],
            command="command",
            server_name="server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.create(
            args=["string"],
            command="command",
            server_name="server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.create(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.create(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.create(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.create(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.create(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.create(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.create(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.create(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.retrieve(
            "mcp_server_id",
        )
        assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.retrieve(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.retrieve(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            args=["string"],
            command="command",
            env={"foo": "string"},
            server_name="server_name",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.update(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.update(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.with_raw_response.update(
                mcp_server_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            token="token",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.update(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.update(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.with_raw_response.update(
                mcp_server_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            token="token",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.update(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.update(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.with_raw_response.update(
                mcp_server_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.list()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.delete(
            "mcp_server_id",
        )
        assert mcp_server is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.delete(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert mcp_server is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.delete(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert mcp_server is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.connect(
            "mcp_server_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.connect(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.connect(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_connect(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.with_raw_response.connect(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refresh(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.refresh(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refresh_with_all_params(self, async_client: AsyncLetta) -> None:
        mcp_server = await async_client.mcp_servers.refresh(
            mcp_server_id="mcp_server_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.with_raw_response.refresh(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.with_streaming_response.refresh(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_refresh(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.with_raw_response.refresh(
                mcp_server_id="",
            )
