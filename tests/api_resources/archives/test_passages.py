# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_client import Letta, AsyncLetta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPassages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        passage = client.archives.passages.delete(
            passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )
        assert passage is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.archives.passages.with_raw_response.delete(
            passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = response.parse()
        assert passage is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.archives.passages.with_streaming_response.delete(
            passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passage = response.parse()
            assert passage is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `archive_id` but received ''"):
            client.archives.passages.with_raw_response.delete(
                passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
                archive_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `passage_id` but received ''"):
            client.archives.passages.with_raw_response.delete(
                passage_id="",
                archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            )


class TestAsyncPassages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        passage = await async_client.archives.passages.delete(
            passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )
        assert passage is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.archives.passages.with_raw_response.delete(
            passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passage = await response.parse()
        assert passage is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.archives.passages.with_streaming_response.delete(
            passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passage = await response.parse()
            assert passage is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `archive_id` but received ''"):
            await async_client.archives.passages.with_raw_response.delete(
                passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
                archive_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `passage_id` but received ''"):
            await async_client.archives.passages.with_raw_response.delete(
                passage_id="",
                archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            )
