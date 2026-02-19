# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import PassageSearchResponse
from letta_client._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPassages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Letta) -> None:
        passage = client.passages.search()
        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Letta) -> None:
        passage = client.passages.search(
            agent_id="agent_id",
            archive_id="archive_id",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            query="query",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag_match_mode="any",
            tags=["string"],
        )
        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Letta) -> None:
        response = client.passages.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = response.parse()
        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Letta) -> None:
        with client.passages.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passage = response.parse()
            assert_matches_type(PassageSearchResponse, passage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPassages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLetta) -> None:
        passage = await async_client.passages.search()
        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLetta) -> None:
        passage = await async_client.passages.search(
            agent_id="agent_id",
            archive_id="archive_id",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            query="query",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag_match_mode="any",
            tags=["string"],
        )
        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLetta) -> None:
        response = await async_client.passages.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = await response.parse()
        assert_matches_type(PassageSearchResponse, passage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLetta) -> None:
        async with async_client.passages.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passage = await response.parse()
            assert_matches_type(PassageSearchResponse, passage, path=["response"])

        assert cast(Any, response.is_closed) is True
