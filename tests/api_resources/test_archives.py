# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import Archive, ArchiveRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArchives:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LettaSDK) -> None:
        archive = client.archives.update(
            name="name",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LettaSDK) -> None:
        archive = client.archives.update(
            name="name",
            description="description",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LettaSDK) -> None:
        response = client.archives.with_raw_response.update(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LettaSDK) -> None:
        with client.archives.with_streaming_response.update(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(Archive, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        archive = client.archives.retrieve()
        assert_matches_type(ArchiveRetrieveResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LettaSDK) -> None:
        archive = client.archives.retrieve(
            after="after",
            agent_id="agent_id",
            before="before",
            limit=0,
            name="name",
            order="asc",
        )
        assert_matches_type(ArchiveRetrieveResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        response = client.archives.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(ArchiveRetrieveResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with client.archives.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(ArchiveRetrieveResponse, archive, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncArchives:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLettaSDK) -> None:
        archive = await async_client.archives.update(
            name="name",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        archive = await async_client.archives.update(
            name="name",
            description="description",
        )
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.archives.with_raw_response.update(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(Archive, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.archives.with_streaming_response.update(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(Archive, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        archive = await async_client.archives.retrieve()
        assert_matches_type(ArchiveRetrieveResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        archive = await async_client.archives.retrieve(
            after="after",
            agent_id="agent_id",
            before="before",
            limit=0,
            name="name",
            order="asc",
        )
        assert_matches_type(ArchiveRetrieveResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.archives.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(ArchiveRetrieveResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.archives.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(ArchiveRetrieveResponse, archive, path=["response"])

        assert cast(Any, response.is_closed) is True
