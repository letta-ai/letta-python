# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types.agents import ArchivalMemorySummary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArchival:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        archival = client.agents.memory.archival.retrieve(
            "agent_id",
        )
        assert_matches_type(ArchivalMemorySummary, archival, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.agents.memory.archival.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival = response.parse()
        assert_matches_type(ArchivalMemorySummary, archival, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.agents.memory.archival.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival = response.parse()
            assert_matches_type(ArchivalMemorySummary, archival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.memory.archival.with_raw_response.retrieve(
                "",
            )


class TestAsyncArchival:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        archival = await async_client.agents.memory.archival.retrieve(
            "agent_id",
        )
        assert_matches_type(ArchivalMemorySummary, archival, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.memory.archival.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archival = await response.parse()
        assert_matches_type(ArchivalMemorySummary, archival, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.memory.archival.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archival = await response.parse()
            assert_matches_type(ArchivalMemorySummary, archival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.memory.archival.with_raw_response.retrieve(
                "",
            )
