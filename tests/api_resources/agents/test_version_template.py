# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types.agents import VersionTemplateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersionTemplate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Letta) -> None:
        version_template = client.agents.version_template.create(
            agent_id="agent_id",
        )
        assert_matches_type(VersionTemplateCreateResponse, version_template, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        version_template = client.agents.version_template.create(
            agent_id="agent_id",
            return_agent_id=True,
            migrate_deployed_agents=True,
        )
        assert_matches_type(VersionTemplateCreateResponse, version_template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.agents.version_template.with_raw_response.create(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version_template = response.parse()
        assert_matches_type(VersionTemplateCreateResponse, version_template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.agents.version_template.with_streaming_response.create(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version_template = response.parse()
            assert_matches_type(VersionTemplateCreateResponse, version_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.version_template.with_raw_response.create(
                agent_id="",
            )


class TestAsyncVersionTemplate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        version_template = await async_client.agents.version_template.create(
            agent_id="agent_id",
        )
        assert_matches_type(VersionTemplateCreateResponse, version_template, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        version_template = await async_client.agents.version_template.create(
            agent_id="agent_id",
            return_agent_id=True,
            migrate_deployed_agents=True,
        )
        assert_matches_type(VersionTemplateCreateResponse, version_template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.version_template.with_raw_response.create(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version_template = await response.parse()
        assert_matches_type(VersionTemplateCreateResponse, version_template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.version_template.with_streaming_response.create(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version_template = await response.parse()
            assert_matches_type(VersionTemplateCreateResponse, version_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.version_template.with_raw_response.create(
                agent_id="",
            )
