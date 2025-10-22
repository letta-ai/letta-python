# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProperties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Letta) -> None:
        property = client.identities.properties.upsert(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            body=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
        )
        assert_matches_type(object, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Letta) -> None:
        response = client.identities.properties.with_raw_response.upsert(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            body=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(object, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Letta) -> None:
        with client.identities.properties.with_streaming_response.upsert(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            body=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(object, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_id` but received ''"):
            client.identities.properties.with_raw_response.upsert(
                identity_id="",
                body=[
                    {
                        "key": "key",
                        "type": "string",
                        "value": "string",
                    }
                ],
            )


class TestAsyncProperties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLetta) -> None:
        property = await async_client.identities.properties.upsert(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            body=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
        )
        assert_matches_type(object, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLetta) -> None:
        response = await async_client.identities.properties.with_raw_response.upsert(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            body=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(object, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLetta) -> None:
        async with async_client.identities.properties.with_streaming_response.upsert(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            body=[
                {
                    "key": "key",
                    "type": "string",
                    "value": "string",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(object, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_id` but received ''"):
            await async_client.identities.properties.with_raw_response.upsert(
                identity_id="",
                body=[
                    {
                        "key": "key",
                        "type": "string",
                        "value": "string",
                    }
                ],
            )
