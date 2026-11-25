# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    Subagent,
    SubagentListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubagents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        subagent = client.subagents.create(
            description="x",
            harness="x",
            parent_conversation_id="x",
        )
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        subagent = client.subagents.create(
            description="x",
            harness="x",
            parent_conversation_id="x",
            agent_id="x",
            archived=True,
            computer="x",
            conversation_id="x",
            fork_context=True,
            mcp_config={"foo": "bar"},
            model_config={"foo": "bar"},
            parent_agent_id="x",
            prompt="prompt",
            repositories=["string"],
            sandbox_size="x",
            status="running",
            subagent_type="x",
            worker_session_id="x",
        )
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.subagents.with_raw_response.create(
            description="x",
            harness="x",
            parent_conversation_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subagent = response.parse()
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.subagents.with_streaming_response.create(
            description="x",
            harness="x",
            parent_conversation_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subagent = response.parse()
            assert_matches_type(Subagent, subagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Letta) -> None:
        subagent = client.subagents.update(
            subagent_id="x",
        )
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        subagent = client.subagents.update(
            subagent_id="x",
            agent_id="x",
            archived=True,
            conversation_id="x",
            status="running",
            worker_session_id="x",
        )
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.subagents.with_raw_response.update(
            subagent_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subagent = response.parse()
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.subagents.with_streaming_response.update(
            subagent_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subagent = response.parse()
            assert_matches_type(Subagent, subagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subagent_id` but received ''"):
            client.subagents.with_raw_response.update(
                subagent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        subagent = client.subagents.list()
        assert_matches_type(SubagentListResponse, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        subagent = client.subagents.list(
            after="x",
            archived="true",
            limit=1,
            parent_agent_id="x",
            parent_conversation_id="x",
        )
        assert_matches_type(SubagentListResponse, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.subagents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subagent = response.parse()
        assert_matches_type(SubagentListResponse, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.subagents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subagent = response.parse()
            assert_matches_type(SubagentListResponse, subagent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubagents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        subagent = await async_client.subagents.create(
            description="x",
            harness="x",
            parent_conversation_id="x",
        )
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        subagent = await async_client.subagents.create(
            description="x",
            harness="x",
            parent_conversation_id="x",
            agent_id="x",
            archived=True,
            computer="x",
            conversation_id="x",
            fork_context=True,
            mcp_config={"foo": "bar"},
            model_config={"foo": "bar"},
            parent_agent_id="x",
            prompt="prompt",
            repositories=["string"],
            sandbox_size="x",
            status="running",
            subagent_type="x",
            worker_session_id="x",
        )
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.subagents.with_raw_response.create(
            description="x",
            harness="x",
            parent_conversation_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subagent = await response.parse()
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.subagents.with_streaming_response.create(
            description="x",
            harness="x",
            parent_conversation_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subagent = await response.parse()
            assert_matches_type(Subagent, subagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        subagent = await async_client.subagents.update(
            subagent_id="x",
        )
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        subagent = await async_client.subagents.update(
            subagent_id="x",
            agent_id="x",
            archived=True,
            conversation_id="x",
            status="running",
            worker_session_id="x",
        )
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.subagents.with_raw_response.update(
            subagent_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subagent = await response.parse()
        assert_matches_type(Subagent, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.subagents.with_streaming_response.update(
            subagent_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subagent = await response.parse()
            assert_matches_type(Subagent, subagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subagent_id` but received ''"):
            await async_client.subagents.with_raw_response.update(
                subagent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        subagent = await async_client.subagents.list()
        assert_matches_type(SubagentListResponse, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        subagent = await async_client.subagents.list(
            after="x",
            archived="true",
            limit=1,
            parent_agent_id="x",
            parent_conversation_id="x",
        )
        assert_matches_type(SubagentListResponse, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.subagents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subagent = await response.parse()
        assert_matches_type(SubagentListResponse, subagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.subagents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subagent = await response.parse()
            assert_matches_type(SubagentListResponse, subagent, path=["response"])

        assert cast(Any, response.is_closed) is True
