# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    jobs,
    runs,
    tags,
    steps,
    blocks,
    health,
    models,
    folders,
    archives,
    projects,
    providers,
    telemetry,
    templates,
    embeddings,
    identities,
    client_side_access_tokens,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import LettaSDKError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.tools import tools
from .resources.agents import agents
from .resources.groups import groups
from .resources.sources import sources
from .resources.messages import messages
from .resources.voice_beta import voice_beta
from .resources._internal_templates import _internal_templates

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LettaSDK",
    "AsyncLettaSDK",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://app.letta.com",
    "environment_1": "http://localhost:8283",
}


class LettaSDK(SyncAPIClient):
    archives: archives.ArchivesResource
    tools: tools.ToolsResource
    sources: sources.SourcesResource
    folders: folders.FoldersResource
    agents: agents.AgentsResource
    groups: groups.GroupsResource
    identities: identities.IdentitiesResource
    _internal_templates: _internal_templates._InternalTemplatesResource
    models: models.ModelsResource
    blocks: blocks.BlocksResource
    jobs: jobs.JobsResource
    health: health.HealthResource
    providers: providers.ProvidersResource
    runs: runs.RunsResource
    steps: steps.StepsResource
    tags: tags.TagsResource
    telemetry: telemetry.TelemetryResource
    messages: messages.MessagesResource
    voice_beta: voice_beta.VoiceBetaResource
    embeddings: embeddings.EmbeddingsResource
    templates: templates.TemplatesResource
    client_side_access_tokens: client_side_access_tokens.ClientSideAccessTokensResource
    projects: projects.ProjectsResource
    with_raw_response: LettaSDKWithRawResponse
    with_streaming_response: LettaSDKWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
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
        """Construct a new synchronous LettaSDK client instance.

        This automatically infers the `api_key` argument from the `LETTA_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LETTA_SDK_API_KEY")
        if api_key is None:
            raise LettaSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LETTA_SDK_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("LETTA_SDK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `LETTA_SDK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

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

        self.archives = archives.ArchivesResource(self)
        self.tools = tools.ToolsResource(self)
        self.sources = sources.SourcesResource(self)
        self.folders = folders.FoldersResource(self)
        self.agents = agents.AgentsResource(self)
        self.groups = groups.GroupsResource(self)
        self.identities = identities.IdentitiesResource(self)
        self._internal_templates = _internal_templates._InternalTemplatesResource(self)
        self.models = models.ModelsResource(self)
        self.blocks = blocks.BlocksResource(self)
        self.jobs = jobs.JobsResource(self)
        self.health = health.HealthResource(self)
        self.providers = providers.ProvidersResource(self)
        self.runs = runs.RunsResource(self)
        self.steps = steps.StepsResource(self)
        self.tags = tags.TagsResource(self)
        self.telemetry = telemetry.TelemetryResource(self)
        self.messages = messages.MessagesResource(self)
        self.voice_beta = voice_beta.VoiceBetaResource(self)
        self.embeddings = embeddings.EmbeddingsResource(self)
        self.templates = templates.TemplatesResource(self)
        self.client_side_access_tokens = client_side_access_tokens.ClientSideAccessTokensResource(self)
        self.projects = projects.ProjectsResource(self)
        self.with_raw_response = LettaSDKWithRawResponse(self)
        self.with_streaming_response = LettaSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

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
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
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


class AsyncLettaSDK(AsyncAPIClient):
    archives: archives.AsyncArchivesResource
    tools: tools.AsyncToolsResource
    sources: sources.AsyncSourcesResource
    folders: folders.AsyncFoldersResource
    agents: agents.AsyncAgentsResource
    groups: groups.AsyncGroupsResource
    identities: identities.AsyncIdentitiesResource
    _internal_templates: _internal_templates.AsyncInternalTemplatesResource
    models: models.AsyncModelsResource
    blocks: blocks.AsyncBlocksResource
    jobs: jobs.AsyncJobsResource
    health: health.AsyncHealthResource
    providers: providers.AsyncProvidersResource
    runs: runs.AsyncRunsResource
    steps: steps.AsyncStepsResource
    tags: tags.AsyncTagsResource
    telemetry: telemetry.AsyncTelemetryResource
    messages: messages.AsyncMessagesResource
    voice_beta: voice_beta.AsyncVoiceBetaResource
    embeddings: embeddings.AsyncEmbeddingsResource
    templates: templates.AsyncTemplatesResource
    client_side_access_tokens: client_side_access_tokens.AsyncClientSideAccessTokensResource
    projects: projects.AsyncProjectsResource
    with_raw_response: AsyncLettaSDKWithRawResponse
    with_streaming_response: AsyncLettaSDKWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
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
        """Construct a new async AsyncLettaSDK client instance.

        This automatically infers the `api_key` argument from the `LETTA_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LETTA_SDK_API_KEY")
        if api_key is None:
            raise LettaSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LETTA_SDK_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("LETTA_SDK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `LETTA_SDK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

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

        self.archives = archives.AsyncArchivesResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.sources = sources.AsyncSourcesResource(self)
        self.folders = folders.AsyncFoldersResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.groups = groups.AsyncGroupsResource(self)
        self.identities = identities.AsyncIdentitiesResource(self)
        self._internal_templates = _internal_templates.AsyncInternalTemplatesResource(self)
        self.models = models.AsyncModelsResource(self)
        self.blocks = blocks.AsyncBlocksResource(self)
        self.jobs = jobs.AsyncJobsResource(self)
        self.health = health.AsyncHealthResource(self)
        self.providers = providers.AsyncProvidersResource(self)
        self.runs = runs.AsyncRunsResource(self)
        self.steps = steps.AsyncStepsResource(self)
        self.tags = tags.AsyncTagsResource(self)
        self.telemetry = telemetry.AsyncTelemetryResource(self)
        self.messages = messages.AsyncMessagesResource(self)
        self.voice_beta = voice_beta.AsyncVoiceBetaResource(self)
        self.embeddings = embeddings.AsyncEmbeddingsResource(self)
        self.templates = templates.AsyncTemplatesResource(self)
        self.client_side_access_tokens = client_side_access_tokens.AsyncClientSideAccessTokensResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.with_raw_response = AsyncLettaSDKWithRawResponse(self)
        self.with_streaming_response = AsyncLettaSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

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
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
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


