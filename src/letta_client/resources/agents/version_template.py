# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import version_template_create_params
from ...types.agents.version_template_create_response import VersionTemplateCreateResponse

__all__ = ["VersionTemplateResource", "AsyncVersionTemplateResource"]


class VersionTemplateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return VersionTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return VersionTemplateResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        return_agent_id: bool | NotGiven = NOT_GIVEN,
        migrate_deployed_agents: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionTemplateCreateResponse:
        """
        Creates a versioned version of an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/version-template",
            body=maybe_transform(
                {"migrate_deployed_agents": migrate_deployed_agents},
                version_template_create_params.VersionTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"return_agent_id": return_agent_id}, version_template_create_params.VersionTemplateCreateParams
                ),
            ),
            cast_to=VersionTemplateCreateResponse,
        )


class AsyncVersionTemplateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/letta-python#with_streaming_response
        """
        return AsyncVersionTemplateResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        return_agent_id: bool | NotGiven = NOT_GIVEN,
        migrate_deployed_agents: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionTemplateCreateResponse:
        """
        Creates a versioned version of an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/version-template",
            body=await async_maybe_transform(
                {"migrate_deployed_agents": migrate_deployed_agents},
                version_template_create_params.VersionTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"return_agent_id": return_agent_id}, version_template_create_params.VersionTemplateCreateParams
                ),
            ),
            cast_to=VersionTemplateCreateResponse,
        )


class VersionTemplateResourceWithRawResponse:
    def __init__(self, version_template: VersionTemplateResource) -> None:
        self._version_template = version_template

        self.create = to_raw_response_wrapper(
            version_template.create,
        )


class AsyncVersionTemplateResourceWithRawResponse:
    def __init__(self, version_template: AsyncVersionTemplateResource) -> None:
        self._version_template = version_template

        self.create = async_to_raw_response_wrapper(
            version_template.create,
        )


class VersionTemplateResourceWithStreamingResponse:
    def __init__(self, version_template: VersionTemplateResource) -> None:
        self._version_template = version_template

        self.create = to_streamed_response_wrapper(
            version_template.create,
        )


class AsyncVersionTemplateResourceWithStreamingResponse:
    def __init__(self, version_template: AsyncVersionTemplateResource) -> None:
        self._version_template = version_template

        self.create = async_to_streamed_response_wrapper(
            version_template.create,
        )
