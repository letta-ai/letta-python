# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    Source,
    FileMetadata,
    SourceListResponse,
    SourceCountResponse,
    SourceGetAgentsResponse,
    OrganizationSourcesStats,
    SourceListPassagesResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.create(
                name="name",
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.create(
                name="name",
                description="description",
                embedding="embedding",
                embedding_chunk_size=0,
                embedding_config={
                    "embedding_dim": 0,
                    "embedding_endpoint_type": "openai",
                    "embedding_model": "embedding_model",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "azure_version": "azure_version",
                    "batch_size": 0,
                    "embedding_chunk_size": 0,
                    "embedding_endpoint": "embedding_endpoint",
                    "handle": "handle",
                },
                instructions="instructions",
                metadata={"foo": "bar"},
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.create(
                name="name",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.create(
                name="name",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.retrieve(
                "source_id",
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.retrieve(
                "source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.retrieve(
                "source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.with_raw_response.retrieve(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.update(
                source_id="source_id",
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.update(
                source_id="source_id",
                description="description",
                embedding_config={
                    "embedding_dim": 0,
                    "embedding_endpoint_type": "openai",
                    "embedding_model": "embedding_model",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "azure_version": "azure_version",
                    "batch_size": 0,
                    "embedding_chunk_size": 0,
                    "embedding_endpoint": "embedding_endpoint",
                    "handle": "handle",
                },
                instructions="instructions",
                metadata={"foo": "bar"},
                name="name",
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.update(
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.update(
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.with_raw_response.update(
                    source_id="",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.list()

        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.delete(
                "source_id",
            )

        assert_matches_type(object, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.delete(
                "source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(object, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.delete(
                "source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(object, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.with_raw_response.delete(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_count(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.count()

        assert_matches_type(SourceCountResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceCountResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.count() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(SourceCountResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_file(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.delete_file(
                file_id="file_id",
                source_id="source_id",
            )

        assert source is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_file(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.delete_file(
                file_id="file_id",
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert source is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_file(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.delete_file(
                file_id="file_id",
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert source is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_file(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.with_raw_response.delete_file(
                    file_id="file_id",
                    source_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                client.sources.with_raw_response.delete_file(
                    file_id="",
                    source_id="source_id",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_agents(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.get_agents(
                "source_id",
            )

        assert_matches_type(SourceGetAgentsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_agents(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.get_agents(
                "source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceGetAgentsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_agents(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.get_agents(
                "source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(SourceGetAgentsResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_agents(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.with_raw_response.get_agents(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_name(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.get_by_name(
                "source_name",
            )

        assert_matches_type(str, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_name(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.get_by_name(
                "source_name",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(str, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_name(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.get_by_name(
                "source_name",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(str, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_name(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_name` but received ''"):
                client.sources.with_raw_response.get_by_name(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_metadata(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.get_metadata()

        assert_matches_type(OrganizationSourcesStats, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_metadata_with_all_params(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.get_metadata(
                include_detailed_per_source_metadata=True,
            )

        assert_matches_type(OrganizationSourcesStats, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_metadata(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.get_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(OrganizationSourcesStats, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_metadata(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.get_metadata() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(OrganizationSourcesStats, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_passages(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.list_passages(
                source_id="source_id",
            )

        assert_matches_type(SourceListPassagesResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_passages_with_all_params(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.list_passages(
                source_id="source_id",
                after="after",
                before="before",
                limit=0,
            )

        assert_matches_type(SourceListPassagesResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_passages(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.list_passages(
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListPassagesResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_passages(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.list_passages(
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(SourceListPassagesResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_passages(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.with_raw_response.list_passages(
                    source_id="",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.upload_file(
                source_id="source_id",
                file=b"raw file contents",
            )

        assert_matches_type(FileMetadata, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file_with_all_params(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = client.sources.upload_file(
                source_id="source_id",
                file=b"raw file contents",
                duplicate_handling="skip",
                name="name",
            )

        assert_matches_type(FileMetadata, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_file(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.sources.with_raw_response.upload_file(
                source_id="source_id",
                file=b"raw file contents",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(FileMetadata, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_file(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.sources.with_streaming_response.upload_file(
                source_id="source_id",
                file=b"raw file contents",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = response.parse()
                assert_matches_type(FileMetadata, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload_file(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                client.sources.with_raw_response.upload_file(
                    source_id="",
                    file=b"raw file contents",
                )


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.create(
                name="name",
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.create(
                name="name",
                description="description",
                embedding="embedding",
                embedding_chunk_size=0,
                embedding_config={
                    "embedding_dim": 0,
                    "embedding_endpoint_type": "openai",
                    "embedding_model": "embedding_model",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "azure_version": "azure_version",
                    "batch_size": 0,
                    "embedding_chunk_size": 0,
                    "embedding_endpoint": "embedding_endpoint",
                    "handle": "handle",
                },
                instructions="instructions",
                metadata={"foo": "bar"},
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.create(
                name="name",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.create(
                name="name",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.retrieve(
                "source_id",
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.retrieve(
                "source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.retrieve(
                "source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.with_raw_response.retrieve(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.update(
                source_id="source_id",
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.update(
                source_id="source_id",
                description="description",
                embedding_config={
                    "embedding_dim": 0,
                    "embedding_endpoint_type": "openai",
                    "embedding_model": "embedding_model",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "azure_version": "azure_version",
                    "batch_size": 0,
                    "embedding_chunk_size": 0,
                    "embedding_endpoint": "embedding_endpoint",
                    "handle": "handle",
                },
                instructions="instructions",
                metadata={"foo": "bar"},
                name="name",
            )

        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.update(
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.update(
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.with_raw_response.update(
                    source_id="",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.list()

        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.delete(
                "source_id",
            )

        assert_matches_type(object, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.delete(
                "source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(object, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.delete(
                "source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(object, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.with_raw_response.delete(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.count()

        assert_matches_type(SourceCountResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceCountResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.count() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(SourceCountResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.delete_file(
                file_id="file_id",
                source_id="source_id",
            )

        assert source is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.delete_file(
                file_id="file_id",
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert source is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.delete_file(
                file_id="file_id",
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert source is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.with_raw_response.delete_file(
                    file_id="file_id",
                    source_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                await async_client.sources.with_raw_response.delete_file(
                    file_id="",
                    source_id="source_id",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_agents(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.get_agents(
                "source_id",
            )

        assert_matches_type(SourceGetAgentsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_agents(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.get_agents(
                "source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceGetAgentsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_agents(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.get_agents(
                "source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(SourceGetAgentsResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_agents(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.with_raw_response.get_agents(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.get_by_name(
                "source_name",
            )

        assert_matches_type(str, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.get_by_name(
                "source_name",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(str, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.get_by_name(
                "source_name",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(str, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_name` but received ''"):
                await async_client.sources.with_raw_response.get_by_name(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_metadata(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.get_metadata()

        assert_matches_type(OrganizationSourcesStats, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_metadata_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.get_metadata(
                include_detailed_per_source_metadata=True,
            )

        assert_matches_type(OrganizationSourcesStats, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_metadata(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.get_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(OrganizationSourcesStats, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_metadata(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.get_metadata() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(OrganizationSourcesStats, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_passages(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.list_passages(
                source_id="source_id",
            )

        assert_matches_type(SourceListPassagesResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_passages_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.list_passages(
                source_id="source_id",
                after="after",
                before="before",
                limit=0,
            )

        assert_matches_type(SourceListPassagesResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_passages(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.list_passages(
                source_id="source_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListPassagesResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_passages(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.list_passages(
                source_id="source_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(SourceListPassagesResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_passages(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.with_raw_response.list_passages(
                    source_id="",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.upload_file(
                source_id="source_id",
                file=b"raw file contents",
            )

        assert_matches_type(FileMetadata, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            source = await async_client.sources.upload_file(
                source_id="source_id",
                file=b"raw file contents",
                duplicate_handling="skip",
                name="name",
            )

        assert_matches_type(FileMetadata, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.sources.with_raw_response.upload_file(
                source_id="source_id",
                file=b"raw file contents",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(FileMetadata, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.sources.with_streaming_response.upload_file(
                source_id="source_id",
                file=b"raw file contents",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source = await response.parse()
                assert_matches_type(FileMetadata, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
                await async_client.sources.with_raw_response.upload_file(
                    source_id="",
                    file=b"raw file contents",
                )
