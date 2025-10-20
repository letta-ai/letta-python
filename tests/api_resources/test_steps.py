# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    Step,
    ProviderTrace,
    StepListResponse,
    StepListMessagesResponse,
    StepRetrieveMetricsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        step = client.steps.retrieve(
            "step_id",
        )
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        response = client.steps.with_raw_response.retrieve(
            "step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with client.steps.with_streaming_response.retrieve(
            "step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(Step, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.steps.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        step = client.steps.list()
        assert_matches_type(StepListResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        step = client.steps.list(
            after="after",
            agent_id="agent_id",
            before="before",
            end_date="end_date",
            feedback="positive",
            has_feedback=True,
            limit=0,
            model="model",
            order="asc",
            order_by="created_at",
            project_id="project_id",
            start_date="start_date",
            tags=["string"],
            trace_ids=["string"],
            x_project="X-Project",
        )
        assert_matches_type(StepListResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.steps.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(StepListResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.steps.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(StepListResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_messages(self, client: LettaSDK) -> None:
        step = client.steps.list_messages(
            step_id="step_id",
        )
        assert_matches_type(StepListMessagesResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_messages_with_all_params(self, client: LettaSDK) -> None:
        step = client.steps.list_messages(
            step_id="step_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(StepListMessagesResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_messages(self, client: LettaSDK) -> None:
        response = client.steps.with_raw_response.list_messages(
            step_id="step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(StepListMessagesResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_messages(self, client: LettaSDK) -> None:
        with client.steps.with_streaming_response.list_messages(
            step_id="step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(StepListMessagesResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_messages(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.steps.with_raw_response.list_messages(
                step_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_metrics(self, client: LettaSDK) -> None:
        step = client.steps.retrieve_metrics(
            "step_id",
        )
        assert_matches_type(StepRetrieveMetricsResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_metrics(self, client: LettaSDK) -> None:
        response = client.steps.with_raw_response.retrieve_metrics(
            "step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(StepRetrieveMetricsResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_metrics(self, client: LettaSDK) -> None:
        with client.steps.with_streaming_response.retrieve_metrics(
            "step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(StepRetrieveMetricsResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_metrics(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.steps.with_raw_response.retrieve_metrics(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_trace(self, client: LettaSDK) -> None:
        step = client.steps.retrieve_trace(
            "step_id",
        )
        assert_matches_type(Optional[ProviderTrace], step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_trace(self, client: LettaSDK) -> None:
        response = client.steps.with_raw_response.retrieve_trace(
            "step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(Optional[ProviderTrace], step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_trace(self, client: LettaSDK) -> None:
        with client.steps.with_streaming_response.retrieve_trace(
            "step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(Optional[ProviderTrace], step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_trace(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.steps.with_raw_response.retrieve_trace(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_feedback(self, client: LettaSDK) -> None:
        step = client.steps.update_feedback(
            step_id="step_id",
        )
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_feedback_with_all_params(self, client: LettaSDK) -> None:
        step = client.steps.update_feedback(
            step_id="step_id",
            feedback="positive",
            tags=["string"],
        )
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_feedback(self, client: LettaSDK) -> None:
        response = client.steps.with_raw_response.update_feedback(
            step_id="step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_feedback(self, client: LettaSDK) -> None:
        with client.steps.with_streaming_response.update_feedback(
            step_id="step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(Step, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_feedback(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.steps.with_raw_response.update_feedback(
                step_id="",
            )


class TestAsyncSteps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.retrieve(
            "step_id",
        )
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.steps.with_raw_response.retrieve(
            "step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.steps.with_streaming_response.retrieve(
            "step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(Step, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.steps.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.list()
        assert_matches_type(StepListResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.list(
            after="after",
            agent_id="agent_id",
            before="before",
            end_date="end_date",
            feedback="positive",
            has_feedback=True,
            limit=0,
            model="model",
            order="asc",
            order_by="created_at",
            project_id="project_id",
            start_date="start_date",
            tags=["string"],
            trace_ids=["string"],
            x_project="X-Project",
        )
        assert_matches_type(StepListResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.steps.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(StepListResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.steps.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(StepListResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_messages(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.list_messages(
            step_id="step_id",
        )
        assert_matches_type(StepListMessagesResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_messages_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.list_messages(
            step_id="step_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
            order_by="created_at",
        )
        assert_matches_type(StepListMessagesResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.steps.with_raw_response.list_messages(
            step_id="step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(StepListMessagesResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.steps.with_streaming_response.list_messages(
            step_id="step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(StepListMessagesResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.steps.with_raw_response.list_messages(
                step_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_metrics(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.retrieve_metrics(
            "step_id",
        )
        assert_matches_type(StepRetrieveMetricsResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_metrics(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.steps.with_raw_response.retrieve_metrics(
            "step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(StepRetrieveMetricsResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_metrics(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.steps.with_streaming_response.retrieve_metrics(
            "step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(StepRetrieveMetricsResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_metrics(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.steps.with_raw_response.retrieve_metrics(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_trace(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.retrieve_trace(
            "step_id",
        )
        assert_matches_type(Optional[ProviderTrace], step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_trace(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.steps.with_raw_response.retrieve_trace(
            "step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(Optional[ProviderTrace], step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_trace(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.steps.with_streaming_response.retrieve_trace(
            "step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(Optional[ProviderTrace], step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_trace(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.steps.with_raw_response.retrieve_trace(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_feedback(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.update_feedback(
            step_id="step_id",
        )
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_feedback_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        step = await async_client.steps.update_feedback(
            step_id="step_id",
            feedback="positive",
            tags=["string"],
        )
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_feedback(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.steps.with_raw_response.update_feedback(
            step_id="step_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(Step, step, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_feedback(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.steps.with_streaming_response.update_feedback(
            step_id="step_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(Step, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_feedback(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.steps.with_raw_response.update_feedback(
                step_id="",
            )
