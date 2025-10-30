# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRefresh:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger(self, client: Letta) -> None:
        refresh = client.mcp_servers.refresh.trigger(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(object, refresh, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_with_all_params(self, client: Letta) -> None:
        refresh = client.mcp_servers.refresh.trigger(
            mcp_server_id="mcp_server_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, refresh, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger(self, client: Letta) -> None:
        response = client.mcp_servers.refresh.with_raw_response.trigger(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        refresh = response.parse()
        assert_matches_type(object, refresh, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger(self, client: Letta) -> None:
        with client.mcp_servers.refresh.with_streaming_response.trigger(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            refresh = response.parse()
            assert_matches_type(object, refresh, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_trigger(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.mcp_servers.refresh.with_raw_response.trigger(
                mcp_server_id="",
            )


class TestAsyncRefresh:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger(self, async_client: AsyncLetta) -> None:
        refresh = await async_client.mcp_servers.refresh.trigger(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(object, refresh, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncLetta) -> None:
        refresh = await async_client.mcp_servers.refresh.trigger(
            mcp_server_id="mcp_server_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, refresh, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncLetta) -> None:
        response = await async_client.mcp_servers.refresh.with_raw_response.trigger(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        refresh = await response.parse()
        assert_matches_type(object, refresh, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncLetta) -> None:
        async with async_client.mcp_servers.refresh.with_streaming_response.trigger(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            refresh = await response.parse()
            assert_matches_type(object, refresh, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.mcp_servers.refresh.with_raw_response.trigger(
                mcp_server_id="",
            )
