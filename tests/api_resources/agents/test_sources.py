# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import AgentState
from letta_sdk.types.agents import SourceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        source = client.agents.sources.list(
            "agent_id",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.agents.sources.with_raw_response.list(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.agents.sources.with_streaming_response.list(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.sources.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach(self, client: LettaSDK) -> None:
        source = client.agents.sources.attach(
            source_id="source_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: LettaSDK) -> None:
        response = client.agents.sources.with_raw_response.attach(
            source_id="source_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(AgentState, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: LettaSDK) -> None:
        with client.agents.sources.with_streaming_response.attach(
            source_id="source_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(AgentState, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.sources.with_raw_response.attach(
                source_id="source_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.agents.sources.with_raw_response.attach(
                source_id="",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach(self, client: LettaSDK) -> None:
        source = client.agents.sources.detach(
            source_id="source_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: LettaSDK) -> None:
        response = client.agents.sources.with_raw_response.detach(
            source_id="source_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(AgentState, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: LettaSDK) -> None:
        with client.agents.sources.with_streaming_response.detach(
            source_id="source_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(AgentState, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.sources.with_raw_response.detach(
                source_id="source_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.agents.sources.with_raw_response.detach(
                source_id="",
                agent_id="agent_id",
            )


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        source = await async_client.agents.sources.list(
            "agent_id",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.sources.with_raw_response.list(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.sources.with_streaming_response.list(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.sources.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncLettaSDK) -> None:
        source = await async_client.agents.sources.attach(
            source_id="source_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.sources.with_raw_response.attach(
            source_id="source_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(AgentState, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.sources.with_streaming_response.attach(
            source_id="source_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(AgentState, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.sources.with_raw_response.attach(
                source_id="source_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.agents.sources.with_raw_response.attach(
                source_id="",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncLettaSDK) -> None:
        source = await async_client.agents.sources.detach(
            source_id="source_id",
            agent_id="agent_id",
        )
        assert_matches_type(AgentState, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.sources.with_raw_response.detach(
            source_id="source_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(AgentState, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.sources.with_streaming_response.detach(
            source_id="source_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(AgentState, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.sources.with_raw_response.detach(
                source_id="source_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.agents.sources.with_raw_response.detach(
                source_id="",
                agent_id="agent_id",
            )
