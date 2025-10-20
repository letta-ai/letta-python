# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    RunListResponse,
    RunListStepsResponse,
    RunListActiveResponse,
    RunListMessagesResponse,
    RunRetrieveUsageResponse,
)
from letta_sdk.types.agents import Run

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        run = client.runs.retrieve(
            "run_id",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        response = client.runs.with_raw_response.retrieve(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with client.runs.with_streaming_response.retrieve(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        run = client.runs.list()
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        run = client.runs.list(
            active=True,
            after="after",
            agent_ids=["string"],
            ascending=True,
            background=True,
            before="before",
            limit=0,
            stop_reason="end_turn",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        run = client.runs.delete(
            "run_id",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.runs.with_raw_response.delete(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.runs.with_streaming_response.delete(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_active(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            run = client.runs.list_active()

        assert_matches_type(RunListActiveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_active_with_all_params(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            run = client.runs.list_active(
                agent_ids=["string"],
                background=True,
            )

        assert_matches_type(RunListActiveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_active(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.runs.with_raw_response.list_active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListActiveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_active(self, client: LettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.runs.with_streaming_response.list_active() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = response.parse()
                assert_matches_type(RunListActiveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_messages(self, client: LettaSDK) -> None:
        run = client.runs.list_messages(
            run_id="run_id",
        )
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_messages_with_all_params(self, client: LettaSDK) -> None:
        run = client.runs.list_messages(
            run_id="run_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
        )
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_messages(self, client: LettaSDK) -> None:
        response = client.runs.with_raw_response.list_messages(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_messages(self, client: LettaSDK) -> None:
        with client.runs.with_streaming_response.list_messages(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListMessagesResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_messages(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.list_messages(
                run_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_steps(self, client: LettaSDK) -> None:
        run = client.runs.list_steps(
            run_id="run_id",
        )
        assert_matches_type(RunListStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_steps_with_all_params(self, client: LettaSDK) -> None:
        run = client.runs.list_steps(
            run_id="run_id",
            after="after",
            before="before",
            limit=0,
            order="order",
        )
        assert_matches_type(RunListStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_steps(self, client: LettaSDK) -> None:
        response = client.runs.with_raw_response.list_steps(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_steps(self, client: LettaSDK) -> None:
        with client.runs.with_streaming_response.list_steps(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListStepsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_steps(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.list_steps(
                run_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_stream(self, client: LettaSDK) -> None:
        run = client.runs.retrieve_stream(
            run_id="run_id",
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_stream_with_all_params(self, client: LettaSDK) -> None:
        run = client.runs.retrieve_stream(
            run_id="run_id",
            batch_size=0,
            include_pings=True,
            poll_interval=0,
            starting_after=0,
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_stream(self, client: LettaSDK) -> None:
        response = client.runs.with_raw_response.retrieve_stream(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_stream(self, client: LettaSDK) -> None:
        with client.runs.with_streaming_response.retrieve_stream(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_stream(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.retrieve_stream(
                run_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_usage(self, client: LettaSDK) -> None:
        run = client.runs.retrieve_usage(
            "run_id",
        )
        assert_matches_type(RunRetrieveUsageResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_usage(self, client: LettaSDK) -> None:
        response = client.runs.with_raw_response.retrieve_usage(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunRetrieveUsageResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_usage(self, client: LettaSDK) -> None:
        with client.runs.with_streaming_response.retrieve_usage(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunRetrieveUsageResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_usage(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.retrieve_usage(
                "",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.retrieve(
            "run_id",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.runs.with_raw_response.retrieve(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.runs.with_streaming_response.retrieve(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.list()
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.list(
            active=True,
            after="after",
            agent_ids=["string"],
            ascending=True,
            background=True,
            before="before",
            limit=0,
            stop_reason="end_turn",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.delete(
            "run_id",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.runs.with_raw_response.delete(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.runs.with_streaming_response.delete(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_active(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            run = await async_client.runs.list_active()

        assert_matches_type(RunListActiveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_active_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            run = await async_client.runs.list_active(
                agent_ids=["string"],
                background=True,
            )

        assert_matches_type(RunListActiveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_active(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.runs.with_raw_response.list_active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListActiveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_active(self, async_client: AsyncLettaSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.runs.with_streaming_response.list_active() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = await response.parse()
                assert_matches_type(RunListActiveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_messages(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.list_messages(
            run_id="run_id",
        )
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_messages_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.list_messages(
            run_id="run_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
        )
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.runs.with_raw_response.list_messages(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListMessagesResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.runs.with_streaming_response.list_messages(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListMessagesResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.list_messages(
                run_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_steps(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.list_steps(
            run_id="run_id",
        )
        assert_matches_type(RunListStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_steps_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.list_steps(
            run_id="run_id",
            after="after",
            before="before",
            limit=0,
            order="order",
        )
        assert_matches_type(RunListStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_steps(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.runs.with_raw_response.list_steps(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_steps(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.runs.with_streaming_response.list_steps(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListStepsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_steps(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.list_steps(
                run_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_stream(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.retrieve_stream(
            run_id="run_id",
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_stream_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.retrieve_stream(
            run_id="run_id",
            batch_size=0,
            include_pings=True,
            poll_interval=0,
            starting_after=0,
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_stream(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.runs.with_raw_response.retrieve_stream(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_stream(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.runs.with_streaming_response.retrieve_stream(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_stream(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.retrieve_stream(
                run_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_usage(self, async_client: AsyncLettaSDK) -> None:
        run = await async_client.runs.retrieve_usage(
            "run_id",
        )
        assert_matches_type(RunRetrieveUsageResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_usage(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.runs.with_raw_response.retrieve_usage(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunRetrieveUsageResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_usage(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.runs.with_streaming_response.retrieve_usage(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunRetrieveUsageResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_usage(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.retrieve_usage(
                "",
            )
