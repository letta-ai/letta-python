# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
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
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.health_response import HealthResponse

if TYPE_CHECKING:
    from .resources import (
        runs,
        tags,
        steps,
        tools,
        agents,
        blocks,
        models,
        folders,
        archives,
        messages,
        passages,
        templates,
        mcp_servers,
        access_tokens,
        conversations,
    )
    from .resources.tags import TagsResource, AsyncTagsResource
    from .resources.tools import ToolsResource, AsyncToolsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.passages import PassagesResource, AsyncPassagesResource
    from .resources.runs.runs import RunsResource, AsyncRunsResource
    from .resources.steps.steps import StepsResource, AsyncStepsResource
    from .resources.access_tokens import AccessTokensResource, AsyncAccessTokensResource
    from .resources.agents.agents import AgentsResource, AsyncAgentsResource
    from .resources.blocks.blocks import BlocksResource, AsyncBlocksResource
    from .resources.models.models import ModelsResource, AsyncModelsResource
    from .resources.folders.folders import FoldersResource, AsyncFoldersResource
    from .resources.archives.archives import ArchivesResource, AsyncArchivesResource
    from .resources.templates.templates import TemplatesResource, AsyncTemplatesResource
    from .resources.mcp_servers.mcp_servers import McpServersResource, AsyncMcpServersResource
    from .resources.conversations.conversations import ConversationsResource, AsyncConversationsResource

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
    # client options
    api_key: str | None
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

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def tools(self) -> ToolsResource:
        from .resources.tools import ToolsResource

        return ToolsResource(self)

    @cached_property
    def blocks(self) -> BlocksResource:
        from .resources.blocks import BlocksResource

        return BlocksResource(self)

    @cached_property
    def archives(self) -> ArchivesResource:
        from .resources.archives import ArchivesResource

        return ArchivesResource(self)

    @cached_property
    def folders(self) -> FoldersResource:
        from .resources.folders import FoldersResource

        return FoldersResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def mcp_servers(self) -> McpServersResource:
        from .resources.mcp_servers import McpServersResource

        return McpServersResource(self)

    @cached_property
    def runs(self) -> RunsResource:
        from .resources.runs import RunsResource

        return RunsResource(self)

    @cached_property
    def steps(self) -> StepsResource:
        from .resources.steps import StepsResource

        return StepsResource(self)

    @cached_property
    def templates(self) -> TemplatesResource:
        from .resources.templates import TemplatesResource

        return TemplatesResource(self)

    @cached_property
    def tags(self) -> TagsResource:
        from .resources.tags import TagsResource

        return TagsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def passages(self) -> PassagesResource:
        from .resources.passages import PassagesResource

        return PassagesResource(self)

    @cached_property
    def conversations(self) -> ConversationsResource:
        from .resources.conversations import ConversationsResource

        return ConversationsResource(self)

    @cached_property
    def access_tokens(self) -> AccessTokensResource:
        from .resources.access_tokens import AccessTokensResource

        return AccessTokensResource(self)

    @cached_property
    def with_raw_response(self) -> LettaWithRawResponse:
        return LettaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LettaWithStreamedResponse:
        return LettaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
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
        """Async health check endpoint."""
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
    # client options
    api_key: str | None
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

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        from .resources.tools import AsyncToolsResource

        return AsyncToolsResource(self)

    @cached_property
    def blocks(self) -> AsyncBlocksResource:
        from .resources.blocks import AsyncBlocksResource

        return AsyncBlocksResource(self)

    @cached_property
    def archives(self) -> AsyncArchivesResource:
        from .resources.archives import AsyncArchivesResource

        return AsyncArchivesResource(self)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        from .resources.folders import AsyncFoldersResource

        return AsyncFoldersResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResource:
        from .resources.mcp_servers import AsyncMcpServersResource

        return AsyncMcpServersResource(self)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        from .resources.runs import AsyncRunsResource

        return AsyncRunsResource(self)

    @cached_property
    def steps(self) -> AsyncStepsResource:
        from .resources.steps import AsyncStepsResource

        return AsyncStepsResource(self)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        from .resources.templates import AsyncTemplatesResource

        return AsyncTemplatesResource(self)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        from .resources.tags import AsyncTagsResource

        return AsyncTagsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def passages(self) -> AsyncPassagesResource:
        from .resources.passages import AsyncPassagesResource

        return AsyncPassagesResource(self)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        from .resources.conversations import AsyncConversationsResource

        return AsyncConversationsResource(self)

    @cached_property
    def access_tokens(self) -> AsyncAccessTokensResource:
        from .resources.access_tokens import AsyncAccessTokensResource

        return AsyncAccessTokensResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLettaWithRawResponse:
        return AsyncLettaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLettaWithStreamedResponse:
        return AsyncLettaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
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
        """Async health check endpoint."""
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
    _client: Letta

    def __init__(self, client: Letta) -> None:
        self._client = client

        self.health = to_raw_response_wrapper(
            client.health,
        )

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithRawResponse:
        from .resources.tools import ToolsResourceWithRawResponse

        return ToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def blocks(self) -> blocks.BlocksResourceWithRawResponse:
        from .resources.blocks import BlocksResourceWithRawResponse

        return BlocksResourceWithRawResponse(self._client.blocks)

    @cached_property
    def archives(self) -> archives.ArchivesResourceWithRawResponse:
        from .resources.archives import ArchivesResourceWithRawResponse

        return ArchivesResourceWithRawResponse(self._client.archives)

    @cached_property
    def folders(self) -> folders.FoldersResourceWithRawResponse:
        from .resources.folders import FoldersResourceWithRawResponse

        return FoldersResourceWithRawResponse(self._client.folders)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def mcp_servers(self) -> mcp_servers.McpServersResourceWithRawResponse:
        from .resources.mcp_servers import McpServersResourceWithRawResponse

        return McpServersResourceWithRawResponse(self._client.mcp_servers)

    @cached_property
    def runs(self) -> runs.RunsResourceWithRawResponse:
        from .resources.runs import RunsResourceWithRawResponse

        return RunsResourceWithRawResponse(self._client.runs)

    @cached_property
    def steps(self) -> steps.StepsResourceWithRawResponse:
        from .resources.steps import StepsResourceWithRawResponse

        return StepsResourceWithRawResponse(self._client.steps)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithRawResponse:
        from .resources.templates import TemplatesResourceWithRawResponse

        return TemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def tags(self) -> tags.TagsResourceWithRawResponse:
        from .resources.tags import TagsResourceWithRawResponse

        return TagsResourceWithRawResponse(self._client.tags)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def passages(self) -> passages.PassagesResourceWithRawResponse:
        from .resources.passages import PassagesResourceWithRawResponse

        return PassagesResourceWithRawResponse(self._client.passages)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithRawResponse:
        from .resources.conversations import ConversationsResourceWithRawResponse

        return ConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def access_tokens(self) -> access_tokens.AccessTokensResourceWithRawResponse:
        from .resources.access_tokens import AccessTokensResourceWithRawResponse

        return AccessTokensResourceWithRawResponse(self._client.access_tokens)


