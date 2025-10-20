# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types._internal_templates import (
    DeploymentDeleteResponse,
    DeploymentListEntitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        deployment = client._internal_templates.deployment.delete(
            "deployment_id",
        )
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client._internal_templates.deployment.with_raw_response.delete(
            "deployment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client._internal_templates.deployment.with_streaming_response.delete(
            "deployment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client._internal_templates.deployment.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_entities(self, client: LettaSDK) -> None:
        deployment = client._internal_templates.deployment.list_entities(
            deployment_id="deployment_id",
        )
        assert_matches_type(DeploymentListEntitiesResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_entities_with_all_params(self, client: LettaSDK) -> None:
        deployment = client._internal_templates.deployment.list_entities(
            deployment_id="deployment_id",
            entity_types=["string"],
        )
        assert_matches_type(DeploymentListEntitiesResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_entities(self, client: LettaSDK) -> None:
        response = client._internal_templates.deployment.with_raw_response.list_entities(
            deployment_id="deployment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentListEntitiesResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_entities(self, client: LettaSDK) -> None:
        with client._internal_templates.deployment.with_streaming_response.list_entities(
            deployment_id="deployment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentListEntitiesResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_entities(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client._internal_templates.deployment.with_raw_response.list_entities(
                deployment_id="",
            )


class TestAsyncDeployment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        deployment = await async_client._internal_templates.deployment.delete(
            "deployment_id",
        )
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client._internal_templates.deployment.with_raw_response.delete(
            "deployment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client._internal_templates.deployment.with_streaming_response.delete(
            "deployment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client._internal_templates.deployment.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_entities(self, async_client: AsyncLettaSDK) -> None:
        deployment = await async_client._internal_templates.deployment.list_entities(
            deployment_id="deployment_id",
        )
        assert_matches_type(DeploymentListEntitiesResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_entities_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        deployment = await async_client._internal_templates.deployment.list_entities(
            deployment_id="deployment_id",
            entity_types=["string"],
        )
        assert_matches_type(DeploymentListEntitiesResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_entities(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client._internal_templates.deployment.with_raw_response.list_entities(
            deployment_id="deployment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentListEntitiesResponse, deployment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_entities(self, async_client: AsyncLettaSDK) -> None:
        async with async_client._internal_templates.deployment.with_streaming_response.list_entities(
            deployment_id="deployment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentListEntitiesResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_entities(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client._internal_templates.deployment.with_raw_response.list_entities(
                deployment_id="",
            )
