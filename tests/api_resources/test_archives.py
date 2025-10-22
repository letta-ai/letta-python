# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    Archive,
    ArchiveListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArchives:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        archive = client.archives.create(
            name="name",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        archive = client.archives.create(
            name="name",
            description="description",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.archives.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.archives.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(Archive, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Letta) -> None:
        archive = client.archives.update(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        archive = client.archives.update(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            description="description",
            name="name",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.archives.with_raw_response.update(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.archives.with_streaming_response.update(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(Archive, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `archive_id` but received ''"):
            client.archives.with_raw_response.update(
                archive_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        archive = client.archives.list()
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        archive = client.archives.list(
            after="after",
            agent_id="agent_id",
            before="before",
            limit=0,
            name="name",
            order="asc",
        )
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.archives.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.archives.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(ArchiveListResponse, archive, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncArchives:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        archive = await async_client.archives.create(
            name="name",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        archive = await async_client.archives.create(
            name="name",
            description="description",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.archives.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.archives.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(Archive, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        archive = await async_client.archives.update(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        archive = await async_client.archives.update(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            description="description",
            name="name",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.archives.with_raw_response.update(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.archives.with_streaming_response.update(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(Archive, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `archive_id` but received ''"):
            await async_client.archives.with_raw_response.update(
                archive_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        archive = await async_client.archives.list()
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        archive = await async_client.archives.list(
            after="after",
            agent_id="agent_id",
            before="before",
            limit=0,
            name="name",
            order="asc",
        )
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.archives.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.archives.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(ArchiveListResponse, archive, path=["response"])

        assert cast(Any, response.is_closed) is True
