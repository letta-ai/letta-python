# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArchives:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach(self, client: Letta) -> None:
        archive = client.agents.archives.attach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Letta) -> None:
        response = client.agents.archives.with_raw_response.attach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(object, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: Letta) -> None:
        with client.agents.archives.with_streaming_response.attach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(object, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archives.with_raw_response.attach(
                archive_id="archive_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `archive_id` but received ''"):
            client.agents.archives.with_raw_response.attach(
                archive_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach(self, client: Letta) -> None:
        archive = client.agents.archives.detach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Letta) -> None:
        response = client.agents.archives.with_raw_response.detach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(object, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: Letta) -> None:
        with client.agents.archives.with_streaming_response.detach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(object, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.archives.with_raw_response.detach(
                archive_id="archive_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `archive_id` but received ''"):
            client.agents.archives.with_raw_response.detach(
                archive_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )


class TestAsyncArchives:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncLetta) -> None:
        archive = await async_client.agents.archives.attach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.archives.with_raw_response.attach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(object, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.archives.with_streaming_response.attach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(object, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archives.with_raw_response.attach(
                archive_id="archive_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `archive_id` but received ''"):
            await async_client.agents.archives.with_raw_response.attach(
                archive_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncLetta) -> None:
        archive = await async_client.agents.archives.detach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(object, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.archives.with_raw_response.detach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(object, archive, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.archives.with_streaming_response.detach(
            archive_id="archive_id",
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(object, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.archives.with_raw_response.detach(
                archive_id="archive_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `archive_id` but received ''"):
            await async_client.agents.archives.with_raw_response.detach(
                archive_id="",
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            )
