# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import (
    template_fork_params,
    template_list_params,
    template_create_params,
    template_rename_params,
    template_save_version_params,
    template_create_agents_params,
    template_list_versions_params,
    template_update_description_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.template_fork_response import TemplateForkResponse
from ..types.template_list_response import TemplateListResponse
from ..types.template_create_response import TemplateCreateResponse
from ..types.template_delete_response import TemplateDeleteResponse
from ..types.template_rename_response import TemplateRenameResponse
from ..types.template_get_snapshot_response import TemplateGetSnapshotResponse
from ..types.template_save_version_response import TemplateSaveVersionResponse
from ..types.template_create_agents_response import TemplateCreateAgentsResponse
from ..types.template_list_versions_response import TemplateListVersionsResponse
from ..types.template_update_description_response import TemplateUpdateDescriptionResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
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
        project: str,
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
        project: str,
        *,
        agent_file: Dict[str, Optional[object]],
        type: Literal["agent_file"],
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
          agent_file: The agent file to use as a template, this should be a JSON file exported from
              the platform

          name: Optional custom name for the template. If not provided, a random name will be
              generated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "type"], ["agent_file", "type"])
    def create(
        self,
        project: str,
        *,
        agent_id: str | Omit = omit,
        type: Literal["agent"] | Literal["agent_file"],
        name: str | Omit = omit,
        agent_file: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        return self._post(
            f"/v1/templates/{project}",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "type": type,
                    "name": name,
                    "agent_file": agent_file,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateResponse,
        )

    def list(
        self,
        *,
        exact: str | Omit = omit,
        limit: str | Omit = omit,
        name: str | Omit = omit,
        offset: Union[str, float] | Omit = omit,
        project_id: str | Omit = omit,
        project_slug: str | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["updated_at", "created_at"] | Omit = omit,
        template_id: str | Omit = omit,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListResponse:
        """
        List all templates

        Args:
          exact: Whether to search for an exact name match

          version: Specify the version you want to return, otherwise will return the latest version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exact": exact,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "project_id": project_id,
                        "project_slug": project_slug,
                        "search": search,
                        "sort_by": sort_by,
                        "template_id": template_id,
                        "version": version,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=TemplateListResponse,
        )

    def delete(
        self,
        template_name: str,
        *,
        project: str,
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
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._delete(
            f"/v1/templates/{project}/{template_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateDeleteResponse,
        )

    def create_agents(
        self,
        template_version: str,
        *,
        project: str,
        agent_name: str | Omit = omit,
        identity_ids: SequenceNotStr[str] | Omit = omit,
        initial_message_sequence: Iterable[template_create_agents_params.InitialMessageSequence] | Omit = omit,
        memory_variables: Dict[str, str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        tool_variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateAgentsResponse:
        """
        Creates an Agent or multiple Agents from a template

        Args:
          agent_name: The name of the agent, optional otherwise a random one will be assigned

          identity_ids: The identity ids to assign to the agent

          initial_message_sequence: Set an initial sequence of messages, if not provided, the agent will start with
              the default message sequence, if an empty array is provided, the agent will
              start with no messages

          memory_variables: The memory variables to assign to the agent

          tags: The tags to assign to the agent

          tool_variables: The tool variables to assign to the agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_version:
            raise ValueError(f"Expected a non-empty value for `template_version` but received {template_version!r}")
        return self._post(
            f"/v1/templates/{project}/{template_version}/agents",
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "identity_ids": identity_ids,
                    "initial_message_sequence": initial_message_sequence,
                    "memory_variables": memory_variables,
                    "tags": tags,
                    "tool_variables": tool_variables,
                },
                template_create_agents_params.TemplateCreateAgentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateAgentsResponse,
        )

    def fork(
        self,
        template_version: str,
        *,
        project: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateForkResponse:
        """
        Forks a template version into a new template

        Args:
          name: Optional custom name for the forked template. If not provided, a random name
              will be generated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_version:
            raise ValueError(f"Expected a non-empty value for `template_version` but received {template_version!r}")
        return self._post(
            f"/v1/templates/{project}/{template_version}/fork",
            body=maybe_transform({"name": name}, template_fork_params.TemplateForkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateForkResponse,
        )

    def get_snapshot(
        self,
        template_version: str,
        *,
        project: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateGetSnapshotResponse:
        """
        Get a snapshot of the template version, this will return the template state at a
        specific version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_version:
            raise ValueError(f"Expected a non-empty value for `template_version` but received {template_version!r}")
        return self._get(
            f"/v1/templates/{project}/{template_version}/snapshot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateGetSnapshotResponse,
        )

    def list_versions(
        self,
        name: str,
        *,
        project_slug: str,
        limit: str | Omit = omit,
        offset: Union[str, float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListVersionsResponse:
        """
        List all versions of a specific template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_slug:
            raise ValueError(f"Expected a non-empty value for `project_slug` but received {project_slug!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/v1/templates/{project_slug}/{name}/versions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    template_list_versions_params.TemplateListVersionsParams,
                ),
            ),
            cast_to=TemplateListVersionsResponse,
        )

    def rename(
        self,
        template_name: str,
        *,
        project: str,
        new_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRenameResponse:
        """Renames all versions of a template with the specified name.

        Versions are
        automatically stripped from the current template name if accidentally included.

        Args:
          new_name: The new name for the template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._patch(
            f"/v1/templates/{project}/{template_name}/name",
            body=maybe_transform({"new_name": new_name}, template_rename_params.TemplateRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRenameResponse,
        )

    def save_version(
        self,
        template_name: str,
        *,
        project: str,
        message: str | Omit = omit,
        migrate_agents: bool | Omit = omit,
        preserve_core_memories_on_migration: bool | Omit = omit,
        preserve_environment_variables_on_migration: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateSaveVersionResponse:
        """
        Saves the current version of the template as a new version

        Args:
          message: A message to describe the changes made in this template version

          migrate_agents: If true, existing agents attached to this template will be migrated to the new
              template version

          preserve_core_memories_on_migration: If true, the core memories will be preserved in the template version when
              migrating agents

          preserve_environment_variables_on_migration: If true, the environment variables will be preserved in the template version
              when migrating agents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._post(
            f"/v1/templates/{project}/{template_name}",
            body=maybe_transform(
                {
                    "message": message,
                    "migrate_agents": migrate_agents,
                    "preserve_core_memories_on_migration": preserve_core_memories_on_migration,
                    "preserve_environment_variables_on_migration": preserve_environment_variables_on_migration,
                },
                template_save_version_params.TemplateSaveVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateSaveVersionResponse,
        )

    def update_description(
        self,
        template_name: str,
        *,
        project: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateUpdateDescriptionResponse:
        """
        Updates the description for all versions of a template with the specified name.
        Versions are automatically stripped from the current template name if
        accidentally included.

        Args:
          description: The new description for the template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._patch(
            f"/v1/templates/{project}/{template_name}/description",
            body=maybe_transform(
                {"description": description}, template_update_description_params.TemplateUpdateDescriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateUpdateDescriptionResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
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
        project: str,
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
        project: str,
        *,
        agent_file: Dict[str, Optional[object]],
        type: Literal["agent_file"],
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
          agent_file: The agent file to use as a template, this should be a JSON file exported from
              the platform

          name: Optional custom name for the template. If not provided, a random name will be
              generated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "type"], ["agent_file", "type"])
    async def create(
        self,
        project: str,
        *,
        agent_id: str | Omit = omit,
        type: Literal["agent"] | Literal["agent_file"],
        name: str | Omit = omit,
        agent_file: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        return await self._post(
            f"/v1/templates/{project}",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "type": type,
                    "name": name,
                    "agent_file": agent_file,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateResponse,
        )

    async def list(
        self,
        *,
        exact: str | Omit = omit,
        limit: str | Omit = omit,
        name: str | Omit = omit,
        offset: Union[str, float] | Omit = omit,
        project_id: str | Omit = omit,
        project_slug: str | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["updated_at", "created_at"] | Omit = omit,
        template_id: str | Omit = omit,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListResponse:
        """
        List all templates

        Args:
          exact: Whether to search for an exact name match

          version: Specify the version you want to return, otherwise will return the latest version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exact": exact,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "project_id": project_id,
                        "project_slug": project_slug,
                        "search": search,
                        "sort_by": sort_by,
                        "template_id": template_id,
                        "version": version,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=TemplateListResponse,
        )

    async def delete(
        self,
        template_name: str,
        *,
        project: str,
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
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._delete(
            f"/v1/templates/{project}/{template_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateDeleteResponse,
        )

    async def create_agents(
        self,
        template_version: str,
        *,
        project: str,
        agent_name: str | Omit = omit,
        identity_ids: SequenceNotStr[str] | Omit = omit,
        initial_message_sequence: Iterable[template_create_agents_params.InitialMessageSequence] | Omit = omit,
        memory_variables: Dict[str, str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        tool_variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateAgentsResponse:
        """
        Creates an Agent or multiple Agents from a template

        Args:
          agent_name: The name of the agent, optional otherwise a random one will be assigned

          identity_ids: The identity ids to assign to the agent

          initial_message_sequence: Set an initial sequence of messages, if not provided, the agent will start with
              the default message sequence, if an empty array is provided, the agent will
              start with no messages

          memory_variables: The memory variables to assign to the agent

          tags: The tags to assign to the agent

          tool_variables: The tool variables to assign to the agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_version:
            raise ValueError(f"Expected a non-empty value for `template_version` but received {template_version!r}")
        return await self._post(
            f"/v1/templates/{project}/{template_version}/agents",
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "identity_ids": identity_ids,
                    "initial_message_sequence": initial_message_sequence,
                    "memory_variables": memory_variables,
                    "tags": tags,
                    "tool_variables": tool_variables,
                },
                template_create_agents_params.TemplateCreateAgentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateAgentsResponse,
        )

    async def fork(
        self,
        template_version: str,
        *,
        project: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateForkResponse:
        """
        Forks a template version into a new template

        Args:
          name: Optional custom name for the forked template. If not provided, a random name
              will be generated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_version:
            raise ValueError(f"Expected a non-empty value for `template_version` but received {template_version!r}")
        return await self._post(
            f"/v1/templates/{project}/{template_version}/fork",
            body=await async_maybe_transform({"name": name}, template_fork_params.TemplateForkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateForkResponse,
        )

    async def get_snapshot(
        self,
        template_version: str,
        *,
        project: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateGetSnapshotResponse:
        """
        Get a snapshot of the template version, this will return the template state at a
        specific version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_version:
            raise ValueError(f"Expected a non-empty value for `template_version` but received {template_version!r}")
        return await self._get(
            f"/v1/templates/{project}/{template_version}/snapshot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateGetSnapshotResponse,
        )

    async def list_versions(
        self,
        name: str,
        *,
        project_slug: str,
        limit: str | Omit = omit,
        offset: Union[str, float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListVersionsResponse:
        """
        List all versions of a specific template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_slug:
            raise ValueError(f"Expected a non-empty value for `project_slug` but received {project_slug!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/v1/templates/{project_slug}/{name}/versions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    template_list_versions_params.TemplateListVersionsParams,
                ),
            ),
            cast_to=TemplateListVersionsResponse,
        )

    async def rename(
        self,
        template_name: str,
        *,
        project: str,
        new_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRenameResponse:
        """Renames all versions of a template with the specified name.

        Versions are
        automatically stripped from the current template name if accidentally included.

        Args:
          new_name: The new name for the template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._patch(
            f"/v1/templates/{project}/{template_name}/name",
            body=await async_maybe_transform({"new_name": new_name}, template_rename_params.TemplateRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRenameResponse,
        )

    async def save_version(
        self,
        template_name: str,
        *,
        project: str,
        message: str | Omit = omit,
        migrate_agents: bool | Omit = omit,
        preserve_core_memories_on_migration: bool | Omit = omit,
        preserve_environment_variables_on_migration: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateSaveVersionResponse:
        """
        Saves the current version of the template as a new version

        Args:
          message: A message to describe the changes made in this template version

          migrate_agents: If true, existing agents attached to this template will be migrated to the new
              template version

          preserve_core_memories_on_migration: If true, the core memories will be preserved in the template version when
              migrating agents

          preserve_environment_variables_on_migration: If true, the environment variables will be preserved in the template version
              when migrating agents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._post(
            f"/v1/templates/{project}/{template_name}",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "migrate_agents": migrate_agents,
                    "preserve_core_memories_on_migration": preserve_core_memories_on_migration,
                    "preserve_environment_variables_on_migration": preserve_environment_variables_on_migration,
                },
                template_save_version_params.TemplateSaveVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateSaveVersionResponse,
        )

    async def update_description(
        self,
        template_name: str,
        *,
        project: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateUpdateDescriptionResponse:
        """
        Updates the description for all versions of a template with the specified name.
        Versions are automatically stripped from the current template name if
        accidentally included.

        Args:
          description: The new description for the template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._patch(
            f"/v1/templates/{project}/{template_name}/description",
            body=await async_maybe_transform(
                {"description": description}, template_update_description_params.TemplateUpdateDescriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateUpdateDescriptionResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_raw_response_wrapper(
            templates.create,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.delete = to_raw_response_wrapper(
            templates.delete,
        )
        self.create_agents = to_raw_response_wrapper(
            templates.create_agents,
        )
        self.fork = to_raw_response_wrapper(
            templates.fork,
        )
        self.get_snapshot = to_raw_response_wrapper(
            templates.get_snapshot,
        )
        self.list_versions = to_raw_response_wrapper(
            templates.list_versions,
        )
        self.rename = to_raw_response_wrapper(
            templates.rename,
        )
        self.save_version = to_raw_response_wrapper(
            templates.save_version,
        )
        self.update_description = to_raw_response_wrapper(
            templates.update_description,
        )


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_raw_response_wrapper(
            templates.create,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            templates.delete,
        )
        self.create_agents = async_to_raw_response_wrapper(
            templates.create_agents,
        )
        self.fork = async_to_raw_response_wrapper(
            templates.fork,
        )
        self.get_snapshot = async_to_raw_response_wrapper(
            templates.get_snapshot,
        )
        self.list_versions = async_to_raw_response_wrapper(
            templates.list_versions,
        )
        self.rename = async_to_raw_response_wrapper(
            templates.rename,
        )
        self.save_version = async_to_raw_response_wrapper(
            templates.save_version,
        )
        self.update_description = async_to_raw_response_wrapper(
            templates.update_description,
        )


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_streamed_response_wrapper(
            templates.create,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            templates.delete,
        )
        self.create_agents = to_streamed_response_wrapper(
            templates.create_agents,
        )
        self.fork = to_streamed_response_wrapper(
            templates.fork,
        )
        self.get_snapshot = to_streamed_response_wrapper(
            templates.get_snapshot,
        )
        self.list_versions = to_streamed_response_wrapper(
            templates.list_versions,
        )
        self.rename = to_streamed_response_wrapper(
            templates.rename,
        )
        self.save_version = to_streamed_response_wrapper(
            templates.save_version,
        )
        self.update_description = to_streamed_response_wrapper(
            templates.update_description,
        )


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_streamed_response_wrapper(
            templates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            templates.delete,
        )
        self.create_agents = async_to_streamed_response_wrapper(
            templates.create_agents,
        )
        self.fork = async_to_streamed_response_wrapper(
            templates.fork,
        )
        self.get_snapshot = async_to_streamed_response_wrapper(
            templates.get_snapshot,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            templates.list_versions,
        )
        self.rename = async_to_streamed_response_wrapper(
            templates.rename,
        )
        self.save_version = async_to_streamed_response_wrapper(
            templates.save_version,
        )
        self.update_description = async_to_streamed_response_wrapper(
            templates.update_description,
        )
