# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import ProviderTrace

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelemetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            telemetry = client.telemetry.retrieve(
                "step_id",
            )

        assert_matches_type(Optional[ProviderTrace], telemetry, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.telemetry.with_raw_response.retrieve(
                "step_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(Optional[ProviderTrace], telemetry, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.telemetry.with_streaming_response.retrieve(
                "step_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                telemetry = response.parse()
                assert_matches_type(Optional[ProviderTrace], telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
                client.telemetry.with_raw_response.retrieve(
                    "",
                )


class TestAsyncTelemetry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            telemetry = await async_client.telemetry.retrieve(
                "step_id",
            )

        assert_matches_type(Optional[ProviderTrace], telemetry, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.telemetry.with_raw_response.retrieve(
                "step_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(Optional[ProviderTrace], telemetry, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.telemetry.with_streaming_response.retrieve(
                "step_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                telemetry = await response.parse()
                assert_matches_type(Optional[ProviderTrace], telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
                await async_client.telemetry.with_raw_response.retrieve(
                    "",
                )
