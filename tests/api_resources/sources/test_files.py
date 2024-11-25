# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from tests.utils import assert_matches_type
from letta.types.sources import FileListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        file = client.sources.files.list(
            source_id="source_id",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        file = client.sources.files.list(
            source_id="source_id",
            cursor="cursor",
            limit=0,
            user_id="user_id",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.sources.files.with_raw_response.list(
            source_id="source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.sources.files.with_streaming_response.list(
            source_id="source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.files.with_raw_response.list(
                source_id="",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        file = await async_client.sources.files.list(
            source_id="source_id",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        file = await async_client.sources.files.list(
            source_id="source_id",
            cursor="cursor",
            limit=0,
            user_id="user_id",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.files.with_raw_response.list(
            source_id="source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.files.with_streaming_response.list(
            source_id="source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.files.with_raw_response.list(
                source_id="",
            )
