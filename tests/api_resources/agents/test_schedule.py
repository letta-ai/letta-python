# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types.agents import (
    ScheduleListResponse,
    ScheduleCreateResponse,
    ScheduleDeleteResponse,
    ScheduleRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        schedule = client.agents.schedule.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": [{"text": "text"}],
                    "role": "user",
                }
            ],
            schedule={"scheduled_at": 0},
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        schedule = client.agents.schedule.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "signature": "signature",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            schedule={
                "scheduled_at": 0,
                "type": "one-time",
            },
            callback_url="https://example.com",
            include_return_message_types=["system_message"],
            max_steps=0,
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.agents.schedule.with_raw_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": [{"text": "text"}],
                    "role": "user",
                }
            ],
            schedule={"scheduled_at": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.agents.schedule.with_streaming_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": [{"text": "text"}],
                    "role": "user",
                }
            ],
            schedule={"scheduled_at": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedule.with_raw_response.create(
                agent_id="",
                messages=[
                    {
                        "content": [{"text": "text"}],
                        "role": "user",
                    }
                ],
                schedule={"scheduled_at": 0},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        schedule = client.agents.schedule.retrieve(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        )
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.agents.schedule.with_raw_response.retrieve(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.agents.schedule.with_streaming_response.retrieve(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedule.with_raw_response.retrieve(
                scheduled_message_id="scheduled_message_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_message_id` but received ''"):
            client.agents.schedule.with_raw_response.retrieve(
                scheduled_message_id="",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        schedule = client.agents.schedule.list(
            agent_id="agent_id",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        schedule = client.agents.schedule.list(
            agent_id="agent_id",
            after="after",
            limit="limit",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.agents.schedule.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.agents.schedule.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedule.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        schedule = client.agents.schedule.delete(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.agents.schedule.with_raw_response.delete(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.agents.schedule.with_streaming_response.delete(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedule.with_raw_response.delete(
                scheduled_message_id="scheduled_message_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_message_id` but received ''"):
            client.agents.schedule.with_raw_response.delete(
                scheduled_message_id="",
                agent_id="agent_id",
            )


class TestAsyncSchedule:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        schedule = await async_client.agents.schedule.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": [{"text": "text"}],
                    "role": "user",
                }
            ],
            schedule={"scheduled_at": 0},
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        schedule = await async_client.agents.schedule.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "signature": "signature",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            schedule={
                "scheduled_at": 0,
                "type": "one-time",
            },
            callback_url="https://example.com",
            include_return_message_types=["system_message"],
            max_steps=0,
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.schedule.with_raw_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": [{"text": "text"}],
                    "role": "user",
                }
            ],
            schedule={"scheduled_at": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.schedule.with_streaming_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": [{"text": "text"}],
                    "role": "user",
                }
            ],
            schedule={"scheduled_at": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedule.with_raw_response.create(
                agent_id="",
                messages=[
                    {
                        "content": [{"text": "text"}],
                        "role": "user",
                    }
                ],
                schedule={"scheduled_at": 0},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        schedule = await async_client.agents.schedule.retrieve(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        )
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.schedule.with_raw_response.retrieve(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.schedule.with_streaming_response.retrieve(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedule.with_raw_response.retrieve(
                scheduled_message_id="scheduled_message_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_message_id` but received ''"):
            await async_client.agents.schedule.with_raw_response.retrieve(
                scheduled_message_id="",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        schedule = await async_client.agents.schedule.list(
            agent_id="agent_id",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        schedule = await async_client.agents.schedule.list(
            agent_id="agent_id",
            after="after",
            limit="limit",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.schedule.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.schedule.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedule.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        schedule = await async_client.agents.schedule.delete(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.agents.schedule.with_raw_response.delete(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.agents.schedule.with_streaming_response.delete(
            scheduled_message_id="scheduled_message_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedule.with_raw_response.delete(
                scheduled_message_id="scheduled_message_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_message_id` but received ''"):
            await async_client.agents.schedule.with_raw_response.delete(
                scheduled_message_id="",
                agent_id="agent_id",
            )