class LettaSDKWithRawResponse:
    def __init__(self, client: LettaSDK) -> None:
        self.archives = archives.ArchivesResourceWithRawResponse(client.archives)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)
        self.sources = sources.SourcesResourceWithRawResponse(client.sources)
        self.folders = folders.FoldersResourceWithRawResponse(client.folders)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.groups = groups.GroupsResourceWithRawResponse(client.groups)
        self.identities = identities.IdentitiesResourceWithRawResponse(client.identities)
        self._internal_templates = _internal_templates._InternalTemplatesResourceWithRawResponse(
            client._internal_templates
        )
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.blocks = blocks.BlocksResourceWithRawResponse(client.blocks)
        self.jobs = jobs.JobsResourceWithRawResponse(client.jobs)
        self.health = health.HealthResourceWithRawResponse(client.health)
        self.providers = providers.ProvidersResourceWithRawResponse(client.providers)
        self.runs = runs.RunsResourceWithRawResponse(client.runs)
        self.steps = steps.StepsResourceWithRawResponse(client.steps)
        self.tags = tags.TagsResourceWithRawResponse(client.tags)
        self.telemetry = telemetry.TelemetryResourceWithRawResponse(client.telemetry)
        self.messages = messages.MessagesResourceWithRawResponse(client.messages)
        self.voice_beta = voice_beta.VoiceBetaResourceWithRawResponse(client.voice_beta)
        self.embeddings = embeddings.EmbeddingsResourceWithRawResponse(client.embeddings)
        self.templates = templates.TemplatesResourceWithRawResponse(client.templates)
        self.client_side_access_tokens = client_side_access_tokens.ClientSideAccessTokensResourceWithRawResponse(
            client.client_side_access_tokens
        )
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)


class AsyncLettaSDKWithRawResponse:
    def __init__(self, client: AsyncLettaSDK) -> None:
        self.archives = archives.AsyncArchivesResourceWithRawResponse(client.archives)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)
        self.sources = sources.AsyncSourcesResourceWithRawResponse(client.sources)
        self.folders = folders.AsyncFoldersResourceWithRawResponse(client.folders)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.groups = groups.AsyncGroupsResourceWithRawResponse(client.groups)
        self.identities = identities.AsyncIdentitiesResourceWithRawResponse(client.identities)
        self._internal_templates = _internal_templates.AsyncInternalTemplatesResourceWithRawResponse(
            client._internal_templates
        )
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.blocks = blocks.AsyncBlocksResourceWithRawResponse(client.blocks)
        self.jobs = jobs.AsyncJobsResourceWithRawResponse(client.jobs)
        self.health = health.AsyncHealthResourceWithRawResponse(client.health)
        self.providers = providers.AsyncProvidersResourceWithRawResponse(client.providers)
        self.runs = runs.AsyncRunsResourceWithRawResponse(client.runs)
        self.steps = steps.AsyncStepsResourceWithRawResponse(client.steps)
        self.tags = tags.AsyncTagsResourceWithRawResponse(client.tags)
        self.telemetry = telemetry.AsyncTelemetryResourceWithRawResponse(client.telemetry)
        self.messages = messages.AsyncMessagesResourceWithRawResponse(client.messages)
        self.voice_beta = voice_beta.AsyncVoiceBetaResourceWithRawResponse(client.voice_beta)
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithRawResponse(client.embeddings)
        self.templates = templates.AsyncTemplatesResourceWithRawResponse(client.templates)
        self.client_side_access_tokens = client_side_access_tokens.AsyncClientSideAccessTokensResourceWithRawResponse(
            client.client_side_access_tokens
        )
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)


