# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk._utils import parse_datetime
from letta_sdk.types.agents import (
    ArchivalMemoryListResponse,
    ArchivalMemoryCreateResponse,
    ArchivalMemorySearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArchivalMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LettaSDK) -> None:
        archival_memory = client.agents.archival_memory.create(
            agent_id="agent_id",
            text="text",
        )
        assert_matches_type(ArchivalMemoryCreateResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LettaSDK) -> None:
        archival_memory = client.agents.archival_memory.create(
            agent_id="agent_id",
            text="text",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            tags=["string"],
        )
        assert_matches_type(ArchivalMemoryCreateResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LettaSDK) -> None:
        response = client.agents.archival_memory.with_raw_response.create(
            agent_id="agent_id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival_memory = response.parse()
        assert_matches_type(ArchivalMemoryCreateResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LettaSDK) -> None:
        with client.agents.archival_memory.with_streaming_response.create(
            agent_id="agent_id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival_memory = response.parse()
            assert_matches_type(ArchivalMemoryCreateResponse, archival_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archival_memory.with_raw_response.create(
                agent_id="",
                text="text",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        archival_memory = client.agents.archival_memory.list(
            agent_id="agent_id",
        )
        assert_matches_type(ArchivalMemoryListResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        archival_memory = client.agents.archival_memory.list(
            agent_id="agent_id",
            after="after",
            ascending=True,
            before="before",
            limit=0,
            search="search",
        )
        assert_matches_type(ArchivalMemoryListResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.agents.archival_memory.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival_memory = response.parse()
        assert_matches_type(ArchivalMemoryListResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.agents.archival_memory.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival_memory = response.parse()
            assert_matches_type(ArchivalMemoryListResponse, archival_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archival_memory.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        archival_memory = client.agents.archival_memory.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.agents.archival_memory.with_raw_response.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival_memory = response.parse()
        assert_matches_type(object, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.agents.archival_memory.with_streaming_response.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival_memory = response.parse()
            assert_matches_type(object, archival_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archival_memory.with_raw_response.delete(
                memory_id="memory_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.agents.archival_memory.with_raw_response.delete(
                memory_id="",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: LettaSDK) -> None:
        archival_memory = client.agents.archival_memory.search(
            agent_id="agent_id",
            query="query",
        )
        assert_matches_type(ArchivalMemorySearchResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: LettaSDK) -> None:
        archival_memory = client.agents.archival_memory.search(
            agent_id="agent_id",
            query="query",
            end_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag_match_mode="any",
            tags=["string"],
            top_k=0,
        )
        assert_matches_type(ArchivalMemorySearchResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: LettaSDK) -> None:
        response = client.agents.archival_memory.with_raw_response.search(
            agent_id="agent_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival_memory = response.parse()
        assert_matches_type(ArchivalMemorySearchResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: LettaSDK) -> None:
        with client.agents.archival_memory.with_streaming_response.search(
            agent_id="agent_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival_memory = response.parse()
            assert_matches_type(ArchivalMemorySearchResponse, archival_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_search(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archival_memory.with_raw_response.search(
                agent_id="",
                query="query",
            )


class TestAsyncArchivalMemory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLettaSDK) -> None:
        archival_memory = await async_client.agents.archival_memory.create(
            agent_id="agent_id",
            text="text",
        )
        assert_matches_type(ArchivalMemoryCreateResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        archival_memory = await async_client.agents.archival_memory.create(
            agent_id="agent_id",
            text="text",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            tags=["string"],
        )
        assert_matches_type(ArchivalMemoryCreateResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.archival_memory.with_raw_response.create(
            agent_id="agent_id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival_memory = await response.parse()
        assert_matches_type(ArchivalMemoryCreateResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.archival_memory.with_streaming_response.create(
            agent_id="agent_id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival_memory = await response.parse()
            assert_matches_type(ArchivalMemoryCreateResponse, archival_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archival_memory.with_raw_response.create(
                agent_id="",
                text="text",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        archival_memory = await async_client.agents.archival_memory.list(
            agent_id="agent_id",
        )
        assert_matches_type(ArchivalMemoryListResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        archival_memory = await async_client.agents.archival_memory.list(
            agent_id="agent_id",
            after="after",
            ascending=True,
            before="before",
            limit=0,
            search="search",
        )
        assert_matches_type(ArchivalMemoryListResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.archival_memory.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival_memory = await response.parse()
        assert_matches_type(ArchivalMemoryListResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.archival_memory.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival_memory = await response.parse()
            assert_matches_type(ArchivalMemoryListResponse, archival_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archival_memory.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        archival_memory = await async_client.agents.archival_memory.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.archival_memory.with_raw_response.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival_memory = await response.parse()
        assert_matches_type(object, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.archival_memory.with_streaming_response.delete(
            memory_id="memory_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival_memory = await response.parse()
            assert_matches_type(object, archival_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archival_memory.with_raw_response.delete(
                memory_id="memory_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.agents.archival_memory.with_raw_response.delete(
                memory_id="",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLettaSDK) -> None:
        archival_memory = await async_client.agents.archival_memory.search(
            agent_id="agent_id",
            query="query",
        )
        assert_matches_type(ArchivalMemorySearchResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        archival_memory = await async_client.agents.archival_memory.search(
            agent_id="agent_id",
            query="query",
            end_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag_match_mode="any",
            tags=["string"],
            top_k=0,
        )
        assert_matches_type(ArchivalMemorySearchResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.archival_memory.with_raw_response.search(
            agent_id="agent_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival_memory = await response.parse()
        assert_matches_type(ArchivalMemorySearchResponse, archival_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.archival_memory.with_streaming_response.search(
            agent_id="agent_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival_memory = await response.parse()
            assert_matches_type(ArchivalMemorySearchResponse, archival_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archival_memory.with_raw_response.search(
                agent_id="",
                query="query",
            )