class AsyncLettaWithRawResponse:
    _client: AsyncLetta

    def __init__(self, client: AsyncLetta) -> None:
        self._client = client

        self.health = async_to_raw_response_wrapper(
            client.health,
        )

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithRawResponse:
        from .resources.tools import AsyncToolsResourceWithRawResponse

        return AsyncToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def blocks(self) -> blocks.AsyncBlocksResourceWithRawResponse:
        from .resources.blocks import AsyncBlocksResourceWithRawResponse

        return AsyncBlocksResourceWithRawResponse(self._client.blocks)

    @cached_property
    def archives(self) -> archives.AsyncArchivesResourceWithRawResponse:
        from .resources.archives import AsyncArchivesResourceWithRawResponse

        return AsyncArchivesResourceWithRawResponse(self._client.archives)

    @cached_property
    def folders(self) -> folders.AsyncFoldersResourceWithRawResponse:
        from .resources.folders import AsyncFoldersResourceWithRawResponse

        return AsyncFoldersResourceWithRawResponse(self._client.folders)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def mcp_servers(self) -> mcp_servers.AsyncMcpServersResourceWithRawResponse:
        from .resources.mcp_servers import AsyncMcpServersResourceWithRawResponse

        return AsyncMcpServersResourceWithRawResponse(self._client.mcp_servers)

    @cached_property
    def runs(self) -> runs.AsyncRunsResourceWithRawResponse:
        from .resources.runs import AsyncRunsResourceWithRawResponse

        return AsyncRunsResourceWithRawResponse(self._client.runs)

    @cached_property
    def steps(self) -> steps.AsyncStepsResourceWithRawResponse:
        from .resources.steps import AsyncStepsResourceWithRawResponse

        return AsyncStepsResourceWithRawResponse(self._client.steps)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithRawResponse:
        from .resources.templates import AsyncTemplatesResourceWithRawResponse

        return AsyncTemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def tags(self) -> tags.AsyncTagsResourceWithRawResponse:
        from .resources.tags import AsyncTagsResourceWithRawResponse

        return AsyncTagsResourceWithRawResponse(self._client.tags)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def passages(self) -> passages.AsyncPassagesResourceWithRawResponse:
        from .resources.passages import AsyncPassagesResourceWithRawResponse

        return AsyncPassagesResourceWithRawResponse(self._client.passages)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithRawResponse:
        from .resources.conversations import AsyncConversationsResourceWithRawResponse

        return AsyncConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def access_tokens(self) -> access_tokens.AsyncAccessTokensResourceWithRawResponse:
        from .resources.access_tokens import AsyncAccessTokensResourceWithRawResponse

        return AsyncAccessTokensResourceWithRawResponse(self._client.access_tokens)


