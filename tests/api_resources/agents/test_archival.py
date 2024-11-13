# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types.agents import (
    ArchivalListResponse,
    ArchivalCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArchival:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        archival = client.agents.archival.create(
            agent_id="agent_id",
            text="text",
        )
        assert_matches_type(ArchivalCreateResponse, archival, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        archival = client.agents.archival.create(
            agent_id="agent_id",
            text="text",
            user_id="user_id",
        )
        assert_matches_type(ArchivalCreateResponse, archival, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.agents.archival.with_raw_response.create(
            agent_id="agent_id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival = response.parse()
        assert_matches_type(ArchivalCreateResponse, archival, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.agents.archival.with_streaming_response.create(
            agent_id="agent_id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival = response.parse()
            assert_matches_type(ArchivalCreateResponse, archival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archival.with_raw_response.create(
                agent_id="",
                text="text",
            )

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        archival = client.agents.archival.list(
            agent_id="agent_id",
        )
        assert_matches_type(ArchivalListResponse, archival, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        archival = client.agents.archival.list(
            agent_id="agent_id",
            after=0,
            before=0,
            limit=0,
            user_id="user_id",
        )
        assert_matches_type(ArchivalListResponse, archival, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.archival.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival = response.parse()
        assert_matches_type(ArchivalListResponse, archival, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.archival.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival = response.parse()
            assert_matches_type(ArchivalListResponse, archival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archival.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        archival = client.agents.archival.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, archival, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Letta) -> None:
        archival = client.agents.archival.delete(
            memory_id="memory_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(object, archival, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.agents.archival.with_raw_response.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival = response.parse()
        assert_matches_type(object, archival, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.agents.archival.with_streaming_response.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival = response.parse()
            assert_matches_type(object, archival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archival.with_raw_response.delete(
                memory_id="memory_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.agents.archival.with_raw_response.delete(
                memory_id="",
                agent_id="agent_id",
            )


class TestAsyncArchival:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        archival = await async_client.agents.archival.create(
            agent_id="agent_id",
            text="text",
        )
        assert_matches_type(ArchivalCreateResponse, archival, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        archival = await async_client.agents.archival.create(
            agent_id="agent_id",
            text="text",
            user_id="user_id",
        )
        assert_matches_type(ArchivalCreateResponse, archival, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.archival.with_raw_response.create(
            agent_id="agent_id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival = await response.parse()
        assert_matches_type(ArchivalCreateResponse, archival, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.archival.with_streaming_response.create(
            agent_id="agent_id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival = await response.parse()
            assert_matches_type(ArchivalCreateResponse, archival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archival.with_raw_response.create(
                agent_id="",
                text="text",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        archival = await async_client.agents.archival.list(
            agent_id="agent_id",
        )
        assert_matches_type(ArchivalListResponse, archival, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        archival = await async_client.agents.archival.list(
            agent_id="agent_id",
            after=0,
            before=0,
            limit=0,
            user_id="user_id",
        )
        assert_matches_type(ArchivalListResponse, archival, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.archival.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival = await response.parse()
        assert_matches_type(ArchivalListResponse, archival, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.archival.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival = await response.parse()
            assert_matches_type(ArchivalListResponse, archival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archival.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        archival = await async_client.agents.archival.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, archival, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLetta) -> None:
        archival = await async_client.agents.archival.delete(
            memory_id="memory_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(object, archival, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.archival.with_raw_response.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival = await response.parse()
        assert_matches_type(object, archival, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.archival.with_streaming_response.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival = await response.parse()
            assert_matches_type(object, archival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archival.with_raw_response.delete(
                memory_id="memory_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.agents.archival.with_raw_response.delete(
                memory_id="",
                agent_id="agent_id",
            )
