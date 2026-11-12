# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from letta_client import Letta, AsyncLetta
from letta_client.types import Goal, GoalListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGoals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Letta) -> None:
        goal = client.goals.create(
            description="x",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Letta) -> None:
        goal = client.goals.create(
            description="x",
            agent_id="x",
            conversation_id="x",
            status="active",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Letta) -> None:
        response = client.goals.with_raw_response.create(
            description="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Letta) -> None:
        with client.goals.with_streaming_response.create(
            description="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(Goal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Letta) -> None:
        goal = client.goals.retrieve(
            "x",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Letta) -> None:
        response = client.goals.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Letta) -> None:
        with client.goals.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(Goal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_id` but received ''"):
            client.goals.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Letta) -> None:
        goal = client.goals.update(
            goal_id="x",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Letta) -> None:
        goal = client.goals.update(
            goal_id="x",
            description="x",
            status="active",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Letta) -> None:
        response = client.goals.with_raw_response.update(
            goal_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Letta) -> None:
        with client.goals.with_streaming_response.update(
            goal_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(Goal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_id` but received ''"):
            client.goals.with_raw_response.update(
                goal_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Letta) -> None:
        goal = client.goals.list()
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Letta) -> None:
        goal = client.goals.list(
            after="x",
            agent_id="x",
            conversation_id="x",
            limit=1,
            status="active",
        )
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Letta) -> None:
        response = client.goals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Letta) -> None:
        with client.goals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(GoalListResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Letta) -> None:
        goal = client.goals.delete(
            "x",
        )
        assert goal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Letta) -> None:
        response = client.goals.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert goal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Letta) -> None:
        with client.goals.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert goal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Letta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_id` but received ''"):
            client.goals.with_raw_response.delete(
                "",
            )


class TestAsyncGoals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLetta) -> None:
        goal = await async_client.goals.create(
            description="x",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLetta) -> None:
        goal = await async_client.goals.create(
            description="x",
            agent_id="x",
            conversation_id="x",
            status="active",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLetta) -> None:
        response = await async_client.goals.with_raw_response.create(
            description="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLetta) -> None:
        async with async_client.goals.with_streaming_response.create(
            description="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(Goal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLetta) -> None:
        goal = await async_client.goals.retrieve(
            "x",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLetta) -> None:
        response = await async_client.goals.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLetta) -> None:
        async with async_client.goals.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(Goal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_id` but received ''"):
            await async_client.goals.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLetta) -> None:
        goal = await async_client.goals.update(
            goal_id="x",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLetta) -> None:
        goal = await async_client.goals.update(
            goal_id="x",
            description="x",
            status="active",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLetta) -> None:
        response = await async_client.goals.with_raw_response.update(
            goal_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLetta) -> None:
        async with async_client.goals.with_streaming_response.update(
            goal_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(Goal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_id` but received ''"):
            await async_client.goals.with_raw_response.update(
                goal_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLetta) -> None:
        goal = await async_client.goals.list()
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLetta) -> None:
        goal = await async_client.goals.list(
            after="x",
            agent_id="x",
            conversation_id="x",
            limit=1,
            status="active",
        )
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLetta) -> None:
        response = await async_client.goals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLetta) -> None:
        async with async_client.goals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(GoalListResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLetta) -> None:
        goal = await async_client.goals.delete(
            "x",
        )
        assert goal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLetta) -> None:
        response = await async_client.goals.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert goal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLetta) -> None:
        async with async_client.goals.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert goal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLetta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_id` but received ''"):
            await async_client.goals.with_raw_response.delete(
                "",
            )
