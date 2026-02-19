# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import AgentState
from letta_client.pagination import SyncArrayPage, AsyncArrayPage
from letta_client.types.agents import FolderListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        folder = client.agents.folders.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(SyncArrayPage[FolderListResponse], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        folder = client.agents.folders.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(SyncArrayPage[FolderListResponse], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.folders.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(SyncArrayPage[FolderListResponse], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.folders.with_streaming_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(SyncArrayPage[FolderListResponse], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.folders.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach(self, client: Letta) -> None:
        folder = client.agents.folders.attach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Letta) -> None:
        response = client.agents.folders.with_raw_response.attach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Optional[AgentState], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: Letta) -> None:
        with client.agents.folders.with_streaming_response.attach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Optional[AgentState], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.folders.with_raw_response.attach(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.agents.folders.with_raw_response.attach(
                folder_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_detach(self, client: Letta) -> None:
        folder = client.agents.folders.detach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Letta) -> None:
        response = client.agents.folders.with_raw_response.detach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Optional[AgentState], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: Letta) -> None:
        with client.agents.folders.with_streaming_response.detach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Optional[AgentState], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.folders.with_raw_response.detach(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.agents.folders.with_raw_response.detach(
                folder_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        folder = await async_client.agents.folders.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(AsyncArrayPage[FolderListResponse], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        folder = await async_client.agents.folders.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(AsyncArrayPage[FolderListResponse], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.folders.with_raw_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(AsyncArrayPage[FolderListResponse], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.folders.with_streaming_response.list(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(AsyncArrayPage[FolderListResponse], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.folders.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncLetta) -> None:
        folder = await async_client.agents.folders.attach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.folders.with_raw_response.attach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Optional[AgentState], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.folders.with_streaming_response.attach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Optional[AgentState], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.folders.with_raw_response.attach(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.agents.folders.with_raw_response.attach(
                folder_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncLetta) -> None:
        folder = await async_client.agents.folders.detach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Optional[AgentState], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.folders.with_raw_response.detach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Optional[AgentState], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.folders.with_streaming_response.detach(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Optional[AgentState], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.folders.with_raw_response.detach(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.agents.folders.with_raw_response.detach(
                folder_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )
