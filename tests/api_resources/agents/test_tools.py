# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import Tool, AgentState
from letta_client.pagination import SyncArrayPage, AsyncArrayPage
from letta_client.types.agents import (
    ToolExecutionResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        tool = client.agents.tools.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(SyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        tool = client.agents.tools.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(SyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.tools.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(SyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.tools.with_streaming_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(SyncArrayPage[Tool], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach(self, client: Letta) -> None:
        tool = client.agents.tools.attach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Letta) -> None:
        response = client.agents.tools.with_raw_response.attach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: Letta) -> None:
        with client.agents.tools.with_streaming_response.attach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Optional[AgentState], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.attach(
                tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.tools.with_raw_response.attach(
                tool_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach(self, client: Letta) -> None:
        tool = client.agents.tools.detach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Letta) -> None:
        response = client.agents.tools.with_raw_response.detach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: Letta) -> None:
        with client.agents.tools.with_streaming_response.detach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Optional[AgentState], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.detach(
                tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.tools.with_raw_response.detach(
                tool_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: Letta) -> None:
        tool = client.agents.tools.run(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Letta) -> None:
        tool = client.agents.tools.run(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            args={"foo": "bar"},
        )
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Letta) -> None:
        response = client.agents.tools.with_raw_response.run(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Letta) -> None:
        with client.agents.tools.with_streaming_response.run(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolExecutionResult, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_run(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.run(
                tool_name="tool_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_name` but received ''"):
            client.agents.tools.with_raw_response.run(
                tool_name="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_approval(self, client: Letta) -> None:
        tool = client.agents.tools.update_approval(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            body_requires_approval=True,
        )
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_approval_with_all_params(self, client: Letta) -> None:
        tool = client.agents.tools.update_approval(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            body_requires_approval=True,
            query_requires_approval=True,
        )
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_approval(self, client: Letta) -> None:
        response = client.agents.tools.with_raw_response.update_approval(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            body_requires_approval=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_approval(self, client: Letta) -> None:
        with client.agents.tools.with_streaming_response.update_approval(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            body_requires_approval=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Optional[AgentState], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_approval(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.update_approval(
                tool_name="tool_name",
                agent_id="",
                body_requires_approval=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_name` but received ''"):
            client.agents.tools.with_raw_response.update_approval(
                tool_name="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                body_requires_approval=True,
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AsyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(AsyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.tools.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AsyncArrayPage[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.tools.with_streaming_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AsyncArrayPage[Tool], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.attach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.tools.with_raw_response.attach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.tools.with_streaming_response.attach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Optional[AgentState], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.attach(
                tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.tools.with_raw_response.attach(
                tool_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.detach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.tools.with_raw_response.detach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.tools.with_streaming_response.detach(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Optional[AgentState], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.detach(
                tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.tools.with_raw_response.detach(
                tool_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.run(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.run(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            args={"foo": "bar"},
        )
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.tools.with_raw_response.run(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolExecutionResult, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.tools.with_streaming_response.run(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolExecutionResult, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.run(
                tool_name="tool_name",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_name` but received ''"):
            await async_client.agents.tools.with_raw_response.run(
                tool_name="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_approval(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.update_approval(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            body_requires_approval=True,
        )
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_approval_with_all_params(self, async_client: AsyncLetta) -> None:
        tool = await async_client.agents.tools.update_approval(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            body_requires_approval=True,
            query_requires_approval=True,
        )
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_approval(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.tools.with_raw_response.update_approval(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            body_requires_approval=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Optional[AgentState], tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_approval(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.tools.with_streaming_response.update_approval(
            tool_name="tool_name",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            body_requires_approval=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Optional[AgentState], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_approval(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.update_approval(
                tool_name="tool_name",
                agent_id="",
                body_requires_approval=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_name` but received ''"):
            await async_client.agents.tools.with_raw_response.update_approval(
                tool_name="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                body_requires_approval=True,
            )
