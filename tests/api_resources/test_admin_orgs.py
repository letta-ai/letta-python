# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta import Letta, AsyncLetta
from letta.types import AdminOrgListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdminOrgs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        admin_org = client.admin_orgs.list()
        assert_matches_type(AdminOrgListResponse, admin_org, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        admin_org = client.admin_orgs.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AdminOrgListResponse, admin_org, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.admin_orgs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_org = response.parse()
        assert_matches_type(AdminOrgListResponse, admin_org, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.admin_orgs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_org = response.parse()
            assert_matches_type(AdminOrgListResponse, admin_org, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdminOrgs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        admin_org = await async_client.admin_orgs.list()
        assert_matches_type(AdminOrgListResponse, admin_org, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        admin_org = await async_client.admin_orgs.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AdminOrgListResponse, admin_org, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.admin_orgs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_org = await response.parse()
        assert_matches_type(AdminOrgListResponse, admin_org, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.admin_orgs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_org = await response.parse()
            assert_matches_type(AdminOrgListResponse, admin_org, path=["response"])

        assert cast(Any, response.is_closed) is True
