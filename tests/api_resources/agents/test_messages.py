# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from letta_sdk import LettaSDK, AsyncLettaSDK
from tests.utils import assert_matches_type
from letta_sdk._utils import parse_datetime
from letta_sdk.types.agents import (
    Run,
    LettaResponse,
    MessageListResponse,
    MessageCancelResponse,
    MessageSearchResponse,
    MessageUpdateResponse,
    MessagePreviewRawPayloadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: LettaSDK) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content="content",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: LettaSDK) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content="content",
            message_type="system_message",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
                content="content",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: LettaSDK) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: LettaSDK) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            message_type="user_message",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
                content=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
                content=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: LettaSDK) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            reasoning="reasoning",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: LettaSDK) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            reasoning="reasoning",
            message_type="reasoning_message",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
            reasoning="reasoning",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
            reasoning="reasoning",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_3(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
                reasoning="reasoning",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
                reasoning="reasoning",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_4(self, client: LettaSDK) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[{"text": "text"}],
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: LettaSDK) -> None:
        message = client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            message_type="assistant_message",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_4(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[{"text": "text"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[{"text": "text"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_4(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
                content=[{"text": "text"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
                content=[{"text": "text"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LettaSDK) -> None:
        message = client.agents.messages.list(
            agent_id="agent_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LettaSDK) -> None:
        message = client.agents.messages.list(
            agent_id="agent_id",
            after="after",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            before="before",
            group_id="group_id",
            include_err=True,
            limit=0,
            use_assistant_message=True,
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: LettaSDK) -> None:
        message = client.agents.messages.cancel(
            agent_id="agent_id",
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: LettaSDK) -> None:
        message = client.agents.messages.cancel(
            agent_id="agent_id",
            run_ids=["string"],
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.cancel(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.cancel(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCancelResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.cancel(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_preview_raw_payload_overload_1(self, client: LettaSDK) -> None:
        message = client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_preview_raw_payload_with_all_params_overload_1(self, client: LettaSDK) -> None:
        message = client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            enable_thinking="enable_thinking",
            include_return_message_types=["system_message"],
            max_steps=0,
            use_assistant_message=True,
        )
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_preview_raw_payload_overload_1(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_preview_raw_payload_overload_1(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_preview_raw_payload_overload_1(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.preview_raw_payload(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_preview_raw_payload_overload_2(self, client: LettaSDK) -> None:
        message = client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_preview_raw_payload_with_all_params_overload_2(self, client: LettaSDK) -> None:
        message = client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
            include_pings=True,
            include_return_message_types=["system_message"],
            max_steps=0,
            stream_tokens=True,
            use_assistant_message=True,
        )
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_preview_raw_payload_overload_2(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_preview_raw_payload_overload_2(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_preview_raw_payload_overload_2(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.preview_raw_payload(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: LettaSDK) -> None:
        message = client.agents.messages.search()
        assert_matches_type(MessageSearchResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: LettaSDK) -> None:
        message = client.agents.messages.search(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            project_id="project_id",
            query="query",
            roles=["assistant"],
            search_mode="vector",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            template_id="template_id",
        )
        assert_matches_type(MessageSearchResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSearchResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSearchResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: LettaSDK) -> None:
        message = client.agents.messages.send(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: LettaSDK) -> None:
        message = client.agents.messages.send(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            enable_thinking="enable_thinking",
            include_return_message_types=["system_message"],
            max_steps=0,
            use_assistant_message=True,
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.send(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.send(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(LettaResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.send(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_async(self, client: LettaSDK) -> None:
        message = client.agents.messages.send_async(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_async_with_all_params(self, client: LettaSDK) -> None:
        message = client.agents.messages.send_async(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            callback_url="callback_url",
            enable_thinking="enable_thinking",
            include_return_message_types=["system_message"],
            max_steps=0,
            use_assistant_message=True,
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_async(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.send_async(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_async(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.send_async(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Run, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send_async(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.send_async(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_stream(self, client: LettaSDK) -> None:
        message = client.agents.messages.send_stream(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(object, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_stream_with_all_params(self, client: LettaSDK) -> None:
        message = client.agents.messages.send_stream(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
            include_pings=True,
            include_return_message_types=["system_message"],
            max_steps=0,
            stream_tokens=True,
            use_assistant_message=True,
        )
        assert_matches_type(object, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_stream(self, client: LettaSDK) -> None:
        response = client.agents.messages.with_raw_response.send_stream(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(object, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_stream(self, client: LettaSDK) -> None:
        with client.agents.messages.with_streaming_response.send_stream(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(object, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send_stream(self, client: LettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.messages.with_raw_response.send_stream(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content="content",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content="content",
            message_type="system_message",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
                content="content",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            message_type="user_message",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
                content=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
                content=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            reasoning="reasoning",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            reasoning="reasoning",
            message_type="reasoning_message",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
            reasoning="reasoning",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
            reasoning="reasoning",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
                reasoning="reasoning",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
                reasoning="reasoning",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[{"text": "text"}],
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            message_type="assistant_message",
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[{"text": "text"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.update(
            message_id="message_id",
            agent_id="agent_id",
            content=[{"text": "text"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="message_id",
                agent_id="",
                content=[{"text": "text"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.agents.messages.with_raw_response.update(
                message_id="",
                agent_id="agent_id",
                content=[{"text": "text"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.list(
            agent_id="agent_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.list(
            agent_id="agent_id",
            after="after",
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            before="before",
            group_id="group_id",
            include_err=True,
            limit=0,
            use_assistant_message=True,
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.list(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.cancel(
            agent_id="agent_id",
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.cancel(
            agent_id="agent_id",
            run_ids=["string"],
        )
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.cancel(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCancelResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.cancel(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCancelResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.cancel(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_preview_raw_payload_overload_1(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_preview_raw_payload_with_all_params_overload_1(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            enable_thinking="enable_thinking",
            include_return_message_types=["system_message"],
            max_steps=0,
            use_assistant_message=True,
        )
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_preview_raw_payload_overload_1(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_preview_raw_payload_overload_1(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_preview_raw_payload_overload_1(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.preview_raw_payload(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_preview_raw_payload_overload_2(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_preview_raw_payload_with_all_params_overload_2(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
            include_pings=True,
            include_return_message_types=["system_message"],
            max_steps=0,
            stream_tokens=True,
            use_assistant_message=True,
        )
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_preview_raw_payload_overload_2(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_preview_raw_payload_overload_2(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.preview_raw_payload(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessagePreviewRawPayloadResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_preview_raw_payload_overload_2(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.preview_raw_payload(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.search()
        assert_matches_type(MessageSearchResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.search(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            project_id="project_id",
            query="query",
            roles=["assistant"],
            search_mode="vector",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            template_id="template_id",
        )
        assert_matches_type(MessageSearchResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSearchResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSearchResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.send(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.send(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            enable_thinking="enable_thinking",
            include_return_message_types=["system_message"],
            max_steps=0,
            use_assistant_message=True,
        )
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.send(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(LettaResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.send(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(LettaResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.send(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_async(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.send_async(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_async_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.send_async(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            callback_url="callback_url",
            enable_thinking="enable_thinking",
            include_return_message_types=["system_message"],
            max_steps=0,
            use_assistant_message=True,
        )
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_async(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.send_async(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Run, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_async(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.send_async(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Run, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send_async(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.send_async(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_stream(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.send_stream(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )
        assert_matches_type(object, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_stream_with_all_params(self, async_client: AsyncLettaSDK) -> None:
        message = await async_client.agents.messages.send_stream(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                    "batch_item_id": "batch_item_id",
                    "group_id": "group_id",
                    "name": "name",
                    "otid": "otid",
                    "sender_id": "sender_id",
                    "type": "message",
                }
            ],
            assistant_message_tool_kwarg="assistant_message_tool_kwarg",
            assistant_message_tool_name="assistant_message_tool_name",
            background=True,
            enable_thinking="enable_thinking",
            include_pings=True,
            include_return_message_types=["system_message"],
            max_steps=0,
            stream_tokens=True,
            use_assistant_message=True,
        )
        assert_matches_type(object, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_stream(self, async_client: AsyncLettaSDK) -> None:
        response = await async_client.agents.messages.with_raw_response.send_stream(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(object, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_stream(self, async_client: AsyncLettaSDK) -> None:
        async with async_client.agents.messages.with_streaming_response.send_stream(
            agent_id="agent_id",
            messages=[
                {
                    "content": [
                        {
                            "text": "text",
                            "type": "text",
                        }
                    ],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(object, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send_stream(self, async_client: AsyncLettaSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.messages.with_raw_response.send_stream(
                agent_id="",
                messages=[
                    {
                        "content": [
                            {
                                "text": "text",
                                "type": "text",
                            }
                        ],
                        "role": "user",
                    }
                ],
            )
