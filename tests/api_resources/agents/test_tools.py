# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import AgentState
from letta_client.types.agents import ToolListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        tool = client.agents.tools.list(
            agent_id="agent_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        tool = client.agents.tools.list(
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.tools.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.tools.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    def test_method_add(self, client: Letta) -> None:
        tool = client.agents.tools.add(
            tool_id="tool_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Letta) -> None:
        tool = client.agents.tools.add(
            tool_id="tool_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Letta) -> None:
        response = client.agents.tools.with_raw_response.add(
            tool_id="tool_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Letta) -> None:
        with client.agents.tools.with_streaming_response.add(
            tool_id="tool_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(AgentState, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.add(
                tool_id="tool_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.tools.with_raw_response.add(
                tool_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_remove(self, client: Letta) -> None:
        tool = client.agents.tools.remove(
            tool_id="tool_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    def test_method_remove_with_all_params(self, client: Letta) -> None:
        tool = client.agents.tools.remove(
            tool_id="tool_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Letta) -> None:
        response = client.agents.tools.with_raw_response.remove(
            tool_id="tool_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Letta) -> None:
        with client.agents.tools.with_streaming_response.remove(
            tool_id="tool_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(AgentState, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.remove(
                tool_id="tool_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.tools.with_raw_response.remove(
                tool_id="",
                agent_id="agent_id",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.list(
            agent_id="agent_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.list(
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.tools.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.tools.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.add(
            tool_id="tool_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.add(
            tool_id="tool_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.tools.with_raw_response.add(
            tool_id="tool_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.tools.with_streaming_response.add(
            tool_id="tool_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AgentState, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.add(
                tool_id="tool_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.tools.with_raw_response.add(
                tool_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.remove(
            tool_id="tool_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.remove(
            tool_id="tool_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.tools.with_raw_response.remove(
            tool_id="tool_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AgentState, tool, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.tools.with_streaming_response.remove(
            tool_id="tool_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AgentState, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.remove(
                tool_id="tool_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.tools.with_raw_response.remove(
                tool_id="",
                agent_id="agent_id",
            )
