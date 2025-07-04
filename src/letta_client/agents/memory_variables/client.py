# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...core.request_options import RequestOptions
from .types.memory_variables_list_response import MemoryVariablesListResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.unchecked_base_model import construct_type
from ...errors.not_found_error import NotFoundError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper


class MemoryVariablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MemoryVariablesListResponse:
        """
        <Note>This endpoint is only available on Letta Cloud.</Note>

        Returns the memory variables associated with an agent.

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MemoryVariablesListResponse
            200

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.agents.memory_variables.list(
            agent_id="agent_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/core-memory/variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MemoryVariablesListResponse,
                    construct_type(
                        type_=MemoryVariablesListResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMemoryVariablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MemoryVariablesListResponse:
        """
        <Note>This endpoint is only available on Letta Cloud.</Note>

        Returns the memory variables associated with an agent.

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MemoryVariablesListResponse
            200

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.memory_variables.list(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/core-memory/variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MemoryVariablesListResponse,
                    construct_type(
                        type_=MemoryVariablesListResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
