# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import (
    Identity,
    IdentityListResponse,
    IdentityCountResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        identity = client.identities.create(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        identity = client.identities.create(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
            agent_ids=["string"],
            block_ids=["string"],
            project_id="project_id",
            properties=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
            x_project="X-Project",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.identities.with_raw_response.create(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.identities.with_streaming_response.create(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(Identity, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        identity = client.identities.retrieve(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.identities.with_raw_response.retrieve(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.identities.with_streaming_response.retrieve(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(Identity, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_id` but received ''"):
            client.identities.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        identity = client.identities.list()
        assert_matches_type(IdentityListResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        identity = client.identities.list(
            after="after",
            before="before",
            identifier_key="identifier_key",
            identity_type="org",
            limit=0,
            name="name",
            order="asc",
            order_by="created_at",
            project_id="project_id",
        )
        assert_matches_type(IdentityListResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.identities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(IdentityListResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.identities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(IdentityListResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        identity = client.identities.delete(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.identities.with_raw_response.delete(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(object, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.identities.with_streaming_response.delete(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(object, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_id` but received ''"):
            client.identities.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_count(self, client: Letta) -> None:
        identity = client.identities.count()
        assert_matches_type(IdentityCountResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: Letta) -> None:
        response = client.identities.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(IdentityCountResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: Letta) -> None:
        with client.identities.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(IdentityCountResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify(self, client: Letta) -> None:
        identity = client.identities.modify(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify_with_all_params(self, client: Letta) -> None:
        identity = client.identities.modify(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            agent_ids=["string"],
            block_ids=["string"],
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
            properties=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_modify(self, client: Letta) -> None:
        response = client.identities.with_raw_response.modify(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_modify(self, client: Letta) -> None:
        with client.identities.with_streaming_response.modify(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(Identity, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_modify(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_id` but received ''"):
            client.identities.with_raw_response.modify(
                identity_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Letta) -> None:
        identity = client.identities.upsert(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Letta) -> None:
        identity = client.identities.upsert(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
            agent_ids=["string"],
            block_ids=["string"],
            project_id="project_id",
            properties=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
            x_project="X-Project",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Letta) -> None:
        response = client.identities.with_raw_response.upsert(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Letta) -> None:
        with client.identities.with_streaming_response.upsert(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(Identity, identity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIdentities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.create(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.create(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
            agent_ids=["string"],
            block_ids=["string"],
            project_id="project_id",
            properties=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
            x_project="X-Project",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.identities.with_raw_response.create(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.identities.with_streaming_response.create(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(Identity, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.retrieve(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.identities.with_raw_response.retrieve(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.identities.with_streaming_response.retrieve(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(Identity, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_id` but received ''"):
            await async_client.identities.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.list()
        assert_matches_type(IdentityListResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.list(
            after="after",
            before="before",
            identifier_key="identifier_key",
            identity_type="org",
            limit=0,
            name="name",
            order="asc",
            order_by="created_at",
            project_id="project_id",
        )
        assert_matches_type(IdentityListResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.identities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(IdentityListResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.identities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(IdentityListResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.delete(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.identities.with_raw_response.delete(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(object, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.identities.with_streaming_response.delete(
            "identity-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(object, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_id` but received ''"):
            await async_client.identities.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.count()
        assert_matches_type(IdentityCountResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncLetta) -> None:
        response = await async_client.identities.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(IdentityCountResponse, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncLetta) -> None:
        async with async_client.identities.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(IdentityCountResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.modify(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify_with_all_params(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.modify(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            agent_ids=["string"],
            block_ids=["string"],
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
            properties=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_modify(self, async_client: AsyncLetta) -> None:
        response = await async_client.identities.with_raw_response.modify(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_modify(self, async_client: AsyncLetta) -> None:
        async with async_client.identities.with_streaming_response.modify(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(Identity, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_modify(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_id` but received ''"):
            await async_client.identities.with_raw_response.modify(
                identity_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.upsert(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncLetta) -> None:
        identity = await async_client.identities.upsert(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
            agent_ids=["string"],
            block_ids=["string"],
            project_id="project_id",
            properties=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
            x_project="X-Project",
        )
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLetta) -> None:
        response = await async_client.identities.with_raw_response.upsert(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(Identity, identity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLetta) -> None:
        async with async_client.identities.with_streaming_response.upsert(
            identifier_key="identifier_key",
            identity_type="org",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(Identity, identity, path=["response"])

        assert cast(Any, response.is_closed) is True