class LettaSDKWithStreamedResponse:
    def __init__(self, client: LettaSDK) -> None:
        self.archives = archives.ArchivesResourceWithStreamingResponse(client.archives)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)
        self.sources = sources.SourcesResourceWithStreamingResponse(client.sources)
        self.folders = folders.FoldersResourceWithStreamingResponse(client.folders)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.groups = groups.GroupsResourceWithStreamingResponse(client.groups)
        self.identities = identities.IdentitiesResourceWithStreamingResponse(client.identities)
        self._internal_templates = _internal_templates._InternalTemplatesResourceWithStreamingResponse(
            client._internal_templates
        )
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.blocks = blocks.BlocksResourceWithStreamingResponse(client.blocks)
        self.jobs = jobs.JobsResourceWithStreamingResponse(client.jobs)
        self.health = health.HealthResourceWithStreamingResponse(client.health)
        self.providers = providers.ProvidersResourceWithStreamingResponse(client.providers)
        self.runs = runs.RunsResourceWithStreamingResponse(client.runs)
        self.steps = steps.StepsResourceWithStreamingResponse(client.steps)
        self.tags = tags.TagsResourceWithStreamingResponse(client.tags)
        self.telemetry = telemetry.TelemetryResourceWithStreamingResponse(client.telemetry)
        self.messages = messages.MessagesResourceWithStreamingResponse(client.messages)
        self.voice_beta = voice_beta.VoiceBetaResourceWithStreamingResponse(client.voice_beta)
        self.embeddings = embeddings.EmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.templates = templates.TemplatesResourceWithStreamingResponse(client.templates)
        self.client_side_access_tokens = client_side_access_tokens.ClientSideAccessTokensResourceWithStreamingResponse(
            client.client_side_access_tokens
        )
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)


class AsyncLettaSDKWithStreamedResponse:
    def __init__(self, client: AsyncLettaSDK) -> None:
        self.archives = archives.AsyncArchivesResourceWithStreamingResponse(client.archives)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)
        self.sources = sources.AsyncSourcesResourceWithStreamingResponse(client.sources)
        self.folders = folders.AsyncFoldersResourceWithStreamingResponse(client.folders)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.groups = groups.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.identities = identities.AsyncIdentitiesResourceWithStreamingResponse(client.identities)
        self._internal_templates = _internal_templates.AsyncInternalTemplatesResourceWithStreamingResponse(
            client._internal_templates
        )
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.blocks = blocks.AsyncBlocksResourceWithStreamingResponse(client.blocks)
        self.jobs = jobs.AsyncJobsResourceWithStreamingResponse(client.jobs)
        self.health = health.AsyncHealthResourceWithStreamingResponse(client.health)
        self.providers = providers.AsyncProvidersResourceWithStreamingResponse(client.providers)
        self.runs = runs.AsyncRunsResourceWithStreamingResponse(client.runs)
        self.steps = steps.AsyncStepsResourceWithStreamingResponse(client.steps)
        self.tags = tags.AsyncTagsResourceWithStreamingResponse(client.tags)
        self.telemetry = telemetry.AsyncTelemetryResourceWithStreamingResponse(client.telemetry)
        self.messages = messages.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.voice_beta = voice_beta.AsyncVoiceBetaResourceWithStreamingResponse(client.voice_beta)
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.templates = templates.AsyncTemplatesResourceWithStreamingResponse(client.templates)
        self.client_side_access_tokens = (
            client_side_access_tokens.AsyncClientSideAccessTokensResourceWithStreamingResponse(
                client.client_side_access_tokens
            )
        )
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)


Client = LettaSDK

AsyncClient = AsyncLettaSDK
