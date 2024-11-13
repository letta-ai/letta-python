# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import JobListResponse, JobActiveResponse
from letta_client.types.shared import Job

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        job = client.jobs.retrieve(
            "job_id",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.jobs.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.jobs.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Letta) -> None:
        job = client.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        job = client.jobs.list(
            source_id="source_id",
            user_id="user_id",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        job = client.jobs.delete(
            "job_id",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.jobs.with_raw_response.delete(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.jobs.with_streaming_response.delete(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_active(self, client: Letta) -> None:
        job = client.jobs.active()
        assert_matches_type(JobActiveResponse, job, path=["response"])

    @parametrize
    def test_method_active_with_all_params(self, client: Letta) -> None:
        job = client.jobs.active(
            user_id="user_id",
        )
        assert_matches_type(JobActiveResponse, job, path=["response"])

    @parametrize
    def test_raw_response_active(self, client: Letta) -> None:
        response = client.jobs.with_raw_response.active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobActiveResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_active(self, client: Letta) -> None:
        with client.jobs.with_streaming_response.active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobActiveResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        job = await async_client.jobs.retrieve(
            "job_id",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.jobs.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.jobs.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        job = await async_client.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        job = await async_client.jobs.list(
            source_id="source_id",
            user_id="user_id",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        job = await async_client.jobs.delete(
            "job_id",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.jobs.with_raw_response.delete(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.jobs.with_streaming_response.delete(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_active(self, async_client: AsyncLetta) -> None:
        job = await async_client.jobs.active()
        assert_matches_type(JobActiveResponse, job, path=["response"])

    @parametrize
    async def test_method_active_with_all_params(self, async_client: AsyncLetta) -> None:
        job = await async_client.jobs.active(
            user_id="user_id",
        )
        assert_matches_type(JobActiveResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_active(self, async_client: AsyncLetta) -> None:
        response = await async_client.jobs.with_raw_response.active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobActiveResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_active(self, async_client: AsyncLetta) -> None:
        async with async_client.jobs.with_streaming_response.active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobActiveResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True
