# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import Tool

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComposio:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: LettaSDK) -> None:
        composio = client.tools.composio.add(
            "composio_action_name",
        )
        assert_matches_type(Tool, composio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: LettaSDK) -> None:
        response = client.tools.composio.with_raw_response.add(
            "composio_action_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        composio = response.parse()
        assert_matches_type(Tool, composio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: LettaSDK) -> None:
        with client.tools.composio.with_streaming_response.add(
            "composio_action_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            composio = response.parse()
            assert_matches_type(Tool, composio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `composio_action_name` but received ''"):
            client.tools.composio.with_raw_response.add(
                "",
            )


class TestAsyncComposio:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncLettaSDK) -> None:
        composio = await async_client.tools.composio.add(
            "composio_action_name",
        )
        assert_matches_type(Tool, composio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.tools.composio.with_raw_response.add(
            "composio_action_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        composio = await response.parse()
        assert_matches_type(Tool, composio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.tools.composio.with_streaming_response.add(
            "composio_action_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            composio = await response.parse()
            assert_matches_type(Tool, composio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `composio_action_name` but received ''"):
            await async_client.tools.composio.with_raw_response.add(
                "",
            )
