# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import Tool
from letta_sdk.types.tools.mcp import (
    ServerAddResponse,
    ServerListResponse,
    ServerDeleteResponse,
    ServerUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
            stdio_config={
                "args": ["string"],
                "command": "command",
                "server_name": "server_name",
                "env": {"foo": "string"},
                "type": "sse",
            },
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.update(
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.update(
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            client.tools.mcp.servers.with_raw_response.update(
                mcp_server_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
            token="token",
            custom_headers={"foo": "string"},
            server_url="server_url",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.update(
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.update(
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            client.tools.mcp.servers.with_raw_response.update(
                mcp_server_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            server_url="server_url",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.update(
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.update(
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_3(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            client.tools.mcp.servers.with_raw_response.update(
                mcp_server_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.list()
        assert_matches_type(ServerListResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerListResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerListResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.delete(
            "mcp_server_name",
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.delete(
            "mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.delete(
            "mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerDeleteResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            client.tools.mcp.servers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_overload_1(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.add(
            args=["string"],
            command="command",
            server_name="server_name",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params_overload_1(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.add(
            args=["string"],
            command="command",
            server_name="server_name",
            env={"foo": "string"},
            type="sse",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_overload_1(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.add(
            args=["string"],
            command="command",
            server_name="server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_overload_1(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.add(
            args=["string"],
            command="command",
            server_name="server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerAddResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_overload_2(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.add(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params_overload_2(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.add(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_overload_2(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.add(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_overload_2(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.add(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerAddResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_overload_3(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.add(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params_overload_3(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.add(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_overload_3(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.add(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_overload_3(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.add(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerAddResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_overload_1(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.connect(
            args=["string"],
            command="command",
            server_name="server_name",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_with_all_params_overload_1(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.connect(
            args=["string"],
            command="command",
            server_name="server_name",
            env={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect_overload_1(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.connect(
            args=["string"],
            command="command",
            server_name="server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect_overload_1(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.connect(
            args=["string"],
            command="command",
            server_name="server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_overload_2(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.connect(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_with_all_params_overload_2(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.connect(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect_overload_2(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.connect(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect_overload_2(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.connect(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_overload_3(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.connect(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_with_all_params_overload_3(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.connect(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect_overload_3(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.connect(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect_overload_3(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.connect(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_tool(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.register_tool(
            mcp_tool_name="mcp_tool_name",
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(Tool, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register_tool(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.register_tool(
            mcp_tool_name="mcp_tool_name",
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(Tool, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register_tool(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.register_tool(
            mcp_tool_name="mcp_tool_name",
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(Tool, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_register_tool(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            client.tools.mcp.servers.with_raw_response.register_tool(
                mcp_tool_name="mcp_tool_name",
                mcp_server_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_tool_name` but received ''"):
            client.tools.mcp.servers.with_raw_response.register_tool(
                mcp_tool_name="",
                mcp_server_name="mcp_server_name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resync(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.resync(
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resync_with_all_params(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.resync(
            mcp_server_name="mcp_server_name",
            agent_id="agent_id",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resync(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.resync(
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resync(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.resync(
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resync(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            client.tools.mcp.servers.with_raw_response.resync(
                mcp_server_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_overload_1(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.test(
            args=["string"],
            command="command",
            server_name="server_name",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_with_all_params_overload_1(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.test(
            args=["string"],
            command="command",
            server_name="server_name",
            env={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_overload_1(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.test(
            args=["string"],
            command="command",
            server_name="server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_overload_1(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.test(
            args=["string"],
            command="command",
            server_name="server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_overload_2(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.test(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_with_all_params_overload_2(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.test(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_overload_2(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.test(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_overload_2(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.test(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_overload_3(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.test(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_with_all_params_overload_3(self, client: LettaSDK) -> None:
        server = client.tools.mcp.servers.test(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_overload_3(self, client: LettaSDK) -> None:
        response = client.tools.mcp.servers.with_raw_response.test(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_overload_3(self, client: LettaSDK) -> None:
        with client.tools.mcp.servers.with_streaming_response.test(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
            stdio_config={
                "args": ["string"],
                "command": "command",
                "server_name": "server_name",
                "env": {"foo": "string"},
                "type": "sse",
            },
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.update(
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.update(
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            await async_client.tools.mcp.servers.with_raw_response.update(
                mcp_server_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
            token="token",
            custom_headers={"foo": "string"},
            server_url="server_url",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.update(
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.update(
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            await async_client.tools.mcp.servers.with_raw_response.update(
                mcp_server_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.update(
            mcp_server_name="mcp_server_name",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            server_url="server_url",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.update(
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.update(
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            await async_client.tools.mcp.servers.with_raw_response.update(
                mcp_server_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.list()
        assert_matches_type(ServerListResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerListResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerListResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.delete(
            "mcp_server_name",
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.delete(
            "mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.delete(
            "mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerDeleteResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            await async_client.tools.mcp.servers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_overload_1(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.add(
            args=["string"],
            command="command",
            server_name="server_name",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params_overload_1(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.add(
            args=["string"],
            command="command",
            server_name="server_name",
            env={"foo": "string"},
            type="sse",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_overload_1(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.add(
            args=["string"],
            command="command",
            server_name="server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_overload_1(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.add(
            args=["string"],
            command="command",
            server_name="server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerAddResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_overload_2(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.add(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params_overload_2(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.add(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_overload_2(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.add(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_overload_2(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.add(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerAddResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_overload_3(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.add(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params_overload_3(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.add(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_overload_3(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.add(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerAddResponse, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_overload_3(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.add(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerAddResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_overload_1(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.connect(
            args=["string"],
            command="command",
            server_name="server_name",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params_overload_1(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.connect(
            args=["string"],
            command="command",
            server_name="server_name",
            env={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect_overload_1(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.connect(
            args=["string"],
            command="command",
            server_name="server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect_overload_1(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.connect(
            args=["string"],
            command="command",
            server_name="server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_overload_2(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.connect(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params_overload_2(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.connect(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect_overload_2(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.connect(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect_overload_2(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.connect(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_overload_3(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.connect(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params_overload_3(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.connect(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect_overload_3(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.connect(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect_overload_3(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.connect(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_tool(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.register_tool(
            mcp_tool_name="mcp_tool_name",
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(Tool, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register_tool(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.register_tool(
            mcp_tool_name="mcp_tool_name",
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(Tool, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register_tool(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.register_tool(
            mcp_tool_name="mcp_tool_name",
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(Tool, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_register_tool(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            await async_client.tools.mcp.servers.with_raw_response.register_tool(
                mcp_tool_name="mcp_tool_name",
                mcp_server_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_tool_name` but received ''"):
            await async_client.tools.mcp.servers.with_raw_response.register_tool(
                mcp_tool_name="",
                mcp_server_name="mcp_server_name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resync(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.resync(
            mcp_server_name="mcp_server_name",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resync_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.resync(
            mcp_server_name="mcp_server_name",
            agent_id="agent_id",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resync(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.resync(
            mcp_server_name="mcp_server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resync(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.resync(
            mcp_server_name="mcp_server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resync(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_name` but received ''"):
            await async_client.tools.mcp.servers.with_raw_response.resync(
                mcp_server_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_overload_1(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.test(
            args=["string"],
            command="command",
            server_name="server_name",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_with_all_params_overload_1(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.test(
            args=["string"],
            command="command",
            server_name="server_name",
            env={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_overload_1(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.test(
            args=["string"],
            command="command",
            server_name="server_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_overload_1(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.test(
            args=["string"],
            command="command",
            server_name="server_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_overload_2(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.test(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_with_all_params_overload_2(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.test(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_overload_2(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.test(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_overload_2(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.test(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_overload_3(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.test(
            server_name="server_name",
            server_url="server_url",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_with_all_params_overload_3(self, async_client: AsyncLettaSDK) -> None:
        server = await async_client.tools.mcp.servers.test(
            server_name="server_name",
            server_url="server_url",
            auth_header="auth_header",
            auth_token="auth_token",
            custom_headers={"foo": "string"},
            type="sse",
        )
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_overload_3(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.mcp.servers.with_raw_response.test(
            server_name="server_name",
            server_url="server_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(object, server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_overload_3(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.mcp.servers.with_streaming_response.test(
            server_name="server_name",
            server_url="server_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True
