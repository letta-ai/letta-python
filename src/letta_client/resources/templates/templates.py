# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, overload

import httpx

from .agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)
from ...types import template_create_params, template_update_params, template_rollback_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.template_create_response import TemplateCreateResponse
from ...types.template_delete_response import TemplateDeleteResponse
from ...types.template_update_response import TemplateUpdateResponse
from ...types.template_rollback_response import TemplateRollbackResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        agent_id: str,
        type: Literal["agent"],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        """
        Creates a new template from an existing agent or agent file

        Args:
          agent_id: The ID of the agent to use as a template, can be from any project

          name: Optional custom name for the template. If not provided, a random name will be
              generated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        agent_file: Dict[str, Optional[object]],
        type: Literal["agent_file"],
        name: str | Omit = omit,
        update_existing_tools: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        """
        Creates a new template from an existing agent or agent file

        Args:
          agent_file: The agent file to use as a template, this should be a JSON file exported from
              the platform

          name: Optional custom name for the template. If not provided, a random name will be
              generated.

          update_existing_tools: If true, update existing custom tools source_code and json_schema (source_type
              cannot be changed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "type"], ["agent_file", "type"])
    def create(
        self,
        *,
        agent_id: str | Omit = omit,
        type: Literal["agent"] | Literal["agent_file"],
        name: str | Omit = omit,
        agent_file: Dict[str, Optional[object]] | Omit = omit,
        update_existing_tools: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        return self._post(
            "/v1/templates",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "type": type,
                    "name": name,
                    "agent_file": agent_file,
                    "update_existing_tools": update_existing_tools,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateResponse,
        )

    def update(
        self,
        template_name: str,
        *,
        agent_file_json: Dict[str, Optional[object]],
        save_existing_changes: bool | Omit = omit,
        update_existing_tools: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateUpdateResponse:
        """
        Updates the current working version of a template from an agent file

        Args:
          agent_file_json: The agent file to update the current template version from

          save_existing_changes: If true, Letta will automatically save any changes as a version before updating
              the template

          update_existing_tools: If true, update existing custom tools source_code and json_schema (source_type
              cannot be changed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._patch(
            f"/v1/templates/{template_name}",
            body=maybe_transform(
                {
                    "agent_file_json": agent_file_json,
                    "save_existing_changes": save_existing_changes,
                    "update_existing_tools": update_existing_tools,
                },
                template_update_params.TemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateUpdateResponse,
        )

    def delete(
        self,
        template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateDeleteResponse:
        """
        Deletes all versions of a template with the specified name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._delete(
            f"/v1/templates/{template_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateDeleteResponse,
        )

    def rollback(
        self,
        template_name: str,
        *,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRollbackResponse:
        """
        Rollback the current working version of a template to a previous saved version.
        If the current version has unsaved changes, they will be automatically saved as
        a new version before rollback.

        Args:
          version: The target version to rollback to (e.g., "1", "2", "latest"). Cannot be
              "current" or "dev".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._post(
            f"/v1/templates/{template_name}/rollback",
            body=maybe_transform({"version": version}, template_rollback_params.TemplateRollbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRollbackResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/letta-ai/letta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/letta-ai/letta-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        agent_id: str,
        type: Literal["agent"],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        """
        Creates a new template from an existing agent or agent file

        Args:
          agent_id: The ID of the agent to use as a template, can be from any project

          name: Optional custom name for the template. If not provided, a random name will be
              generated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        agent_file: Dict[str, Optional[object]],
        type: Literal["agent_file"],
        name: str | Omit = omit,
        update_existing_tools: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        """
        Creates a new template from an existing agent or agent file

        Args:
          agent_file: The agent file to use as a template, this should be a JSON file exported from
              the platform

          name: Optional custom name for the template. If not provided, a random name will be
              generated.

          update_existing_tools: If true, update existing custom tools source_code and json_schema (source_type
              cannot be changed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "type"], ["agent_file", "type"])
    async def create(
        self,
        *,
        agent_id: str | Omit = omit,
        type: Literal["agent"] | Literal["agent_file"],
        name: str | Omit = omit,
        agent_file: Dict[str, Optional[object]] | Omit = omit,
        update_existing_tools: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        return await self._post(
            "/v1/templates",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "type": type,
                    "name": name,
                    "agent_file": agent_file,
                    "update_existing_tools": update_existing_tools,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateResponse,
        )

    async def update(
        self,
        template_name: str,
        *,
        agent_file_json: Dict[str, Optional[object]],
        save_existing_changes: bool | Omit = omit,
        update_existing_tools: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateUpdateResponse:
        """
        Updates the current working version of a template from an agent file

        Args:
          agent_file_json: The agent file to update the current template version from

          save_existing_changes: If true, Letta will automatically save any changes as a version before updating
              the template

          update_existing_tools: If true, update existing custom tools source_code and json_schema (source_type
              cannot be changed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._patch(
            f"/v1/templates/{template_name}",
            body=await async_maybe_transform(
                {
                    "agent_file_json": agent_file_json,
                    "save_existing_changes": save_existing_changes,
                    "update_existing_tools": update_existing_tools,
                },
                template_update_params.TemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateUpdateResponse,
        )

    async def delete(
        self,
        template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateDeleteResponse:
        """
        Deletes all versions of a template with the specified name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._delete(
            f"/v1/templates/{template_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateDeleteResponse,
        )

    async def rollback(
        self,
        template_name: str,
        *,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRollbackResponse:
        """
        Rollback the current working version of a template to a previous saved version.
        If the current version has unsaved changes, they will be automatically saved as
        a new version before rollback.

        Args:
          version: The target version to rollback to (e.g., "1", "2", "latest"). Cannot be
              "current" or "dev".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._post(
            f"/v1/templates/{template_name}/rollback",
            body=await async_maybe_transform({"version": version}, template_rollback_params.TemplateRollbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRollbackResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_raw_response_wrapper(
            templates.create,
        )
        self.update = to_raw_response_wrapper(
            templates.update,
        )
        self.delete = to_raw_response_wrapper(
            templates.delete,
        )
        self.rollback = to_raw_response_wrapper(
            templates.rollback,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._templates.agents)


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_raw_response_wrapper(
            templates.create,
        )
        self.update = async_to_raw_response_wrapper(
            templates.update,
        )
        self.delete = async_to_raw_response_wrapper(
            templates.delete,
        )
        self.rollback = async_to_raw_response_wrapper(
            templates.rollback,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._templates.agents)


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_streamed_response_wrapper(
            templates.create,
        )
        self.update = to_streamed_response_wrapper(
            templates.update,
        )
        self.delete = to_streamed_response_wrapper(
            templates.delete,
        )
        self.rollback = to_streamed_response_wrapper(
            templates.rollback,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._templates.agents)


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_streamed_response_wrapper(
            templates.create,
        )
        self.update = async_to_streamed_response_wrapper(
            templates.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            templates.delete,
        )
        self.rollback = async_to_streamed_response_wrapper(
            templates.rollback,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._templates.agents)
