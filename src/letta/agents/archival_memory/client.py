# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.archival_memory_summary import ArchivalMemorySummary
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.passage import Passage
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ArchivalMemoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_summary(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArchivalMemorySummary:
        """
        Retrieve the summary of the archival memory of a specific agent.

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArchivalMemorySummary
            Successful Response

        Examples
        --------
        from letta import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.agents.archival_memory.get_summary(
            agent_id="agent_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/memory/archival",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ArchivalMemorySummary,
                    parse_obj_as(
                        type_=ArchivalMemorySummary,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        agent_id: str,
        *,
        after: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Passage]:
        """
        Retrieve the memories in an agent's archival memory store (paginated query).

        Parameters
        ----------
        agent_id : str

        after : typing.Optional[int]
            Unique ID of the memory to start the query range at.

        before : typing.Optional[int]
            Unique ID of the memory to end the query range at.

        limit : typing.Optional[int]
            How many results to include in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Passage]
            Successful Response

        Examples
        --------
        from letta import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.agents.archival_memory.list(
            agent_id="agent_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/archival",
            method="GET",
            params={
                "after": after,
                "before": before,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, agent_id: str, *, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Passage]:
        """
        Insert a memory into an agent's archival memory store.

        Parameters
        ----------
        agent_id : str

        text : str
            Text to write to archival memory.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Passage]
            Successful Response

        Examples
        --------
        from letta import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.agents.archival_memory.create(
            agent_id="agent_id",
            text="text",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/archival",
            method="POST",
            json={
                "text": text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, agent_id: str, memory_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Delete a memory from an agent's archival memory store.

        Parameters
        ----------
        agent_id : str

        memory_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        from letta import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.agents.archival_memory.delete(
            agent_id="agent_id",
            memory_id="memory_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/archival/{jsonable_encoder(memory_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncArchivalMemoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_summary(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArchivalMemorySummary:
        """
        Retrieve the summary of the archival memory of a specific agent.

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArchivalMemorySummary
            Successful Response

        Examples
        --------
        import asyncio

        from letta import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.archival_memory.get_summary(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/memory/archival",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ArchivalMemorySummary,
                    parse_obj_as(
                        type_=ArchivalMemorySummary,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self,
        agent_id: str,
        *,
        after: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Passage]:
        """
        Retrieve the memories in an agent's archival memory store (paginated query).

        Parameters
        ----------
        agent_id : str

        after : typing.Optional[int]
            Unique ID of the memory to start the query range at.

        before : typing.Optional[int]
            Unique ID of the memory to end the query range at.

        limit : typing.Optional[int]
            How many results to include in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Passage]
            Successful Response

        Examples
        --------
        import asyncio

        from letta import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.archival_memory.list(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/archival",
            method="GET",
            params={
                "after": after,
                "before": before,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, agent_id: str, *, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Passage]:
        """
        Insert a memory into an agent's archival memory store.

        Parameters
        ----------
        agent_id : str

        text : str
            Text to write to archival memory.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Passage]
            Successful Response

        Examples
        --------
        import asyncio

        from letta import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.archival_memory.create(
                agent_id="agent_id",
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/archival",
            method="POST",
            json={
                "text": text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, agent_id: str, memory_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Delete a memory from an agent's archival memory store.

        Parameters
        ----------
        agent_id : str

        memory_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from letta import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.archival_memory.delete(
                agent_id="agent_id",
                memory_id="memory_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{jsonable_encoder(agent_id)}/archival/{jsonable_encoder(memory_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)