# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["VoiceBetaResource", "AsyncVoiceBetaResource"]


class VoiceBetaResource(SyncAPIResource):
    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> VoiceBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return VoiceBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return VoiceBetaResourceWithStreamingResponse(self)


class AsyncVoiceBetaResource(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVoiceBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncVoiceBetaResourceWithStreamingResponse(self)


class VoiceBetaResourceWithRawResponse:
    def __init__(self, voice_beta: VoiceBetaResource) -> None:
        self._voice_beta = voice_beta

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._voice_beta.chat)


class AsyncVoiceBetaResourceWithRawResponse:
    def __init__(self, voice_beta: AsyncVoiceBetaResource) -> None:
        self._voice_beta = voice_beta

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._voice_beta.chat)


class VoiceBetaResourceWithStreamingResponse:
    def __init__(self, voice_beta: VoiceBetaResource) -> None:
        self._voice_beta = voice_beta

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._voice_beta.chat)


class AsyncVoiceBetaResourceWithStreamingResponse:
    def __init__(self, voice_beta: AsyncVoiceBetaResource) -> None:
        self._voice_beta = voice_beta

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._voice_beta.chat)