class LettaWithStreamedResponse:
    _client: Letta

    def __init__(self, client: Letta) -> None:
        self._client = client

        self.health = to_streamed_response_wrapper(
            client.health,
        )

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithStreamingResponse:
        from .resources.tools import ToolsResourceWithStreamingResponse

        return ToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def blocks(self) -> blocks.BlocksResourceWithStreamingResponse:
        from .resources.blocks import BlocksResourceWithStreamingResponse

        return BlocksResourceWithStreamingResponse(self._client.blocks)

    @cached_property
    def archives(self) -> archives.ArchivesResourceWithStreamingResponse:
        from .resources.archives import ArchivesResourceWithStreamingResponse

        return ArchivesResourceWithStreamingResponse(self._client.archives)

    @cached_property
    def folders(self) -> folders.FoldersResourceWithStreamingResponse:
        from .resources.folders import FoldersResourceWithStreamingResponse

        return FoldersResourceWithStreamingResponse(self._client.folders)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def mcp_servers(self) -> mcp_servers.McpServersResourceWithStreamingResponse:
        from .resources.mcp_servers import McpServersResourceWithStreamingResponse

        return McpServersResourceWithStreamingResponse(self._client.mcp_servers)

    @cached_property
    def runs(self) -> runs.RunsResourceWithStreamingResponse:
        from .resources.runs import RunsResourceWithStreamingResponse

        return RunsResourceWithStreamingResponse(self._client.runs)

    @cached_property
    def steps(self) -> steps.StepsResourceWithStreamingResponse:
        from .resources.steps import StepsResourceWithStreamingResponse

        return StepsResourceWithStreamingResponse(self._client.steps)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithStreamingResponse:
        from .resources.templates import TemplatesResourceWithStreamingResponse

        return TemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def tags(self) -> tags.TagsResourceWithStreamingResponse:
        from .resources.tags import TagsResourceWithStreamingResponse

        return TagsResourceWithStreamingResponse(self._client.tags)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def passages(self) -> passages.PassagesResourceWithStreamingResponse:
        from .resources.passages import PassagesResourceWithStreamingResponse

        return PassagesResourceWithStreamingResponse(self._client.passages)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithStreamingResponse:
        from .resources.conversations import ConversationsResourceWithStreamingResponse

        return ConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def access_tokens(self) -> access_tokens.AccessTokensResourceWithStreamingResponse:
        from .resources.access_tokens import AccessTokensResourceWithStreamingResponse

        return AccessTokensResourceWithStreamingResponse(self._client.access_tokens)


class AsyncLettaWithStreamedResponse:
    _client: AsyncLetta

    def __init__(self, client: AsyncLetta) -> None:
        self._client = client

        self.health = async_to_streamed_response_wrapper(
            client.health,
        )

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithStreamingResponse:
        from .resources.tools import AsyncToolsResourceWithStreamingResponse

        return AsyncToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def blocks(self) -> blocks.AsyncBlocksResourceWithStreamingResponse:
        from .resources.blocks import AsyncBlocksResourceWithStreamingResponse

        return AsyncBlocksResourceWithStreamingResponse(self._client.blocks)

    @cached_property
    def archives(self) -> archives.AsyncArchivesResourceWithStreamingResponse:
        from .resources.archives import AsyncArchivesResourceWithStreamingResponse

        return AsyncArchivesResourceWithStreamingResponse(self._client.archives)

    @cached_property
    def folders(self) -> folders.AsyncFoldersResourceWithStreamingResponse:
        from .resources.folders import AsyncFoldersResourceWithStreamingResponse

        return AsyncFoldersResourceWithStreamingResponse(self._client.folders)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def mcp_servers(self) -> mcp_servers.AsyncMcpServersResourceWithStreamingResponse:
        from .resources.mcp_servers import AsyncMcpServersResourceWithStreamingResponse

        return AsyncMcpServersResourceWithStreamingResponse(self._client.mcp_servers)

    @cached_property
    def runs(self) -> runs.AsyncRunsResourceWithStreamingResponse:
        from .resources.runs import AsyncRunsResourceWithStreamingResponse

        return AsyncRunsResourceWithStreamingResponse(self._client.runs)

    @cached_property
    def steps(self) -> steps.AsyncStepsResourceWithStreamingResponse:
        from .resources.steps import AsyncStepsResourceWithStreamingResponse

        return AsyncStepsResourceWithStreamingResponse(self._client.steps)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithStreamingResponse:
        from .resources.templates import AsyncTemplatesResourceWithStreamingResponse

        return AsyncTemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def tags(self) -> tags.AsyncTagsResourceWithStreamingResponse:
        from .resources.tags import AsyncTagsResourceWithStreamingResponse

        return AsyncTagsResourceWithStreamingResponse(self._client.tags)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def passages(self) -> passages.AsyncPassagesResourceWithStreamingResponse:
        from .resources.passages import AsyncPassagesResourceWithStreamingResponse

        return AsyncPassagesResourceWithStreamingResponse(self._client.passages)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithStreamingResponse:
        from .resources.conversations import AsyncConversationsResourceWithStreamingResponse

        return AsyncConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def access_tokens(self) -> access_tokens.AsyncAccessTokensResourceWithStreamingResponse:
        from .resources.access_tokens import AsyncAccessTokensResourceWithStreamingResponse

        return AsyncAccessTokensResourceWithStreamingResponse(self._client.access_tokens)


Client = Letta

AsyncClient = AsyncLetta
