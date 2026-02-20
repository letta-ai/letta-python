# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types.steps import MetricRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        metric = client.steps.metrics.retrieve(
            "step-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(MetricRetrieveResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.steps.metrics.with_raw_response.retrieve(
            "step-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricRetrieveResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.steps.metrics.with_streaming_response.retrieve(
            "step-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricRetrieveResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.steps.metrics.with_raw_response.retrieve(
                "",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        metric = await async_client.steps.metrics.retrieve(
            "step-123e4567-e89b-42d3-8456-426614174000",
        )
        assert_matches_type(MetricRetrieveResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.steps.metrics.with_raw_response.retrieve(
            "step-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricRetrieveResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.steps.metrics.with_streaming_response.retrieve(
            "step-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricRetrieveResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.steps.metrics.with_raw_response.retrieve(
                "",
            )
