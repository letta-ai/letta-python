# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    Folder,
    FileMetadata,
    FolderListResponse,
    FolderCountResponse,
    FolderListFilesResponse,
    FolderListAgentsResponse,
    OrganizationSourcesStats,
    FolderListPassagesResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LettaSDK) -> None:
        folder = client.folders.create(
            name="name",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LettaSDK) -> None:
        folder = client.folders.create(
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
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        folder = client.folders.retrieve(
            "folder_id",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.retrieve(
            "folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.retrieve(
            "folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LettaSDK) -> None:
        folder = client.folders.update(
            folder_id="folder_id",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LettaSDK) -> None:
        folder = client.folders.update(
            folder_id="folder_id",
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
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.update(
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.update(
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.update(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        folder = client.folders.list()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        folder = client.folders.list(
            after="after",
            before="before",
            limit=0,
            name="name",
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        folder = client.folders.delete(
            "folder_id",
        )
        assert_matches_type(object, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.delete(
            "folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(object, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.delete(
            "folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(object, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_count(self, client: LettaSDK) -> None:
        folder = client.folders.count()
        assert_matches_type(FolderCountResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderCountResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderCountResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_file(self, client: LettaSDK) -> None:
        folder = client.folders.delete_file(
            file_id="file_id",
            folder_id="folder_id",
        )
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_file(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.delete_file(
            file_id="file_id",
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_file(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.delete_file(
            file_id="file_id",
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_file(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.delete_file(
                file_id="file_id",
                folder_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.folders.with_raw_response.delete_file(
                file_id="",
                folder_id="folder_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_name(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            folder = client.folders.get_by_name(
                "folder_name",
            )

        assert_matches_type(str, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_name(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.folders.with_raw_response.get_by_name(
                "folder_name",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(str, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_name(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.folders.with_streaming_response.get_by_name(
                "folder_name",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                folder = response.parse()
                assert_matches_type(str, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_name(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_name` but received ''"):
                client.folders.with_raw_response.get_by_name(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_agents(self, client: LettaSDK) -> None:
        folder = client.folders.list_agents(
            folder_id="folder_id",
        )
        assert_matches_type(FolderListAgentsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_agents_with_all_params(self, client: LettaSDK) -> None:
        folder = client.folders.list_agents(
            folder_id="folder_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(FolderListAgentsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_agents(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.list_agents(
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListAgentsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_agents(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.list_agents(
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListAgentsResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_agents(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.list_agents(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_files(self, client: LettaSDK) -> None:
        folder = client.folders.list_files(
            folder_id="folder_id",
        )
        assert_matches_type(FolderListFilesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_files_with_all_params(self, client: LettaSDK) -> None:
        folder = client.folders.list_files(
            folder_id="folder_id",
            after="after",
            before="before",
            include_content=True,
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(FolderListFilesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_files(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.list_files(
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListFilesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_files(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.list_files(
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListFilesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_files(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.list_files(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_passages(self, client: LettaSDK) -> None:
        folder = client.folders.list_passages(
            folder_id="folder_id",
        )
        assert_matches_type(FolderListPassagesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_passages_with_all_params(self, client: LettaSDK) -> None:
        folder = client.folders.list_passages(
            folder_id="folder_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(FolderListPassagesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_passages(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.list_passages(
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListPassagesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_passages(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.list_passages(
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListPassagesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_passages(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.list_passages(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_metadata(self, client: LettaSDK) -> None:
        folder = client.folders.retrieve_metadata()
        assert_matches_type(OrganizationSourcesStats, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_metadata_with_all_params(self, client: LettaSDK) -> None:
        folder = client.folders.retrieve_metadata(
            include_detailed_per_source_metadata=True,
        )
        assert_matches_type(OrganizationSourcesStats, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_metadata(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.retrieve_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(OrganizationSourcesStats, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_metadata(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.retrieve_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(OrganizationSourcesStats, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file(self, client: LettaSDK) -> None:
        folder = client.folders.upload_file(
            folder_id="folder_id",
            file=b"raw file contents",
        )
        assert_matches_type(FileMetadata, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file_with_all_params(self, client: LettaSDK) -> None:
        folder = client.folders.upload_file(
            folder_id="folder_id",
            file=b"raw file contents",
            duplicate_handling="skip",
            name="name",
        )
        assert_matches_type(FileMetadata, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_file(self, client: LettaSDK) -> None:
        response = client.folders.with_raw_response.upload_file(
            folder_id="folder_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FileMetadata, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_file(self, client: LettaSDK) -> None:
        with client.folders.with_streaming_response.upload_file(
            folder_id="folder_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FileMetadata, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload_file(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.upload_file(
                folder_id="",
                file=b"raw file contents",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.create(
            name="name",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.create(
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
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.retrieve(
            "folder_id",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.retrieve(
            "folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.retrieve(
            "folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.update(
            folder_id="folder_id",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.update(
            folder_id="folder_id",
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
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.update(
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.update(
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.update(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.list()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.list(
            after="after",
            before="before",
            limit=0,
            name="name",
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.delete(
            "folder_id",
        )
        assert_matches_type(object, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.delete(
            "folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(object, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.delete(
            "folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(object, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.count()
        assert_matches_type(FolderCountResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderCountResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderCountResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_file(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.delete_file(
            file_id="file_id",
            folder_id="folder_id",
        )
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_file(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.delete_file(
            file_id="file_id",
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_file(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.delete_file(
            file_id="file_id",
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.delete_file(
                file_id="file_id",
                folder_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.folders.with_raw_response.delete_file(
                file_id="",
                folder_id="folder_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            folder = await async_client.folders.get_by_name(
                "folder_name",
            )

        assert_matches_type(str, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.folders.with_raw_response.get_by_name(
                "folder_name",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(str, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.folders.with_streaming_response.get_by_name(
                "folder_name",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                folder = await response.parse()
                assert_matches_type(str, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_name` but received ''"):
                await async_client.folders.with_raw_response.get_by_name(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_agents(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.list_agents(
            folder_id="folder_id",
        )
        assert_matches_type(FolderListAgentsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_agents_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.list_agents(
            folder_id="folder_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(FolderListAgentsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_agents(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.list_agents(
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListAgentsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_agents(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.list_agents(
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListAgentsResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_agents(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.list_agents(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_files(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.list_files(
            folder_id="folder_id",
        )
        assert_matches_type(FolderListFilesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_files_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.list_files(
            folder_id="folder_id",
            after="after",
            before="before",
            include_content=True,
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(FolderListFilesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_files(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.list_files(
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListFilesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_files(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.list_files(
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListFilesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_files(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.list_files(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_passages(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.list_passages(
            folder_id="folder_id",
        )
        assert_matches_type(FolderListPassagesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_passages_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.list_passages(
            folder_id="folder_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(FolderListPassagesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_passages(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.list_passages(
            folder_id="folder_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListPassagesResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_passages(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.list_passages(
            folder_id="folder_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListPassagesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_passages(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.list_passages(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_metadata(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.retrieve_metadata()
        assert_matches_type(OrganizationSourcesStats, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_metadata_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.retrieve_metadata(
            include_detailed_per_source_metadata=True,
        )
        assert_matches_type(OrganizationSourcesStats, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_metadata(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.retrieve_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(OrganizationSourcesStats, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_metadata(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.retrieve_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(OrganizationSourcesStats, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.upload_file(
            folder_id="folder_id",
            file=b"raw file contents",
        )
        assert_matches_type(FileMetadata, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        folder = await async_client.folders.upload_file(
            folder_id="folder_id",
            file=b"raw file contents",
            duplicate_handling="skip",
            name="name",
        )
        assert_matches_type(FileMetadata, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_file(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.folders.with_raw_response.upload_file(
            folder_id="folder_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FileMetadata, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_file(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.folders.with_streaming_response.upload_file(
            folder_id="folder_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FileMetadata, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload_file(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.upload_file(
                folder_id="",
                file=b"raw file contents",
            )
