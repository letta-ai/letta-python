# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from letta.types import (
    User,
    AdminUserListResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdminUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        admin_user = client.admin_users.create(
            name="name",
            organization_id="organization_id",
        )
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.admin_users.with_raw_response.create(
            name="name",
            organization_id="organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = response.parse()
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.admin_users.with_streaming_response.create(
            name="name",
            organization_id="organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = response.parse()
            assert_matches_type(User, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Letta) -> None:
        admin_user = client.admin_users.update(
            id="id",
        )
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        admin_user = client.admin_users.update(
            id="id",
            name="name",
            organization_id="organization_id",
        )
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.admin_users.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = response.parse()
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.admin_users.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = response.parse()
            assert_matches_type(User, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        admin_user = client.admin_users.list()
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        admin_user = client.admin_users.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.admin_users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = response.parse()
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.admin_users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = response.parse()
            assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        admin_user = client.admin_users.delete(
            user_id="user_id",
        )
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.admin_users.with_raw_response.delete(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = response.parse()
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.admin_users.with_streaming_response.delete(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = response.parse()
            assert_matches_type(User, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdminUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        admin_user = await async_client.admin_users.create(
            name="name",
            organization_id="organization_id",
        )
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.admin_users.with_raw_response.create(
            name="name",
            organization_id="organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = await response.parse()
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.admin_users.with_streaming_response.create(
            name="name",
            organization_id="organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = await response.parse()
            assert_matches_type(User, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        admin_user = await async_client.admin_users.update(
            id="id",
        )
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        admin_user = await async_client.admin_users.update(
            id="id",
            name="name",
            organization_id="organization_id",
        )
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.admin_users.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = await response.parse()
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.admin_users.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = await response.parse()
            assert_matches_type(User, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        admin_user = await async_client.admin_users.list()
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        admin_user = await async_client.admin_users.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.admin_users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = await response.parse()
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.admin_users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = await response.parse()
            assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        admin_user = await async_client.admin_users.delete(
            user_id="user_id",
        )
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.admin_users.with_raw_response.delete(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = await response.parse()
        assert_matches_type(User, admin_user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.admin_users.with_streaming_response.delete(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = await response.parse()
            assert_matches_type(User, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True
