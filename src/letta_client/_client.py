# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import tags, tools, archives
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import LettaError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.runs import runs
from .resources.steps import steps
from .resources.agents import agents
from .resources.blocks import blocks
from .resources.groups import groups
from .resources.models import models
from .resources.batches import batches
from .resources.folders import folders
from .resources.templates import templates
from .resources.identities import identities
from .resources.mcp_servers import mcp_servers
from .types.health_response import HealthResponse

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Letta",
    "AsyncLetta",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "cloud": "https://api.letta.com",
    "local": "http://localhost:8283",
}


class Letta(SyncAPIClient):
    archives: archives.ArchivesResource
    tools: tools.ToolsResource
    folders: folders.FoldersResource
    agents: agents.AgentsResource
    groups: groups.GroupsResource
    identities: identities.IdentitiesResource
    models: models.ModelsResource
    blocks: blocks.BlocksResource
    runs: runs.RunsResource
    steps: steps.StepsResource
    tags: tags.TagsResource
    batches: batches.BatchesResource
    templates: templates.TemplatesResource
    mcp_servers: mcp_servers.McpServersResource
    with_raw_response: LettaWithRawResponse
    with_streaming_response: LettaWithStreamedResponse

    # client options
    api_key: str
    project_id: str | None
    project: str | None

    _environment: Literal["cloud", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        project_id: str | None = None,
        project: str | None = None,
        environment: Literal["cloud", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Letta client instance.

        This automatically infers the `api_key` argument from the `LETTA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LETTA_API_KEY")
        if api_key is None:
            raise LettaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LETTA_API_KEY environment variable"
            )
        self.api_key = api_key

        self.project_id = project_id

        self.project = project

        self._environment = environment

        base_url_env = os.environ.get("LETTA_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `LETTA_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "cloud"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

        self.archives = archives.ArchivesResource(self)
        self.tools = tools.ToolsResource(self)
        self.folders = folders.FoldersResource(self)
        self.agents = agents.AgentsResource(self)
        self.groups = groups.GroupsResource(self)
        self.identities = identities.IdentitiesResource(self)
        self.models = models.ModelsResource(self)
        self.blocks = blocks.BlocksResource(self)
        self.runs = runs.RunsResource(self)
        self.steps = steps.StepsResource(self)
        self.tags = tags.TagsResource(self)
        self.batches = batches.BatchesResource(self)
        self.templates = templates.TemplatesResource(self)
        self.mcp_servers = mcp_servers.McpServersResource(self)
        self.with_raw_response = LettaWithRawResponse(self)
        self.with_streaming_response = LettaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Project-Id": self.project_id if self.project_id is not None else Omit(),
            "X-Project": self.project if self.project is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        project_id: str | None = None,
        project: str | None = None,
        environment: Literal["cloud", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            project_id=project_id or self.project_id,
            project=project or self.project,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthResponse:
        """Check Health"""
        return self.get(
            "/v1/health/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLetta(AsyncAPIClient):
    archives: archives.AsyncArchivesResource
    tools: tools.AsyncToolsResource
    folders: folders.AsyncFoldersResource
    agents: agents.AsyncAgentsResource
    groups: groups.AsyncGroupsResource
    identities: identities.AsyncIdentitiesResource
    models: models.AsyncModelsResource
    blocks: blocks.AsyncBlocksResource
    runs: runs.AsyncRunsResource
    steps: steps.AsyncStepsResource
    tags: tags.AsyncTagsResource
    batches: batches.AsyncBatchesResource
    templates: templates.AsyncTemplatesResource
    mcp_servers: mcp_servers.AsyncMcpServersResource
    with_raw_response: AsyncLettaWithRawResponse
    with_streaming_response: AsyncLettaWithStreamedResponse

    # client options
    api_key: str
    project_id: str | None
    project: str | None

    _environment: Literal["cloud", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        project_id: str | None = None,
        project: str | None = None,
        environment: Literal["cloud", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLetta client instance.

        This automatically infers the `api_key` argument from the `LETTA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LETTA_API_KEY")
        if api_key is None:
            raise LettaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LETTA_API_KEY environment variable"
            )
        self.api_key = api_key

        self.project_id = project_id

        self.project = project

        self._environment = environment

        base_url_env = os.environ.get("LETTA_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `LETTA_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "cloud"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

        self.archives = archives.AsyncArchivesResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.folders = folders.AsyncFoldersResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.groups = groups.AsyncGroupsResource(self)
        self.identities = identities.AsyncIdentitiesResource(self)
        self.models = models.AsyncModelsResource(self)
        self.blocks = blocks.AsyncBlocksResource(self)
        self.runs = runs.AsyncRunsResource(self)
        self.steps = steps.AsyncStepsResource(self)
        self.tags = tags.AsyncTagsResource(self)
        self.batches = batches.AsyncBatchesResource(self)
        self.templates = templates.AsyncTemplatesResource(self)
        self.mcp_servers = mcp_servers.AsyncMcpServersResource(self)
        self.with_raw_response = AsyncLettaWithRawResponse(self)
        self.with_streaming_response = AsyncLettaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Project-Id": self.project_id if self.project_id is not None else Omit(),
            "X-Project": self.project if self.project is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        project_id: str | None = None,
        project: str | None = None,
        environment: Literal["cloud", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            project_id=project_id or self.project_id,
            project=project or self.project,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthResponse:
        """Check Health"""
        return await self.get(
            "/v1/health/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LettaWithRawResponse:
    def __init__(self, client: Letta) -> None:
        self.archives = archives.ArchivesResourceWithRawResponse(client.archives)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)
        self.folders = folders.FoldersResourceWithRawResponse(client.folders)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.groups = groups.GroupsResourceWithRawResponse(client.groups)
        self.identities = identities.IdentitiesResourceWithRawResponse(client.identities)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.blocks = blocks.BlocksResourceWithRawResponse(client.blocks)
        self.runs = runs.RunsResourceWithRawResponse(client.runs)
        self.steps = steps.StepsResourceWithRawResponse(client.steps)
        self.tags = tags.TagsResourceWithRawResponse(client.tags)
        self.batches = batches.BatchesResourceWithRawResponse(client.batches)
        self.templates = templates.TemplatesResourceWithRawResponse(client.templates)
        self.mcp_servers = mcp_servers.McpServersResourceWithRawResponse(client.mcp_servers)

        self.health = to_raw_response_wrapper(
            client.health,
        )


class AsyncLettaWithRawResponse:
    def __init__(self, client: AsyncLetta) -> None:
        self.archives = archives.AsyncArchivesResourceWithRawResponse(client.archives)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)
        self.folders = folders.AsyncFoldersResourceWithRawResponse(client.folders)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.groups = groups.AsyncGroupsResourceWithRawResponse(client.groups)
        self.identities = identities.AsyncIdentitiesResourceWithRawResponse(client.identities)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.blocks = blocks.AsyncBlocksResourceWithRawResponse(client.blocks)
        self.runs = runs.AsyncRunsResourceWithRawResponse(client.runs)
        self.steps = steps.AsyncStepsResourceWithRawResponse(client.steps)
        self.tags = tags.AsyncTagsResourceWithRawResponse(client.tags)
        self.batches = batches.AsyncBatchesResourceWithRawResponse(client.batches)
        self.templates = templates.AsyncTemplatesResourceWithRawResponse(client.templates)
        self.mcp_servers = mcp_servers.AsyncMcpServersResourceWithRawResponse(client.mcp_servers)

        self.health = async_to_raw_response_wrapper(
            client.health,
        )


class LettaWithStreamedResponse:
    def __init__(self, client: Letta) -> None:
        self.archives = archives.ArchivesResourceWithStreamingResponse(client.archives)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)
        self.folders = folders.FoldersResourceWithStreamingResponse(client.folders)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.groups = groups.GroupsResourceWithStreamingResponse(client.groups)
        self.identities = identities.IdentitiesResourceWithStreamingResponse(client.identities)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.blocks = blocks.BlocksResourceWithStreamingResponse(client.blocks)
        self.runs = runs.RunsResourceWithStreamingResponse(client.runs)
        self.steps = steps.StepsResourceWithStreamingResponse(client.steps)
        self.tags = tags.TagsResourceWithStreamingResponse(client.tags)
        self.batches = batches.BatchesResourceWithStreamingResponse(client.batches)
        self.templates = templates.TemplatesResourceWithStreamingResponse(client.templates)
        self.mcp_servers = mcp_servers.McpServersResourceWithStreamingResponse(client.mcp_servers)

        self.health = to_streamed_response_wrapper(
            client.health,
        )


class AsyncLettaWithStreamedResponse:
    def __init__(self, client: AsyncLetta) -> None:
        self.archives = archives.AsyncArchivesResourceWithStreamingResponse(client.archives)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)
        self.folders = folders.AsyncFoldersResourceWithStreamingResponse(client.folders)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.groups = groups.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.identities = identities.AsyncIdentitiesResourceWithStreamingResponse(client.identities)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.blocks = blocks.AsyncBlocksResourceWithStreamingResponse(client.blocks)
        self.runs = runs.AsyncRunsResourceWithStreamingResponse(client.runs)
        self.steps = steps.AsyncStepsResourceWithStreamingResponse(client.steps)
        self.tags = tags.AsyncTagsResourceWithStreamingResponse(client.tags)
        self.batches = batches.AsyncBatchesResourceWithStreamingResponse(client.batches)
        self.templates = templates.AsyncTemplatesResourceWithStreamingResponse(client.templates)
        self.mcp_servers = mcp_servers.AsyncMcpServersResourceWithStreamingResponse(client.mcp_servers)

        self.health = async_to_streamed_response_wrapper(
            client.health,
        )


Client = Letta

AsyncClient = AsyncLetta
