# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client._utils import parse_datetime
from letta_client.types.agents import (
    PassageListResponse,
    PassageCreateResponse,
    PassageSearchResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPassages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = client.agents.passages.create(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                text="text",
            )

        assert_matches_type(PassageCreateResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = client.agents.passages.create(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                text="text",
                created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                tags=["string"],
            )

        assert_matches_type(PassageCreateResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.agents.passages.with_raw_response.create(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                text="text",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = response.parse()
        assert_matches_type(PassageCreateResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with client.agents.passages.with_streaming_response.create(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                text="text",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                passage = response.parse()
                assert_matches_type(PassageCreateResponse, passage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.agents.passages.with_raw_response.create(
                    agent_id="",
                    text="text",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = client.agents.passages.list(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert_matches_type(PassageListResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = client.agents.passages.list(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                after="after",
                ascending=True,
                before="before",
                limit=0,
                search="search",
            )

        assert_matches_type(PassageListResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.agents.passages.with_raw_response.list(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = response.parse()
        assert_matches_type(PassageListResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with client.agents.passages.with_streaming_response.list(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                passage = response.parse()
                assert_matches_type(PassageListResponse, passage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.agents.passages.with_raw_response.list(
                    agent_id="",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = client.agents.passages.delete(
                memory_id="memory_id",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert_matches_type(object, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.agents.passages.with_raw_response.delete(
                memory_id="memory_id",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = response.parse()
        assert_matches_type(object, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with client.agents.passages.with_streaming_response.delete(
                memory_id="memory_id",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                passage = response.parse()
                assert_matches_type(object, passage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.agents.passages.with_raw_response.delete(
                    memory_id="memory_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
                client.agents.passages.with_raw_response.delete(
                    memory_id="",
                    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = client.agents.passages.search(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                query="query",
            )

        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = client.agents.passages.search(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                query="query",
                end_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
                tag_match_mode="any",
                tags=["string", "string"],
                top_k=0,
            )

        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.agents.passages.with_raw_response.search(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                query="query",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = response.parse()
        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with client.agents.passages.with_streaming_response.search(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                query="query",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                passage = response.parse()
                assert_matches_type(PassageSearchResponse, passage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_search(self, client: Letta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.agents.passages.with_raw_response.search(
                    agent_id="",
                    query="query",
                )


class TestAsyncPassages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = await async_client.agents.passages.create(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                text="text",
            )

        assert_matches_type(PassageCreateResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = await async_client.agents.passages.create(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                text="text",
                created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                tags=["string"],
            )

        assert_matches_type(PassageCreateResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.agents.passages.with_raw_response.create(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                text="text",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = await response.parse()
        assert_matches_type(PassageCreateResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.agents.passages.with_streaming_response.create(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                text="text",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                passage = await response.parse()
                assert_matches_type(PassageCreateResponse, passage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.agents.passages.with_raw_response.create(
                    agent_id="",
                    text="text",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = await async_client.agents.passages.list(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert_matches_type(PassageListResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = await async_client.agents.passages.list(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                after="after",
                ascending=True,
                before="before",
                limit=0,
                search="search",
            )

        assert_matches_type(PassageListResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.agents.passages.with_raw_response.list(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = await response.parse()
        assert_matches_type(PassageListResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.agents.passages.with_streaming_response.list(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                passage = await response.parse()
                assert_matches_type(PassageListResponse, passage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.agents.passages.with_raw_response.list(
                    agent_id="",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = await async_client.agents.passages.delete(
                memory_id="memory_id",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert_matches_type(object, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.agents.passages.with_raw_response.delete(
                memory_id="memory_id",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = await response.parse()
        assert_matches_type(object, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.agents.passages.with_streaming_response.delete(
                memory_id="memory_id",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                passage = await response.parse()
                assert_matches_type(object, passage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.agents.passages.with_raw_response.delete(
                    memory_id="memory_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
                await async_client.agents.passages.with_raw_response.delete(
                    memory_id="",
                    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = await async_client.agents.passages.search(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                query="query",
            )

        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            passage = await async_client.agents.passages.search(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                query="query",
                end_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
                tag_match_mode="any",
                tags=["string", "string"],
                top_k=0,
            )

        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.agents.passages.with_raw_response.search(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                query="query",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = await response.parse()
        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.agents.passages.with_streaming_response.search(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                query="query",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                passage = await response.parse()
                assert_matches_type(PassageSearchResponse, passage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncLetta) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.agents.passages.with_raw_response.search(
                    agent_id="",
                    query="query",
                )
