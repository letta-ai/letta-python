# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types.agents import Memory, CoreMemoryRetrieveVariablesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCoreMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        core_memory = client.agents.core_memory.retrieve(
            "agent_id",
        )
        assert_matches_type(Memory, core_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        response = client.agents.core_memory.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        core_memory = response.parse()
        assert_matches_type(Memory, core_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with client.agents.core_memory.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            core_memory = response.parse()
            assert_matches_type(Memory, core_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.core_memory.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_variables(self, client: LettaSDK) -> None:
        core_memory = client.agents.core_memory.retrieve_variables(
            "agent_id",
        )
        assert_matches_type(CoreMemoryRetrieveVariablesResponse, core_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_variables(self, client: LettaSDK) -> None:
        response = client.agents.core_memory.with_raw_response.retrieve_variables(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        core_memory = response.parse()
        assert_matches_type(CoreMemoryRetrieveVariablesResponse, core_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_variables(self, client: LettaSDK) -> None:
        with client.agents.core_memory.with_streaming_response.retrieve_variables(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            core_memory = response.parse()
            assert_matches_type(CoreMemoryRetrieveVariablesResponse, core_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_variables(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.core_memory.with_raw_response.retrieve_variables(
                "",
            )


class TestAsyncCoreMemory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        core_memory = await async_client.agents.core_memory.retrieve(
            "agent_id",
        )
        assert_matches_type(Memory, core_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.core_memory.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        core_memory = await response.parse()
        assert_matches_type(Memory, core_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.core_memory.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            core_memory = await response.parse()
            assert_matches_type(Memory, core_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.core_memory.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_variables(self, async_client: AsyncLettaSDK) -> None:
        core_memory = await async_client.agents.core_memory.retrieve_variables(
            "agent_id",
        )
        assert_matches_type(CoreMemoryRetrieveVariablesResponse, core_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_variables(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.core_memory.with_raw_response.retrieve_variables(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        core_memory = await response.parse()
        assert_matches_type(CoreMemoryRetrieveVariablesResponse, core_memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_variables(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.core_memory.with_streaming_response.retrieve_variables(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            core_memory = await response.parse()
            assert_matches_type(CoreMemoryRetrieveVariablesResponse, core_memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_variables(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.core_memory.with_raw_response.retrieve_variables(
                "",
            )
