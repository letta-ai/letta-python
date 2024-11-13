# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    Source,
    SourceListResponse,
)
from letta_client.types.shared import Job

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        source = client.sources.create(
            name="name",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        source = client.sources.create(
            name="name",
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "embedding_endpoint_type",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
            },
            metadata={},
            user_id="user_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.sources.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.sources.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        source = client.sources.retrieve(
            source_name="source_name",
        )
        assert_matches_type(str, source, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Letta) -> None:
        source = client.sources.retrieve(
            source_name="source_name",
            user_id="user_id",
        )
        assert_matches_type(str, source, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.sources.with_raw_response.retrieve(
            source_name="source_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(str, source, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.sources.with_streaming_response.retrieve(
            source_name="source_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(str, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_name` but received ''"):
            client.sources.with_raw_response.retrieve(
                source_name="",
            )

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        source = client.sources.update(
            source_id="source_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        source = client.sources.update(
            source_id="source_id",
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "embedding_endpoint_type",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
            },
            metadata={},
            name="name",
            user_id="user_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.sources.with_raw_response.update(
            source_id="source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.sources.with_streaming_response.update(
            source_id="source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.update(
                source_id="",
            )

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        source = client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        source = client.sources.list(
            user_id="user_id",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        source = client.sources.delete(
            source_id="source_id",
        )
        assert_matches_type(object, source, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Letta) -> None:
        source = client.sources.delete(
            source_id="source_id",
            user_id="user_id",
        )
        assert_matches_type(object, source, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.sources.with_raw_response.delete(
            source_id="source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(object, source, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.sources.with_streaming_response.delete(
            source_id="source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(object, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.delete(
                source_id="",
            )

    @parametrize
    def test_method_attach(self, client: Letta) -> None:
        source = client.sources.attach(
            source_id="source_id",
            agent_id="agent_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_method_attach_with_all_params(self, client: Letta) -> None:
        source = client.sources.attach(
            source_id="source_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_raw_response_attach(self, client: Letta) -> None:
        response = client.sources.with_raw_response.attach(
            source_id="source_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_streaming_response_attach(self, client: Letta) -> None:
        with client.sources.with_streaming_response.attach(
            source_id="source_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.attach(
                source_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_detach(self, client: Letta) -> None:
        source = client.sources.detach(
            source_id="source_id",
            agent_id="agent_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_method_detach_with_all_params(self, client: Letta) -> None:
        source = client.sources.detach(
            source_id="source_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_raw_response_detach(self, client: Letta) -> None:
        response = client.sources.with_raw_response.detach(
            source_id="source_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    def test_streaming_response_detach(self, client: Letta) -> None:
        with client.sources.with_streaming_response.detach(
            source_id="source_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_detach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.detach(
                source_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_upload(self, client: Letta) -> None:
        source = client.sources.upload(
            source_id="source_id",
            file=b"raw file contents",
        )
        assert_matches_type(Job, source, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Letta) -> None:
        source = client.sources.upload(
            source_id="source_id",
            file=b"raw file contents",
            user_id="user_id",
        )
        assert_matches_type(Job, source, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Letta) -> None:
        response = client.sources.with_raw_response.upload(
            source_id="source_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Job, source, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Letta) -> None:
        with client.sources.with_streaming_response.upload(
            source_id="source_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(Job, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.upload(
                source_id="",
                file=b"raw file contents",
            )


class TestAsyncSources:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.create(
            name="name",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.create(
            name="name",
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "embedding_endpoint_type",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
            },
            metadata={},
            user_id="user_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.retrieve(
            source_name="source_name",
        )
        assert_matches_type(str, source, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.retrieve(
            source_name="source_name",
            user_id="user_id",
        )
        assert_matches_type(str, source, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.with_raw_response.retrieve(
            source_name="source_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(str, source, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.with_streaming_response.retrieve(
            source_name="source_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(str, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_name` but received ''"):
            await async_client.sources.with_raw_response.retrieve(
                source_name="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.update(
            source_id="source_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.update(
            source_id="source_id",
            description="description",
            embedding_config={
                "embedding_dim": 0,
                "embedding_endpoint_type": "embedding_endpoint_type",
                "embedding_model": "embedding_model",
                "azure_deployment": "azure_deployment",
                "azure_endpoint": "azure_endpoint",
                "azure_version": "azure_version",
                "embedding_chunk_size": 0,
                "embedding_endpoint": "embedding_endpoint",
            },
            metadata={},
            name="name",
            user_id="user_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.with_raw_response.update(
            source_id="source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.with_streaming_response.update(
            source_id="source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.update(
                source_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.list(
            user_id="user_id",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.delete(
            source_id="source_id",
        )
        assert_matches_type(object, source, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.delete(
            source_id="source_id",
            user_id="user_id",
        )
        assert_matches_type(object, source, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.with_raw_response.delete(
            source_id="source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(object, source, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.with_streaming_response.delete(
            source_id="source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(object, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.delete(
                source_id="",
            )

    @parametrize
    async def test_method_attach(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.attach(
            source_id="source_id",
            agent_id="agent_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_method_attach_with_all_params(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.attach(
            source_id="source_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.with_raw_response.attach(
            source_id="source_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.with_streaming_response.attach(
            source_id="source_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.attach(
                source_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_detach(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.detach(
            source_id="source_id",
            agent_id="agent_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_method_detach_with_all_params(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.detach(
            source_id="source_id",
            agent_id="agent_id",
            user_id="user_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.with_raw_response.detach(
            source_id="source_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Source, source, path=["response"])

    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.with_streaming_response.detach(
            source_id="source_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_detach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.detach(
                source_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.upload(
            source_id="source_id",
            file=b"raw file contents",
        )
        assert_matches_type(Job, source, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncLetta) -> None:
        source = await async_client.sources.upload(
            source_id="source_id",
            file=b"raw file contents",
            user_id="user_id",
        )
        assert_matches_type(Job, source, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncLetta) -> None:
        response = await async_client.sources.with_raw_response.upload(
            source_id="source_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Job, source, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncLetta) -> None:
        async with async_client.sources.with_streaming_response.upload(
            source_id="source_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(Job, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.upload(
                source_id="",
                file=b"raw file contents",
            )
