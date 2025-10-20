# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import EmbeddingGetTotalStorageSizeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_total_storage_size(self, client: LettaSDK) -> None:
        embedding = client.embeddings.get_total_storage_size()
        assert_matches_type(EmbeddingGetTotalStorageSizeResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_total_storage_size_with_all_params(self, client: LettaSDK) -> None:
        embedding = client.embeddings.get_total_storage_size(
            storage_unit="storage-unit",
        )
        assert_matches_type(EmbeddingGetTotalStorageSizeResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_total_storage_size(self, client: LettaSDK) -> None:
        response = client.embeddings.with_raw_response.get_total_storage_size()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingGetTotalStorageSizeResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_total_storage_size(self, client: LettaSDK) -> None:
        with client.embeddings.with_streaming_response.get_total_storage_size() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingGetTotalStorageSizeResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_total_storage_size(self, async_client: AsyncLettaSDK) -> None:
        embedding = await async_client.embeddings.get_total_storage_size()
        assert_matches_type(EmbeddingGetTotalStorageSizeResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_total_storage_size_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        embedding = await async_client.embeddings.get_total_storage_size(
            storage_unit="storage-unit",
        )
        assert_matches_type(EmbeddingGetTotalStorageSizeResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_total_storage_size(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.embeddings.with_raw_response.get_total_storage_size()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingGetTotalStorageSizeResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_total_storage_size(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.embeddings.with_streaming_response.get_total_storage_size() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingGetTotalStorageSizeResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True
