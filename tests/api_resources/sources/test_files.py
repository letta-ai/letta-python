# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import FileMetadata
from letta_sdk.types.sources import FileListResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.sources.files.retrieve(
                file_id="file_id",
                source_id="source_id",
            )

        assert_matches_type(FileMetadata, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.sources.files.retrieve(
                file_id="file_id",
                source_id="source_id",
                include_content=True,
            )

        assert_matches_type(FileMetadata, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.files.with_raw_response.retrieve(
                file_id="file_id",
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileMetadata, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.files.with_streaming_response.retrieve(
                file_id="file_id",
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(FileMetadata, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.files.with_raw_response.retrieve(
                    file_id="file_id",
                    source_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                client.sources.files.with_raw_response.retrieve(
                    file_id="",
                    source_id="source_id",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.sources.files.list(
                source_id="source_id",
            )

        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.sources.files.list(
                source_id="source_id",
                after="after",
                check_status_updates=True,
                include_content=True,
                limit=0,
            )

        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.files.with_raw_response.list(
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.files.with_streaming_response.list(
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.files.with_raw_response.list(
                    source_id="",
                )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.sources.files.retrieve(
                file_id="file_id",
                source_id="source_id",
            )

        assert_matches_type(FileMetadata, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.sources.files.retrieve(
                file_id="file_id",
                source_id="source_id",
                include_content=True,
            )

        assert_matches_type(FileMetadata, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.files.with_raw_response.retrieve(
                file_id="file_id",
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileMetadata, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.files.with_streaming_response.retrieve(
                file_id="file_id",
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(FileMetadata, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.files.with_raw_response.retrieve(
                    file_id="file_id",
                    source_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                await async_client.sources.files.with_raw_response.retrieve(
                    file_id="",
                    source_id="source_id",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.sources.files.list(
                source_id="source_id",
            )

        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.sources.files.list(
                source_id="source_id",
                after="after",
                check_status_updates=True,
                include_content=True,
                limit=0,
            )

        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.files.with_raw_response.list(
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.files.with_streaming_response.list(
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.files.with_raw_response.list(
                    source_id="",
                )
