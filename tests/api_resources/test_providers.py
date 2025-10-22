# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk.types import (
    Provider,
    ProviderListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LettaSDK) -> None:
        provider = client.providers.create(
            api_key="api_key",
            name="name",
            provider_type="anthropic",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LettaSDK) -> None:
        provider = client.providers.create(
            api_key="api_key",
            name="name",
            provider_type="anthropic",
            access_key="access_key",
            api_version="api_version",
            base_url="base_url",
            region="region",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LettaSDK) -> None:
        response = client.providers.with_raw_response.create(
            api_key="api_key",
            name="name",
            provider_type="anthropic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LettaSDK) -> None:
        with client.providers.with_streaming_response.create(
            api_key="api_key",
            name="name",
            provider_type="anthropic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LettaSDK) -> None:
        provider = client.providers.retrieve(
            "provider_id",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LettaSDK) -> None:
        response = client.providers.with_raw_response.retrieve(
            "provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LettaSDK) -> None:
        with client.providers.with_streaming_response.retrieve(
            "provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.providers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LettaSDK) -> None:
        provider = client.providers.update(
            provider_id="provider_id",
            api_key="api_key",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LettaSDK) -> None:
        provider = client.providers.update(
            provider_id="provider_id",
            api_key="api_key",
            access_key="access_key",
            api_version="api_version",
            base_url="base_url",
            region="region",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LettaSDK) -> None:
        response = client.providers.with_raw_response.update(
            provider_id="provider_id",
            api_key="api_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LettaSDK) -> None:
        with client.providers.with_streaming_response.update(
            provider_id="provider_id",
            api_key="api_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.providers.with_raw_response.update(
                provider_id="",
                api_key="api_key",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        provider = client.providers.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        provider = client.providers.list(
            after="after",
            before="before",
            limit=0,
            name="name",
            order="asc",
            order_by="created_at",
            provider_type="anthropic",
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LettaSDK) -> None:
        provider = client.providers.delete(
            "provider_id",
        )
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LettaSDK) -> None:
        response = client.providers.with_raw_response.delete(
            "provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LettaSDK) -> None:
        with client.providers.with_streaming_response.delete(
            "provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(object, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.providers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check(self, client: LettaSDK) -> None:
        provider = client.providers.check(
            api_key="api_key",
            provider_type="anthropic",
        )
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_with_all_params(self, client: LettaSDK) -> None:
        provider = client.providers.check(
            api_key="api_key",
            provider_type="anthropic",
            access_key="access_key",
            api_version="api_version",
            base_url="base_url",
            region="region",
        )
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: LettaSDK) -> None:
        response = client.providers.with_raw_response.check(
            api_key="api_key",
            provider_type="anthropic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: LettaSDK) -> None:
        with client.providers.with_streaming_response.check(
            api_key="api_key",
            provider_type="anthropic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(object, provider, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.create(
            api_key="api_key",
            name="name",
            provider_type="anthropic",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.create(
            api_key="api_key",
            name="name",
            provider_type="anthropic",
            access_key="access_key",
            api_version="api_version",
            base_url="base_url",
            region="region",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.providers.with_raw_response.create(
            api_key="api_key",
            name="name",
            provider_type="anthropic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.providers.with_streaming_response.create(
            api_key="api_key",
            name="name",
            provider_type="anthropic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.retrieve(
            "provider_id",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.providers.with_raw_response.retrieve(
            "provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.providers.with_streaming_response.retrieve(
            "provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.providers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.update(
            provider_id="provider_id",
            api_key="api_key",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.update(
            provider_id="provider_id",
            api_key="api_key",
            access_key="access_key",
            api_version="api_version",
            base_url="base_url",
            region="region",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.providers.with_raw_response.update(
            provider_id="provider_id",
            api_key="api_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.providers.with_streaming_response.update(
            provider_id="provider_id",
            api_key="api_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.providers.with_raw_response.update(
                provider_id="",
                api_key="api_key",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.list(
            after="after",
            before="before",
            limit=0,
            name="name",
            order="asc",
            order_by="created_at",
            provider_type="anthropic",
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.delete(
            "provider_id",
        )
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.providers.with_raw_response.delete(
            "provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.providers.with_streaming_response.delete(
            "provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(object, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.providers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.check(
            api_key="api_key",
            provider_type="anthropic",
        )
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        provider = await async_client.providers.check(
            api_key="api_key",
            provider_type="anthropic",
            access_key="access_key",
            api_version="api_version",
            base_url="base_url",
            region="region",
        )
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.providers.with_raw_response.check(
            api_key="api_key",
            provider_type="anthropic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(object, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.providers.with_streaming_response.check(
            api_key="api_key",
            provider_type="anthropic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(object, provider, path=["response"])

        assert cast(Any, response.is_closed) is True
